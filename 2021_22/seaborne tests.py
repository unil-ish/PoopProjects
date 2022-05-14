# Import seaborn
import seaborn as sns
import matplotlib
import pandas as pd
import numpy as np

data_replique = np.array([["replique1","emotion3","emotion3"],
                 ["replique2","emotion5","emotion1"],
                 ["replique3","emotion3","emotion2"],
                 ["replique4","emotion2","emotion4"],
                 ["replique5","emotion4","emotion1"],
                 ["replique6","emotion2","emotion1"],
                 ["replique7","emotion2","emotion3"],
                 ["replique8","emotion1","emotion2"],
                 ["replique9","emotion3","emotion5"],
                 ["replique10","emotion2","emotion1"],
                 ["replique11","emotion4","emotion3"],
                 ["replique12","emotion4","emotion5"],
                 ["replique13","emotion4","emotion3"],
                 ["replique14","emotion2","emotion1"],
                 ["replique15","emotion1","emotion4"],
                 ["replique16","emotion3","emotion5"]])

data_char1 = np.array([["char1","emotion3","emotion3"],
                 ["char2","emotion5","emotion1"],
                 ["char3","emotion3","emotion2"],
                 ["char4","emotion2","emotion4"],
                 ["char5","emotion4","emotion1"],
                 ["char6","emotion2","emotion1"],
                 ["char7","emotion2","emotion3"],
                 ["char8","emotion1","emotion2"],
                 ["char9","emotion3","emotion5"],
                 ["char10","emotion2","emotion1"],
                 ["char11","emotion4","emotion3"],
                 ["char12","emotion4","emotion5"],
                 ["char13","emotion4","emotion3"],
                 ["char14","emotion2","emotion1"],
                 ["char15","emotion1","emotion4"],
                 ["char16","emotion3","emotion5"]])

data_char = np.array([[1,"emotion3","char1"],
                 [2,"emotion1","char2"],
                 [3,"emotion2","char3"],
                 [4,"emotion4","char4"],
                 [5,"emotion1","char5"],
                 [6,"emotion1","char6"],
                 [7,"emotion3","char7"],
                 [8,"emotion2","char8"],
                 [9,"emotion5","char9"],
                 [10,"emotion1","char10"],
                 [11,"emotion3","char11"],
                 [12,"emotion5","char12"],
                 [13,"emotion3","char13"],
                 [14,"emotion1","char14"],
                 [15,"emotion4","char15"],
                 [16,"emotion5","char16"]])

# pass column names in the columns parameter
df_replique = pd.DataFrame(data_replique, columns = ['replique', 'emotion 1','emotion 2'])
print(df_replique)

df_char = pd.DataFrame(data_char, columns = ['character', 'emotion 1','emotion 2'])
print(df_char)

# Apply the default theme
# Gray bg + grid
sns.set_theme()

# Makes the graph easier to read for presentations
sns.set_context("talk")

# Removes top and right borders for graph
#sns.despine()

# No grid + gray bg
#sns.set_style("dark")

# Adds ticks but no grid
#sns.set_style("ticks")


# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips, #kind="line", #makes it a line graph instead of scatter plot
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

#adds uncertainty
#sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")

#data_char = sns.load_dataset("emotions") #TEMP VAR
sns.jointplot(data=df_char, x="emotion 1", y="emotion 2", hue="character") #SOMETHING LIKE THIS


matplotlib.pyplot.show()