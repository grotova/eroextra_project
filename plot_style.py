import matplotlib.font_manager
import matplotlib.pyplot as plt

def set_plot_style():
    
    plt.rcParams['figure.figsize'  ] = (2*10/3,3)
    plt.rcParams['font.size'       ] = 9
    plt.rcParams['legend.fontsize' ] = 9
    plt.rcParams['legend.frameon'  ] = True
    plt.rcParams['xtick.direction' ] = 'in'
    plt.rcParams['ytick.direction' ] = 'in'
    plt.rcParams['xtick.top'       ] = False
    plt.rcParams['ytick.right'     ] = False
    plt.rcParams['xtick.major.size'] = 2
    plt.rcParams['xtick.minor.size'] = 1
    plt.rcParams['ytick.major.size'] = 2
    plt.rcParams['ytick.minor.size'] = 1
    plt.rcParams['xtick.major.width'] = 0.75
    plt.rcParams['xtick.minor.width'] = 0.5
    plt.rcParams['ytick.major.width'] = 0.75
    plt.rcParams['ytick.minor.width'] = 0.5
    plt.rc('axes', titlesize=9)     
    plt.rc('axes', labelsize=9) 
    #plt.rc('font', family='Nimbus Roman')
    plt.rc('font', family='Times New Roman')
    
    


