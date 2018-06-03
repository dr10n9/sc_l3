
from clusterizer import Clusterizer
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class Preprocessor:

    def remove_stopwords(self, word_list):

        processed_word_list = []
        for word in word_list:
            word = word.lower() # in case they aren't all lower cased
            if word not in stopwords.words("english"):
                processed_word_list.append(word)
        return processed_word_list


    def preprocess_text(self, raw_text):

        text = raw_text.lower()
        text = ''.join(c for c in text if c not in punctuation)
        wordlist = get_lemmatized(remove_stopwords(word_tokenize(text)))

        clusterizer = Clusterizer()
        clusters_dict = clusterizer.clusterize_text(' '.join(word[0] for word in wordlist))
        return clusters_dict


    def get_tokens(self, text):
     return word_tokenize(text)


    def get_lemmatized(self, word_list):

        lemmatized_wordlist = []
        lemmatizer = WordNetLemmatizer()
        lemmatized_wordlist.append([lemmatizer.lemmatize(t) for t in word_list])

        return lemmatized_wordlist


