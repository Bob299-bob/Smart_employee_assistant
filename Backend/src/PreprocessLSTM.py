import tensorflow as tf
from tensorflow.keras import layers
from sklearn.feature_extraction.text import TfidfVectorizer
from feature_engineer import featured_data
import pickle

df,data=featured_data()
vectorizer=TfidfVectorizer()
#Embedding into vectors
vector1=vectorizer.fit_transform(data)
pickle.dump(vector1,open('../models/vector.pkl','wb'))
pickle.dump(vectorizer,open('../models/vectorizer.pkl','wb'))