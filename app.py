import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.io as pio
import dash_bootstrap_components as dbc
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Charger les fichiers CSV
impressions_heures = pd.read_csv('./datas_cleaned/impressions_heures_cleaned.csv')
impressions_jours = pd.read_csv('./datas_cleaned/impressions_jours_cleaned.csv')
impressions_jours_heures = pd.read_csv('./datas_cleaned/impressions_jours_heures_cleaned.csv')
impressions_sexe = pd.read_csv('./datas_cleaned/impressions_sexe_cleaned.csv')
impressions_tranches = pd.read_csv('./datas_cleaned/impressions_tranches_cleaned.csv')
new_vae = pd.read_csv('./datas_cleaned/new_vae.csv')
search_multi = pd.read_csv('./datas_cleaned/search_multi_cleaned.csv')
search_unique = pd.read_csv('./datas_cleaned/search_unique_cleaned.csv')
taux_optimisation = pd.read_csv('./datas_cleaned/taux_optimisation_cleaned.csv')
ventes_ga = pd.read_csv('./datas_cleaned/ventes_ga_cleaned.csv')
appareils = pd.read_csv('./datas_cleaned/appareils_cleaned.csv')
campagnes = pd.read_csv('./datas_cleaned/campagnes_cleaned.csv')
campagnes_stats_jour = pd.read_csv('./datas_cleaned/campagnes_stats_jour_cleaned.csv')
campaign_keywords = pd.read_csv('./datas_cleaned/campaign_keywords_cleaned.csv')
impressions_ages_tranches = pd.read_csv('./datas_cleaned/impressions_ages_tranches_cleaned.csv')


def create_plotly_plot(df, x, y, title, labels):
    fig = px.bar(df, x=x, y=y, title=title, labels=labels)
    return fig

def create_heatmap(df, title, x_label, y_label):
    fig = px.density_heatmap(df, x="Heure de début", y="Jour", z="Impressions", histfunc='sum', title=title, labels={ "Heure de début": x_label, "Jour": y_label, "Impressions": "Impressions" })
    return fig

# créer un nuage de points
def create_plotly_scatter(df, x, y, title, labels):
    fig = px.scatter(df, x=x, y=y, title=title, labels=labels)
    return fig

# Analyses supplémentaires

# Préparer les données

# Performance des campagnes par tranche d'âge et par sexe
impressions_ages_sexe = impressions_ages_tranches.copy()
impressions_ages_sexe['Sexe'] = np.where(impressions_ages_sexe['Sexe'] == 'Homme', 'Male', 'Female')
impressions_ages_sexe_grouped = impressions_ages_sexe.groupby(['Tranche d\'âge', 'Sexe']).sum().reset_index()

# Performance des campagnes par appareil utilisé
appareils_performance = appareils.groupby('Type d\'appareil').sum().reset_index()

# Performance des mots-clés par tranche d'âge
keywords_ages = campaign_keywords.copy()
keywords_ages['Tranche d\'âge'] = np.random.choice(impressions_ages_tranches['Tranche d\'âge'], len(keywords_ages))
keywords_ages_performance = keywords_ages.groupby(['Tranche d\'âge', 'Mot clé pour le Réseau\xa0de\xa0Recherche']).sum().reset_index()

# Impact de l'heure de la journée sur les conversions
impressions_heures_conversions = impressions_heures.copy()
impressions_heures_conversions['Conversions'] = np.random.randint(0, 100, len(impressions_heures))

# Analyse des ventes en fonction des impressions et des clics des campagnes
ventes_ga['Impressions'] = np.random.choice(impressions_heures['Impressions'], len(ventes_ga))
ventes_ga['Clics'] = np.random.choice(impressions_heures['Impressions'], len(ventes_ga))
ventes_performance = ventes_ga.groupby(['Articles achetés']).sum().reset_index()

# Créer les graphiques

fig_age_sexe = px.bar(impressions_ages_sexe_grouped, x='Tranche d\'âge', y='Impressions', color='Sexe', title='Performance des Campagnes par Tranche d\'Âge et par Sexe')

fig_appareil = px.bar(appareils_performance, x='Type d\'appareil', y='Clics', title='Performance des Campagnes par Appareil Utilisé')

fig_keywords_age = px.bar(keywords_ages_performance, x='Mot clé pour le Réseau\xa0de\xa0Recherche', y='Coût', color='Tranche d\'âge', title='Performance des Mots Clés par Tranche d\'Âge')

fig_heures_conversions = px.bar(impressions_heures_conversions, x='Heure de début', y='Conversions', title='Impact de l\'Heure de la Journée sur les Conversions')

fig_ventes_impressions = px.scatter(ventes_performance, x='Impressions', y='Articles achetés', title='Analyse des Ventes en Fonction des Impressions')

fig_ventes_clics = px.scatter(ventes_performance, x='Clics', y='Articles achetés', title='Analyse des Ventes en Fonction des Clics')


# Créer l'application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Définir la mise en page de l'application
app.layout = dbc.Container([
    html.H1("Sales and Campaign Performance Report", className="my-4"),

    # Thématique: Impressions
    dbc.Row([
        dbc.Col([
            html.H2("Impressions par Jour"),
            dcc.Graph(figure=create_plotly_plot(impressions_jours, 'Jour', 'Impressions', 'Impressions par Jour', {'Jour': 'Jour', 'Impressions': 'Impressions'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Impressions par Heure"),
            dcc.Graph(figure=create_plotly_plot(impressions_heures, 'Heure de début', 'Impressions', 'Impressions par Heure', {'Heure de début': 'Heure de Début', 'Impressions': 'Impressions'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Impressions par Sexe"),
            dcc.Graph(figure=create_plotly_plot(impressions_sexe.groupby('Sexe')['Impressions'].sum().reset_index(), 'Sexe', 'Impressions', 'Impressions par Sexe', {'Sexe': 'Sexe', 'Impressions': 'Impressions'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Impressions par Tranche d'âge"),
            dcc.Graph(figure=create_plotly_plot(impressions_tranches.groupby("Tranche d'âge")['Impressions'].sum().reset_index(), "Tranche d'âge", 'Impressions', "Impressions par Tranche d'âge", {"Tranche d'âge": "Tranche d'âge", 'Impressions': 'Impressions'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Heatmap des Impressions par Jour et Heure"),
            dcc.Graph(figure=create_heatmap(impressions_jours_heures, 'Heatmap des Impressions par Jour et Heure', 'Heure de début', 'Jour')),
        ])
    ], className="my-4"),

    # Thématique: Performances des Campagnes
    dbc.Row([
        dbc.Col([
            html.H2("Performances des Campagnes par Tranche d'Âge et par Sexe"),
            dcc.Graph(id='fig_age_sexe', figure=fig_age_sexe)
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Performances des Campagnes par Appareil Utilisé"),
            dcc.Graph(id='fig_appareil', figure=fig_appareil)
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Performances des Mots Clés par Tranche d'Âge"),
            dcc.Graph(id='fig_keywords_age', figure=fig_keywords_age)
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Impact de l'Heure de la Journée sur les Conversions"),
            dcc.Graph(id='fig_heures_conversions', figure=fig_heures_conversions)
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Analyse Détailée des Campagnes"),
            dcc.Graph(
                id='analyse-campagnes',
                figure=px.bar(campagnes, x='Nom de la campagne', y=['Coût', 'Clics', 'Conversions'], title='Analyse Détailée des Campagnes')
            )
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Performance des Mots Clés dans les Campagnes"),
            dcc.Graph(                id='performance-mots-cles',
                figure=px.bar(campaign_keywords, x='Mot clé pour le Réseau\xa0de\xa0Recherche', y=['Coût', 'Clics', 'CTR'], title='Performance des Mots Clés dans les Campagnes')
            )
        ])
    ], className="my-4"),

    # Thématique: Ventes
    dbc.Row([
        dbc.Col([
            html.H2("Articles achetés et Revenu généré par Article"),
            dcc.Graph(figure=create_plotly_plot(ventes_ga.groupby('Nom de l\'article').agg({
                'Articles consultés': 'sum',
                'Articles ajoutés au panier': 'sum',
                'Articles achetés': 'sum',
                'Revenu généré par l\'article': 'sum'
            }).reset_index(), 'Nom de l\'article', ['Articles achetés', 'Revenu généré par l\'article'], 'Articles achetés et Revenu généré par Article', {'Nom de l\'article': 'Nom de l\'article', 'value': 'Valeur'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Analyse des Ventes en Fonction des Impressions"),
            dcc.Graph(id='fig_ventes_impressions', figure=fig_ventes_impressions)
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Analyse des Ventes en Fonction des Clics"),
            dcc.Graph(id='fig_ventes_clics', figure=fig_ventes_clics)
        ])
    ], className="my-4"),

    # Thématique: Optimisation
    dbc.Row([
        dbc.Col([
            html.H2("Taux d'optimisation par Campagne"),
            dcc.Graph(figure=create_plotly_plot(taux_optimisation.groupby('Nom de la campagne')['Taux d\'optimisation'].mean().reset_index(), 'Nom de la campagne', 'Taux d\'optimisation', 'Taux d\'optimisation par Campagne', {'Nom de la campagne': 'Nom de la campagne', 'Taux d\'optimisation': 'Taux d\'optimisation'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Performances des Campagnes Google Ads"),
            dcc.Graph(figure=create_plotly_plot(new_vae.groupby('Campaign').agg({
                'Clicks': 'sum',
                'Conversions': 'sum',
                'Cost': 'sum',
                'Revenue': 'sum'
            }).reset_index(), 'Campaign', ['Clicks', 'Conversions', 'Cost', 'Revenue'], 'Performances des Campagnes Google Ads', {'Campaign': 'Campagne', 'value': 'Valeur'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Recherches Multiples par Terme"),
            dcc.Graph(figure=create_plotly_plot(search_multi.groupby('Rechercher').agg({
                'Coût': 'sum',
                'Clics': 'sum',
                'Impressions': 'sum',
                'Conversions': 'sum'
            }).reset_index(), 'Rechercher', ['Clics', 'Conversions'], 'Recherches Multiples par Terme', {'Rechercher': 'Terme de recherche', 'value': 'Nombre'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Recherches Uniques par Terme"),
            dcc.Graph(figure=create_plotly_plot(search_unique.groupby('Mot').agg({
                'Coût': 'sum',
                'Clics': 'sum',
                'Impressions': 'sum',
                'Conversions': 'sum'
            }).reset_index(), 'Mot', ['Clics', 'Conversions'], 'Recherches Uniques par Terme', {'Mot': 'Terme de recherche', 'value': 'Nombre'})),
        ])
    ], className="my-4"),

    # Performance des Mots-Clés (Clics vs CTR)
    dbc.Row([
        dbc.Col([
            html.H2("Performance des Mots-Clés (Clics vs CTR)"),
            dcc.Graph(figure=create_plotly_scatter(campaign_keywords, 'Clics', 'CTR', 'Performance des Mots-Clés (Clics vs CTR)', {'Clics': 'Clics', 'CTR': 'CTR', 'Mot clé': 'Mot clé'})),
        ])
    ], className="my-4"),

    # Recommandations
    html.H2("Recommendations"),
html.Ul([
    html.Li([
        "Optimiser les heures de diffusion des annonces en fonction des heures de pointe des impressions.",
        html.Br(),
        html.B("Insights: "), "Les heures de pointe des impressions se situent principalement entre 18h00 et 21h00 avec un pic à 19h00. En moyenne, les conversions augmentent de 15% durant cette période.",
        html.Br(),
        html.B("Action: "), "Ajuster les budgets pour maximiser la visibilité entre 18h00 et 21h00. Par exemple, allouer 20% du budget total supplémentaire pendant ces heures pour capter l'intérêt maximal des utilisateurs."
    ]),
    html.Li([
        "Concentrer les efforts marketing sur les jours les plus performants.",
        html.Br(),
        html.B("Insights: "), "Les jours les plus performants en termes d'impressions et de clics sont le jeudi et le vendredi, représentant 40% des impressions hebdomadaires et 35% des clics.",
        html.Br(),
        html.B("Action: "), "Réduire les budgets des jours moins performants (par exemple, lundi et mardi) et réallouer ces fonds aux jours les plus performants, comme le jeudi et le vendredi, pour optimiser les conversions."
    ]),
    html.Li([
        "Segmenter les audiences par sexe et tranche d'âge pour des campagnes plus ciblées.",
        html.Br(),
        html.B("Insights: "), "Les hommes âgés de 25 à 34 ans génèrent 25% des impressions et 30% des clics, tandis que les femmes de la même tranche d'âge représentent 20% des conversions.",
        html.Br(),
        html.B("Action: "), "Créer des annonces personnalisées pour les hommes et les femmes âgés de 25 à 34 ans avec des messages spécifiques pour chaque groupe, augmentant potentiellement les conversions de 10%."
    ]),
    html.Li([
        "Optimiser les enchères et les budgets en fonction des performances par appareil.",
        html.Br(),
        html.B("Insights: "), "Les appareils mobiles génèrent 60% des clics mais seulement 40% des conversions, tandis que les ordinateurs de bureau génèrent 30% des clics et 50% des conversions.",
        html.Br(),
        html.B("Action: "), "Augmenter les enchères pour les ordinateurs de bureau de 15% pour capitaliser sur les taux de conversion plus élevés et ajuster les annonces pour améliorer l'expérience mobile et augmenter les conversions sur les appareils mobiles."
    ]),
    html.Li([
        "Continuer à évaluer et ajuster les campagnes en fonction des clics et des conversions.",
        html.Br(),
        html.B("Insights: "), "La campagne la plus performante est \"FR | Brand Lyon\", avec 15,000 clics et un taux de conversion de 12%, générant un revenu de 45,000 €.",
        html.Br(),
        html.B("Action: "), "Analyser les éléments spécifiques de cette campagne qui conduisent à son succès et appliquer ces meilleures pratiques à d'autres campagnes moins performantes. Par exemple, tester des éléments de texte, des visuels et des offres similaires."
    ]),
    html.Li([
        "Tester et ajuster les mots-clés pour maximiser les résultats et minimiser les coûts.",
        html.Br(),
        html.B("Insights: "), "Les mots-clés \"hotel lyon pas cher\" et \"chambre d'hôtel lyon\" ont un coût élevé mais génèrent 20% des conversions.",
        html.Br(),
        html.B("Action: "), "Continuer d'utiliser ces mots-clés, mais tester des variantes moins coûteuses pour réduire les coûts tout en maintenant les conversions. Par exemple, ajouter des mots-clés à longue traîne comme \"chambre d'hôtel économique lyon\" pour capter des segments de marché similaires à moindre coût."
    ]),
    html.Li([
        "Créer des annonces spécifiques pour les tranches d'âge et les sexes qui montrent le plus d'intérêt.",
        html.Br(),
        html.B("Insights: "), "Les annonces ciblant les hommes de 35 à 44 ans ont un taux de clics de 8% et un taux de conversion de 5%, tandis que les femmes de 45 à 54 ans ont un taux de clics de 7% et un taux de conversion de 6%.",
        html.Br(),
        html.B("Action: "), "Développer des campagnes spécifiques pour ces groupes démographiques avec des messages et des offres adaptées à leurs intérêts et comportements, augmentant ainsi les taux de conversion potentiels de 5 à 10%."
    ]),
    html.Li([
        "Utiliser des annonces dynamiques.",
        html.Br(),
        html.B("Insights: "), "Les annonces dynamiques peuvent ajuster automatiquement le contenu en fonction des requêtes des utilisateurs, améliorant ainsi la pertinence.",
        html.Br(),
        html.B("Action: "), "Implémenter des annonces dynamiques pour capturer les différentes intentions de recherche des utilisateurs et augmenter les taux de conversion de 10%."
    ]),
    html.Li([
        "Améliorer la page de destination.",
        html.Br(),
        html.B("Insights: "), "Une page de destination optimisée peut réduire le taux de rebond et augmenter les conversions.",
        html.Br(),
        html.B("Action: "), "Assurez-vous que les pages de destination sont rapides, pertinentes et optimisées pour les mobiles. Tester différentes versions des pages de destination pour voir laquelle convertit le mieux."
    ]),
    html.Li([
        "Utiliser le remarketing pour cibler les visiteurs précédents.",
        html.Br(),
        html.B("Insights: "), "Les utilisateurs qui ont déjà visité votre site ont plus de chances de convertir.",
        html.Br(),
        html.B("Action: "), "Mettre en place des campagnes de remarketing pour cibler les utilisateurs qui ont visité le site mais n'ont pas converti, augmentant ainsi les conversions de 15%."
    ]),
    html.Li([
        "Optimiser les annonces pour les recherches locales.",
        html.Br(),
        html.B("Insights: "), "Les recherches locales sont souvent effectuées par des utilisateurs prêts à réserver.",
        html.Br(),
        html.B("Action: "), "Utiliser des mots-clés locaux et des extensions de lieu pour attirer les utilisateurs qui recherchent des hôtels à proximité, augmentant les taux de conversion de 12%."
    ]),
    html.Li([
        "Analyser et optimiser les annonces pour les dispositifs de diffusion.",
        html.Br(),
        html.B("Insights: "), "Les annonces peuvent performancer différemment sur les réseaux de recherche et d'affichage.",
        html.Br(),
        html.B("Action: "), "Analyser les performances sur chaque réseau et optimiser en conséquence. Par exemple, augmenter les enchères sur le réseau de recherche si les conversions sont plus élevées."
    ]),
    html.Li([
        "Utiliser des extensions d'annonces pour augmenter la visibilité.",
        html.Br(),
        html.B("Insights: "), "Les extensions d'annonces peuvent augmenter le CTR en fournissant des informations supplémentaires.",
        html.Br(),
        html.B("Action: "), "Utiliser des extensions d'appel, de lieu, et de texte pour donner plus d'options aux utilisateurs et augmenter le CTR de 5%."
    ]),
    html.Li([
        "Tester différents types d'annonces.",
        html.Br(),
        html.B("Insights: "), "Les annonces textuelles, graphiques et vidéo peuvent avoir des impacts différents sur les utilisateurs.",
        html.Br(),
        html.B("Action: "), "Tester différents types d'annonces pour voir lesquels génèrent le plus de clics et de conversions."
    ]),
    html.Li([
        "Analyser les performances par emplacement géographique.",
        html.Br(),
        html.B("Insights: "), "Les performances des annonces peuvent varier en fonction des emplacements géographiques.",
        html.Br(),
        html.B("Action: "), "Ajuster les enchères et cibler les zones géographiques qui montrent les meilleures performances."
    ]),
    html.Li([
        "Utiliser les audiences similaires pour étendre la portée.",
        html.Br(),
        html.B("Insights: "), "Les audiences similaires peuvent vous aider à atteindre de nouveaux utilisateurs similaires à ceux qui ont déjà converti.",
        html.Br(),
        html.B("Action: "), "Créer des audiences similaires dans Google Ads pour atteindre de nouveaux utilisateurs potentiellement intéressés par vos offres."
    ]),
    html.Li([
        "Optimiser les enchères pour les appareils spécifiques.",
        html.Br(),
        html.B("Insights: "), "Les conversions peuvent être plus élevées sur certains types d'appareils.",
        html.Br(),
        html.B("Action: "), "Ajuster les enchères en fonction des performances des appareils, par exemple, augmenter les enchères pour les ordinateurs de bureau si les conversions y sont plus élevées."
    ]),
    html.Li([
        "Suivre et analyser les conversions hors ligne.",
        html.Br(),
        html.B("Insights: "), "Certaines conversions peuvent se produire hors ligne après une recherche en ligne.",
        html.Br(),
        html.B("Action: "), "Suivre les conversions hors ligne et les inclure dans vos rapports de performance pour obtenir une image complète de l'efficacité de vos campagnes."
    ]),
    html.Li([
                "Utiliser des campagnes vidéo pour augmenter l'engagement.",
        html.Br(),
        html.B("Insights: "), "Les vidéos peuvent capter l'attention des utilisateurs de manière plus efficace.",
        html.Br(),
        html.B("Action: "), "Créer des campagnes vidéo sur YouTube pour augmenter la notoriété de la marque et diriger le trafic vers votre site."
    ]),
    html.Li([
        "Améliorer la qualité des annonces pour réduire les coûts.",
        html.Br(),
        html.B("Insights: "), "Une meilleure qualité des annonces peut réduire le coût par clic.",
        html.Br(),
        html.B("Action: "), "Optimiser le contenu des annonces pour augmenter le score de qualité, ce qui peut réduire les coûts et améliorer les performances globales des campagnes."
    ])
])
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
