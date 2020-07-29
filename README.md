# Learning Jupyter with Bloomberg

This webinar will run Python code in JupyterLab. Therefore, as a basic requirement, you will need to have both Python and JupyterLab installed on your computer. Fortunately this is made easier thanks to package managers like *_Conda_* and *_Pip_*.

## Local or online
You have two options when it comes to installing and running a working Python environment:
1. Use a custom, local installation
2. Use an online, pre-configured environment

We recommend following along with a local installation, as it achieves two main goals: it teaches an integral part of development and Python programming in general, and it gives you more control over the installed packages and your data (which will persist in a local installation, but might not in an online environment). The instructions below will cover both options.

### Conda and Pip
**Conda** is a language-agnostic cross-platform environment manager.
**Pip** is a general-purpose manager for Python packages.

For you, the user, the most salient distinction is probably this:
* **Conda** installs *any* package within *conda* environments;
* **Pip** installs *Python* packages within *any* environment.

**We highly recommend using Conda as your package manager for this webinar, as it will allow you to install non-Python dependencies in an isolated environment. This will make for a much smoother installation process! But, if you still want to use pip, we have provided installation instructions below.**

For **Conda** installation: [https://docs.conda.io/projects/conda/en/latest/user-guide/install/](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
For **Pip** installation: [https://packaging.python.org/tutorials/installing-packages/](https://packaging.python.org/tutorials/installing-packages/)

## Local installation with Conda

```bash
# Clone this repository
git clone https://github.com/ibdafna/jupyter_masterclass

# Navigate into the root directory of the clone repository
cd jupyter_masterclass

# Execute the Conda installation recipe file. This will create Conda environment and install all dependencies.
conda env create -f binder/environment.yml

# Activate the Conda environment
conda activate jupyter-masterclass

# Create a kernel for this environment
ipython kernel install --name jupyter-masterclass --display-name jupyter-masterclass --sys-prefix

# Build JupyterLab assets
jupyter labextension install @jupyter-widgets/jupyterlab-manager bqplot
```

Once you are done with the installation steps, you can start JupyterLab by executing `jupyter lab` in the root repo directory.

## Local installation with Pip
`Pip` is a Python package manager. As such, it can only bundle Python-related packages such as `pandas`, `numpy`, etc. Although Python is a big and integral part of the Jupyter ecosystem, we rely on other languages, such as JavaScript and TypeScript, for all of the front-end code. This means that we work with `nodejs` and `npm` quite a lot. 

To build JupyterLab and its assets, we need to transpile TypeScript code into JavaScript code and then bundle it into a single file which is consumed by the web browser. This process is achieved with `npm`, a JavaScript package manager. `npm` is bundled with `nodejs`, so to get it installed, you will need to follow the 'nodejs' installation process. Please make sure `npm` is installed on your machine before continuing with the installation instructions below. 

**nodejs/npm** installation: [https://nodejs.org/en/](https://nodejs.org/en/)

Once you have installed `npm`, follow the installation instructions below:
```bash
# Clone this repository
git clone https://github.com/ibdafna/jupyter_masterclass

# Navigate into the root directory of the clone repository
cd jupyter_masterclass

# Create a virtual python virtual environment
virtualenv jupyter-masterclass

# Activate the virtual environment
source jupyter-masterclass/bin/activate

# Install all packages
python -m pip install -r requirements.txt

# Create a kernel for this environment
ipython kernel install --name jupyter-masterclass --display-name jupyter-masterclass --sys-prefix

# Build JupyterLab assets
jupyter labextension install @jupyter-widgets/jupyterlab-manager bqplot
```

Once you are done with the installation steps, you can start JupyterLab by executing `jupyter lab` in the root repo directory.

## Use an online, pre-configured environment

**Binder is great for experimenting, but note that any changes you make to these files will not persist, and the environment will time out after a period of inactivity**

Click the image below to run Binder with a pre-configured Jupyter Masterclass environment:

[![Binder](docs/source/binder-logo.svg)](https://mybinder.org/v2/gh/ibdafna/jupyter_masterclass/master?urlpath=lab)
