import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = './ventes_ga/VENTES GA.csv'
sales_data = pd.read_csv(file_path)


# Statistiques descriptives pour les colonnes numériques
sales_numeric_stats = sales_data.describe()

# export des données nettoyées
sales_data.to_csv('ventes_ga_cleaned.csv', index=False)

# Analyse des campagnes
campaign_counts_sales = sales_data['Campagne de la session'].value_counts()

# Analyse des articles
articles_consulted = sales_data[['Nom de l\'article', 'Articles consultés']].sort_values(by='Articles consultés', ascending=False)
articles_added_to_cart = sales_data[['Nom de l\'article', 'Articles ajoutés au panier']].sort_values(by='Articles ajoutés au panier', ascending=False)
articles_purchased = sales_data[['Nom de l\'article', 'Articles achetés']].sort_values(by='Articles achetés', ascending=False)

# Analyse des revenus
revenues_generated = sales_data[['Nom de l\'article', 'Revenu généré par l\'article']].sort_values(by='Revenu généré par l\'article', ascending=False)

# Visualisation des campagnes
plt.figure(figsize=(12, 6))
campaign_counts_sales.plot(kind='bar', color='skyblue')
plt.title('Nombre de sessions par campagne')
plt.xlabel('Campagnes')
plt.ylabel('Nombre de sessions')
plt.xticks(rotation=90)
plt.show()

# Visualisation des articles consultés
plt.figure(figsize=(12, 6))
plt.bar(articles_consulted['Nom de l\'article'], articles_consulted['Articles consultés'], color='lightgreen')
plt.title('Articles les plus consultés')
plt.xlabel('Nom de l\'article')
plt.ylabel('Nombre de consultations')
plt.xticks(rotation=90)
plt.show()

# Visualisation des revenus générés par article
plt.figure(figsize=(12, 6))
plt.bar(revenues_generated['Nom de l\'article'], revenues_generated['Revenu généré par l\'article'], color='lightcoral')
plt.title('Revenus générés par article')
plt.xlabel('Nom de l\'article')
plt.ylabel('Revenu généré')
plt.xticks(rotation=90)
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Sales Numeric Statistics", dataframe=sales_numeric_stats)

sales_numeric_stats, campaign_counts_sales.head(10), articles_consulted.head(10), articles_added_to_cart.head(10), articles_purchased.head(10), revenues_generated.head(10)
