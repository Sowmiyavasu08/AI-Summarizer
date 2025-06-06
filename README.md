# 🧠 Universal Document Summarizer

This repository contains a **Universal Document Summarizer** that can summarize various types of documents using both **OpenAI** and **Azure OpenAI** models. It supports file types like **PDF**, **DOCX**, **TXT**, **JPG**, **PNG**, and **JPEG**.


### 📦 Table of Contents

1. [Introduction](#-introduction)
2. [Screenshots](#-screenshots)
3. [Features](#-features)
4. [Setup Instructions](#-setup-instructions)
5. [How It Works](#-how-it-works)
6. [File Details](#-file-details)
7. [Customization](#-customization)
8. [Contributing](#-contributing)


## 🧑‍💻 Introduction

The **Universal Document Summarizer** allows you to upload different types of documents, extract their text, and generate concise summaries. It uses:

* **OpenAI GPT** via Streamlit
* **Azure OpenAI** via HTML templates
* **GroqAI Meta LLaMA 4** via Streamlit for advanced summarization

## 📸 Screenshots

Here are some screenshots of the app in action(completely free source):

### Streamlit UI for Text and File Upload

![Streamlit Text Upload](assets/groq_summarizer_home.png)

### Streamlit UI Showing Summary Output

![Streamlit Summary Output](assets/groq_summarizer_second.png)


**Supported file types**:

* 📝 TXT (Plain Text)
* 📄 PDF
* 📃 DOCX (Word Document)
* 🖼️ Images (JPG, PNG, JPEG)


## 🌟 Features

* ✅ Extracts text from **PDF, DOCX, TXT, JPG, PNG, and JPEG**
* 🔀 Provides two summarization options:

  * OpenAI GPT (Streamlit UI)
  * Azure OpenAI GPT (HTML templates)
  * GroqAI Meta LLaMA 4 (Streamlit UI)  
* 👡 Simple and intuitive interface


## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/universal-summarizer.git
cd universal-summarizer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file and add your API credentials:

```env
# OpenAI API Key (For GPT-based Summarization)
OPENAI_API_KEY="your-openai-api-key"

# Azure OpenAI API Configuration
AZURE_OPENAI_KEY="your-azure-openai-api-key"
AZURE_OPENAI_ENDPOINT="https://your-azure-openai-endpoint"
AZURE_OPENAI_VERSION="2023-03-15-preview"

# GroqAI API Key (for Meta LLaMA 4)
GROQ_API_KEY="your-groq-api-key"
```

### 4. Run the Application

* **Streamlit (OpenAI GPT or GroqAI LLaMA 4)**:

  ```bash
  streamlit run summarize.py
  streamlit run summarize_using_groq.py
  ```

* **Flask (Azure OpenAI)**:

  ```bash
  python Summarize_Using_AzureOpenAI.py
  ```

## 🧹 How It Works

### 1. Text Extraction

Depending on the file type:

* **TXT**: Read as plain text
* **DOCX**: Parsed using `python-docx`
* **PDF**: Processed via `PyMuPDF`
* **Images**: OCR via `Tesseract`

### 2. Summarization

Once extracted, the text is summarized using:

* **OpenAI GPT** (via OpenAI API)
* **Azure OpenAI GPT** (via Azure deployment)
* **GroqAI Meta LLaMA 4** (via Groq API)


## 📂 File Details

### `summarize.py`

* Streamlit app for summarizing with OpenAI
* Upload documents → Extract text → Generate summary

### `Summarize_Using_AzureOpenAI.py`

* HTML template-based summarization using Azure OpenAI
* Flask-based file upload and summarization logic

### `summarize_using_groq.py`
* Streamlit app for summarizing with GroqAI
* Upload documents/Give Text → Extract text → Generate summary

## ⚙️ Customization

### Summarization Settings

You can configure:

* `temperature`: Controls creativity
* `max_tokens`: Controls summary length
* `model`: e.g., GPT-3.5, GPT-4 or Meta LLaMA 4

### Text Extraction

Extend extraction logic for:

* Additional formats
* Custom OCR pipelines
* Language-specific adjustments


## 🎉 Contributing

We welcome contributions!
Feel free to submit a pull request for:

* Bug fixes
* New features
* Docs improvement

### Steps:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a pull request

