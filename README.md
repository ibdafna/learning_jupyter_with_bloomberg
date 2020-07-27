# Jupyter Masterclass

The “Learn Jupyter with Bloomberg” webinar series is focused on Jupyter, and will cover an introduction to comparison between the classic Jupyter Notebook and JupyterLab, as well as how to choose a data source, how to analyze your data, and an overview of widgets and dashboarding. 

 - Learn Jupyter with Bloomberg: Introduction
 - Learn Jupyter with Bloomberg: Choosing a Data Source
- Learn Jupyter with Bloomberg: Analyzing Data Using Pandas
- Learn Jupyter with Bloomberg: Intro to Widgets Ecosystem and ipywidgets
- Learn Jupyter with Bloomberg: Interactive Visualization with bqplot
- Learn Jupyter with Bloomberg: Dashboarding and Deployment with Voilà

## Local installation with conda
```bash
conda env create -f binder/environment.yml

conda activate jupyter-masterclass

# Create a kernel for this environment
ipython kernel install --name jupyter-masterclass --display-name jupyter-masterclass --sys-prefix
```

## Use an online preconfigured environment
**Binder is great for experimenting, but note any changes you make to files will not persist, and the environment will time out after a period of inactivity**

Try this repo on Binder:

[![Binder](docs/source/binder-logo.svg)](https://mybinder.org/v2/gh/ibdafna/jupyter_masterclass/master?urlpath=lab)
