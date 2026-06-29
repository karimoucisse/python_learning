from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = [
	"What's your name?",
	"How is the weather today",
	"Can you play fooyball?"
]

embeddings = model.encode(sentences)
print(embeddings.shape)
print(embeddings[0][:5])

similarities = model.similarity(embeddings, embeddings)
print(similarities)
