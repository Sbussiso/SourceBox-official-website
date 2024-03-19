from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import openai
import os
openai.api_key = "OPENAI_API_KEY"

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("where can I donate?")
print(response)