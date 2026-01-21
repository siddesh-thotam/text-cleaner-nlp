# 🧹 Text Cleaner using NLTK

A beginner-friendly **Natural Language Processing (NLP)** mini project that cleans raw text and prepares it for downstream NLP tasks such as vectorization, sentiment analysis, or modeling.

This project is built from scratch to **understand NLP fundamentals**, not just use libraries blindly.

---

## ✨ Features

- Convert text to lowercase
- Remove URLs and email addresses
- Remove punctuation and numbers
- Tokenize text using NLTK
- Remove stopwords
- Preserve important negation words (`not`, `no`, `never`)
- Simple Command Line Interface (CLI)

---

## 🛠 Tech Stack

- Python
- NLTK
- Regular Expressions (`re`)
- Git & GitHub

---

## 📂 Project Structure

```text
text-cleaner-nlp/
│
├── cleaner.py          # Core text cleaning logic
├── main.py             # CLI entry point
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
├── .gitignore
└── venv/               # Virtual environment (ignored)

----------------------------------------------------

⚙️ Setup Instructions

1️⃣ Clone the repository

git clone https://github.com/siddesh-thotam/text-cleaner-nlp.git
cd text-cleaner-nlp

2️⃣ Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

----------------------------------------------------

🚀 Usage (CLI)
Run the cleaner directly from the command line:

-> python main.py "I do NOT like this movie at all!!! 😡"

Output
Original Text:
I do NOT like this movie at all!!!

Cleaned Text:
not like movie

----------------------------------------------------

🧠 What this project teaches
This project helps beginners learn:

-How raw text is cleaned in NLP

-Why stopwords are removed

-Why negation words must be preserved

-How regex is used in text preprocessing

-How NLP pipelines are structured

-How to build and publish a real GitHub project

----------------------------------------------------

🔮 Future Improvements

-Add stemming and lemmatization

-Add unit tests

-spaCy-based cleaner for comparison

-Support for multiple languages

-Turn into a reusable Python package

----------------------------------------------------