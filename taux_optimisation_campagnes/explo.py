import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV des taux d'optimisation des 3 campagnes
optimization_rates_file_path = './taux_optimisation_campagnes/taux_optimisation.csv'
optimization_rates_data = pd.read_csv(optimization_rates_file_path)

# Nettoyage des données: convertir la colonne 'Taux d'optimisation' en numérique
optimization_rates_data['Taux d\'optimisation'] = optimization_rates_data['Taux d\'optimisation'].str.replace('%', '').str.replace(',', '.').str.replace(' ', '').astype(float)

# Statistiques descriptives pour la colonne 'Taux d\'optimisation'
optimization_rates_numeric_stats = optimization_rates_data['Taux d\'optimisation'].describe()

# export des données nettoyées
optimization_rates_data.to_csv('taux_optimisation_cleaned.csv', index=False)

# Visualisation des taux d'optimisation par campagne
plt.figure(figsize=(12, 6))
plt.bar(optimization_rates_data['Nom de la campagne'], optimization_rates_data['Taux d\'optimisation'], color='skyblue')
plt.title('Taux d\'optimisation par campagne')
plt.xlabel('Nom de la campagne')
plt.ylabel('Taux d\'optimisation (%)')
plt.xticks(rotation=45)
plt.show()

# Afficher les statistiques descriptives dans un dataframe
import ace_tools as tools; tools.display_dataframe_to_user(name="Optimization Rates Numeric Stats", dataframe=optimization_rates_numeric_stats)

# Afficher les résultats
print("Statistiques Descriptives:")
print(optimization_rates_numeric_stats)
print("\nDonnées des Taux d'Optimisation par Campagne:")
print(optimization_rates_data[['Nom de la campagne', 'Taux d\'optimisation']])
