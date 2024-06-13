import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV des métriques par type d'appareils
devices_metrics_file_path = './appareils_stats/appareils.csv'
devices_metrics_data = pd.read_csv(devices_metrics_file_path)

# Renommer la colonne 'Clics ' pour supprimer l'espace
devices_metrics_data.rename(columns={'Clics ': 'Clics'}, inplace=True)

# Nettoyage des données: convertir les colonnes 'Coût', 'Clics', et 'Conversions' en numérique
devices_metrics_data['Coût'] = devices_metrics_data['Coût'].str.replace('€', '').str.replace(',', '.').str.replace(' ', '').str.replace(' ', '').astype(float)
devices_metrics_data['Clics'] = devices_metrics_data['Clics'].str.replace(' ', '').astype(int)
devices_metrics_data['Conversions'] = devices_metrics_data['Conversions'].str.replace(',', '.').astype(float)

# Statistiques descriptives pour les colonnes 'Coût', 'Clics', et 'Conversions'
devices_numeric_stats = devices_metrics_data[['Coût', 'Clics', 'Conversions']].describe()

# export des données nettoyées
devices_metrics_data.to_csv('appareils_cleaned.csv', index=False)

# Visualisation des coûts par type d'appareil
plt.figure(figsize=(12, 6))
plt.bar(devices_metrics_data['Type d\'appareil'], devices_metrics_data['Coût'], color='skyblue')
plt.title('Coût par type d\'appareil')
plt.xlabel('Type d\'appareil')
plt.ylabel('Coût (€)')
plt.xticks(rotation=45)
plt.show()

# Visualisation des clics par type d'appareil
plt.figure(figsize=(12, 6))
plt.bar(devices_metrics_data['Type d\'appareil'], devices_metrics_data['Clics'], color='lightgreen')
plt.title('Clics par type d\'appareil')
plt.xlabel('Type d\'appareil')
plt.ylabel('Nombre de clics')
plt.xticks(rotation=45)
plt.show()

# Visualisation des conversions par type d'appareil
plt.figure(figsize=(12, 6))
plt.bar(devices_metrics_data['Type d\'appareil'], devices_metrics_data['Conversions'], color='lightcoral')
plt.title('Conversions par type d\'appareil')
plt.xlabel('Type d\'appareil')
plt.ylabel('Nombre de conversions')
plt.xticks(rotation=45)
plt.show()

# Afficher les statistiques descriptives dans un dataframe
import ace_tools as tools; tools.display_dataframe_to_user(name="Devices Metrics Numeric Stats", dataframe=devices_numeric_stats)

# Afficher les résultats
print("Statistiques Descriptives:")
print(devices_numeric_stats)
print("\nDonnées par Type d'Appareil:")
print(devices_metrics_data[['Type d\'appareil', 'Coût', 'Clics', 'Conversions']])
