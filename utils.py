# utils.py

import re


def clean_text(text):
    """
    Clean resume text by removing unwanted characters
    """

    # Convert text into lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def extract_words(text):
    """
    Convert text into list of words
    """

    words = text.split()

    return words