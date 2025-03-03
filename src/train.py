import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
from generate_urls import generate_data
from preprocess import preprocess_data

def train():
    # Generate synthetic data
    legitimate_urls, phishing_urls = generate_data()
    data = preprocess_data(legitimate_urls, phishing_urls)
    df = pd.DataFrame(data)

    # Split data into features and labels
    X = df.drop(['url', 'label'], axis=1)
    y = df['label']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save the model
    joblib.dump(model, "models/urlguard_model.pkl")

if __name__ == "__main__":
    train()
