# Recommendation Systems

This project uses data science to build a recommendation systems for IBM Watson Studio, a collaborative community ecosystem of articles, datasets, notebooks and other AI nd ML assets.

## Getting Started

The recommendation systems are constructed step by step in the notebook Recommendations_with_IBM.ipynb.
The notebook is exported for review in html format with the same file name.

## Structure

The project has the following folders:
* **data**: contains the raw data for the project in csv format and pickled files for testing.
* **notebooks**: contains the data science workflow where the recommendation system is created.
    * Recommendations_with_IBM.ipynb: Jupyter notebook with step-by-step creation of the models.
    * Recommendations_with_IBM.html: An export of the notebook for review
    * project_tests.py: Test method to confirm the correctness of the approach in the notebool.
* **tests**: contains a simple test to check if the environment is correctly configured.

### Dependencies

Packages required for the analysis:
```
numpy
pandas
scikit-learn
matplotlib
```

Packages required for the IDE
```
notebook
ruff
pyright
pytest
pandoc
setuptools
```

## Installation

There are two ways to install this project:
* Use uv (https://docs.astral.sh/uv/) and sync with pyproject.toml
* Run pip install -r /requirements.txt

## License

[License](LICENSE.txt)
