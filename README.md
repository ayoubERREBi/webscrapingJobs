Linkedin job Scrapping 
Description et Présentation du Projet de Scraping LinkedIn :
Le projet de scraping LinkedIn est conçu pour collecter des données relatives aux offres d'emploi en 
se basant sur des critères spécifiques tels que la date de publication et le domaine d’activité (data 
science). Ce projet utilise Selenium pour l'automatisation des interactions avec le navigateur et 
permet de récupérer des informations cruciales à partir de pages LinkedIn ces offres d’emplois sont 
enregistrés dans une base de donnée et apprès ces offres sont envoyés au utilisateur qui utilisent la 
pages web qui affiche les offres d’emplois .
Ce projet se compose de deux parties :
Une pour la collection des offres d’emplois en utilisant des techniques de Scrapping.
Une partie pour la gestion des utilisateurs qui offre une page web pour naviguer dans les 
offres d’emplois qui sont déjà collectées, les offres d’emplois sont également envoyées aux 
utilisateurs par email.
➢ Description de la première partie : Scrapping et sauvegarde de ces offres
Ce projet de scraping LinkedIn permet une collecte automatisée et intelligente d'informations 
cruciales sur les offres d'emploi.Ce projet offre une gamme complète de fonctionnalités clés pour 
simplifier et optimiser le processus.
L'utilisateur bénéficie d'une personnalisation acceptable, garantissant une recherche d'opportunités 
adaptée à ses besoins. L'automatisation de la navigation élimine toute intervention manuelle, 
assurant un accès fluide à l'URL LinkedIn fournie.
La dynamique extraction du nombre d'offres d'emploi, basée sur Selenium, s'ajuste en temps réel 
aux changements sur la plateforme, tandis que l'exploration intelligente des offres assure une 
collecte exhaustive des données grâce à un défilement proactif de la page.
Les informations clés telles que le nom de l'entreprise, le titre du poste, le lien vers l'offre et la date 
de publication sont extraites avec précision. Une conversion intelligente de la durée standardise les 
expressions de temps variées, simplifiant la gestion temporelle.
L'utilisation de Pandas facilite le traitement et l'organisation des données dans une structure 
tabulaire, permettant des analyses détaillées et une préparation efficace pour le stockage. La 
sauvegarde structurée avec la platforme Deta offre une solution sécurisée et évolutive pour la 
gestion des données collectées.
➢ Description de la deuxième partie : gestion des utilisateurs et envoie 
plus affichage des offres d’emplois dans la page web (Application Web 
Streamlit pour la Gestion d'Opportunités Professionnelles)
Cette partie du projet étend l'expérience utilisateur en créant une interface utilisateur interactive 
à l'aide de Streamlit. Voici une description complète des fonctionnalités clés de cette partie :
L'application commence par une authentification sécurisée à l'aide de Streamlit Authenticator et 
Deta. Les informations des utilisateurs, y compris les courriels, noms d'utilisateur et mots de 
passe, sont récupérées à partir de Deta pour permettre l'accès sécurisé.
Une fois authentifié avec succès, l'utilisateur est accueilli dans l'interface de gestion des 
opportunités professionnelles. Les utilisateurs ont la possibilité de consulter les offres d'emploi 
disponibles au cours des 7 derniers jours, extraites de la base de données Deta.
Chaque offre d'emploi est présentée sous forme de lien cliquable, affichant le titre du poste et le 
nom de l'entreprise. En outre, un e-mail est envoyé à l'utilisateur authentifié pour chaque offre 
d'emploi répertoriée, fournissant des détails pertinents et un lien direct vers l'opportunité.
L'application Streamlit est également équipée d'une fonction de déconnexion pour permettre 
aux utilisateurs de se déconnecter de manière sécurisée après avoir consulté les opportunités. 
Les erreurs d'authentification et les avertissements sont gérés de manière élégante, offrant une 
expérience utilisateur transparente.

Description d'objectifs des fichiers :
Linkedin job Scrapping description ===> pour la description du mini projet

mainDetaStreamlit.py ====> l'application web principale

streamlit_Deta.py ====>ce fichier contient des fonctions pour une utilisation dans
le fichier mainDetaStreamlit.py c'est seulement comme une bibliotheque des fonctions.

ScrapingSelenium.ipynb====> le fichier qui fait l'extraction et le sauvgarde des stages
