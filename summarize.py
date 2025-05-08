import streamlit as st
import openai
import fitz  # PyMuPDF for PDFs
import docx
import pytesseract
from PIL import Image
import io, os

from dotenv import load_dotenv
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_type="openai"

# Summarize function using OpenAI
def generate_summary(text):
    if not text.strip():
        return "No text to summarize."
    
    response = openai.completions.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
        prompt=[
            {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ],
        temperature=0.5,
        max_tokens=300
    )
    print("response start**********")
    print(response)
    print("response end**********")

    return response.choices[0].message.content.strip()

# Extract text from .docx
def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# Extract text from .pdf
def extract_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Extract text from image using OCR
def extract_image_text(file):
    img = Image.open(file)
    return pytesseract.image_to_string(img)

# Main Streamlit App
def main():
    st.title("🧠 Universal Document Summarizer")
    st.write("Upload a file (PDF, DOCX, TXT, Image) and get a concise summary using OpenAI.")

    uploaded_file = st.file_uploader("Upload file", type=["pdf", "docx", "txt", "png", "jpg", "jpeg"])

    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1].lower()

        with st.spinner("Extracting text..."):
            if file_type == "txt":
                text = uploaded_file.read().decode("utf-8")
            elif file_type == "docx":
                text = extract_docx(uploaded_file)
            elif file_type == "pdf":
                text = extract_pdf(uploaded_file)
            elif file_type in ["png", "jpg", "jpeg"]:
                text = extract_image_text(uploaded_file)
            else:
                st.error("Unsupported file type.")
                return

        st.subheader("📄 Extracted Text")
        st.text_area("Text", value=text, height=200)

        if st.button("Summarize"):
            with st.spinner("Generating summary..."):
                summary = generate_summary(text)
                st.subheader("📝 Summary")
                st.success(summary)

if __name__ == "__main__":
    main()


# git remote add origin https://github.com/Sowmiyavasu08/AI-Summarizer.git
# git branch -M main
# git push -u origin main