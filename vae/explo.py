import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
file_path = './vae/vae_cleaned.csv'
cleaned_data = pd.read_csv(file_path)

# Statistiques descriptives pour les colonnes numériques
numeric_stats = cleaned_data.describe()

# Analyse des campagnes
campaign_counts = cleaned_data['Campaign'].value_counts()

# Analyse des budgets
budget_analysis = cleaned_data['Budget'].describe()

# Analyse des conversions
conversion_analysis = cleaned_data[['Standard conversion goals', 'Display All conv value']].describe()

# Visualisation des campagnes
plt.figure(figsize=(12, 6))
campaign_counts.plot(kind='bar', color='skyblue')
plt.title('Nombre de campagnes par type')
plt.xlabel('Campagnes')
plt.ylabel('Nombre')
plt.xticks(rotation=90)
plt.show()

# Visualisation des budgets
plt.figure(figsize=(12, 6))
plt.hist(cleaned_data['Budget'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution des budgets des campagnes')
plt.xlabel('Budget')
plt.ylabel('Fréquence')
plt.show()

# Visualisation des conversions
plt.figure(figsize=(12, 6))
plt.hist(cleaned_data['Display All conv value'], bins=20, color='lightcoral', edgecolor='black')
plt.title('Distribution des valeurs de toutes les conversions')
plt.xlabel('Valeur de conversion')
plt.ylabel('Fréquence')
plt.show()

# Affichage des statistiques
import ace_tools as tools; tools.display_dataframe_to_user(name="Numeric Statistics (Mean, Max, etc.)", dataframe=numeric_stats)
