"""copyright: abhirup.ghosh.184098@gmail.com"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This makes our plots higher resolution
plt.rcParams['figure.dpi'] = 100


def make_economist_lineplot(fig_size=(8,4), 
                        title_text="Title", 
                        sub_title_text="Sub-title",
                        source_text="Source",
                        y_labels=np.arange(-120,20,20)):

    # Setup plot size.
    fig, ax = plt.subplots(figsize=fig_size)

    # Create grid 
    # Zorder tells it which layer to put it on. We are setting this to 1 and our data to 2 so the grid is behind the data.
    ax.grid(which="major", axis='y', color='#758D99', alpha=0.6, zorder=1)

    # Remove splines. Can be done one at a time or can slice with a list.
    ax.spines[['top','right','left']].set_visible(False)     

    # Reformat y-axis tick labels
    ax.set_yticklabels(y_labels,            # Set labels again
                   ha = 'right',                 # Set horizontal alignment to right
                   verticalalignment='bottom')   # Set vertical alignment to make labels on top of gridline

    ax.yaxis.set_tick_params(pad=-2,         # Pad tick labels so they don't go over y-axis
                         labeltop=True,      # Put y-axis labels on top
                         labelbottom=False,  # Set no x-axis labels on bottom
                         bottom=False,       # Set no ticks on bottom
                         labelsize=11)       # Set tick label size
    
    # Reformat x-axis tick labels
    ax.xaxis.set_tick_params(labeltop=False,      # Put x-axis labels on top
                         labelbottom=True,  # Set no x-axis labels on bottom
                         bottom=False,       # Set no ticks on bottom
                         labelsize=11,       # Set tick label size
                         pad=-1)             # Lower tick labels a bit

    # Add in line and tag
    ax.plot([0.12, .9],                  # Set width of line
        [.98, .98],                  # Set height of line
        transform=fig.transFigure,   # Set location relative to plot
        clip_on=False, 
        color='#E3120B', 
        linewidth=.6)
    ax.add_patch(plt.Rectangle((0.12,.98),                 # Set location of rectangle by lower left corder
                           0.04,                       # Width of rectangle
                           -0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#E3120B', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))

    # Add in title and subtitle
    ax.text(x=0.12, y=.91, s=title_text, transform=fig.transFigure, ha='left', fontsize=13, weight='bold', alpha=.8)
    ax.text(x=0.12, y=.86, s=sub_title_text, transform=fig.transFigure, ha='left', fontsize=11, alpha=.8)

    # Set source text
    ax.text(x=0.12, y=0.01, s=source_text, transform=fig.transFigure, ha='left', fontsize=9, alpha=.7)

    # Export plot as high resolution PNG
    #plt.savefig('images/economist_dumbbell.png',    # Set path and filename
    #            dpi = 300,                          # Set dots per inch
    #            bbox_inches="tight",                # Remove extra whitespace around plot
    #            facecolor='white')                  # Set background color to white

    return fig, ax


if __name__ == '__main__':

    x = np.linspace(0,1,100)
    y = 0.1*np.random.randn(len(x)) + 0.5

    fig, ax = make_economist_lineplot(y_labels=[0,1,2,3,4])
    ax.plot(x, y)

    ax.set_xlim([0,1])
    plt.show()