import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("synthetic_fps_spatiotemporal.csv")

features = df[["x", "y"]]

kmeans = KMeans(n_clusters=4, random_state=42)
df["zone"] = kmeans.fit_predict(features)

print(df.head())
