import pandas as pd
from nba_api.stats.endpoints import leaguegamelog, leaguedashplayerstats
import time

print("🏀 Veri Çekme Operasyonu Başladı (1980-2024)...")

# 1. HEDEF SEZONLAR (Hipotezini desteklemek için 10'ar yıllık aralıklar aldık)
target_seasons = ['1980-81', '1990-91', '2000-01', '2010-11', '2023-24']

all_games = []
all_players = []

# 2. DÖNGÜ İLE VERİ ÇEKME
for season in target_seasons:
    print(f"⏳ {season} verisi çekiliyor...")
    
    # A. MAÇ SKORLARI (Total Score analizi için)
    # NBA API'den o sezonun tüm maçlarını istiyoruz
    game_log = leaguegamelog.LeagueGameLog(season=season, player_or_team_abbreviation='T')
    games_df = game_log.get_data_frames()[0]
    games_df['SEASON_ID'] = season # Hangi sezon olduğunu not düşüyoruz
    all_games.append(games_df)
    
    # B. OYUNCU İSTATİSTİKLERİ (Pozisyon analizi için - Enrichment)
    # O sezon kim ne kadar üçlük atmış, hangi pozisyonda oynuyormuş?
    player_log = leaguedashplayerstats.LeagueDashPlayerStats(season=season)
    players_df = player_log.get_data_frames()[0]
    players_df['SEASON_ID'] = season
    all_players.append(players_df)
    
    # API bizi banlamasın diye 1 saniye nefes alıyoruz
    time.sleep(1)

# 3. VERİLERİ BİRLEŞTİRME
final_games_df = pd.concat(all_games, ignore_index=True)
final_players_df = pd.concat(all_players, ignore_index=True)

# 4. TEMİZLEME & POZİSYON AYARLAMA (Zenginleştirme Şartı) 
# Pozisyonları basit hale getiriyoruz: Guard, Forward, Center
def simplify_pos(pos):
    if isinstance(pos, str):
        if 'G' in pos: return 'Guard'
        elif 'F' in pos: return 'Forward'
        elif 'C' in pos: return 'Center'
    return 'Other'

final_players_df['SIMPLE_POS'] = final_players_df['PLAYER_POSITION'].apply(simplify_pos)

# 5. DOSYALARI KAYDETME (Somut Kanıt)
final_games_df.to_csv('nba_games_1980_2024.csv', index=False)
final_players_df.to_csv('nba_players_1980_2024.csv', index=False)

print("\n✅ İŞLEM TAMAMLANDI!")
print("📂 'nba_games_1980_2024.csv' dosyası oluşturuldu (Maç Skorları)")
print("📂 'nba_players_1980_2024.csv' dosyası oluşturuldu (Pozisyon Verisi)")
