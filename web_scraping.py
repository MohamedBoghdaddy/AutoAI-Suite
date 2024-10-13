from transformers import pipeline
import requests
from bs4 import BeautifulSoup

# Create a summarization pipeline using a pre-trained model
summarizer = pipeline('summarization')

def scrape_and_summarize(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from paragraphs
    text = ' '.join([p.text for p in soup.find_all('p')])

    # Summarize the extracted text
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']
