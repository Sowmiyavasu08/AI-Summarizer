from flask import Flask, render_template, request
import openai, fitz, docx, pytesseract
from PIL import Image
import io, os

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_VERSION")

app = Flask(__name__)

def generate_summary(text):
    if not text.strip():
        return "No text to summarize."

    response = openai.completions.create(
        model="gpt-4",
        prompt=[
            {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ],
        temperature=0.5,
        max_tokens=300
    )
    return response.choices[0].message["content"].strip()

def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_image_text(file):
    img = Image.open(file)
    return pytesseract.image_to_string(img)

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = ""
    summary = ""
    if request.method == "POST":
        file = request.files["document"]
        file_type = file.filename.split('.')[-1].lower()

        if file_type == "txt":
            extracted_text = file.read().decode("utf-8")
        elif file_type == "docx":
            extracted_text = extract_docx(file)
        elif file_type == "pdf":
            extracted_text = extract_pdf(file)
        elif file_type in ["png", "jpg", "jpeg"]:
            extracted_text = extract_image_text(file)
        else:
            extracted_text = "Unsupported file type."

        if "summarize" in request.form:
            summary = generate_summary(extracted_text)

    return render_template("index.html", extracted_text=extracted_text, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
