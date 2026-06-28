#import library
from ddgs import DDGS
import pdfplumber
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

#Defining Embedding Model
model=SentenceTransformer(
    'all-MiniLM-L6-V2'
)

#extract pdf
def extract_pdf(pdf):
    data=""
    with pdfplumber.open(pdf) as file:
        for page in file.pages:
            page_text=page.extract_text()
            if page_text:
                data+=page_text+""
    return data

#Internet Search
def search(query):
    result=[]
    try:
        with DDGS() as ddgs:
            search_result=list(ddgs.text(query,max_results=5))
            for results in search_result:
                result.append(f"Content:{results.get('body','')}") 
    except Exception as e:
        print(e)
    return "\n\n".join(result)

#to divide data into chunks 
def data_chunk(data):
    chunks=[]
    for c in data.split("\n\n"):
        c=c.strip()
        if len(c)>20:
            chunks.append(c)
    return chunks 

#rag_system
def rag_system(chunk_data):
    embed_data=np.array(model.encode(chunk_data)).astype('float32')
    faiss.normalize_L2(embed_data)
    index=faiss.IndexFlatL2(embed_data.shape[1])
    index.add(embed_data)
    return index

#Retrieve_system
def retrieve_system(query,index,chunk_data):
    embed_query=model.encode([query]).astype('float32')
    faiss.normalize_L2(embed_query)
    distance,indices=index.search(embed_query,k=3)
    context=[]
    for idx in indices[0]:
        context.append(chunk_data[idx])
    return "\n\n".join(context)

"""data=extract_pdf('mdecial.pdf')
chunk=data_chunk(data)
index=rag_system(chunk)
query='what document is this'
result=retrieve_system(query,index,chunk)
print(f'result is \n{result}')"""