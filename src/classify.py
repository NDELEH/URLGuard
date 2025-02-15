import joblib
from preprocess import extract_features

def classify_url(url):
    # Ensure the URL has a scheme
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Load the model
    model = joblib.load("models/urlguard_model.pkl")

    # Extract features
    features = extract_features(url)

    # Convert features dictionary to a 2D array
    feature_values = [list(features.values())]

    # Predict
    prediction = model.predict(feature_values)
    return "Phishing" if prediction[0] == 1 else "Legitimate"

if __name__ == "__main__":
    url = input("Enter URL: ")
    print("Classification:", classify_url(url))
