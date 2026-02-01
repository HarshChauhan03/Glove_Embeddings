# 🌍 Word Embeddings using GloVe | Advanced NLP

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NLP](https://img.shields.io/badge/Field-NLP-green)
![Embeddings](https://img.shields.io/badge/Embeddings-GloVe-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project demonstrates **GloVe (Global Vectors for Word Representation)**, a pre-trained word embedding model used in modern Natural Language Processing (NLP).

Unlike Word2Vec (trained locally), GloVe uses **global word co-occurrence statistics** from large corpora to generate meaningful word vectors.

---

## 📌 What are GloVe Embeddings?

GloVe is a pre-trained word embedding model developed by Stanford University.  
It represents words as dense vectors that capture semantic relationships.

### Key Properties:
- Words with similar meanings have similar vectors  
- Semantic relationships can be computed mathematically  
- Works well for NLP tasks like sentiment analysis, chatbots, search, and translation  

**Example Relationship:**
king − man + woman ≈ queen


---

## 🎯 Project Objective

This project aims to:

✅ Load pre-trained GloVe word vectors  
✅ Convert words into vector form  
✅ Measure similarity between words  
✅ Demonstrate word analogy using vector arithmetic  

---

## 🧠 How It Works

GloVe vectors are trained on large text corpora.  
Each word is represented as a 50-dimensional vector (in this project).

We use cosine similarity to:
- Compare word meanings  
- Solve word analogy problems  

---

## 📂 Project Structure

Day09_GloVe_Embeddings/
├── glove_embeddings.py
└── README.md


---

## ⬇️ Download GloVe Dataset

1. Visit: https://nlp.stanford.edu/projects/glove/  
2. Download **glove.6B.zip**  
3. Extract the file  
4. Place **glove.6B.50d.txt** inside the project folder  

---

## ⚙️ Technologies Used

- Python 🐍  
- NumPy  
- Scikit-learn  

---

## ▶️ How to Run

### Step 1 — Install dependencies
```bash
pip install numpy scikit-learn
Step 2 — Ensure GloVe file is present
Place glove.6B.50d.txt in the project folder.

Step 3 — Run the script
python glove_embeddings.py
✅ Output You Will See
Vector representation of a word

Similarity scores between words

Word analogy result (e.g., king - man + woman)

🚀 Learning Outcomes
By completing this project, you will:

✔ Understand pre-trained word embeddings
✔ Learn how machines capture semantic meaning
✔ Use cosine similarity in NLP
✔ Explore vector arithmetic for word relationships
✔ Move closer to modern AI-based NLP systems

📖 Why This Matters
GloVe embeddings are used in:

Chatbots 🤖

Search engines 🔍

Recommendation systems 🎯

Sentiment analysis

Machine translation

They form the base for advanced models like BERT, GPT, and Transformers.

👨‍💻 Author
Harsh Chauhan
