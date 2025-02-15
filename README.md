# URLGuard

URLGuard is a machine learning-based tool designed to detect phishing URLs. It uses synthetic data generation to train a Random Forest classifier, which can classify URLs as either **phishing** or **legitimate**.

---

## **Problem Statement**
Phishing attacks are one of the most common cybersecurity threats today. Attackers use deceptive URLs to trick users into revealing sensitive information, such as login credentials or financial details. Traditional rule-based systems struggle to keep up with the evolving tactics of attackers. Machine learning offers a promising solution by learning patterns from data and detecting phishing URLs more effectively.

---

## **Why This Project?**
The goal of this project is to:
1. **Simulate real-world phishing detection** using synthetic data.
2. **Provide a self-contained solution** that doesn’t rely on external datasets.
3. **Educate users** on how machine learning can be applied to cybersecurity.

---

## **Finished Product**
The final product is a Python-based tool that:
1. **Generates synthetic phishing and legitimate URLs**.
2. **Preprocesses URLs** and extracts features like domain length, number of subdomains, and presence of suspicious keywords.
3. **Trains a Random Forest classifier** on the synthetic data.
4. **Classifies new URLs** as phishing or legitimate.

---

## **Features**
- **Synthetic Data Generation**: No need for external datasets.
- **Feature Extraction**: Extracts key features from URLs for classification.
- **Machine Learning**: Uses a Random Forest classifier for accurate predictions.
- **Easy to Use**: Simple command-line interface for classification.

---

## **How to Clone and Run**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/URLGuard.git
cd URLGuard
