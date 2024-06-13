import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV des statistiques globales des 3 campagnes
campaigns_stats_file_path = './campagnes_stats/campagnes.csv'
campaigns_stats_data = pd.read_csv(campaigns_stats_file_path)

# Renommer la colonne 'Clics ' pour supprimer l'espace
campaigns_stats_data.rename(columns={'Clics ': 'Clics'}, inplace=True)

# Nettoyage des données: convertir les colonnes 'Coût', 'Clics', et 'Conversions' en numérique
campaigns_stats_data['Coût'] = campaigns_stats_data['Coût'].str.replace('€', '').str.replace(',', '.').str.replace(' ', '').astype(float)
campaigns_stats_data['Clics'] = campaigns_stats_data['Clics'].str.replace(' ', '').astype(int)
campaigns_stats_data['Conversions'] = campaigns_stats_data['Conversions'].str.replace(',', '.').astype(float)

# Statistiques descriptives pour les colonnes 'Coût', 'Clics', et 'Conversions'
campaigns_numeric_stats = campaigns_stats_data[['Coût', 'Clics', 'Conversions']].describe()

# export des données nettoyées
campaigns_stats_data.to_csv('campagnes_cleaned.csv', index=False)

# Visualisation des coûts par campagne
plt.figure(figsize=(12, 6))
plt.bar(campaigns_stats_data['Nom de la campagne'], campaigns_stats_data['Coût'], color='skyblue')
plt.title('Coût par campagne')
plt.xlabel('Nom de la campagne')
plt.ylabel('Coût (€)')
plt.xticks(rotation=45)
plt.show()

# Visualisation des clics par campagne
plt.figure(figsize=(12, 6))
plt.bar(campaigns_stats_data['Nom de la campagne'], campaigns_stats_data['Clics'], color='lightgreen')
plt.title('Clics par campagne')
plt.xlabel('Nom de la campagne')
plt.ylabel('Nombre de clics')
plt.xticks(rotation=45)
plt.show()

# Visualisation des conversions par campagne
plt.figure(figsize=(12, 6))
plt.bar(campaigns_stats_data['Nom de la campagne'], campaigns_stats_data['Conversions'], color='lightcoral')
plt.title('Conversions par campagne')
plt.xlabel('Nom de la campagne')
plt.ylabel('Nombre de conversions')
plt.xticks(rotation=45)
plt.show()

# Afficher les statistiques descriptives dans un dataframe
import ace_tools as tools; tools.display_dataframe_to_user(name="Campaigns Numeric Stats", dataframe=campaigns_numeric_stats)

# Afficher les résultats
print("Statistiques Descriptives:")
print(campaigns_numeric_stats)
print("\nDonnées des Campagnes:")
print(campaigns_stats_data[['Nom de la campagne', 'Coût', 'Clics', 'Conversions']])
