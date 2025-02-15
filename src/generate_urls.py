import random
import string

def generate_legitimate_url():
    domains = ["example.com", "google.com", "github.com", "wikipedia.org"]
    paths = ["", "about", "contact", "products", "blog"]
    return f"https://{random.choice(domains)}/{random.choice(paths)}"

def generate_phishing_url():
    suspicious_domains = ["secure-login.com", "verify-account.com", "update-info.com"]
    suspicious_paths = ["login", "verify", "account", "secure"]
    return f"https://{random.choice(suspicious_domains)}/{random.choice(suspicious_paths)}"

def generate_data(num_legitimate=1000, num_phishing=1000):
    legitimate_urls = [generate_legitimate_url() for _ in range(num_legitimate)]
    phishing_urls = [generate_phishing_url() for _ in range(num_phishing)]
    return legitimate_urls, phishing_urls

if __name__ == "__main__":
    legitimate_urls, phishing_urls = generate_data()
    print(f"Generated {len(legitimate_urls)} legitimate URLs and {len(phishing_urls)} phishing URLs.")
