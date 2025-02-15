import joblib
from preprocess import extract_features

def classify_url(url):
    model = joblib.load("models/urlguard_model.pkl")
    features = extract_features(url)
    prediction = model.predict([features])
    return "Phishing" if prediction[0] == 1 else "Legitimate"

if __name__ == "__main__":
    url = input("Enter URL: ")
    print("Classification:", classify_url(url))
