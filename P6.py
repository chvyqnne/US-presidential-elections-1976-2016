# Final Project Problem 4
# Cheyanne Cabang & Ricardo Sauerbrey

import os

# os.environ["PROJ_LIB"] = "Users\Ricardo\anaconda3\pkgs\proj-7.2.0-h3e70539_0\Library\lib"  # I had to do this for
# # basemap to work. Plz update to personal library
os.environ["PROJ_LIB"] = "Users\Ricardo\Documents\GitHub\CSC-148-final-project\proj-7.2.0-h3e70539_0"
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon


def us_map_2016():
    m = Basemap(llcrnrlon=-119,
                llcrnrlat=22,
                urcrnrlon=-64,
                urcrnrlat=49,  # coordinates for US Map
                projection='lcc',  # Lambert Conformal projection
                lat_1=33,
                lat_2=45,
                lon_0=-95,
                resolution='c')

    plt.title('Map of 2016 Presidential Elections')  # Title for the Plot

    # https://github.com/matplotlib/basemap/raw/master/examples/st99_d00.shp
    m.readshapefile('st99_d00', name='states', drawbounds=True)

    state_names = []
    for shape_dict in m.states_info:
        state_names.append(shape_dict['NAME'])  # Gathers the names of states from the shp file to look up by name

    ax = plt.gca()  # current axes

    seg = m.states[state_names.index('Texas')]  # Selects the desired state
    poly = Polygon(seg, facecolor='red', edgecolor='red')  # changes the color to red or blue
    ax.add_patch(poly)

    seg = m.states[state_names.index('Florida')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Georgia')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Alabama')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Mississippi')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Louisiana')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Oklahoma')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Arkansas')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('South Carolina')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('North Carolina')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Tennessee')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Kentucky')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('West Virginia')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Pennsylvania')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Ohio')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Indiana')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Michigan')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Wisconsin')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Missouri')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Kansas')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Nebraska')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Iowa')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('South Dakota')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('North Dakota')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Montana')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Wyoming')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Idaho')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Utah')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Arizona')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Alaska')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    seg = m.states[state_names.index('California')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Oregon')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Washington')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Nevada')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Colorado')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('New Mexico')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Minnesota')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Illinois')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Virginia')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Maryland')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('District of Columbia')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Delaware')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('New Jersey')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Connecticut')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Rhode Island')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Massachusetts')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('New York')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Vermont')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('New Hampshire')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Maine')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    seg = m.states[state_names.index('Hawaii')]
    poly = Polygon(seg, facecolor='blue', edgecolor='blue')
    ax.add_patch(poly)

    plt.show()


us_map_2016()