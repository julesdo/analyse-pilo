import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
search_stats_data = pd.read_csv('./search_multi/search_multi.csv', sep=',')



# Renommer la colonne 'Clics ' pour supprimer l'espace
search_stats_data.rename(columns={'Clics ': 'Clics'}, inplace=True)

# Statistiques descriptives pour les colonnes numériques
search_numeric_stats = search_stats_data.describe()

# changer le type de la colonne 'Coût' en float
search_stats_data['Coût'] = search_stats_data['Coût'].str.replace('€', '').str.replace(',', '.').str.replace(' ', '').astype(float)

# changer le type de la colonne 'Conversion' en float
search_stats_data['Conversions'] = search_stats_data['Conversions'].str.replace(',', '.').astype(float)

# export des données nettoyées
search_stats_data.to_csv('search_multi_cleaned.csv', index=False)

# Analyse des mots-clés
keyword_counts = search_stats_data['Rechercher'].value_counts()

# Analyse des clics et impressions
clicks_impressions = search_stats_data[['Rechercher', 'Clics', 'Impressions']].sort_values(by='Impressions', ascending=False)

# Analyse des coûts et conversions
costs_conversions = search_stats_data[['Rechercher', 'Coût', 'Conversions']].sort_values(by='Coût', ascending=False)

# Visualisation des mots-clés les plus fréquents
plt.figure(figsize=(12, 6))
keyword_counts.head(20).plot(kind='bar', color='skyblue')
plt.title('Top 20 des mots-clés les plus fréquents')
plt.xlabel('Mots-clés')
plt.ylabel('Fréquence')
plt.xticks(rotation=90)
plt.show()

# Visualisation des clics par mot-clé
plt.figure(figsize=(12, 6))
plt.bar(clicks_impressions['Rechercher'].head(20), clicks_impressions['Clics'].head(20), color='lightgreen')
plt.title('Top 20 des mots-clés par nombre de clics')
plt.xlabel('Mots-clés')
plt.ylabel('Nombre de clics')
plt.xticks(rotation=90)
plt.show()

# Visualisation des coûts par mot-clé
plt.figure(figsize=(12, 6))
plt.bar(costs_conversions['Rechercher'].head(20), costs_conversions['Coût'].head(20), color='lightcoral')
plt.title('Top 20 des mots-clés par coût')
plt.xlabel('Mots-clés')
plt.ylabel('Coût (€)')
plt.xticks(rotation=90)
plt.show()

# Visualisation des conversions par mot-clé
plt.figure(figsize=(12, 6))
plt.bar(costs_conversions['Rechercher'].head(20), costs_conversions['Conversions'].head(20), color='gold')
plt.title('Top 20 des mots-clés par conversions')
plt.xlabel('Mots-clés')
plt.ylabel('Nombre de conversions')
plt.xticks(rotation=90)
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Search Statistics Numeric Stats", dataframe=search_numeric_stats)

search_numeric_stats, keyword_counts.head(10), clicks_impressions.head(10), costs_conversions.head(10)
