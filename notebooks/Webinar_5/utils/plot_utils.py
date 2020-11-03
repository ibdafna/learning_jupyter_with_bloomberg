import matplotlib.pyplot as plt

def set_style(style='blackviz'):
    plt.rc('figure', facecolor='0.065', autolayout=False, dpi=120)
    plt.rc('axes', facecolor='0.125', edgecolor='w', grid=True, labelcolor='lightgrey', labelsize='large',
                  prop_cycle=plt.cycler('color', ['deepskyblue', 'orangered', 'green', 'yellow', 'mintcream','magenta', 'darkorange']))
           
    plt.rc('xtick', color='w')
    plt.rc('ytick', color='w')
    plt.rc('grid', color='w', linestyle='-', alpha=0.25)
    plt.rc('font', size=12)
    plt.rc('text', color='lightgrey')
    plt.rc('lines', linewidth=2)
    plt.rc('figure', figsize = '10, 8', titlesize='x-large')