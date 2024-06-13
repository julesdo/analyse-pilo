import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
gender_age_impressions_data = pd.read_csv('./impressions_ages_tranches/impressions_ages_tranches.csv', sep=',')



# Nettoyage des données: convertir les colonnes 'Impressions' et 'Pourcentage du total connu' en numérique
gender_age_impressions_data['Impressions'] = gender_age_impressions_data['Impressions'].str.replace(' ', '').astype(int)
gender_age_impressions_data['Pourcentage du total connu'] = gender_age_impressions_data['Pourcentage du total connu'].str.replace('%', '').str.replace(',', '.').str.replace(' ', '').astype(float)

# Statistiques descriptives pour la colonne 'Impressions'
gender_age_impressions_numeric_stats = gender_age_impressions_data['Impressions'].describe()

# Analyse des impressions par sexe et tranche d'âge
impressions_by_gender_age = gender_age_impressions_data.pivot_table(index='Sexe', columns='Tranche d\'âge', values='Impressions', aggfunc='sum')
percentage_by_gender_age = gender_age_impressions_data.pivot_table(index='Sexe', columns='Tranche d\'âge', values='Pourcentage du total connu', aggfunc='sum')

# export des données nettoyées
gender_age_impressions_data.to_csv('impressions_ages_tranches_cleaned.csv', index=False)

# Visualisation des impressions par sexe et tranche d'âge
plt.figure(figsize=(12, 6))
impressions_by_gender_age.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Impressions par sexe et tranche d\'âge')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'impressions')
plt.xticks(rotation=0)
plt.legend(title='Tranche d\'âge')
plt.show()

# Visualisation du pourcentage des impressions connues par sexe et tranche d'âge
plt.figure(figsize=(12, 6))
percentage_by_gender_age.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Pourcentage des impressions connues par sexe et tranche d\'âge')
plt.xlabel('Sexe')
plt.ylabel('Pourcentage')
plt.xticks(rotation=0)
plt.legend(title='Tranche d\'âge')
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Gender Age Impressions Numeric Stats", dataframe=gender_age_impressions_numeric_stats)

gender_age_impressions_numeric_stats, impressions_by_gender_age, percentage_by_gender_age
