import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
campaign_keywords_data = pd.read_csv('./campaign_keywords/campaign_keywords.csv', sep=',')
campaign_keywords_data.rename(columns={'Clics ': 'Clics'}, inplace=True)



# Statistiques descriptives pour les colonnes numériques
campaign_keywords_numeric_stats = campaign_keywords_data.describe()

# Analyse des mots-clés
campaign_keyword_counts = campaign_keywords_data['Mot clé pour le Réseau de Recherche'].value_counts()

# Analyse des clics
campaign_clicks = campaign_keywords_data[['Mot clé pour le Réseau de Recherche', 'Clics']].sort_values(by='Clics', ascending=False)

# changer le type de la colonne 'Coût' en float
campaign_keywords_data['Coût'] = campaign_keywords_data['Coût'].str.replace('€', '').str.replace(',', '.').str.replace(' ', '').astype(float)

# changer le type de la colonne 'CTR' en float
campaign_keywords_data['CTR'] = campaign_keywords_data['CTR'].str.replace('%', '').str.replace(',', '.').astype(float)

# Analyse des coûts et CTR
campaign_costs_ctr = campaign_keywords_data[['Mot clé pour le Réseau de Recherche', 'Coût', 'CTR']].sort_values(by='Coût', ascending=False)

# export des données nettoyées
campaign_keywords_data.to_csv('campaign_keywords_cleaned.csv', index=False)

# Visualisation des mots-clés les plus fréquents
plt.figure(figsize=(12, 6))
campaign_keyword_counts.head(20).plot(kind='bar', color='skyblue')
plt.title('Top 20 des mots-clés les plus fréquents')
plt.xlabel('Mots-clés')
plt.ylabel('Fréquence')
plt.xticks(rotation=90)
plt.show()

# Visualisation des clics par mot-clé
plt.figure(figsize=(12, 6))
plt.bar(campaign_clicks['Mot clé pour le Réseau de Recherche'].head(20), campaign_clicks['Clics'].head(20), color='lightgreen')
plt.title('Top 20 des mots-clés par nombre de clics')
plt.xlabel('Mots-clés')
plt.ylabel('Nombre de clics')
plt.xticks(rotation=90)
plt.show()

# Visualisation des coûts par mot-clé
plt.figure(figsize=(12, 6))
plt.bar(campaign_costs_ctr['Mot clé pour le Réseau de Recherche'].head(20), campaign_costs_ctr['Coût'].head(20), color='lightcoral')
plt.title('Top 20 des mots-clés par coût')
plt.xlabel('Mots-clés')
plt.ylabel('Coût (€)')
plt.xticks(rotation=90)
plt.show()

# Visualisation des CTR par mot-clé
plt.figure(figsize=(12, 6))
plt.bar(campaign_costs_ctr['Mot clé pour le Réseau de Recherche'].head(20), campaign_costs_ctr['CTR'].head(20), color='gold')
plt.title('Top 20 des mots-clés par CTR')
plt.xlabel('Mots-clés')
plt.ylabel('CTR (%)')
plt.xticks(rotation=90)
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Campaign Keywords Numeric Stats", dataframe=campaign_keywords_numeric_stats)

campaign_keywords_numeric_stats, campaign_keyword_counts.head(10), campaign_clicks.head(10), campaign_costs_ctr.head(10)
