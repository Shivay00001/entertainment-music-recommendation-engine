import pandas as pd
import numpy as np

def load_mock_dataset():
    """Generates a mock dataset of 50 songs with audio features."""
    genres = ['Rock', 'Pop', 'Jazz', 'HipHop', 'Classical']
    
    data = []
    
    # Manually curating a few hits for demo
    data.append({"id": 1, "title": "Bohemian Rhapsody", "artist": "Queen", "genre": "Rock", "tempo": 0.4, "energy": 0.8, "danceability": 0.3})
    data.append({"id": 2, "title": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop", "tempo": 0.6, "energy": 0.7, "danceability": 0.9})
    data.append({"id": 3, "title": "Take Five", "artist": "Dave Brubeck", "genre": "Jazz", "tempo": 0.5, "energy": 0.4, "danceability": 0.5})
    data.append({"id": 4, "title": "Lose Yourself", "artist": "Eminem", "genre": "HipHop", "tempo": 0.7, "energy": 0.9, "danceability": 0.7})
    data.append({"id": 5, "title": "Four Seasons", "artist": "Vivaldi", "genre": "Classical", "tempo": 0.5, "energy": 0.3, "danceability": 0.2})
    
    # Random fill
    for i in range(6, 51):
        g = np.random.choice(genres)
        data.append({
            "id": i,
            "title": f"Song #{i}",
            "artist": f"Artist {np.random.randint(1, 20)}",
            "genre": g,
            "tempo": np.round(np.random.random(), 2),
            "energy": np.round(np.random.random(), 2),
            "danceability": np.round(np.random.random(), 2)
        })
        
    return pd.DataFrame(data)
