import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df1 = pd.read_json ('emotion_data.json')

sns.set_theme(style="whitegrid")

#doesn't cut off the X-axis labels
plt.subplots_adjust(bottom=0.30)

sns.barplot(x='emotion', y=df1.columns[1], data=df1)

#rotates the X-axis labels to improve readability
plt.xticks(rotation=60)

plt.show()