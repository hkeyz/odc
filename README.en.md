# ODC — Python, Data Science & Machine Learning

[Français](README.md) | **English**

From introductory Python exercises to image classification, this repository brings together my practical assignments, technical presentations, and final projects from my ODC training.

It documents my learning journey through data manipulation, visualization, supervised learning, and clustering, using Python scripts and Jupyter notebooks.

## Featured projects

| Project | Objective | Methods and tools |
|---|---|---|
| [Student success prediction](Projet%20de%20fin%20de%20formation/probleme1.ipynb) | Explore factors associated with student outcomes and model student success using OULAD data. | Data preparation, exploratory analysis, logistic regression, confusion matrices. |
| [Image classification](Projet%20de%20fin%20de%20formation/probleme2.ipynb) | Classify CIFAR-10 images into ten categories. | Convolutional neural network, Keras, data augmentation, learning curves. |
| [Movie review clustering](Projet%20de%20fin%20de%20formation/probleme3.ipynb) | Explore automatic grouping of reviews from the IMDb corpus. | CountVectorizer, K-means, the elbow method with Yellowbrick, projection with TruncatedSVD. |
| [Titanic](titanic/titanic.ipynb) | Predict passenger survival and experiment with age prediction. | Preprocessing, feature engineering, decision trees, cross-validation. |
| [Learning activity analysis](Tp%20NumPy%20Pandas/Tp%20NumPy%20Pandas.ipynb) | Analyze sessions, scores, and pass rates by module using SCORM tracking data. | NumPy, pandas, aggregations, and Matplotlib charts. |

## Skills practiced

- **Python**: functions, classes, lists, calculations, and interactive command-line menus.
- **Data analysis**: reading CSV files, cleaning, joining, grouping, and building indicators.
- **Visualization**: exploring distributions, correlations, and model results.
- **Machine learning**: classification, regression, cross-validation, and unsupervised learning.
- **Deep learning**: building and training a convolutional neural network for image classification.
- **Technical research**: presentations on Python and Git.

## Repository structure

```text
odc/
├── Projet de fin de formation/
│   ├── probleme1.ipynb          # Student success prediction
│   ├── probleme2.ipynb          # CIFAR-10 image classification
│   └── probleme3.ipynb          # IMDb review clustering
├── Tp NumPy Pandas/
│   ├── Tp NumPy Pandas.ipynb
│   └── scorm_tracking_copy.csv
├── Tp Python/
│   └── Exercice3/
│       ├── Exercice3.py         # Main menu
│       ├── exercice1.py
│       └── exercice2.py
├── Veille 1 Python/             # PowerPoint presentation
├── Veille Git/                  # PowerPoint presentation
├── titanic/
│   ├── titanic.ipynb
│   ├── train.csv
│   ├── test.csv
│   └── ...                     # Prediction and submission files
├── README.md                   # French version
└── README.en.md                # English version
```

## Getting started

You can view the notebooks directly on GitHub. To work locally, install Git and Python 3, then clone the repository:

```bash
git clone https://github.com/hkeyz/odc.git
cd odc
python -m venv .venv
```

Activate the virtual environment in **Windows PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on **Linux / macOS**:

```bash
source .venv/bin/activate
```

Install the core tools for the data analysis notebooks:

```bash
python -m pip install jupyterlab numpy pandas matplotlib seaborn scikit-learn plotly
jupyter lab
```

Open a notebook and check its data paths before running the cells in order.

The final project notebooks also include **TensorFlow / Keras** imports; the third notebook uses **Yellowbrick** as well. Install versions of these additional dependencies that are compatible with the code.

To run the interactive Python exercises from the repository root:

```bash
python "Tp Python/Exercice3/Exercice3.py"
```

## Datasets

| Work | Availability and setup |
|---|---|
| NumPy / pandas assignment | `scorm_tracking_copy.csv` is included in the notebook's directory. |
| Titanic | `train.csv` and `test.csv` are included in `titanic/`. |
| Student success prediction | Download [OULAD from the Open University](https://research.stem.open.ac.uk/ouanalyse/dataset/). Place `studentInfo.csv`, `assessments.csv`, `studentAssessment.csv`, `studentVle.csv`, and `vle.csv` in `Projet de fin de formation/anonymiseddata/`. |
| Image classification | The notebook loads [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) using `cifar10.load_data()`. Internet access is required for the initial download. |
| Text clustering | Download the [Stanford Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/), then adjust the path passed to `load_files()` and the directory structure to match the selected corpus. The notebook currently contains a local path specific to the original machine. |

## Project status and reproducibility

These projects were created for learning purposes. Library versions are not pinned in a dependency file, and the final project notebooks list Python 3.9.13 in their metadata.

The steps above set up a working environment; they do not guarantee that every notebook will run from start to finish without changes. Some notebooks require fixes to cells, paths, or library calls, particularly those involving Keras (`ImageDataGenerator`, `fit_generator`). Review the evaluation methodology behind the reported metrics before comparing model performance.

## Possible improvements

- Document a reproducible environment with pinned dependency versions.
- Standardize data paths.
- Verify that each notebook runs from start to finish with a fresh kernel.
- Strengthen model evaluation and provide a summary of results.

## Author

[hkeyz](https://github.com/hkeyz)

To report a problem or suggest an improvement, open an [issue](https://github.com/hkeyz/odc/issues).
