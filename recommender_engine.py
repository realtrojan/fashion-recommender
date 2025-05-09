# This code is developed by Afolabi Williams on the 10th of April, 2025
# Updated May 9th, 2025
# Python Methodologies by Professor Lars
# Final Project: Fashion Search & Recommendation Algorithim
# Source of data is from kaggle.com



import pandas as pd
import os

class FashionRecommender:
    def __init__(self, df):
        self.df = df

    def get_user_preferences(self):
        print("\n--- Build Your Fashion Profile ---")
        profile = {}
        index_group_options = ['ladies', 'mens', 'divided', 'sport', 'ladiesaccessories', 'mensaccessories']

        print("1. Who are you shopping for?")
        print(f"   Options: {', '.join(index_group_options)}")
        while True:
            value = input("   Enter one: ").strip().lower().replace("_", "")
            if value in index_group_options:
                profile['index_group'] = value
                break
            print("   Invalid option. Try again.")

        profile['product_types'] = [pt.strip().lower().replace("_", "") for pt in input("2. Clothing types (comma-separated): ").split(',') if pt.strip()]
        profile['colors'] = [c.strip().lower().replace("_", "") for c in input("3. Preferred colors (comma-separated): ").split(',') if c.strip()]

        print("--- Profile Complete ---")
        return profile

    def calculate_scores(self, profile):
        weights = {'index_group': 50, 'product_type': 25, 'color': 10}
        self.df['index_group_score'] = self.df['index_group_name'].apply(lambda x: weights['index_group'] if profile['index_group'] in x else 0)
        self.df['product_type_score'] = self.df['product_type_name'].apply(lambda x: weights['product_type'] if any(pt in x for pt in profile['product_types']) else 0)
        self.df['color_score'] = self.df['colour_group_name'].apply(lambda x: weights['color'] if any(c in x for c in profile['colors']) else 0)
        self.df['total_score'] = self.df[['index_group_score', 'product_type_score', 'color_score']].sum(axis=1)

        scored_df = self.df[self.df['total_score'] > 0]
        print(f"Total recommendations scored: {len(scored_df)}")
        if not scored_df.empty:
            print(f"Highest score: {scored_df['total_score'].max()}")
            print(f"Lowest score: {scored_df['total_score'].min()}")
        return scored_df

    def get_recommendations(self, scored_df, top_n=10, threshold=10):
        top_items = scored_df.sort_values(by='total_score', ascending=False)
        return top_items[top_items['total_score'] > threshold].head(top_n)

    def save_recommendations(self, recommendations, path):
        if recommendations.empty:
            print("No recommendations to save.")
            return
        try:
            recommendations.to_csv(path, index=False)
            print(f"Saved recommendations to {os.path.abspath(path)}")
        except Exception as e:
            print(f"Error saving file: {e}")
