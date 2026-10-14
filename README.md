# ODC — Python, Data Science & Machine Learning

Des premiers exercices Python à la classification d’images : ce dépôt rassemble mes travaux pratiques, mes supports de veille et mes projets de fin de formation ODC.

Il présente mon parcours à travers la manipulation de données, la visualisation, l’apprentissage supervisé et le clustering, sous forme de scripts Python et de notebooks Jupyter.

## Projets à découvrir

| Projet | Objectif | Méthodes et outils |
|---|---|---|
| [Réussite des apprenants](Projet%20de%20fin%20de%20formation/probleme1.ipynb) | Étudier les facteurs liés aux résultats des étudiants et modéliser leur réussite à partir des données OULAD. | Préparation des données, analyse exploratoire, régression logistique, matrices de confusion. |
| [Classification d’images](Projet%20de%20fin%20de%20formation/probleme2.ipynb) | Classer les images de CIFAR-10 dans dix catégories. | Réseau de neurones convolutif, Keras, augmentation de données, courbes d’apprentissage. |
| [Clustering de critiques de films](Projet%20de%20fin%20de%20formation/probleme3.ipynb) | Explorer le regroupement automatique de critiques du corpus IMDb. | CountVectorizer, K-means, méthode du coude avec Yellowbrick, projection avec TruncatedSVD. |
| [Titanic](titanic/titanic.ipynb) | Prédire la survie des passagers et expérimenter la prédiction de leur âge. | Prétraitement, création de variables, arbres de décision, validation croisée. |
| [Analyse de données de formation](Tp%20NumPy%20Pandas/Tp%20NumPy%20Pandas.ipynb) | Analyser les sessions, les scores et les taux de réussite par module à partir de données de suivi SCORM. | NumPy, pandas, agrégations et graphiques Matplotlib. |

## Compétences mises en pratique

- **Python** : fonctions, classes, listes, calculs et menus interactifs en console.
- **Analyse de données** : lecture de fichiers CSV, nettoyage, jointures, regroupements et création d’indicateurs.
- **Visualisation** : exploration des distributions, corrélations et résultats des modèles.
- **Machine learning** : classification, régression, validation croisée et apprentissage non supervisé.
- **Deep learning** : construction et entraînement d’un réseau convolutif pour la classification d’images.
- **Veille technique** : supports de présentation sur Python et Git.

## Organisation du dépôt

```text
odc/
├── Projet de fin de formation/
│   ├── probleme1.ipynb          # Réussite des apprenants
│   ├── probleme2.ipynb          # Classification d’images CIFAR-10
│   └── probleme3.ipynb          # Clustering de critiques IMDb
├── Tp NumPy Pandas/
│   ├── Tp NumPy Pandas.ipynb
│   └── scorm_tracking_copy.csv
├── Tp Python/
│   └── Exercice3/
│       ├── Exercice3.py         # Menu principal
│       ├── exercice1.py
│       └── exercice2.py
├── Veille 1 Python/             # Présentation PowerPoint
├── Veille Git/                  # Présentation PowerPoint
├── titanic/
│   ├── titanic.ipynb
│   ├── train.csv
│   ├── test.csv
│   └── ...                     # Fichiers de prédictions et de soumission
└── README.md
```

## Prise en main

Les notebooks peuvent être consultés directement sur GitHub. Pour travailler localement, installer Git et Python 3, puis cloner le dépôt :

```bash
git clone https://github.com/hkeyz/odc.git
cd odc
python -m venv .venv
```

Activer l’environnement virtuel sous **Windows PowerShell** :

```powershell
.\.venv\Scripts\Activate.ps1
```

Ou sous **Linux / macOS** :

```bash
source .venv/bin/activate
```

Installer les outils de base pour les notebooks d’analyse :

```bash
python -m pip install jupyterlab numpy pandas matplotlib seaborn scikit-learn plotly
jupyter lab
```

Ouvrir le notebook souhaité et vérifier les chemins des données avant d’exécuter ses cellules dans l’ordre.

Les notebooks de fin de formation comportent aussi des imports **TensorFlow / Keras** ; le troisième utilise **Yellowbrick**. Ces dépendances complémentaires doivent être installées dans des versions compatibles avec le code.

Pour lancer les exercices Python interactifs, depuis la racine du dépôt :

```bash
python "Tp Python/Exercice3/Exercice3.py"
```

## Données utilisées

| Travail | Disponibilité et préparation |
|---|---|
| TP NumPy / pandas | Le fichier `scorm_tracking_copy.csv` est inclus dans le dossier du notebook. |
| Titanic | Les fichiers `train.csv` et `test.csv` sont inclus dans `titanic/`. |
| Réussite des apprenants | Télécharger [OULAD auprès de l’Open University](https://research.stem.open.ac.uk/ouanalyse/dataset/). Placer `studentInfo.csv`, `assessments.csv`, `studentAssessment.csv`, `studentVle.csv` et `vle.csv` dans `Projet de fin de formation/anonymiseddata/`. |
| Classification d’images | Le notebook charge [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) avec `cifar10.load_data()`. Une connexion Internet est nécessaire au premier téléchargement. |
| Clustering de textes | Télécharger le [Large Movie Review Dataset de Stanford](https://ai.stanford.edu/~amaas/data/sentiment/), puis adapter le chemin passé à `load_files()` et l’organisation des dossiers au corpus retenu. Le notebook contient actuellement un chemin local propre à la machine d’origine. |

## État des travaux et reproductibilité

Ces travaux ont une vocation pédagogique. Les versions des bibliothèques ne sont pas figées dans un fichier de dépendances et les notebooks de fin de formation indiquent Python 3.9.13 dans leurs métadonnées.

La procédure ci-dessus prépare un environnement de travail ; elle ne garantit pas une exécution intégrale sans adaptation. Certains notebooks nécessitent des corrections de cellules, de chemins ou d’appels aux bibliothèques, notamment autour de Keras (`ImageDataGenerator`, `fit_generator`). Les métriques présentes dans les notebooks doivent être examinées avec leur protocole d’évaluation avant toute comparaison de performances.

## Pistes d’amélioration

- Documenter un environnement reproductible avec les versions des dépendances.
- Uniformiser les chemins d’accès aux données.
- Vérifier l’exécution complète des notebooks depuis un noyau vierge.
- Consolider l’évaluation des modèles et présenter une synthèse des résultats.

## Auteur

[hkeyz](https://github.com/hkeyz)

Pour signaler un problème ou proposer une amélioration, ouvrir une [issue](https://github.com/hkeyz/odc/issues).
