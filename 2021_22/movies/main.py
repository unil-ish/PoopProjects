list_1st_emotion = []
list_2nd_emotion = []

for w in disambiguate_dialog_df["Word"]:
    #wm=w.lower()

    if w in senticnet.senticnet.keys():
        #mylist = senticnet.senticnet[wm]
        #print(f'key for word {wm} : {senticnet.senticnet[wm]} which sentiments are : {senticnet.senticnet[wm][4]} and {mylist[5].strip("#")}')
        list_1st_emotion.append(senticnet.senticnet[w][4])
        list_2nd_emotion.append(senticnet.senticnet[w][5])
    elif w in senticnet.senticnet.values():
        list_1st_emotion.append(senticnet.senticnet[w][4])
        list_2nd_emotion.append(senticnet.senticnet[w][5])
        print("Synonyme")
    elif w not in senticnet.senticnet.keys() and senticnet.senticnet.values() :
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
            else :
                list_1st_emotion.append("not found")
                list_2nd_emotion.append("not found")
        else:
            list_1st_emotion.append("not found")
            list_2nd_emotion.append("not found")

disambiguate_dialog_df["1st Emotion"] = list_1st_emotion
disambiguate_dialog_df["2nd Emotion"] = list_2nd_emotion

print(disambiguate_dialog_df)