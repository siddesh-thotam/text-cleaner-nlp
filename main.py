import sys
import nltk 
from cleaner import clean_text

nltk.download("punkt")
nltk.download("stopwords")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your text here\"")
        return

    text = sys.argv[1]
    cleaned = clean_text(text)

    print("\nOriginal Text:")
    print(text)

    print("\nCleaned Text:")
    print(cleaned)


if __name__ == "__main__":
    main()
