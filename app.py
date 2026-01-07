
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/caption"

st.set_page_config(page_title="Image Caption Generator", page_icon="✨", layout="wide")

# --- your CSS here (same as you already have) ---
st.markdown("""<style>
/* keep your existing CSS ... */

/* (optional) cap preview image height so it doesn't look huge */
img {max-height: 420px !important; object-fit: contain;}
</style>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.4, 1])

with col2:
    st.markdown('<div class="ai-badge">✨ AI-Powered</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Image Caption Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Upload any image and let AI create a perfect, descriptive caption for you</p>',
                unsafe_allow_html=True)

    # uploader (keep it here)
    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed",
    )

    st.markdown('<div class="custom-footer">Powered by AI Vision Technology</div>', unsafe_allow_html=True)

    # ✅ Move EVERYTHING related to preview + button inside col2
    if uploaded_file is not None:
        st.success("Image uploaded successfully!")

        # smaller preview (choose ONE)
        st.image(uploaded_file, caption="Your uploaded image", use_container_width=True)
        # OR: st.image(uploaded_file, caption="Your uploaded image", width=520)

        if st.button("🎨 Generate Caption", type="primary", use_container_width=True):
            with st.spinner("Generating caption..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    resp = requests.post(API_URL, files=files, timeout=180)
                    resp.raise_for_status()
                    caption = resp.json().get("caption", "No caption returned.")
                    st.markdown(
                        f'<div class="caption-box"><strong>Caption:</strong> {caption}</div>',
                        unsafe_allow_html=True,
                    )
                except requests.exceptions.RequestException as exc:
                    st.error(f"Request failed: {exc}")



