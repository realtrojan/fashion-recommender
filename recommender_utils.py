# This code is developed by Afolabi Williams on the 10th of April, 2025
# Updated May 9th, 2025
# Python Methodologies by Professor Lars
# Final Project: Fashion Search & Recommendation Algorithim
# Source of data is from kaggle.com



import pandas as pd
import os

REQUIRED_COLUMNS = [
    'article_id', 'prod_name', 'product_type_name', 'url', 'price', 'stockState',
    'colour_group_name', 'isOnline', 'colors', 'colorShades',
    'index_group_name', 'detail_desc'
]

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        print(f"Loading data from: {self.filepath}")
        if not os.path.exists(self.filepath):
            print(f"Error: File not found at '{os.path.abspath(self.filepath)}'")
            return None

        try:
            df = pd.read_csv(self.filepath)
            missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
            if missing_cols:
                print(f"Warning: Missing columns: {', '.join(missing_cols)}")

            for col in ['product_type_name', 'index_group_name', 'colour_group_name', 'colors']:
                if col in df.columns:
                    df[col] = df[col].str.replace("_", "").str.lower().fillna('unknown')

            df = df.drop_duplicates(subset='article_id', keep='first')

            print("--- Dataset Overview ---")
            print("Index Group Options:", df['index_group_name'].dropna().unique())
            print("Product Type Options:", df['product_type_name'].dropna().unique())
            print("Color Options:", df['colour_group_name'].dropna().unique())

            return df
        except Exception as e:
            print(f"Error loading file: {e}")
            return None
