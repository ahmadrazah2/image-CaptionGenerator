from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import torch
from PIL import Image
import io

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base",
    device=device,

)

@app.post("/caption")
async def caption(file: UploadFile = File(...)):
    img_bytes = await file.read()
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    result = captioner(
        image,
        max_new_tokens=200,
        generate_kwargs={"num_beams": 5, "temperature": 0.8, "repetition_penalty": 1.1},
    )
    return {"caption": result[0]["generated_text"]}
