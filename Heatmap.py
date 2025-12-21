import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("synthetic_fps_spatiotemporal.csv")
plt.figure(figsize=(8,6))
sns.kdeplot(
    x=df["x"],
    y=df["y"],
    fill=True,
    cmap="Reds",
    thresh=0.05

)
plt.title("Player Movement heatmap")
plt.xlabel("x position")
plt.ylabel("y position")
plt.tight_layout()
plt.show()