# 🧠 Universal Document Summarizer
This repository contains a Universal Document Summarizer that can summarize various types of documents using both OpenAI and Azure OpenAI models. It supports file types like PDF, DOCX, TXT, JPG, PNG, and JPEG.

### 📦 Table of Contents
    1.Introduction
    2.Features
    3.Setup Instructions
    4.How It Works
    5.File Details
    6.Customization
    7.Contributing
    8.Contact Info


### 🧑‍💻 Introduction
The Universal Document Summarizer allows you to upload different types of documents, extract their text, and generate concise summaries. The app uses OpenAI for summarization through Streamlit and Azure OpenAI via templates.

This application supports the following file types:

    📝 TXT (Plain Text)
    📄 PDF
    📃 DOCX (Word Document)
    🖼️ Images (JPG, PNG, JPEG)

### 🌟 Features
Extracts text from various file formats: PDF, DOCX, TXT, and Image Files (JPG, PNG, JPEG).
Provides two summarization options:

OpenAI GPT (via Streamlit)
Azure OpenAI GPT (via HTML templates)

Easy-to-use interface to upload files and generate summaries.

### 🔧 Setup Instructions

###### 1. Clone the repository:
`git clone https://github.com/your-username/universal-summarizer.git`
`cd universal-summarizer`

###### 2. Install dependencies:
Install the required Python packages listed in requirements.txt:
`pip install -r requirements.txt`

###### 3. Configure environment variables:
Create a .env file in the project root and add the necessary API keys and endpoint configurations. Example:
# OpenAI API Key (For GPT-based Summarization)
`OPENAI_API_KEY="your-openai-api-key"`

# Azure OpenAI API Configuration
`AZURE_OPENAI_KEY="your-azure-openai-api-key"`
`AZURE_OPENAI_ENDPOINT="https://your-azure-openai-endpoint"`
`AZURE_OPENAI_VERSION="2023-03-15-preview"`

###### 4. Run the app:
To run the application, use the following commands:

For OpenAI-based Summarizer (Streamlit):
    `streamlit run summarize.py`
For Azure OpenAI-based Summarizer (HTML Templates):
    `python Summarize_Using_AzureOpenAI.py`

### 🧩 How It Works
The application operates in two main phases:

###### 1. Text Extraction:
It extracts text from uploaded documents using different methods based on the file type:

    TXT: Directly reads the text from the file.
    DOCX: Uses python-docx to parse Word files.
    PDF: Uses PyMuPDF to extract text from PDF files.
    Image: Uses Tesseract OCR to extract text from image files (JPG, PNG, JPEG).

###### 2. Summarization:
Once the text is extracted, it is passed to the summarization model:

    OpenAI GPT: Uses OpenAI's GPT model to generate a summary.
    Azure OpenAI GPT: Uses Azure OpenAI's GPT model for summarization.

### 📂 File Details
###### 1. summarize.py:
This file sets up a Streamlit interface for summarization using OpenAI GPT.

It allows users to upload files, view the extracted text, and then generate a summary.

###### 2. Summarize_Using_AzureOpenAI.py:
This script is for summarization using Azure OpenAI GPT through templates.

It provides a web interface with HTML templates for summarizing uploaded documents.

### ⚙️ Customization
The application allows for customization in various parts:

###### 1. Summarization Settings:
You can modify the following parameters to control the summarization behavior:

Temperature: Controls the randomness of the summary (higher = more creative).

Max tokens: Controls the length of the summary.

Model Type: You can switch between different models (e.g., GPT-3.5, GPT-4) based on your access.

###### 2. Text Extraction:
You can adjust or add new methods to extract text from other document types if needed.

### 🎉 Contributing
We welcome contributions! Whether it's fixing bugs, adding features, or improving documentation, feel free to open an issue or submit a pull request.

###### Steps to contribute:
    Fork the repository.
    Create a new branch.
    Make your changes and commit them.
    Submit a pull request with a description of the changes.