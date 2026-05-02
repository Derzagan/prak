import chromadb
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")



client = chromadb.Client()
collection = client.create_collection("my_collection")



chunks = [
    "LLM это большая языковая модель",
    "RAG это поиск + генерация",
    "Python это язык программирования"
]


for i, chunk in enumerate(chunks):
    vector = model.encode(chunk).tolist()


    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[vector]
    )





questions = "что значить программировать на python?"

question_vector = model.encode(questions).tolist()

res = collection.query(
    query_embeddings=[question_vector],
    n_results = 1
)

context = res['documents'][0][0]
print(context)


