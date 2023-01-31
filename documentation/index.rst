My ML Project
=================

Introduction
--------------
Le but de ce projet est d'entraîner un modèle de Machine Learning pour “Home Credit Risk Classification”, qui pourra prédire si un individu a des difficultés, ou pas, à rembourser un prêt. Une fois le modèle entraîné, il faut l’enregistrer et gérer les étapes du cycle du projet ML via l’outil MLFlow. La librairie Shap nous permettra également de rentrer dans l’interprétabilité des prédictions réalisées par le modèle, grâce au concept des Shap Values.

Le data set utilisé provient de Kaggle:https://www.kaggle.com/c/home-credit-default-risk/data, seulement les fichiers application_train.csv et application_test.csv ont été traités.


Données
-------
Le jeu de données comprend deux fichiers principaux : `application_train.csv` et `application_test.csv`. Les données incluent des informations sur les clients, telles que l'âge, le sexe, le niveau de formation, etc.

Traitement
-------------
Avant de construire un modèle de machine learning, nous avons effectué les étapes suivantes de prétraitement :

- Data collection 
La collecte de données consiste à récupérer les données brutes, et à les exporter en local sous un format exploitable. Nous avons donc récupéré les données en lisant des fichiers csv.

- Data analyse
Cette analyse est faite en amont des modifications des données brutes. Afin de savoir quelles modifications appliquer, il faut d’abord analyser les données. Nous avons donc étudié les différentes features de notre CSV. On analyse notre dataset. Il s'agit de connaître les types de chaque features qui constituent notre jeu de données il peut s’agir d’un bon indicateur, ou complément d’informations pour la suite de l’analyse. Ceci permet également de comprendre des erreurs de code plus rapidement, si on connaît les types des features récupérées par le code python.
Il est possible de réaliser de nombreuses analyses de données, grâce à de nombreux outils (notamment des outils statistiques). Dans le cadre de notre projet, nous avons procédé à l’analyse d’un seul aspect de notre dataset, afin de rester dans un modèle simplifié du cycle de vie du projet de Machine Learning. En effet, l’aspect que nous avons analysé a été les proportions d’exemples de données que nous possédions dans notre dataset : En récupérant les données brutes, on a pu voir que le nombre de lignes dont la prédiction était à 0 était très disproportionné par rapport à celui dont la prédiction était de 1. Cette analyse débouche alors sur des traitements dans les étapes de cleaning et de feature engineering, permettant d’avoir un dataset plus équilibré, ce qui conduira donc à un meilleur apprentissage de notre modèle.

- Data cleaning: Remplacement des valeurs manquantes
Cette étape consiste à nettoyer le dataset en différentes sous-étapes, et en fonction du dataset que nous avons. Il est possible d’avoir à modifier certains types de features, ou certains caractères spéciaux du dataset. Suite à l’analyse, nous aurions pu également supprimer certaines colonnes qui n’ont pas d’impacts. 
Dans un ensemble de données brutes, certaines données peuvent être incomplètes, on parle alors de valeurs manquantes. Dans le but d’avoir un ensemble de données fiable et pertinent, nous avons supprimé toutes les valeurs manquantes de notre data set.

- Feature engineering
Cette étape permet de créer de nouvelles données à partir des données brutes de notre dataset. Ces nouvelles données permettent un meilleur apprentissage de notre modèle, et des prédictions plus fiables. Dans notre cas, suite à l’analyse de notre dataset déséquilibré, nous avons fait de l’augmentation de données, pour générer d'avantages d’exemples de la classe dont le nombre d’exemples était moindre dans le dataset.

- Data Processing
Cette étape permet de faire une mise à l’échelle des valeurs, ce qu’on appelle du « scaling ». Elle permet de standardiser les valeurs des features numériques pour que celles-ci soient plus compréhensibles par le modèle à entraîner. Il permet d’encoder les valeurs des features catégorielles (qualitatives). 
Pour ce projet, nous avons utilisé le label Encoding. On va remplacer chaque valeur possible de la variable par un nombre. Nous l’avons utilisé parce que l’algorithme du  random forest ne comprenait pas les strings. Il fallait donc les traduire en valeur numérique pour qu’il puisse les interpréter. 

-	Entrainement du modèle 
Cette étape consiste à entraîner le modèle souhaité avec les données traitées et l’algorithme choisi. Après avoir traité les données, nous avons décidé d’utiliser le random forest comme algorithme pour faire l'entraînement du modèle.

-	Evaluation des performances 
Cette étape est la dernière du cycle avant la mise en production. Elle permet d’évaluer, par le biais de différentes métriques, les résultats des prédictions de notre modèle : Elle nous permet ainsi de mesurer la fiabilité des prédictions réalisées par notre modèle de Machine Learning. Cette étape finit toujours par nous faire repasser sur les étapes antérieures afin d’ajuster les différents hyperparamètres et/ou le traitement fait sur les données, afin d’affiner la précision de notre prédiction. 


Algorithmes de ML utilisés
--------------------------
Nous avons utilisé l'algorithme de random forest classifier les risques de crédit à la maison

Outils de ML utilisés
--------------------------

- ML FLOW
ML Flow est un outil de gestion de cycle de vie de projet machine learning qui permet de gérer et de suivre les expériences de modèles. Il a pour but d’enregistrer et de requêter les expériences comme le code, les données ou les résultats par MLflow tracking. Aussi, il permet de packager pour rendre les expériences productives avec MLflow Projects. Enfin, il permet de proposer un format générique pour envoyer les modèles vers plusieurs outils de déploiements avec MLflow Models.

- SHAP
Le concept des shap values est tiré de celui des valeurs shapley, qui est d’expliquer la contribution de chaque feature dans une prédiction réalisée, plus communément appelée output. 
La prédiction consiste à prendre en entrée plusieurs caractéristiques (features), et à en sortir un nombre.
Ainsi, les shap values vont tenter d’expliquer des modèles de Machine Learning, plus ou moins complexes, en mettant en place des modèles simples, qui reproduiront les mêmes résultats.  





Conclusions
-----------
En conclusion, ce projet a aboutit à la mise en place d’un modèle de Home Credit Risk Classification en utilisant l’algorithme Random Forest. Grâce à l’utilisation de ML Flow, nous avons pu effectuer un suivi efficace et intuitif de nos expériences, tandis qu eles valeurs Shap ont contribué à une meilleure compréhension de nos prédictions.Nous avons adopté les bonnes pratiques en matière de développement, en utilisant un cookie cutter pour avoir un projet bien structuré et Git pour facilité la collaboration en équipe.