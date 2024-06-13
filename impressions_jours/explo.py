import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
daily_impressions_data = pd.read_csv('./impressions_jours/impressions_jours.csv')

# Nettoyage des données: convertir la colonne 'Impressions' en numérique
daily_impressions_data['Impressions'] = daily_impressions_data['Impressions'].str.replace(' ', '').astype(int)

# Statistiques descriptives pour la colonne 'Impressions'
daily_impressions_numeric_stats = daily_impressions_data['Impressions'].describe()

# Analyse des impressions par jour
impressions_by_day = daily_impressions_data.set_index('Jour')

# export des données nettoyées
daily_impressions_data.to_csv('impressions_jours_cleaned.csv', index=False)

# Visualisation des impressions par jour
plt.figure(figsize=(12, 6))
impressions_by_day.plot(kind='bar', color='skyblue')
plt.title('Impressions par jour')
plt.xlabel('Jour')
plt.ylabel('Nombre d\'impressions')
plt.xticks(rotation=45)
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Daily Impressions Numeric Stats", dataframe=daily_impressions_numeric_stats)

daily_impressions_numeric_stats, impressions_by_day
