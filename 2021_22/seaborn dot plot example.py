import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
df1 = pd.read_json ('emotion_data.json')


sns.set_theme(style="whitegrid")


# Make the PairGrid
g = sns.PairGrid(df1.sort_values("Gerard", ascending=False),
                 x_vars=df1.columns[-4:], y_vars=["emotion"],
                 height=10, aspect=.25)

# Draw a dot plot using the stripplot function
g.map(sns.stripplot, size=10, orient="h", jitter=False,
      palette="flare_r", linewidth=1, edgecolor="w")

# Use the same x axis limits on all columns and remove labels
g.set(xlim=(0, 15), xlabel="", ylabel="")

# Use column titles for their respective graph
titles = [df1.columns[1],df1.columns[2],df1.columns[3],df1.columns[4]]

for ax, title in zip(g.axes.flat, titles):

    # Set a different title for each axes
    ax.set(title=title)

    # Make the grid horizontal instead of vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)

sns.despine(left=True, bottom=True)

plt.show()