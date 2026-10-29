import requests
import re
from collections import Counter

# Fetch trending repos from GitHub API (mock data for demo)
def fetch_trending():
    # In real use, call GitHub search API; here simulate with sample data
    return [
        "folkbench AI API relay benchmark claude codex llm",
        "solid-glass design system ai agents react shadcn tailwind",
        "new-term-radar daily radar ai terms model names products",
        "indra ocr model cpu onnx document parsing pdf",
        "motionmaxxing motion graphics agent skill video films"
    ]

def extract_terms(texts, min_len=3):
    # Simple regex to find words, filter out common stopwords
    stopwords = {'the', 'and', 'for', 'with', 'that', 'this', 'from', 'are', 'was'}
    words = []
    for text in texts:
        found = re.findall(r'[a-z0-9-]+', text.lower())
        words.extend([w for w in found if w not in stopwords and len(w) >= min_len])
    return Counter(words)

def main():
    trending = fetch_trending()
    counter = extract_terms(trending)
    # Filter terms that are likely new/trending (appear more than once)
    new_terms = [word for word, count in counter.most_common(20) if count > 1]
    print("New AI terms detected (simulated):")
    for term in new_terms[:10]:
        print(f"- {term}")

if __name__ == "__main__":
    main()
