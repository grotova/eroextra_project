import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_rgba

colors = ['#542788','#d8daeb','#f1a340','#b35806']
positions = [0, 0.45, 0.65, 1]
colormap_dict = {'red':[], 'green':[], 'blue':[]}

for i in range(len(colors)):
    r, g, b, _ = to_rgba(colors[i])
    colormap_dict['red'].append((positions[i], r, r))
    colormap_dict['green'].append((positions[i], g, g))
    colormap_dict['blue'].append((positions[i], b, b))

custom_cmap_gamma = LinearSegmentedColormap('purple-orange', colormap_dict)
