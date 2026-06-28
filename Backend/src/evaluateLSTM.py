from sklearn.metrics.pairwise import cosine_similarity
import pickle
from feature_engineer import featured_data


df,data=featured_data()
vectorizer=pickle.load(open('../models/vectorizer.pkl','rb'))
vector=pickle.load(open('../models/vector.pkl','rb'))

def evaluate(query):
    q_vector=vectorizer.transform([query])
    similar=cosine_similarity(q_vector,vector).flatten()
    idx=similar.argmax()
    print(similar[idx])
    print(df.iloc[idx])
    result=df.iloc[idx]
    return result


