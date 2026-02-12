# Spatial_Temporal_Analysis_Learning

# Spatial & Temporal Analysis (Learning Repo)

A small **learning / experimentation repo** for working with **spatio-temporal data** (e.g., player / agent movement over time). It includes scripts to generate **trajectories**, **heatmaps**, **temporal analysis**, and **simple behavior clustering** using synthetic datasets. :contentReference[oaicite:0]{index=0}

---

## What’s inside

- **Trajectory visualization** (plot paths / movement traces over time)
- **Spatial heatmaps** (density / overlap heatmaps of movement)
- **Temporal analysis** (basic time-based patterns)
- **Behavior clustering** (group similar movement behaviors)

Repo also includes sample **CSV datasets** and a few **PNG outputs** for reference. :contentReference[oaicite:1]{index=1}

---

## Repository structure

Key files in the root: :contentReference[oaicite:2]{index=2}

- `trajectory.py` — trajectory/path plotting
- `Heatmap.py` — heatmap generation
- `temporal_analysis.py` — temporal stats/plots
- `behaviour_cluster.py` — clustering-based behavior grouping
- `check_data.py` — quick dataset sanity checks
- `synthetic_fps_spatiotemporal.csv` — sample dataset
- `large_synthetic_fps_spatiotemporal.csv` — larger sample dataset
- Output examples:
  - `player_trajectory.png`
  - `player_movement.png`
  - `overlap_heat_trajectory.png`
  - `overlap_heatmap_trajectory` (artifact/output folder)
- `Synthetic_Data/` — additional synthetic data folder :contentReference[oaicite:3]{index=3}

---

## Quickstart

### 1 Create a virtual environment (recommended)
```bash
python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows
# .venv\Scripts\activate
```
### 2 Install dependencies
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
## Data format
```bash
The scripts use the provided synthetic CSVs, which generally represent movement data with:
an entity id (player/agent)
x, y coordinates
a time index (frame / timestamp)
```
## How to run:
```bash
python check_data.py
python trajectory.py
python Heatmap.py
python temporal_analysis.py
python behaviour_cluster.py
```
