import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

class MusicRecommender:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.features = ['tempo', 'energy', 'danceability']
        self._prepare_model()

    def _prepare_model(self):
        # Normalize features
        scaler = MinMaxScaler()
        self.feature_matrix = scaler.fit_transform(self.data[self.features])
        
        # Compute Similarity Matrix (Item-Item)
        self.sim_matrix = cosine_similarity(self.feature_matrix)

    def recommend(self, song_title: str, top_k=5):
        # Find index
        try:
            idx = self.data[self.data['title'].str.lower() == song_title.lower()].index[0]
        except IndexError:
            return None

        # Get similarity scores
        scores = list(enumerate(self.sim_matrix[idx]))
        
        # Sort desc
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        
        # Skip top 1 (itself) and get top K
        top_indices = [i[0] for i in scores[1:top_k+1]]
        
        return self.data.iloc[top_indices]
