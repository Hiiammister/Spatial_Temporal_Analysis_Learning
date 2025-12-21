import pandas as pd

df = pd.read_csv("synthetic_fps_spatiotemporal.csv")

early = df[df["timestamp"] < 200]
mid   = df[(df["timestamp"] >= 200) & (df["timestamp"] < 400)]
late  = df[df["timestamp"] >= 400]

print("Early game events:\n", early["event"].value_counts())
print("\nMid game events:\n", mid["event"].value_counts())
print("\nLate game events:\n", late["event"].value_counts())
