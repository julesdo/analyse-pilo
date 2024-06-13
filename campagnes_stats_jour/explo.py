import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV des statistiques cumulées par jours
time_series_file_path = './campagnes_stats_jour/campagnes_stats_jour.csv'
time_series_data_raw = pd.read_csv(time_series_file_path, dtype=str)

# Remplacer les abréviations françaises des mois et des jours par des équivalents compréhensibles
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('janv.', 'Jan', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('févr.', 'Feb', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('mars', 'Mar', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('avr.', 'Apr', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('mai', 'May', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('juin', 'Jun', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('juil.', 'Jul', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('août', 'Aug', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('sept.', 'Sep', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('oct.', 'Oct', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('nov.', 'Nov', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('déc.', 'Dec', regex=False)

time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('lun.', 'Mon', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('mar.', 'Tue', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('mer.', 'Wed', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('jeu.', 'Thu', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('ven.', 'Fri', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('sam.', 'Sat', regex=False)
time_series_data_raw['Date'] = time_series_data_raw['Date'].str.replace('dim.', 'Sun', regex=False)

# Conversion de la colonne 'Date' en format datetime
time_series_data_raw['Date'] = pd.to_datetime(time_series_data_raw['Date'], format='%a %d %b %Y', errors='coerce')

# Renommer les colonnes pour supprimer les espaces
time_series_data_raw.rename(columns={'Clics ': 'Clics', 'Impressions': 'Impressions', 'Conversions': 'Conversions', 'Coût': 'Coût'}, inplace=True)

# Nettoyage des données: convertir les colonnes 'Conversions' et 'Coût' en numérique
time_series_data_raw['Conversions'] = time_series_data_raw['Conversions'].str.replace(',', '.').astype(float)
time_series_data_raw['Coût'] = time_series_data_raw['Coût'].str.replace('€', '').str.replace(',', '.').str.replace(' ', '').astype(float)
time_series_data_raw['Clics'] = time_series_data_raw['Clics'].astype(int)
time_series_data_raw['Impressions'] = time_series_data_raw['Impressions'].astype(int)

# Statistiques descriptives pour les colonnes 'Clics', 'Impressions', 'Conversions', et 'Coût'
time_series_numeric_stats = time_series_data_raw[['Clics', 'Impressions', 'Conversions', 'Coût']].describe()

# export des données nettoyées
time_series_data_raw.to_csv('campagnes_stats_jour_cleaned.csv', index=False)

# Visualisation des clics par jour
plt.figure(figsize=(12, 6))
plt.plot(time_series_data_raw['Date'], time_series_data_raw['Clics'], marker='o', linestyle='-', color='skyblue')
plt.title('Clics par jour')
plt.xlabel('Date')
plt.ylabel('Nombre de clics')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Visualisation des impressions par jour
plt.figure(figsize=(12, 6))
plt.plot(time_series_data_raw['Date'], time_series_data_raw['Impressions'], marker='o', linestyle='-', color='lightgreen')
plt.title('Impressions par jour')
plt.xlabel('Date')
plt.ylabel('Nombre d\'impressions')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Visualisation des conversions par jour
plt.figure(figsize=(12, 6))
plt.plot(time_series_data_raw['Date'], time_series_data_raw['Conversions'], marker='o', linestyle='-', color='lightcoral')
plt.title('Conversions par jour')
plt.xlabel('Date')
plt.ylabel('Nombre de conversions')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Visualisation des coûts par jour
plt.figure(figsize=(12, 6))
plt.plot(time_series_data_raw['Date'], time_series_data_raw['Coût'], marker='o', linestyle='-', color='gold')
plt.title('Coût par jour')
plt.xlabel('Date')
plt.ylabel('Coût (€)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Afficher les statistiques descriptives dans un dataframe
import ace_tools as tools; tools.display_dataframe_to_user(name="Time Series Numeric Stats", dataframe=time_series_numeric_stats)

# Afficher les résultats
print("Statistiques Descriptives:")
print(time_series_numeric_stats)
print("\nDonnées par Jour:")
print(time_series_data_raw[['Date', 'Clics', 'Impressions', 'Conversions', 'Coût']])
