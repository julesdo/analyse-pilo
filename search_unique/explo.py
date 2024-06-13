import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
new_search_stats_data = pd.read_csv('./search_unique/search_unique.csv', sep=',')

new_search_stats_data.rename(columns={'Clics ': 'Clics'}, inplace=True)



# Nettoyage des données: convertir les colonnes 'Clics', 'Impressions', et 'Conversions' en numérique
new_search_stats_data['Clics'] = new_search_stats_data['Clics'].str.replace(' ', '').astype(int)
new_search_stats_data['Impressions'] = new_search_stats_data['Impressions'].str.replace(' ', '').astype(int)
new_search_stats_data['Conversions'] = new_search_stats_data['Conversions'].str.replace(',', '.').astype(float)

# Nettoyage des données: convertir la colonne 'Coût' en numérique
new_search_stats_data['Coût'] = new_search_stats_data['Coût'].str.replace('€', '').str.replace(',', '.').str.replace(' ', '').astype(float)

# Statistiques descriptives pour les colonnes numériques
new_search_numeric_stats = new_search_stats_data.describe()

# export des données nettoyées
new_search_stats_data.to_csv('search_unique_cleaned.csv', index=False)

# Analyse des mots-clés
new_keyword_counts = new_search_stats_data['Mot'].value_counts()

# Analyse des clics et impressions
new_clicks_impressions = new_search_stats_data[['Mot', 'Clics', 'Impressions']].sort_values(by='Impressions', ascending=False)

# Analyse des coûts et conversions
new_costs_conversions = new_search_stats_data[['Mot', 'Coût', 'Conversions']].sort_values(by='Coût', ascending=False)

# Visualisation des mots-clés les plus fréquents
plt.figure(figsize=(12, 6))
new_keyword_counts.head(20).plot(kind='bar', color='skyblue')
plt.title('Top 20 des mots-clés les plus fréquents')
plt.xlabel('Mots-clés')
plt.ylabel('Fréquence')
plt.xticks(rotation=90)
plt.show()

# Visualisation des clics par mot-clé
plt.figure(figsize=(12, 6))
plt.bar(new_clicks_impressions['Mot'].head(20), new_clicks_impressions['Clics'].head(20), color='lightgreen')
plt.title('Top 20 des mots-clés par nombre de clics')
plt.xlabel('Mots-clés')
plt.ylabel('Nombre de clics')
plt.xticks(rotation=90)
plt.show()

# Visualisation des coûts par mot-clé
plt.figure(figsize=(12, 6))
plt.bar(new_costs_conversions['Mot'].head(20), new_costs_conversions['Coût'].head(20), color='lightcoral')
plt.title('Top 20 des mots-clés par coût')
plt.xlabel('Mots-clés')
plt.ylabel('Coût (€)')
plt.xticks(rotation=90)
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="New Search Statistics Numeric Stats", dataframe=new_search_numeric_stats)

new_search_numeric_stats, new_keyword_counts.head(10), new_clicks_impressions.head(10), new_costs_conversions.head(10)
