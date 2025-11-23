import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle


# loading file (spam.csv) - path thoda adjust karna pade to dekh lena
d = pd.read_csv("../dataset/spam.csv", encoding="latin-1")

# only these two cols matter.. baaki faltu hatadiye
d = d[['v1','v2']]
d.columns = ['lab','txt']  


# converting ham/spam into numbers (0/1 basically)
# I could use map but apply laga diya... habit hai meri
def _m(x):
    if x == "spam":
        return 1
    return 0

d["y"] = d["lab"].apply(_m)


# split kar diya.. 80/20.. kuch khas reason nahi bas default yahi rakhta hu
x_tr, x_ts, y_tr, y_ts = train_test_split(
    d.txt, d.y, test_size = 0.2, random_state = 42
)


# tfidf init. Stopwords english rakhe (zyada fark nahi padta honestly)
tfidf = TfidfVectorizer(stop_words="english")
Xtr = tfidf.fit_transform(x_tr)



# Model bana diya - NB hi simplest lagta spam ke liye
model_nb = MultinomialNB()
model_nb.fit(Xtr, y_tr)



# saving model & vectorizer .. haan path sahi hona chahiye
m_path = "../model/spam_model.pkl"
v_path = "../model/vectorizer.pkl"

with open(m_path, "wb") as mm:
    pickle.dump(model_nb, mm)

with open(v_path, "wb") as vv:
    pickle.dump(tfidf, vv)


print("ok stored.. I guess it's done")