"""
STREAMLIT est une librairie utiliser par les data analyste pour la visualisation des donnée.
Dans ce fichier, nous allons travailler sur un fichier dataset de la vente des téléphones de la marque Tecno DRC.
"""

##########################
# IMPORTATION LIBRAIRIES
########
import pandas as pd
import streamlit as st
import plotly.express as px
# import plotly.offline as py
import plotly.graph_objects as go

##########################
# IMPORTER LE DATASET
########

st.title(
    "TECNO DATA VISUALISATION 2023"
)
st.text(
    """
    Bonjour et Bienvenu(e) dans notre fichier de visualisations de la vente des 
    téléphones de la Marque Tecno DRC.
    Dans cette analyse sera traité la question de la vente générale annuelle, 
    la vente mensuelle, vente modéles et la vente par région.
    
    """)
st.markdown("___")
st.subheader("Auteur :")
st.text("""
        Rodrigue NSINSULU MAYANZA, suis un Data Analyste en Python avec 2 ans d'expériences 
        et Channel supervisor dans le departement Tecno DRC.
        Contact : +243 896663756 | E-mail : rodriguensinsulu@gmail.com 
        """)
st.markdown("[Facebook](https://www.facebook.com)")
st.markdown("___")

st.subheader("IMPORTATION DU DATASET")

file = st.file_uploader("Inserer le fichier CSV", type=["csv", "xlsx"])

if file is not None:
    dataset = pd.read_csv(file)
    dataset_drc = dataset[dataset["Pays livraison"] == "Democratic Republic of the Congo"]
    st.dataframe(dataset_drc)

    ##########################
    # CREATION SIDEBAR
    ########
    st.sidebar.write("RESUMER DE L'ETUDE")

    ##########################
    # VISUALISATION
    ########
    # 1-VENTE ANNUELLE
    #########################

    st.subheader("1- SITUATION ANNUELLE DE LA VENTE EN 2022-2023")  # Le titre
    years = dataset_drc.groupby("Annee", as_index=False)["Vente(Pcs)"].sum()
    # st.dataframe(years)

    sidebar_year = st.sidebar.radio("1- SITUATION ANNUELLE DE LA VENTE EN 2022-2023", options=("Line", "Bar"))

    if sidebar_year == "Line":

        fig = px.line(years, x="Annee", y="Vente(Pcs)", title="Vente Annuelle 2022-2023", text="Vente(Pcs)",
                      markers=True)
        st.plotly_chart(fig)  # Pour afficher le graphique dans Streamlit

    elif sidebar_year == "Bar":
        fig = px.bar(years, x="Annee", y="Vente(Pcs)", title="Vente Annuelle 2022-2023", text="Vente(Pcs)",
                     color="Annee")
        # Mettre la valeur totale de la barre au-dessus des barres avec 2 valeurs de précision
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        # Faire pivoter les étiquettes de 45 degrés
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig)

    st.text("""
            Cette premiere graphique est celui de la vente annuelle pour l'année 2022-2023.
            
            La vente en l'ans 2023 est faible car nous n'avons consideré que les données
            de celui du mois de Decembre 2022.
            
            Tandis que pour l'annee 2023, nous avons consideré partant du Mois de Janvier 2023
            à Décembre 2023.
    """)
    st.markdown("___")

    # 2-VENTE MENSUELLE 2023
    ############################
    st.text("""
    """)
    st.subheader("2- SITUATION MENSUEllE DE LA VENTE EN 2023")
    years_2023 = dataset_drc[dataset_drc.Annee == 2023]
    # st.dataframe(years_2023)

    month = years_2023.groupby("Date", as_index=False)["Vente(Pcs)"].sum()
    # st.dataframe(month)

    sidebar_month = st.sidebar.radio("2- SITUATION MENSUEllE DE LA VENTE EN 2023", options=("Line", "Bar", "camembert"))

    if sidebar_month == "Line":
        fig_month = px.line(month, x="Date", y="Vente(Pcs)", title="Vente mensuelle en 2023",
                            markers=True, text="Vente(Pcs)")
        st.plotly_chart(fig_month)  # Pour afficher le graphique dans Streamlit

    elif sidebar_month == "Bar":
        fig_month = px.bar(month, x="Date", y="Vente(Pcs)", title="Vente mensuelle en 2023",
                           text="Vente(Pcs)", color="Date")
        # Mettre la valeur totale de la barre au-dessus des barres avec 2 valeurs de précision
        # fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        # Faire pivoter les étiquettes de 45 degrés
        fig_month.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_month)  # Pour afficher le graphique dans Streamlit

    elif sidebar_month == "camembert":
        label = month.Date
        fig_month = go.Figure(data=[go.Pie(labels=month.Date, values=month["Vente(Pcs)"],
                                           pull=[0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0])])
        # Utiliser les traces de mise à jour pour personnaliser les informations de survol, le texte, 
        # la quantité de tirage pour chaque part de camembert et le trait
        st.plotly_chart(fig_month)

    st.text("""
            Cette deuxieme graphique montre la réalisation de la vente  pour chaques Mois 
            de l'année 2023.
            
            La vente fut excellente en 2023 au Mois de Juillet avec une vente de 27808pcs 
            qui place le Mois Juillet-2023 à la prémière position avec une poucentage de  xx%,
            suivis du Mois de Octobre-2023.
    """)
    st.markdown("___")

    # 3-VENTE PAR MODELES
    #########################
    st.text("""
    """)
    st.subheader("3- SITUATION DE LA VENTE PAR MODELES POUR L'ANNEE 2023")
    sidebar_modele = st.sidebar.radio("3- SITUATION DE LA VENTE PAR MODELES POUR L'ANNEE 2023",
                                      options=("Line", "Bar", "camembert", "Bar_empiler"))

    df_models = years_2023.groupby("Modeles", as_index=False)["Vente(Pcs)"].sum()
    # st.dataframe(df_models)

    if sidebar_modele == "Line":
        line = px.line(df_models, x="Modeles", y="Vente(Pcs)",
                       title="Vente annuelle par Modeles en 2023", markers=True, text="Vente(Pcs)")
        st.plotly_chart(line)

        st.text("""
            Cette troisieme graphique montre la réalisation de la vente par modeles pour chaque Mois 
            de l'année 2023 .
        """)

    elif sidebar_modele == "Bar":
        bar = px.bar(df_models, x="Modeles", y="Vente(Pcs)", title="Vente annuelle par Modeles en 2023",
                     color="Modeles", text="Vente(Pcs)")
        # Mettre la valeur totale de la barre au-dessus des barres avec 2 valeurs de précision
        # fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        # Faire pivoter les étiquettes de 45 degrés
        st.plotly_chart(bar)

        st.text("""
            Cette troisieme graphique montre la réalisation de la vente par modeles pour chaque Mois 
            de l'année 2023.
        """)

    elif sidebar_modele == "camembert":
        pie = go.Figure(data=[go.Pie(labels=df_models.Modeles, values=df_models["Vente(Pcs)"],
                                     pull=[0, 0, 0, 0, 0, 0, 0.2])])
        # Utiliser les traces de mise à jour pour personnaliser les informations de survol, le texte, 
        st.plotly_chart(pie)

        st.text("""
            Cette troisieme graphique montre la réalisation de la vente par modeles pour chaque Mois 
            de l'année 2023.
        """)

    elif sidebar_modele == "Bar_empiler":
        # Ici il s'agit de la vente des modele par mois
        models_mois = years_2023.groupby(["Modeles", "Date"], as_index=False)["Vente(Pcs)"].sum()
        # st.dataframe(models_mois)

        bar_empiler = px.bar(models_mois, x="Date", y="Vente(Pcs)", title="Vente des modeles par Mois en 2023",
                             color="Modeles", text="Vente(Pcs)")
        st.plotly_chart(bar_empiler)

        st.text("""
            Cette troisieme graphique montre la réalisation de la vente des modeles pour chaque Mois 
            de l'année 2023.
        """)

    st.markdown("___")

    # 4- VENTE PAR SERIES
    #########################
    st.text("""
    """)
    st.subheader("4- SITUATION DE LA VENTE PAR SERIES POUR L'ANNEE 2023")
    s_series_annee = st.sidebar.radio("4- SITUATION DE LA VENTE PAR SERIES POUR L'ANNEE 2023",
                                      options=("Line", "camembert"))

    serie_annee = years_2023.groupby(["Modeles Series", "Annee"], as_index=False)["Vente(Pcs)"].sum()
    # st.dataframe(serie_annee)

    if s_series_annee == "Line":
        serie_years = px.line(serie_annee, x="Modeles Series", y="Vente(Pcs)", title="La vente par series des modeles")
        st.plotly_chart(serie_years)


    elif s_series_annee == "camembert":
        serie_years = go.Figure(data=[go.Pie(labels=serie_annee["Modeles Series"], values=serie_annee["Vente(Pcs)"])])
        st.plotly_chart(serie_years)

    st.text("""
            Cette quatrieme graphique montre la réalisation de la vente.
    """)
    st.markdown("___")

    # 5-VENTE PAR SEMAINES
    #########################
    st.text("""
    """)
    st.subheader("5- SITUATION DE LA VENTE PAR SEMAINES POUR L'ANNEE 2023")

    semaine = years_2023.groupby("Semaines", as_index=False)["Vente(Pcs)"].sum()

    semaine_plot = px.bar(semaine, x="Semaines", y="Vente(Pcs)", color="Semaines",
                          title="La vente par Semaines en 2023")
    st.plotly_chart(semaine_plot)

    st.text("""
            Cette cinquieme graphique montre la réalisation de la vente  par semaines pour 
            l'annee 2023. 
    """)
    st.markdown("___")

    # 6-VENTE PAR SHOPS
    #########################

    st.text("""
    """)
    st.subheader("6- SITUATION DE LA VENTE PAR SHOPS POUR L'ANNEE 2023")

    # Nombre des shops
    shop_sale = years_2023.groupby("Nom Shop", as_index=False)["Vente(Pcs)"].sum()
    st.dataframe(shop_sale)
    st.text("""
            Le nombre total des shops actifs en 2023 est : 889 shops reparti en DRC. 
        """)

    shop = years_2023.groupby(["Nom Shop", "Date"], as_index=False)["Vente(Pcs)"].sum()
    selectionShops = st.selectbox("Selectionnez un shop", options=shop["Nom Shop"].unique())
    st.write("Vous avez selectionné le shop {}".format(selectionShops))
    filtrage_shops = shop[shop["Nom Shop"] == selectionShops]
    affichage_shops = px.line(filtrage_shops, x="Date", y="Vente(Pcs)", text="Vente(Pcs)")
    st.plotly_chart(affichage_shops)

    st.text("""
            Cette sixieme graphique montre la réalisation de la vente  par shops pour 
            l'annee 2023.      
        """)
    st.markdown("___")

    # 7- VENTE PAR REGIONS
    #########################
    st.text("""
    """)
    st.subheader("7- SITUATION DE LA VENTE PAR REGIONS POUR L'ANNEE 2023")

    df_region = years_2023.groupby("Ventes Regions", as_index=False)[
        "Vente(Pcs)"].sum()  # On recupere la vente par regions
    # st.dataframe(df_region)

    regions = go.Figure(data=[
        go.Pie(labels=df_region["Ventes Regions"], values=df_region["Vente(Pcs)"], hole=0.3, textinfo='label+percent')])
    st.plotly_chart(regions)

    # -------------------------------------------------------------------------------------------------------------------------------------
    select_regions = st.multiselect("Pouvez-vous selectionner vos regions ?",
                                    options=(df_region["Ventes Regions"].unique().tolist()))
    st.write("Vous avez selectionné les regions suivantes : {}".format(select_regions))

    dfs_region = {region: df_region[df_region["Ventes Regions"] == region] for region in select_regions}

    regionFigure = go.Figure()
    for region, df_region in dfs_region.items():
        regionFigure = regionFigure.add_trace(go.Bar(x=df_region["Ventes Regions"],
                                                     y=df_region["Vente(Pcs)"], name=region,
                                                     text=df_region["Vente(Pcs)"]))
    st.plotly_chart(regionFigure)
    # -------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------
    df_region_mois = years_2023.groupby(["Ventes Regions", "Date"], as_index=False)[
        "Vente(Pcs)"].sum()  # On recupere la vente par regions pour chaque mois
    # st.dataframe(df_region_mois)

    select_mois = st.selectbox("Selectionne la region ", options=(df_region_mois["Ventes Regions"].unique()))
    st.write("Vous avez selectionné les regions suivantes : {}".format(select_mois))
    filter_region = df_region_mois[df_region_mois["Ventes Regions"] == select_mois]

    fig_region_mois = px.line(filter_region, x="Date", y="Vente(Pcs)", text="Vente(Pcs)")
    st.plotly_chart(fig_region_mois)
    # -------------------------------------------------------------------------------------------------------------------------------------
    st.markdown("___")

    ## 8- SITUATION DE LA VENTE PAR ACTIVATION
    ###########################################
    st.text("""
    """)
    st.subheader("8- SITUATION DE LA VENTE PAR ACTIVATION POUR L'ANNEE 2023")
    sidebar_activation = st.sidebar.radio("8- SITUATION DE LA VENTE PAR ACTIVATION POUR L'ANNEE 2023",
                                          options=("camembert", "Bar", "Bar_empiler"))

    activation = years_2023.groupby("Activation", as_index=False)["Vente(Pcs)"].sum()

    if sidebar_activation == "camembert":
        # Connaitre le nombre de telephone activer et non activer par ans
        st.dataframe(activation)
        actifs = go.Figure(data=[go.Pie(labels=activation["Activation"], values=activation["Vente(Pcs)"],
                                        hole=0.3, textinfo='label+percent')])
        st.plotly_chart(actifs)

    elif sidebar_activation == "Bar":
        # Connaitre le mois ayant les telephones non activer
        activation = years_2023.groupby(["Activation", "Date"], as_index=False)["Vente(Pcs)"].sum()
        filtrage = activation[activation["Activation"] == "Non Activé"]

        affichage = px.bar(filtrage, x="Date", y="Vente(Pcs)", text="Vente(Pcs)", color="Vente(Pcs)",
                           title="Graphique des téléphones non activé par mois")
        st.plotly_chart(affichage)


    elif sidebar_activation == "Bar_empiler":
        # Connaitre le mois ayant les telephones non activer pour chaques regions
        inactif = years_2023.groupby(["Ventes Regions", "Activation"], as_index=False)["Vente(Pcs)"].sum()
        st.write(inactif)

        inactif_graph = px.bar(inactif, x="Activation", y="Ventes Regions", color="Ventes Regions",
                               text="Vente(Pcs)", barmode="group")
        st.plotly_chart(inactif_graph)

    st.markdown("___")

    ##9- PAYS DE LIVRAISON ET ACTIVATION
    #######################################
    st.text("""
    """)
    st.subheader("9- SITUATION PAR PAYS DE LIVRAISON ET ACTIVATION POUR L'ANNEE 2023")
    sidebar_activation = st.sidebar.radio("9- SITUATION PAR PAYS DE LIVRAISON ET ACTIVATION POUR L'ANNEE 2023",
                                          options=("Pays Livraison", "DRC", "Smuggle"))

    years_2023_all = dataset[dataset.Annee == 2023]

    if sidebar_activation == "Pays Livraison":
        # Connaitre les pays de livraison des telephones par ans
        pays = years_2023_all.groupby("Pays livraison", as_index=False)["Vente(Pcs)"].sum()

        fig = px.bar(pays, x="Pays livraison", y="Vente(Pcs)", title="Pays de livraison")
        st.plotly_chart(fig)

    elif sidebar_activation == "DRC":
        # Compasrer les pays des livraisons avec celui de l'activation en selectionner la RDC comme pays de livraison
        pays = years_2023_all.groupby(["Pays livraison", "Pays Activation"], as_index=False)["Vente(Pcs)"].sum()
        payx = pays[pays["Pays livraison"] == "Democratic Republic of the Congo"]

        fig = px.bar(payx, x="Pays Activation", y="Vente(Pcs)", text="Vente(Pcs)",
                     title="Pays d'activation des phones livrer en DRC")
        st.plotly_chart(fig)


    elif sidebar_activation == "Smuggle":
        # Compasrer les pays des livraisons avec celui d'activation en excluant la RDC comme pays de livraison
        pays = years_2023_all.groupby(["Pays livraison", "Pays Activation"], as_index=False)["Vente(Pcs)"].sum()
        payx = pays[pays["Pays livraison"] != "Democratic Republic of the Congo"]
        pay_rdc = payx[payx["Pays Activation"] == "Democratic Republic of the Congo"]
        #st.dataframe(pay_rdc)

        fig = px.bar(pay_rdc, x="Pays livraison", y="Vente(Pcs)", text="Vente(Pcs)", title="Le smuggle vendu en DRC")
        st.plotly_chart(fig)

        st.markdown("___")

        ## Dans cette partie nous allons afficher les shops qui vend les smuggle

        years_2023_rwd = years_2023_all[years_2023_all[
                                            "Pays livraison"] == "Rwanda"]
        # recupere les produits provenant du Rwanda

        # Graphique en Bar
        shop_smart_bar = years_2023_rwd.groupby("Nom Shop", as_index=False)["Vente(Pcs)"].sum()
        years_smart = px.bar(shop_smart_bar, x="Nom Shop", y="Vente(Pcs)",
                             title="Les shops ayant vendu les smuggle prevenant de Rwanda en 2023")
        st.plotly_chart(years_smart)

        st.markdown("___")

        # Graphique en Line
        shop_smart = years_2023_rwd.groupby(["Nom Shop", "Date"], as_index=False)["Vente(Pcs)"].sum()
        smart_shop_filtre = shop_smart["Nom Shop"].unique()

        Shops_smart = st.selectbox("Selectionner le shop vendant les smuggles", options=smart_shop_filtre)
        st.write("Le shop selectionné est {}".format(Shops_smart))

        filtre_shops = shop_smart[shop_smart["Nom Shop"] == Shops_smart]
        affiche_shops = px.line(filtre_shops, x="Date", y="Vente(Pcs)", text="Vente(Pcs)")
        st.plotly_chart(affiche_shops)


    st.markdown("___")
