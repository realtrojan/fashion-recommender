# This code is developed by Afolabi Williams on the 10th of April, 2025
# Updated May 9th, 2025
# Python Methodologies by Professor Lars
# Final Project: Fashion Search & Recommendation Algorithim
# Source of data is from kaggle.com



import os
from recommender_utils import DataLoader
from recommender_engine import FashionRecommender

# Constants
DATA_FILE = 'hmfashiondb.csv'
OUTPUT_FILE = 'fashion_recommendations_output.csv'
TOP_N_RECOMMENDATIONS = 10
SCORE_THRESHOLD = 10

if __name__ == '__main__':
    print("--- H&M Fashion Recommender ---")
    loader = DataLoader(DATA_FILE)
    df = loader.load_data()

    if df is not None:
        recommender = FashionRecommender(df)
        user_profile = recommender.get_user_preferences()
        scored = recommender.calculate_scores(user_profile)
        recommendations = recommender.get_recommendations(scored, TOP_N_RECOMMENDATIONS, SCORE_THRESHOLD)

        print(f"\n--- Top {len(recommendations)} Recommendations ---")
        print(recommendations)

        recommender.save_recommendations(recommendations, OUTPUT_FILE)
    else:
        print("Failed to load data. Exiting.")
    print("--- Recommender Finished! Happy Shopping! ---")
