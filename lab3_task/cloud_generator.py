from wordcloud import WordCloud
import matplotlib.pyplot as plt

class WordCloudCreator:

    #some prescriptions

    STOPWORDS = "english"

    def create_cloud(word_string):

        cloud = WordCloud(font_path="/fonts/Symbola.ttf",
                          stopwords=STOPWORDS,
                          background_color='black',
                          width=1200,
                          height=1000
                          ).generate(word_string)

        plt.imshow(cloud)
        plt.axis('off')
        plt.show()

        return plt

