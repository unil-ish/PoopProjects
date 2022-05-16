from codes import xml2df
import seaborn as sns
import matplotlib.pyplot as plt
data = xml2df("./data/AbrahamLincolnbyJohnDrinkwater11172.xml")

#interface catplot
g = sns.catplot(
    data=data, kind="count",
    y="speaker"
)
plt.xlabel('speech_count')
#saving figures to file
plt.savefig('data_image.jpg')

data_2 = xml2df("./data/AManofthePeopleADramaofAbrahamLincolnbyThomasDixon25814.xml")

diagramme = sns.swarmplot(
    x="speaker", y="speech",
    data=data
)
plt.savefig('data_2_image.jpg')