import pandas as pd
df=pd.read_csv("synthetic_fps_spatiotemporal.csv")
print(df.head())
print("\nColumns:", df.columns.tolist())
print("\nTotal rows:", len(df))
print("\nUnique matches:", df["match_id"].nunique())
print("Unique players:", df["player_id"].nunique())
print("\nEvent distribution:")
print(df["event"].value_counts())
