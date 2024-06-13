import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
gender_impressions_data = pd.read_csv('./impressions_sexe/impressions_sexe.csv', sep=',')


# Nettoyage des données: convertir les colonnes 'Impressions' et 'Pourcentage du total connu' en numérique
gender_impressions_data['Impressions'] = gender_impressions_data['Impressions'].str.replace(' ', '').astype(int)
gender_impressions_data['Pourcentage du total connu'] = gender_impressions_data['Pourcentage du total connu'].str.replace('%', '').str.replace(',', '.').str.replace(' ', '').astype(float)

# Statistiques descriptives pour la colonne 'Impressions'
gender_impressions_numeric_stats = gender_impressions_data['Impressions'].describe()

# export des données nettoyées
gender_impressions_data.to_csv('impressions_sexe_cleaned.csv', index=False)

# Analyse des impressions par sexe
impressions_by_gender = gender_impressions_data.set_index('Sexe')

# Visualisation des impressions par sexe
plt.figure(figsize=(12, 6))
impressions_by_gender['Impressions'].plot(kind='bar', color='skyblue')
plt.title('Impressions par sexe')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'impressions')
plt.xticks(rotation=0)
plt.show()

# Visualisation du pourcentage des impressions connues par sexe
plt.figure(figsize=(12, 6))
impressions_by_gender['Pourcentage du total connu'].plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightcoral'], startangle=90)
plt.title('Pourcentage des impressions connues par sexe')
plt.ylabel('')
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Gender Impressions Numeric Stats", dataframe=gender_impressions_numeric_stats)

gender_impressions_numeric_stats, impressions_by_gender
