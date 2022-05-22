import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

# fig, axs = plt.subplots(ncols=2)

df1 = pd.read_json('primary_emotions_data.json')

ax = sns.countplot(x="Primary_emotion", hue="Secondary_emotion", data=df1)

plt.show()