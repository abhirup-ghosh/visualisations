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


def make_economist_barplot(fig_size=(3,6), 
                        title_text="Title", 
                        sub_title_text="Sub-title",
                        source_text="Source"):

    # Setup plot size.
    fig, ax = plt.subplots(figsize=fig_size)

    # Create grid 
    # Zorder tells it which layer to put it on. We are setting this to 1 and our data to 2 so the grid is behind the data.
    ax.grid(which="major", axis='x', color='#758D99', alpha=0.6, zorder=1)

    # Remove splines. Can be done one at a time or can slice with a list.
    ax.spines[['top','right','bottom']].set_visible(False)

    # Make left spine slightly thicker
    ax.spines['left'].set_linewidth(1.1)
    ax.spines['left'].set_linewidth(1.1)

    # Reformat x-axis tick labels
    ax.xaxis.set_tick_params(labeltop=True,      # Put x-axis labels on top
                            labelbottom=False,  # Set no x-axis labels on bottom
                            bottom=False,       # Set no ticks on bottom
                            labelsize=11,       # Set tick label size
                            pad=-1)             # Lower tick labels a bit

    # Reformat y-axis tick labels
    ax.yaxis.set_tick_params(pad=2,            # Pad tick labels so they don't go over y-axis
                            labelsize=11,       # Set label size
                            bottom=False)       # Set no ticks on bottom/left


    # Add in line and tag
    ax.plot([-.1, .87],                 # Set width of line
        [1.02, 1.02],                # Set height of line
            transform=fig.transFigure,   # Set location relative to plot
            clip_on=False, 
            color='#E3120B', 
            linewidth=.6)
    ax.add_patch(plt.Rectangle((-.1,1.02),                # Set location of rectangle by lower left corder
                           0.12,                       # Width of rectangle
                           -0.02,                      # Height of rectangle. Negative so it goes down.
                            facecolor='#E3120B', 
                            transform=fig.transFigure, 
                            clip_on=False, 
                            linewidth = 0))

    # Add in title and subtitle
    ax.text(x=-.1, y=.96, s=title_text, transform=fig.transFigure, ha='left', fontsize=10, weight='bold', alpha=.8, fontname="Arial Black")
    ax.text(x=-.1, y=.925, s=sub_title_text, transform=fig.transFigure, ha='left', fontsize=8, alpha=.8, fontname="Arial Narrow")

    # Set source text
    ax.text(x=-.1, y=.05, s=source_text, transform=fig.transFigure, ha='left', fontsize=5, alpha=.7, fontname="Arial Narrow")

    plt.tight_layout()

    return fig, ax


if __name__ == '__main__':


    # Make the base plot using the function above
    fig, ax = make_economist_barplot(fig_size=(5,5),
                                    title_text="Ahead of the pack",
                                    sub_title_text="Top 9 countries by GDP, in trillions of USD",
                                    source_text="""Source: "GDP of all countries(1960-2020)" via Kaggle.com""")



    # Setup data
    gdp = pd.read_csv('../notebooks/gdp_1960_2020.csv')
    gdp['gdp_trillions'] = gdp['gdp'] / 1_000_000_000_000
    gdp['country'] = gdp['country'].replace('the United States', 'United States')
    gdp_bar = gdp[gdp['year'] == 2020].sort_values(by='gdp_trillions')[-9:]
    # Plot data
    ax.barh(gdp_bar['country'], gdp_bar['gdp_trillions'], color='#006BA2', zorder=2)

    # Set custom labels for x-axis
    ax.set_xticks([0, 5, 10, 15, 20])
    ax.set_xticklabels([0, 5, 10, 15, 20])

    # Set custom labels for y-axis
    ax.set_yticklabels(gdp_bar['country'],      # Set labels again
                    ha = 'right')              # Set horizontal alignment to left

    # Shrink y-lim to make plot a bit tighter
    ax.set_ylim(-0.5, 8.5)

    # Export plot as high resolution PNG
    plt.savefig('economist_barplot.png',    # Set path and filename
                dpi = 300,                          # Set dots per inch
                bbox_inches="tight",                # Remove extra whitespace around plot
                facecolor='white')                  # Set background color to white
