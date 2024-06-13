import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.io as pio
import dash_bootstrap_components as dbc

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

# Créer l'application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Définir la mise en page de l'application
app.layout = dbc.Container([
    html.H1("Sales and Campaign Performance Report", className="my-4"),

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

    dbc.Row([
        dbc.Col([
            html.H2("Performances par Type d'Appareil"),
            dcc.Graph(figure=create_plotly_plot(appareils.groupby('Type d\'appareil').agg({
                'Coût': 'sum',
                'Clics': 'sum',
                'Conversions': 'sum'
            }).reset_index(), 'Type d\'appareil', ['Clics', 'Conversions'], 'Performances par Type d\'Appareil', {'Type d\'appareil': 'Type d\'appareil', 'value': 'Nombre'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Performances des Campagnes"),
            dcc.Graph(figure=create_plotly_plot(campagnes.groupby('Nom de la campagne').agg({
                'Coût': 'sum',
                'Clics': 'sum',
                'Conversions': 'sum'
            }).reset_index(), 'Nom de la campagne', ['Clics', 'Conversions'], 'Performances des Campagnes', {'Nom de la campagne': 'Nom de la campagne', 'value': 'Nombre'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Performances des Mots-Clés"),
            dcc.Graph(figure=create_plotly_plot(campaign_keywords.groupby('Mot clé pour le Réseau de Recherche').agg({
                'Coût': 'sum',
                'Clics': 'sum',
                'CTR': 'mean'
            }).reset_index(), 'Mot clé pour le Réseau de Recherche', ['Clics', 'CTR'], 'Performances des Mots-Clés', {'Mot clé pour le Réseau de Recherche': 'Mot clé', 'value': 'Valeur'})),
        ])
    ], className="my-4"),
    dbc.Row([
        dbc.Col([
            html.H2("Impressions par Tranche d'âge et Sexe"),
            dcc.Graph(figure=create_plotly_plot(impressions_ages_tranches.groupby(['Tranche d\'âge', 'Sexe']).agg({
                'Impressions': 'sum'
            }).reset_index().pivot(index='Tranche d\'âge', columns='Sexe', values='Impressions').reset_index(), 'Tranche d\'âge', ['Homme', 'Femme'], 'Impressions par Tranche d\'âge et Sexe', {'Tranche d\'âge': 'Tranche d\'âge', 'value': 'Impressions'})),
        ])
    ], className="my-4"),

    dbc.Row([
        dbc.Col([
            html.H2("Heatmap des Impressions par Jour et Heure"),
            dcc.Graph(figure=create_heatmap(impressions_jours_heures, 'Heatmap des Impressions par Jour et Heure', 'Heure de début', 'Jour')),
        ])
    ], className="my-4"),

    html.H2("Recommendations"),
    html.Ul([
        html.Li("Optimiser les heures de diffusion des annonces en fonction des heures de pointe des impressions."),
        html.Li("Concentrer les efforts marketing sur les jours les plus performants."),
        html.Li("Segmenter les audiences par sexe et tranche d'âge pour des campagnes plus ciblées."),
        html.Li("Optimiser les enchères et les budgets en fonction des performances par appareil."),
        html.Li("Continuer à évaluer et ajuster les campagnes en fonction des clics et des conversions."),
        html.Li("Tester et ajuster les mots-clés pour maximiser les résultats et minimiser les coûts."),
        html.Li("Créer des annonces spécifiques pour les tranches d'âge et les sexes qui montrent le plus d'intérêt."),
    ])
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
