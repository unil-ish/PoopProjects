# Import the packages that we need
import senticnet
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

# Import every .py file that we need
import preprocessor
import disambiguator
import emo_extractor
import visualizator

import matplotlib.pyplot as plt

# Run every classes in the correct order
def main():

    # Run the preprocessor, we give it the path to the folders, and it returns the dataframe with speaker and speeches
    processor = preprocessor.Preprocessor('../data/dialogs_movies')
    df_speakers_speeches = processor.process_speakers_and_speeches()
    #print(df_speakers_speeches)

    # Run the visualizator, that take the previous dataframe (speaker/speech) and return a graph
    visualize = visualizator.Visualizator(df_speakers_speeches)
    visualization_gender = visualize.gender_visualize()
    # print(visualization_gender)
    plt.show()
    visualization_file = visualize.file_vizualize()
    #print(visualization_file)
    plt.show()

    # Run the disambiguator, that take the previous dataframe (speaker/speech) and return a new dataframe
    # with a disambiguated column
    disambiguer = disambiguator.Disambiguator(df_speakers_speeches)
    disambiguated_df = disambiguer.disambiguate()
    # print(disambiguated_df)

    # Run the emotions extractor, that take the previous dataframe (disambiguated) and return a new one
    # with 2 new columns, 1st and 2nd emotion.
    emoextractor = emo_extractor.Emo_Extractor(disambiguated_df)
    emotions_df = emoextractor.extract_emotion()
    #print(emotions_df)

    # Save the dataframe into a CSV file
    emotions_df.to_csv('the_dataframe.csv')

#2498 texts

if __name__ == "__main__":
    main()