import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
age_impressions_data = pd.read_csv('./impressions_tranches/impressions_tranches.csv', sep=',')



# Nettoyage des données: convertir les colonnes 'Impressions' et 'Pourcentage du total connu' en numérique
age_impressions_data['Impressions'] = age_impressions_data['Impressions'].str.replace(' ', '').astype(int)
age_impressions_data['Pourcentage du total connu'] = age_impressions_data['Pourcentage du total connu'].str.replace('%', '').str.replace(',', '.').str.replace(' ', '').astype(float)

# Statistiques descriptives pour la colonne 'Impressions'
age_impressions_numeric_stats = age_impressions_data['Impressions'].describe()

# export des données nettoyées
age_impressions_data.to_csv('impressions_tranches_cleaned.csv', index=False)

# Analyse des impressions par tranche d'âge
impressions_by_age = age_impressions_data.set_index('Tranche d\'âge')

# Visualisation des impressions par tranche d'âge
plt.figure(figsize=(12, 6))
impressions_by_age['Impressions'].plot(kind='bar', color='skyblue')
plt.title('Impressions par tranche d\'âge')
plt.xlabel('Tranche d\'âge')
plt.ylabel('Nombre d\'impressions')
plt.xticks(rotation=45)
plt.show()

# Visualisation du pourcentage des impressions connues par tranche d'âge
plt.figure(figsize=(12, 6))
impressions_by_age['Pourcentage du total connu'].plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightcoral', 'lightgreen', 'lightyellow', 'lightgrey', 'lightsalmon'], startangle=90)
plt.title('Pourcentage des impressions connues par tranche d\'âge')
plt.ylabel('')
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Age Impressions Numeric Stats", dataframe=age_impressions_numeric_stats)

age_impressions_numeric_stats, impressions_by_age
