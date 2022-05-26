import senticnet
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
import preprocessor
import disambiguator
import emo_extractor


def main():

    processor = preprocessor.Preprocessor('../data/dialogs_movies')
    df_speakers_speeches = processor.process_speakers_and_speeches()
    #print(df_speakers_speeches)

    disambiguer = disambiguator.Disambiguator(df_speakers_speeches)
    disambiguated_df = disambiguer.disambiguate()
    #print(disambiguated_df)

    emoextractor = emo_extractor.Emo_Extractor(disambiguated_df)
    emotions_df = emoextractor.extract_emotion()
    #print(emotions_df)




"""

def main2():
    preprocessor = Preprocessor()
    disambiguator = Disambiguator()
    emo_extractor = Emo_Extractor()

    list_1st_emotion = []
    list_2nd_emotion = []

    for w in disambiguate_dialog_df["Word"]:
        #wm=w.lower()
        if w in senticnet.senticnet.keys():
            emo_extractor.extract_emotion()
        elif w in senticnet.senticnet.values():
            emo_extractor.extract_emotion()
        elif w not in senticnet.senticnet.keys() and senticnet.senticnet.values() :
            #
            check_w = wn.synsets(w)
            if check_w:
                word = wn.synsets(w)[0]
                check_hypernym = word.hypernyms()
                if check_hypernym :
                    hypernym_word = word.hypernyms()[0]
                    regex = re.compile("(?<=Synset\(')[^_.]+")
                    regex_word = str(regex.findall(str(hypernym_word)))
                    ok_word_1 = regex_word.replace("['", "")
                    ok_word_2 = ok_word_1.replace("']", "")
                    if ok_word_2 in senticnet.senticnet.keys() or senticnet.senticnet.values() :
                        emotion_1 = senticnet.senticnet[ok_word_2][4]
                        emotion_2 = senticnet.senticnet[ok_word_2][5]
                        list_1st_emotion.append(emotion_1)
                        list_2nd_emotion.append(emotion_2)
                        disambiguate_dialog_df["1st Emotion"] = list_1st_emotion
                        disambiguate_dialog_df["2nd Emotion"] = list_2nd_emotion
                else :
                    list_1st_emotion.append("not found")
                    list_2nd_emotion.append("not found")
                    disambiguate_dialog_df["1st Emotion"] = list_1st_emotion
                    disambiguate_dialog_df["2nd Emotion"] = list_2nd_emotion
            else:
                list_1st_emotion.append("not found")
                list_2nd_emotion.append("not found")
                disambiguate_dialog_df["1st Emotion"] = list_1st_emotion
                disambiguate_dialog_df["2nd Emotion"] = list_2nd_emotion


    print(disambiguate_dialog_df)
"""

if __name__ == "__main__":
    main()