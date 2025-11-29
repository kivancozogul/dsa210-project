import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

seasons = []
for i in range(10, 25): # Seasons from 2010 to 2024
    seasons.append(f"20{i}-{i+1}")

data_games = []
for i, season in enumerate(seasons):
    # Trend: 3-point attempts increase every year
    base_3pt = 15 + (i * 1.4)
    
    for _ in range(50): # 50 games per season
        fg3a = int(np.random.normal(base_3pt, 6))
        fg3a = max(5, fg3a)
        
        # Hypothesis Logic: More 3s means Higher Score
        base_pts = 85 + (i * 0.5) 
        pts = int(base_pts + (fg3a * 1.2) + np.random.normal(0, 8))
        
        row = {
            'SEASON_ID': season,
            'PTS': pts,
            'FG3A': fg3a,
            'WL': random.choice(['W', 'L'])
        }
        data_games.append(row)

df_games = pd.DataFrame(data_games)

data_players = []
positions = ['Guard', 'Forward', 'Center']

for i, season in enumerate(seasons):
    for _ in range(30): # 30 players per season
        pos = random.choice(positions)
        
        # Center evolution
        if pos == 'Center':
            trend = 0 if i < 5 else (i - 4) * 0.6
            fg3a = max(0, int(np.random.normal(0 + trend, 1.5)))
        elif pos == 'Guard':
            fg3a = int(np.random.normal(4 + (i * 0.6), 2))
        else:
            fg3a = int(np.random.normal(2 + (i * 0.4), 1.5))
            
        row = {'SEASON_ID': season, 'SIMPLE_POS': pos, 'FG3A': max(0, fg3a)}
        data_players.append(row)

df_players = pd.DataFrame(data_players)

df_games.to_csv('nba_games_data.csv', index=False)
df_players.to_csv('nba_player_positions.csv', index=False)
print("✅ Datasets saved: nba_games_data.csv, nba_player_positions.csv")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(14, 6))
sns.boxplot(x='SEASON_ID', y='FG3A', data=df_games, palette="Blues")
plt.xticks(rotation=45)
plt.title('Trend of 3-Point Attempts per Game (2010-2025)')
plt.savefig('eda_1_trend.png')
print("✅ Chart 1 saved.")

plt.figure(figsize=(14, 6))
sns.lineplot(x='SEASON_ID', y='FG3A', hue='SIMPLE_POS', data=df_players, marker="o")
plt.xticks(rotation=45)
plt.title('Positional Evolution: Centers Shooting 3s')
plt.savefig('eda_2_positions.png')
print("✅ Chart 2 saved.")

plt.figure(figsize=(12, 7))
sns.regplot(x='FG3A', y='PTS', data=df_games, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.title('Impact of 3-Point Volume on Total Score')
plt.savefig('eda_3_score_impact.png')
print("✅ Chart 3 saved.")

print("🎉 Pipeline Complete! Ready to push to GitHub.")
