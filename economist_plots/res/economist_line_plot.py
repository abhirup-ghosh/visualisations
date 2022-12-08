"""copyright: abhirup.ghosh.184098@gmail.com

This code aims at making The Economist-styled line plots.
This code is heavily influenced by Robert Ritz's code here:
https://www.datafantic.com/making-economist-style-plots-in-matplotlib-2/

The Economist itself details its graphics here:
https://www.economist.com/graphic-detail

and has a style-guide:
https://design-system.economist.com/documents/CHARTstyleguide_20170505.pdf

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This makes our plots higher resolution
plt.rcParams['figure.dpi'] = 100


def make_economist_lineplot(fig_size=(8,4), 
                        title_text="Title", 
                        sub_title_text="Sub-title",
                        source_text="Source"):

    # Setup plot size.
    fig, ax = plt.subplots(figsize=fig_size)

    # Create grid 
    ax.grid(which="major", axis='y', color='#758D99', alpha=0.2, zorder=1)    

    # Remove splines. Can be done one at a time or can slice with a list.
    ax.spines[['top','right','left']].set_visible(False)

    # Reformat y-axis tick labels
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
    ax.plot([0, 1],                 # Set width of line
            [1.25, 1.25],                  # Set height of line
        transform=ax.transAxes,   # Set location relative to plot
        clip_on=False, 
        color='#E3120B', 
        linewidth=.6)
    ax.add_patch(plt.Rectangle((0, 1.25),                 # Set location of rectangle by lower left corder
                            0.08,                       # Width of rectangle
                            -0.03,                      # Height of rectangle. Negative so it goes down.
                            facecolor='#E3120B', 
                            transform=ax.transAxes, 
                            clip_on=False, 
                            linewidth = 0))

    # Add in title and subtitle
    ax.text(x=0, y=1.15, s=title_text, transform=ax.transAxes, ha='left', fontsize=13, weight='bold', alpha=.8, fontname="Arial Narrow")
    ax.text(x=0, y=1.08, s=sub_title_text, transform=ax.transAxes, ha='left', fontsize=11, alpha=.8, fontname="Georgia")                         

    # Set source text
    ax.text(x=0, y=-0.12, s=source_text, transform=ax.transAxes, ha='left', fontsize=9, alpha=.7, fontname="Georgia")

    plt.tight_layout()

    return fig, ax


if __name__ == '__main__':


    # Make the base plot using the function above
    fig, ax = make_economist_lineplot(fig_size=(10,4))
    
    # dummy data to be plot
    x = np.linspace(0,1,100)
    for idx in range(10):
        ax.plot(x, np.random.randn(len(x)), alpha=0.3, lw=3, color='k')

    ax.set_xlim([0,1])
    ax.set_xlabel('time (s)', fontname = "Helvetica", fontsize=12)

    ## limits
    ax.set_ylim([-10, 10])    

    ## yticks
    ax.set_yticks(np.arange(-10, 15, 5))

    # Reformat y-axis tick labels
    ax.set_yticklabels([-10, -5, 0, 5, 10],            # Set labels again
                    ha = 'right',                 # Set horizontal alignment to right
                    verticalalignment='bottom')   # Set vertical alignment to make labels on top of gridline    

    # Export plot as high resolution PNG
    plt.savefig('economist_lineplot.png',    # Set path and filename
                dpi = 300,                          # Set dots per inch
                bbox_inches="tight",                # Remove extra whitespace around plot
                facecolor='white')                  # Set background color to white