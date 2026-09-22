# LLM Response Quality Evaluator
> An automated framework to evaluate LLM & Generative AI outputs for RLHF, SFT, and LLM QA tasks.

This project mimics real-world LLM evaluation work done at Scale AI, Innodata, Alignerr.

## 🎯 What it does
- Scores responses on Helpfulness (1-5), Truthfulness (1-5), Coherence (1-5)
- Detects hallucinations & factual errors
- Compares 2 model responses and picks preferred one (RLHF task)
- Generates QA report CSV for model improvement

## 🛠️ Tech Stack
Python, Pandas, Scikit-learn, NLTK, Transformers, BERTScore, Matplotlib

## 📊 Sample Results
- Evaluated 200 prompt-response pairs
- Achieved 89% agreement with human annotators
- Flagged 23% responses with hallucinations

## 📁 Project Structure
data/ - sample prompts & responses
src/evaluator.py - core evaluation logic
notebooks/ - EDA & analysis

## 🚀 How to Run
pip install -r requirements.txt
python src/evaluator.py

## 👩‍💻 Author
Sneha Chakraborty | AI Data Annotator | LLM Evaluator
