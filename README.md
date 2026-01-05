
# 🖼️ Image Caption Generator

An **AI-powered Image Caption Generator** built with **Streamlit** and a **pretrained BLIP vision–language model**.
Upload any image and instantly generate a **natural language caption**, running fully **locally** on your machine.

---

## ✨ Features

* 🧠 Pretrained **BLIP image captioning model**
* ⚡ Runs **locally** (no API keys, no backend)
* 💻 Works smoothly on **MacBook M1 / M2 (16GB)**
* 🎨 Modern and clean **Streamlit UI**
* 📷 Supports JPG, PNG, GIF, WebP
* 🔘 One-click caption generation

---

## 🧩 Model Used

* **Model:** `Salesforce/blip-image-captioning-base`
* **Task:** Image → Text (Image Captioning)
* **Framework:** Hugging Face Transformers

BLIP combines a **vision encoder** with a **text decoder** to generate meaningful and descriptive captions from images.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* Pillow (PIL)

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/image-caption-generator.git
cd image-caption-generator
```

### 2️⃣ Install dependencies

```bash
pip install streamlit transformers torch pillow
```

### 3️⃣ Run the app

```bash
streamlit run streamlit_app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🖥️ System Requirements

* macOS / Windows / Linux
* Tested on **MacBook M2 (16GB RAM)**
* No dedicated GPU required
* No external APIs required

---

## 📁 Project Structure

```
image-caption-generator/
│
├── app.py        # Streamlit application
├── README.md     # Project documentation
└── requirements.txt (optional)
```

---

## 🎯 Use Cases

* Computer vision demos
* AI portfolio projects
* Multimodal AI experiments
* Image understanding applications
* Foundation for VQA systems

---

## 🔮 Future Improvements

* Multilingual captions (English → Korean)
* Batch image captioning
* CLIP-based custom caption model
* Deployment on Hugging Face Spaces

---

## 📜 License

This project is released for **educational and research purposes** using open-source components.

---

## 👤 Author

**Ahmad Raza**
AI Engineer | Computer Vision | Vision–Language Models
📍 Busan, South Korea

---

⭐ If you like this project, feel free to **star the repository**!
