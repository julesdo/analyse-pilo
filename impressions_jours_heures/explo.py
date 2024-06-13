import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
impressions_data = pd.read_csv('./impressions_jours_heures/impressions_jours_heures.csv', sep=',')
impressions_data.rename(columns={'Clics ': 'Clics'}, inplace=True)



# Statistiques descriptives pour la colonne 'Impressions'
impressions_numeric_stats = impressions_data['Impressions'].describe()

# export des données nettoyées
impressions_data.to_csv('impressions_jours_heures_cleaned.csv', index=False)

# Analyse des impressions par jour
impressions_by_day = impressions_data.groupby('Jour')['Impressions'].sum().sort_values(ascending=False)

# Analyse des impressions par heure
impressions_by_hour = impressions_data.groupby('Heure de début')['Impressions'].sum().sort_values(ascending=False)

# Analyse combinée des impressions par jour et par heure
impressions_by_day_hour = impressions_data.pivot_table(index='Jour', columns='Heure de début', values='Impressions', aggfunc='sum')

# Visualisation des impressions par jour
plt.figure(figsize=(12, 6))
impressions_by_day.plot(kind='bar', color='skyblue')
plt.title('Impressions par jour')
plt.xlabel('Jour')
plt.ylabel('Nombre d\'impressions')
plt.xticks(rotation=45)
plt.show()

# Visualisation des impressions par heure
plt.figure(figsize=(12, 6))
impressions_by_hour.plot(kind='bar', color='lightgreen')
plt.title('Impressions par heure')
plt.xlabel('Heure de début')
plt.ylabel('Nombre d\'impressions')
plt.xticks(rotation=45)
plt.show()

# Visualisation combinée des impressions par jour et par heure
plt.figure(figsize=(12, 8))
plt.title('Impressions par jour et par heure')
sns.heatmap(impressions_by_day_hour, annot=True, fmt="d", cmap="YlGnBu")
plt.xlabel('Heure de début')
plt.ylabel('Jour')
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Impressions Numeric Stats", dataframe=impressions_numeric_stats)

impressions_numeric_stats, impressions_by_day, impressions_by_hour
