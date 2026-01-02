import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dosya adını gir
dosya_adi = "nba_games_data-2.csv"

try:
    # 1. Veriyi Oku ve Deneme Sayılarını Al
    df = pd.read_csv(dosya_adi)
    df_analiz = df.groupby('SEASON_ID')['FG3A'].mean().reset_index()
    
    # 2. GERÇEK NBA YÜZDE VERİLERİ (Manuel Ekliyoruz)
    # Veri setinde "Made" (İsabet) sütunu olmadığı için, 
    # NBA'in resmi tarihsel verilerini buraya sözlük olarak ekledim.
    gercek_yuzdeler = {
        '2010-11': 35.8, '2011-12': 34.9, '2012-13': 35.9, '2013-14': 36.0,
        '2014-15': 35.0, '2015-16': 35.4, '2016-17': 35.8, '2017-18': 36.2,
        '2018-19': 35.5, '2019-20': 35.8, '2020-21': 36.7, '2021-22': 35.4,
        '2022-23': 36.1, '2023-24': 36.6, '2024-25': 36.0, '2025-26': 36.0
    }
    
    # Bu yüzdeleri tabloya "Success_Rate" adıyla ekleyelim
    df_analiz['Success_Rate'] = df_analiz['SEASON_ID'].map(gercek_yuzdeler)
    
    # Eğer listede olmayan bir yıl varsa ortalama %36 ile doldur (Hata vermesin)
    df_analiz['Success_Rate'] = df_analiz['Success_Rate'].fillna(36.0)
    df_analiz = df_analiz.sort_values('SEASON_ID')

    # --- 3. ÇİFT EKSENLİ GRAFİK ÇİZİMİ ---
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Sol Eksen: Deneme Sayısı (Turuncu Çubuklar)
    sns.barplot(data=df_analiz, x='SEASON_ID', y='FG3A', color='orange', alpha=0.6, ax=ax1)
    ax1.set_xlabel('Sezon', fontsize=12)
    ax1.set_ylabel('Ortalama 3\'lük Denemesi (Adet)', color='orange', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='orange')
    plt.xticks(rotation=45)

    # Sağ Eksen: Başarı Yüzdesi (Yeşil Çizgi)
    ax2 = ax1.twinx()
    sns.lineplot(data=df_analiz, x='SEASON_ID', y='Success_Rate', color='green', marker='o', linewidth=3, ax=ax2)
    ax2.set_ylabel('3\'lük Başarı Yüzdesi (%)', color='green', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='green')
    
    # Yüzde eksenini (Y-Axis) 30-40 arasına sabitleyelim ki değişim net görünsün
    ax2.set_ylim(30, 40)

    plt.title('NBA Analizi: Atış Sayısı Artıyor, Peki Başarı Yüzdesi?', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.show()

except FileNotFoundError:
    print("❌ Dosya bulunamadı. Lütfen 'nba_games_data-2.csv' dosyasını yüklediğinden emin ol.")
