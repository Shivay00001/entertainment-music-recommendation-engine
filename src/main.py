import argparse
from src.dataset import load_mock_dataset
from src.recommender import MusicRecommender

def main():
    parser = argparse.ArgumentParser(description="Music Recommendation Engine")
    parser.add_argument("--song", type=str, required=True, help="Title of the song you like")
    
    args = parser.parse_args()
    
    print("--- Loading Engine ---")
    df = load_mock_dataset()
    engine = MusicRecommender(df)
    
    print(f"Finding recommendations for: '{args.song}'...\n")
    
    results = engine.recommend(args.song)
    
    if results is None:
        print(f"❌ Song '{args.song}' not found in database. Try: 'Bohemian Rhapsody', 'Shape of You'.")
    else:
        print(results[['title', 'artist', 'genre', 'energy']].to_markdown(index=False))

if __name__ == "__main__":
    main()
