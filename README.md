# 📰 News Clustering and Sentiment Analysis

## 📌 Overview

This project implements a complete Natural Language Processing (NLP) pipeline to perform **News Clustering** and **Sentiment Analysis** on real-world news data.

It uses **TF-IDF vectorization** to convert text into numerical features, **K-Means clustering** to group similar news articles, and **TextBlob** to analyze the sentiment (positive, negative, neutral).

---

## 🚀 Features

* 🔤 Text preprocessing (cleaning, stopword removal, normalization)
* 📊 TF-IDF vectorization
* 🤖 K-Means clustering (unsupervised learning)
* 😊 Sentiment analysis using TextBlob
* 📈 Cluster visualization using Matplotlib
* 🧠 Automatic cluster interpretation (custom labels)

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* NLTK
* TextBlob
* Matplotlib

---

## 📂 Project Structure

```
News Clustering And Sentiment Analyzer/
│
├── data/
│   └── dataset.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── vectorizer.py
│   ├── clustering.py
│   ├── sentiment.py
│   ├── evaluation.py
│   └── utils.py
│
├── main.py
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/news-clustering.git
cd news-clustering
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Download NLTK data

```
python -m textblob.download_corpora
```

---

## ▶️ Usage

Run the main script:

```
python main.py
```

---

## 📊 Output

### 🔹 Sample Output

* News grouped into clusters (e.g., War/Politics, General, Health)
* Sentiment classification (Positive, Negative, Neutral)

Example:

```
Title                                 Cluster Name     Sentiment
Ukraine war news...                   War/Politics     Negative
Covid vaccine update...               Health           Positive
```

---

### 📈 Visualization

* Bar graph showing distribution of clusters

---

## 🧠 Methodology

1. **Data Preprocessing**

   * Lowercasing
   * Removing punctuation
   * Stopword removal

2. **Feature Extraction**

   * TF-IDF (Term Frequency - Inverse Document Frequency)

3. **Clustering**

   * K-Means algorithm groups similar news articles

4. **Sentiment Analysis**

   * TextBlob calculates polarity to classify sentiment

---

## 🎯 Key Concepts

* Natural Language Processing (NLP)
* Unsupervised Learning
* Text Vectorization
* Clustering Algorithms
* Sentiment Analysis

---

## 🧪 Results

* Successfully clustered thousands of news articles
* Identified dominant topics using unsupervised learning
* Classified sentiment of each article
* Visualized cluster distribution

---

## 🎓 Use Case

* News aggregation platforms
* Trend analysis
* Content categorization
* Social media monitoring

---

## 📌 Future Improvements

* Use advanced models like BERT
* Improve clustering accuracy
* Add real-time news scraping
* Deploy as a web application

---

## 👨‍💻 Author

Prince Agrawal
Nitin Sharma
---

## ⭐ Acknowledgements

* Scikit-learn documentation
* NLTK library
* TextBlob library
* Open-source datasets

---

## 📜 License

This project is for educational purposes.
# News-Clustering-And-Sentiment-Analyzer
News Clustering and Sentiment Analysis using NLP and Machine Learning. This project uses TF-IDF for text vectorization, K-Means for clustering similar news articles, and TextBlob for sentiment analysis.
