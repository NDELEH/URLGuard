from urllib.parse import urlparse
import re
from math import log

def get_home_url(url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"

def calculate_entropy(text):
    if not text:
        return 0
    entropy = 0
    for char in set(text):
        p = text.count(char) / len(text)
        entropy -= p * log(p, 2)
    return entropy

def extract_features(url):
    home_url = get_home_url(url)
    parsed = urlparse(home_url)
    features = {
        'domain_length': len(parsed.netloc),
        'num_subdomains': parsed.netloc.count('.'),
        'has_suspicious_keywords': int(bool(re.search(r'(login|verify|account|secure)', url, re.IGNORECASE))),
        'entropy': calculate_entropy(url),
    }
    return features

def preprocess_data(legitimate_urls, phishing_urls):
    legitimate_data = [{'url': url, 'label': 0} for url in legitimate_urls]
    phishing_data = [{'url': url, 'label': 1} for url in phishing_urls]
    data = legitimate_data + phishing_data
    for entry in data:
        entry.update(extract_features(entry['url']))
    return data
