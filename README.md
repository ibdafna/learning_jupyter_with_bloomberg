# Jupyter Masterclass

This webinars series will be held in python, within a JupyterLab IDE.  Therefore as a basic requirements we need to have python installed on our computer thanks to a package manager: **pip** or **conda**.

### Pip and Conda
**Pip** is a general-purpose manager for Python packages;
**Conda** is a language-agnostic cross-platform environment manager.

For the user, the most salient distinction is probably this:
* pip installs *python* packages within *any* environment;
* conda installs *any* package within *conda* environments.

For **conda** installation: [https://docs.conda.io/projects/conda/en/latest/user-guide/install/](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

For **pip** installation: [https://packaging.python.org/tutorials/installing-packages/](https://packaging.python.org/tutorials/installing-packages/)

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
