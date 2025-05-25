# AI Summarizer using GroqAI 🚀
# Streamlit App to summarize documents and text using Meta LLaMA 4 (Groq API)

import streamlit as st
from groq import Groq
import fitz  # PyMuPDF
import docx
import pytesseract
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# 🧠 Generate summary using GroqAI LLaMA 4
def generate_summary(text):
    if not text.strip():
        return "No text to summarize."

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()

# 📄 Extract text from DOCX
def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# 📄 Extract text from PDF
def extract_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# 🖼️ Extract text from images using OCR
def extract_image_text(file):
    img = Image.open(file)
    return pytesseract.image_to_string(img)

# 🚀 Streamlit UI
def main():
    st.set_page_config(page_title="AI Summarizer using GroqAI", page_icon="🧠", layout="centered")

    # 🎨 Custom CSS for gradient title
    st.markdown("""
        <style>
        .gradient-text {
            font-weight: 800;
            font-size: 2.5rem;
            text-align: center;
            background: linear-gradient(90deg, #00F260, #0575E6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .subtext {
            text-align: center;
            font-size: 1.1rem;
            color: #444;

        }
        .block-container {
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='gradient-text'>🧠 AI Summarizer using GroqAI</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtext'>Summarize documents or pasted content with Meta LLaMA 4 hosted on Groq</div>", unsafe_allow_html=True)

    st.divider()

    input_method = st.radio("📥 Choose Input Method", options=["Paste Text", "Upload File"], horizontal=True)

    final_text = ""

    if input_method == "Paste Text":
        user_input = st.text_area("✍️ Enter your text below:", height=180)
        final_text = user_input.strip()

    elif input_method == "Upload File":
        uploaded_file = st.file_uploader("📎 Upload a document (PDF, DOCX, TXT, PNG, JPG)", type=["pdf", "docx", "txt", "png", "jpg", "jpeg"])
        if uploaded_file:
            file_type = uploaded_file.name.split('.')[-1].lower()
            with st.spinner("🔍 Extracting text..."):
                if file_type == "txt":
                    final_text = uploaded_file.read().decode("utf-8")
                elif file_type == "docx":
                    final_text = extract_docx(uploaded_file)
                elif file_type == "pdf":
                    final_text = extract_pdf(uploaded_file)
                elif file_type in ["png", "jpg", "jpeg"]:
                    final_text = extract_image_text(uploaded_file)
                else:
                    st.error("❌ Unsupported file type.")
                    return

            st.subheader("📄 Extracted Text Preview")
            st.text_area("Preview", value=final_text, height=200, key="file_text_preview")

    if final_text:
        if st.button("🪄 Summarize"):
            with st.spinner("💭 Generating summary..."):
                summary = generate_summary(final_text)
                st.subheader("✅ AI-Generated Summary")
                st.success(summary)
    else:
        st.info("👉 Paste some text or upload a file to begin summarization.")

# 🔽 Entry point
if __name__ == "__main__":
    main()
