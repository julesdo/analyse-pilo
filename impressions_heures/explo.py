import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
hourly_impressions_data = pd.read_csv('./impressions_heures/impressions_heures.csv')


# Nettoyage des données: convertir la colonne 'Impressions' en numérique
hourly_impressions_data['Impressions'] = hourly_impressions_data['Impressions'].str.replace(' ', '').astype(int)

# Statistiques descriptives pour la colonne 'Impressions'
hourly_impressions_numeric_stats = hourly_impressions_data['Impressions'].describe()

# export des données nettoyées
hourly_impressions_data.to_csv('impressions_heures_cleaned.csv', index=False)

# Analyse des impressions par heure
impressions_by_hour = hourly_impressions_data.set_index('Heure de début')

# Visualisation des impressions par heure
plt.figure(figsize=(12, 6))
impressions_by_hour.plot(kind='bar', color='skyblue')
plt.title('Impressions par heure')
plt.xlabel('Heure de début')
plt.ylabel('Nombre d\'impressions')
plt.xticks(rotation=45)
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Hourly Impressions Numeric Stats", dataframe=hourly_impressions_numeric_stats)

hourly_impressions_numeric_stats, impressions_by_hour
