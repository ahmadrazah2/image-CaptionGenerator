import io
import streamlit as st
from PIL import Image
import torch
from transformers import pipeline

# Page config
st.set_page_config(page_title="Image Caption Generator", page_icon="✨", layout="wide")

@st.cache_resource
def load_captioner():
    # Streamlit Cloud uses CPU. This logic handles both environments.
    if torch.cuda.is_available():
        device = 0  # NVIDIA GPU
    elif torch.backends.mps.is_available():
        device = "mps" # Apple Silicon
    else:
        device = -1 # CPU (Streamlit Cloud default)
    
    return pipeline(
        "image-to-text",
        model="Salesforce/blip-image-captioning-base",
        device=device
    )

captioner = load_captioner()

# CSS styling
st.markdown(
    """
    <style>
    .block-container {padding-top: 1.5rem; padding-bottom: 1rem; max-width: 1200px;}
    .stApp {background: linear-gradient(135deg, #f5f7fa 0%, #e8eaf6 50%, #e1f5fe 100%);}
    #MainMenu, footer, header {visibility: hidden;}
    .ai-badge {display: inline-block; background: white; padding: 6px 14px; border-radius: 20px; font-size: 13px;
               color: #7c4dff; font-weight: 500; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);}
    .main-title {font-size: 2.8rem; font-weight: 700; text-align: center;
                 background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #2196f3 100%);
                 -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 10px; line-height: 1.2;}
    .subtitle {text-align: center; font-size: 1rem; color: #666; margin-bottom: 25px; line-height: 1.4;}
    .upload-container {background: white; border: 3px solid transparent; border-image: linear-gradient(135deg, #667eea, #2196f3) 1;
                       border-radius: 20px; padding: 35px 30px; text-align: center; margin: 0 auto 20px;
                       box-shadow: 0 10px 30px rgba(0,0,0,0.1);}
    .upload-icon {width: 60px; height: 60px; background: linear-gradient(135deg, #e8eaf6, #f3e5f5); border-radius: 50%;
                  display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8rem;}
    .upload-text {font-size: 1.15rem; font-weight: 600; color: #333; margin-bottom: 8px;}
    .upload-subtext {color: #999; font-size: 0.9rem; margin-bottom: 10px;}
    .supported-formats {color: #bbb; font-size: 0.8rem;}
    img {max-height: 320px !important; object-fit: contain; border-radius: 12px; margin: 15px auto;}
    .caption-box {background: white; padding: 20px; border-radius: 12px; margin-top: 15px;
                  box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: left; border-left: 4px solid #667eea;}
    .caption-box strong {color: #667eea; font-size: 1.1rem;}
    .custom-footer {text-align: center; color: #999; font-size: 0.85rem; margin-top: 20px;}
    .stButton > button {margin-top: 12px; height: 48px; font-size: 1rem; font-weight: 600;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Hero
col1, col2, col3 = st.columns([1, 1.6, 1])
with col2:
    st.markdown('<div class="ai-badge">✨ AI-Powered</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Image Caption Generator</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Upload any image and let AI create a perfect,<br>descriptive caption for you</p>',
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed",
    )

    if uploaded_file is None:
        st.markdown('<div class="upload-container">', unsafe_allow_html=True)
        st.markdown(
            '<div class="upload-icon">📤</div>'
            '<div class="upload-text">Drag & drop your image</div>'
            '<div class="upload-subtext">or click to browse from your device</div>'
            '<div class="supported-formats">Supports JPG, PNG, JPEG</div>',
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        img_col, cap_col = st.columns([1.2, 1])

        with img_col:
            st.image(uploaded_file, use_container_width=True)

        with cap_col:
            caption_placeholder = st.empty()
            if st.button("🎨 Generate Caption", type="primary", use_container_width=True):
                caption_placeholder.markdown(
                    '<div class="caption-box" style="border-left-color:#667eea;">'
                    '<strong style="color:#667eea;">Generating...</strong>'
                    '</div>',
                    unsafe_allow_html=True,
                )
                try:
                    image = Image.open(io.BytesIO(uploaded_file.getvalue())).convert("RGB")
                    result = captioner(
                        image,
                        max_new_tokens=60,
                        generate_kwargs={"num_beams": 5, "temperature": 0.8, "repetition_penalty": 1.1},
                    )
                    caption = result[0].get("generated_text", "No caption returned.")
                    caption_placeholder.markdown(
                        f'<div class="caption-box"><strong>📝 Caption:</strong><br><span style="color:#111827;">{caption}</span></div>',
                        unsafe_allow_html=True,
                    )
                except Exception as exc:
                    caption_placeholder.error(f"❌ Caption failed: {exc}")

    st.markdown('<div class="custom-footer">Powered by AI Vision Technology</div>', unsafe_allow_html=True)
