# Entertainment Music Recommendation Engine

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade Content-Based Filtering recommendation system** for music. This repository implements a vector-based similarity engine (Cosine Similarity) that recommends songs based on audio features (tempo, energy, danceability) and metadata (tags, genre).

## 🚀 Features

- **Content-Based Filtering**: Suggests items similar to those a user likes.
- **Vectorization**: Converts song features into high-dimensional vectors.
- **Cosine Similarity**: Calculates geometric proximity between songs.
- **Cold Start Handling**: Recommends popular/trending songs for new users.
- **Scalable Design**: Uses `sklearn` for efficient nearest neighbor search.

## 📁 Project Structure

```
entertainment-music-recommendation-engine/
├── src/
│   ├── dataset.py        # Mock Song Database
│   ├── recommender.py    # ML Logic
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/entertainment-music-recommendation-engine.git

# Install
pip install -r requirements.txt

# Run Recommender
python src/main.py --song "Bohemian Rhapsody"
```

## 📄 License

MIT License
