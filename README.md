# Jupyter Masterclass

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
