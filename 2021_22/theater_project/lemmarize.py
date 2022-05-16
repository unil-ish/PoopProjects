from pywsd import disambiguate as dis
from pywsd.similarity import max_similarity as maxsim
import pandas as pd

""" THIS PROGRAMM IS A WORK IN PROGRESS

This programm uses the disambiguate module from the pywsd library in order to extract
all lemmas from disambiguated Synsets of ambiguous words. Returns a Panda DataFrame with:
   
    - Columns : Disambiguated words
    - Rows : Possible lemmas of the disambiguated sense of the word.

Returns a DataFrame with a single row of arrays as of right now. Trying to fix it has proven quite difficult.

"""

# Initializing some variables
test = "The sound waves are pouring on me"
synset_array = []
syn_df = pd.DataFrame()

# Disambiguate function 
disamb = (dis(test, algorithm=maxsim, similarity_option='wup', keepLemmas=True))

# Extracting every disambiguated Synset
# Since disambiguate returns a list of tuples 
# we can use unpacking to extract all disambiguated Synsets.
for disamb_tuple in disamb:
    (word, wroot, synset) = disamb_tuple
    if synset:
        synset_array.append(synset)

# Store all lemmas of disambiguated Synset 
for syn in synset_array:
    syn_df[syn.lemma_names()[0]] = pd.Series([syn.lemma_names()])


# WORK IN PROGRESS
#for sy, _ in enumerate(synset_array):
#
#    dataframe = dataframe.explode([synset_array[sy].lemma_names()[0]], ignore_index=True)


print(syn_df)

