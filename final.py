######################---------------------------------#############################################
###################### Code By Kannan, Akshay, Balaji  #############################################
######################---------------------------------#############################################

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
 
def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
 
    if tag.startswith('V'):
        return 'v'
 
    if tag.startswith('J'):
        return 'a'
 
    if tag.startswith('R'):
        return 'r'
 
    return None
 

def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
 
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
 

def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
 
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
    
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
 
    score, count = 0.0, 0
    if(synsets1!=[] and synsets2!=[]): 
    # For each word in the first sentence
      for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = max([synset.path_similarity(ss) for ss in synsets2])
 
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1
    else:
       return 0
    # Average the values
    if count==0:
       return 0
    else:
     score /= count
     return score
count11=0
with open("final_test.csv","w") as result:
  writer=csv.writer(result)
  with open("test.csv","r") as source:
         reader=csv.reader(source)
         next(reader)
         for r in reader:
             score=sentence_similarity(r[1],r[2])
             writer.writerow((r[1],r[2],score))


#######################################################################################################
