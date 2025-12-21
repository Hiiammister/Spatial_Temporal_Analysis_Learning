import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("synthetic_fps_spatiotemporal.csv")
player=df[(df["match_id"]==1) & (df["player_id"]==1)]

plt.figure(figsize=(7, 7))
plt.plot(player["x"], player["y"], marker="o", markersize=2)
plt.title("Player Trajectory (Match 1, Player 1)")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.tight_layout()
plt.show()