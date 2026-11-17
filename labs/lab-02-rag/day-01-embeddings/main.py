import os

from google import genai
from google.genai import types
import numpy as np
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

question_embedding = client.models.embed_content(
    model="gemini-embedding-001",
    contents=["Maaş nə vaxt verilir?"],
    config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY", output_dimensionality=768)
)

documents_embedding = client.models.embed_content(
    model="gemini-embedding-001",
    contents=["Əmək haqqı ayda iki dəfə bank kartına köçürülür.",
              "Yanğın siqnalı səsləndikdə pilləkənlə binanı tərk edin."],
    config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT", output_dimensionality=768),
)

question_vector = question_embedding.embeddings[0].values
answer1_vector = documents_embedding.embeddings[0].values
answer2_vector = documents_embedding.embeddings[1].values

def cousin_similarity(vector1, vector2):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

print(round(cousin_similarity(question_vector, answer1_vector), 2))
print(round(cousin_similarity(question_vector, answer2_vector), 2))
print(len(question_vector))
