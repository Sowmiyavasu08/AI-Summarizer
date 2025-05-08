🧠 Universal Document Summarizer
This project is a dual-mode web app that extracts and summarizes content from various document types using:

✅ OpenAI GPT via Streamlit (file: summarize.py)

✅ Azure OpenAI via Flask and HTML templates (file: Summarize_Using_AzureOpenAI.py)

It supports multiple document formats:

📄 PDF

📃 DOCX

📝 TXT

🖼️ Images (PNG, JPG, JPEG) using OCR

🚀 Features
Extract text from PDFs, DOCX, TXT, and images

Summarize using OpenAI GPT (OpenAI or Azure OpenAI)

OCR support with Tesseract for image text extraction

Two UI options: Streamlit and Flask with HTML templates

📁 File Structure

📦 universal-summarizer
├── summarize.py                     # Streamlit app using OpenAI
├── Summarize_Using_AzureOpenAI.py  # Flask app using Azure OpenAI
├── templates/
│   └── index.html                  # HTML template for Azure app
├── .env                            # Environment variables (not committed)
├── requirements.txt                # Python dependencies
└── README.md                       # Project readme
⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/universal-summarizer.git
cd universal-summarizer
2. Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
🔐 Environment Variables
Create a .env file in the root directory with the following:

# OpenAI (for summarize.py)
OPENAI_API_KEY=your-openai-api-key

# Azure OpenAI (for Summarize_Using_AzureOpenAI.py)
AZURE_OPENAI_KEY=your-azure-openai-key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_VERSION=2023-03-15-preview

▶️ Running the Apps
Option 1: OpenAI with Streamlit
streamlit run summarize.py

Option 2: Azure OpenAI with Flask + HTML
python Summarize_Using_AzureOpenAI.py
Then open http://localhost:5000 in your browser.

📸 Example Use Cases
Extracting insights from research papers

Summarizing meeting transcripts or scanned notes

Getting a brief from long contracts or proposals

📂 Supported File Types
Type	Support
PDF	✅ via PyMuPDF
DOCX	✅ via python-docx
TXT	✅ via direct decoding
PNG, JPG, JPEG	✅ via Tesseract OCR

