🧠 Universal Document Summarizer

Universal Document Summarizer is an AI-powered web application that uses OpenAI GPT and Azure OpenAI to extract and summarize content from various document formats including:

* 📄 PDF
* 📃 DOCX
* 📝 TXT
* 🖼️ PNG, JPG, JPEG (via OCR using Tesseract)

The app provides two versions:

* Streamlit interface using OpenAI – summarize.py

* HTML template interface using Azure OpenAI – Summarize_Using_AzureOpenAI.py

✨ Features
✅ Extract text from PDF, DOCX, TXT, and Image files

✅ Summarize documents using OpenAI or Azure OpenAI GPT models

✅ OCR support for images

✅ User-friendly UI with Streamlit or HTML templates

✅ Modular and clean codebase

📁 File Structure
.
├── summarize.py                      # Streamlit app using OpenAI
├── Summarize_Using_AzureOpenAI.py   # Flask app using Azure OpenAI + templates
├── templates/
│   └── summarize.html               # HTML template for Azure OpenAI version
├── .env                             # Store environment variables securely
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/universal-document-summarizer.git
cd universal-document-summarizer

2. Install Dependencies
It's recommended to use a virtual environment:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file in the root directory and add:

For OpenAI:
OPENAI_API_KEY=your_openai_key_here
For Azure OpenAI:
AZURE_OPENAI_KEY=your_azure_openai_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_VERSION=2023-03-15-preview

▶️ Running the Apps
🔹 OpenAI (Streamlit)
streamlit run summarize.py
This version uses standard OpenAI GPT to process and summarize documents via a sleek Streamlit interface.

🔹 Azure OpenAI (Flask + HTML Template)
python Summarize_Using_AzureOpenAI.py
Navigate to http://127.0.0.1:5000 in your browser. This version uses Azure OpenAI via a Flask backend with an HTML-based frontend.

📦 Supported File Types
| Type  | Extension               | Notes                         |
| ----- | ----------------------- | ----------------------------- |
| Text  | `.txt`                  | UTF-8 encoded                 |
| PDF   | `.pdf`                  | Extracted using PyMuPDF       |
| Word  | `.docx`                 | Extracted using `python-docx` |
| Image | `.png`, `.jpg`, `.jpeg` | OCR with Tesseract            |


🛡️ Security Tip
Never hardcode API keys. Use .env and python-dotenv to load keys securely.

📬 Contact
For suggestions or issues, open an issue.
