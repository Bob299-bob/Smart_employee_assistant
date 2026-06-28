#import library
from rag import extract_pdf,data_chunk,rag_system,retrieve_system,search
from dotenv import load_dotenv
import os
from groq import Groq


#fetch api
load_dotenv()
client=Groq(api_key=os.getenv('GROQ_API_KEY'))

def prerag(query,context,search_result):
    search_result=search_result[:4000]
    context=context[:4000]
    prompt=f"""
You are an intelligent PDF Brain assistant.

Your task is to answer the user's question using ONLY the information provided in the PDF context and retrieved search results.

Instructions:
1. Carefully analyze the provided context.
2. Answer the question accurately and concisely.
3. If the answer exists in the context, provide a detailed response.
4. If the context contains partial information, answer with what is available and mention any limitations.
5. If the answer is NOT present in the context, respond with:
   "I could not find this information in the provided PDF."
6. Do NOT make up facts or use external knowledge.
7. When possible, cite relevant sections or key details from the context.

User Question:
{query}

PDF Context:
{context}

Retrieved Chunks:
{search_result}

Answer:
"""
    response=client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=[{'role':'user','content':prompt}]
    )
    return response.choices[0].message.content

"""
data=extract_pdf('mdecial.pdf')
chunk=data_chunk(data)
index=rag_system(chunk)
query='what document is this'
result=retrieve_system(query,index,chunk)
search_result=search(query)

final=prerag(query,result,search_result)
print(final)
print('here is a search result')
print(search_result)
"""