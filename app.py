from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
from Heatmap import *

app = Flask(__name__)

# Load data once
df = pd.read_csv("large_synthetic_fps_spatiotemporal.csv")

@app.route("/Heatmap")
def spatial():
    heatmap_html = spatial_heatmap(df)
    return render_template(
        "spatial.html",
        heatmap=heatmap_html
    )


def spatial_heatmap(df):
    fig = px.density_heatmap(
        df,
        x="x",
        y="y",
        nbinsx=50,
        nbinsy=50,
        color_continuous_scale="Reds",
        title="Player Position Heatmap"
    )

    fig.update_layout(
        xaxis_title="Map X",
        yaxis_title="Map Y",
        template="plotly_dark"
    )

    return fig.to_html(full_html=False)

@app.route("/")
def index():
    stats = {
        "matches": df["match_id"].nunique(),
        "players": df["player_id"].nunique(),
        "events": len(df)
    }
    return render_template("index.html", stats=stats)

@app.route("/spatial")
def spatial():
    return render_template("spatial.html")

@app.route("/player")
def player():
    match_id = request.args.get("match_id", 1, type=int)
    player_id = request.args.get("player_id", 1, type=int)

    player_df = df[
        (df["match_id"] == match_id) &
        (df["player_id"] == player_id)
    ]

    return render_template(
        "player.html",
        match_id=match_id,
        player_id=player_id,
        points=len(player_df)
    )


@app.route("/metrics")
def metrics():
    kills = df[df["event"] == "kill"]
    top_players = kills["player_id"].value_counts().head(5)

    return render_template(
        "metrics.html",
        top_players=top_players.to_dict()
    )

if __name__ == "__main__":
    app.run(debug=True)
