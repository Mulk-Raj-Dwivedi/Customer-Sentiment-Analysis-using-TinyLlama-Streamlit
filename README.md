# Customer-Sentiment-Analysis-using-TinyLlama-Streamlit
AI-powered Customer Sentiment Analysis system using TinyLlama, Hugging Face Transformers, and Streamlit to analyze customer call transcripts from JSON files and classify sentiments as Positive, Neutral, or Negative. Features local model loading, Streamlit caching, CSV export, and scalable transcript processing for Voice of Customer (VOC) analytics.


Project Overview


This project is an AI-powered Customer Sentiment Analysis System built using:

TinyLlama (LLM)

Hugging Face Transformers

PyTorch

Streamlit

JSON Transcript Processing


The application analyzes customer conversations from transcript JSON files and predicts the overall customer sentiment as:

Positive

Neutral

Negative


The system extracts only customer statements from the transcript and performs sentiment classification using a locally hosted Large Language Model (LLM).


Features :

Upload single or multiple transcript JSON files

Extract customer-only conversations

AI-powered sentiment analysis using TinyLlama

Streamlit web application

Download sentiment results as CSV

Local model loading for faster inference

Cached model loading using Streamlit

Production-style modular architecture


Tech Stack :

Technology	              Purpose

Python	                  Backend Logic

Streamlit	                Web Application

Hugging Face Transformers LLM Integration

TinyLlama	                Sentiment Prediction

PyTorch	                  Deep Learning Backend

Pandas	                  Data Handling

YAML	                    Configuration

JSON	                    Transcript Storage


Repository Structure :

Customer-Sentiment-Analysis/
│
├── app.py

├── voc_extract_sentiment_test.py

├── customer_sentiment_fields.yaml

├── sentiment_results.csv

├── requirements.txt

├── download_model.py

│
├── saved_model/

│   ├── config.json

│   ├── tokenizer.json

│   ├── model.safetensors

│   └── other model files

│
├── sample_transcripts/

│   ├── call_001.json

│   ├── call_002.json

│   ├── call_003.json

│   └── ...
│
└── README.md

Files Description

1. app.py

Main Streamlit application.

Responsibilities:

Upload transcript files

Run sentiment analysis

Display predictions

Export CSV results

2. voc_extract_sentiment_test.py

Core backend processing module.

Contains:

Transcript extraction logic

Customer text extraction

TinyLlama model loading

Sentiment prediction pipeline

Utility functions

3. customer_sentiment_fields.yaml

YAML configuration file for sentiment analysis fields.

Example:

fields:

  - name: customer_sentiment
    
    description: |
    
      Analyze ONLY the CUSTOMER statements.
    
      Determine overall sentiment.
    
4. sentiment_results.csv

Generated output file containing:

Call ID

Transcript

Predicted sentiment

5. download_model.py

Downloads TinyLlama model once and saves locally for faster loading.

6. saved_model/

Contains locally saved Hugging Face model files.

This prevents:

repeated downloads

slow app startup

internet dependency

7. sample_transcripts/

Contains sample customer call transcript JSON files.

Transcript JSON Format

Example:

{
  "transcription": {
    "transcript": "Agent: Hello\nCustomer: I am unhappy with the service."
  },
  
  "metadata": {
    "call_id": "CALL_001",
    "language": "english"
  }

}

Model Used

TinyLlama

Model:

TinyLlama/TinyLlama-1.1B-Chat-v1.0

Used for:

conversational sentiment understanding

customer emotion classification

lightweight local inference

Sentiment Classes

Sentiment	Meaning

Positive	Happy, satisfied, appreciative
Neutral	Calm inquiry or discussion
Negative	Angry, frustrated, disappointed

Installation

Clone Repository

cd Customer-Sentiment-Analysis


Install Dependencies

pip install -r requirements.txt

requirements.txt

streamlit

transformers

torch

pandas

pyyaml

sentencepiece

accelerate

Download Model Locally

Run once:

python download_model.py

This creates:

saved_model/

Run Streamlit App

streamlit run app.py

Streamlit Application Workflow


Upload JSON Files
        ↓
Extract Transcript
        ↓
Extract Customer Statements
        ↓
Generate Sentiment Prompt
        ↓
TinyLlama Prediction
        ↓
Display Results
        ↓
Download CSV


Core Functions

_extract_transcript_text()

Extracts transcript text from JSON.

extract_customer_only_text()

Filters only customer conversation lines.

load_model()

Loads TinyLlama locally using Streamlit caching.

process_all_transcripts()

Processes all transcript files and generates sentiment results.

Performance Optimizations

Local Model Storage

The model is downloaded once and stored locally.

Benefits:

Faster startup

Offline execution

No repeated Hugging Face downloads

Streamlit Caching

@st.cache_resource

Prevents model reload on every UI refresh.

Sample Output

Call ID	    Sentiment

CALL_001	  Negative

CALL_002	  Positive

CALL_003	  Neutral


Future Improvements :

Real-time sentiment scoring

Multi-language support

Emotion detection

Speech-to-text integration

GPU acceleration

Dashboard analytics

API deployment using FastAPI

Batch processing support


Use Cases :

Customer Support Analytics

Banking Call Analysis

Insurance Complaint Monitoring

Contact Center Intelligence

Voice of Customer (VOC)

Customer Experience Monitoring


Author :

Mulk Raj Dwivedi

AI/ML Engineer | Data Engineer | Generative AI Enthusiast

Skills:

Machine Learning

Deep Learning

NLP

Generative AI

LangChain

Streamlit

Python

SQL

LinkedIn:

[Mulk Raj Dwivedi LinkedIn](https://www.linkedin.com/in/mulk-raj-dwivedi/)

License

MIT License

Added in repository :

Streamlit UI screenshot

Transcript JSONs

Prediction CSV output

