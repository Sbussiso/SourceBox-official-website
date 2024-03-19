from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import openai
import os
openai.api_key = "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"

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("where can I donate?")
print(response)