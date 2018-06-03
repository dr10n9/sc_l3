from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# documents = ["Human machine interface for lab abc computer applications",
#              "A survey of user opinion of computer system response time",
#              "The EPS user interface management system",
#              "System and human system engineering testing of EPS",
#              "Relation of user perceived response time to error measurement",
#              "The generation of random binary unordered trees",
#              "The intersection graph of paths in trees",
#              "Graph minors IV Widths of trees and well quasi ordering",
#              "Graph minors A survey"]


class Clusterizer:

    def clusterize_text(self, text):

        #vectorizing(converting strings to numeric values)

        vectorizer = TfidfVectorizer(stop_words='english')
        #X = vectorizer.fit_transform(documents)
        vector = vectorizer.fit_transform(text)

        print(vector.shape)
        print(type(vector))
        print(vector.toarray())

        #clustering

        true_k = 2
        km_model = KMeans(n_clusters=true_k, init='random', max_iter=100, n_init=1, verbose=1)
        #model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)

        km_model.fit(vector)
        labels = km_model.predict(vector)

        row_dict = {} ## in row_dict we store actual meanings of rows, in our case it's russian words
        clusters = {}
        n = 0
        for item in labels:
            if item in clusters:
                clusters[item].append(row_dict[n])
            else:
                clusters[item] = [row_dict[n]]
            n += 1

        #print the result
        for item in clusters:
            print("Cluster ", item)
            for i in clusters[item]:
                print(i)

        return clusters

        # print top terms per cluster clusters
        # print("Top terms per cluster:")
        # order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        # terms = vectorizer.get_feature_names()
        # for i in range(true_k):
        #     print
        #     "Cluster %d:" % i,
        #     for ind in order_centroids[i, :10]:
        #         print
        #         ' %s' % terms[ind],
        #     print