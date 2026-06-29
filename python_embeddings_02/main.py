from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
f = open("text.txt")

# documents = f.read()
# documents = documents.split("\n")

# with open("text.txt", encoding="utf-8") as f:
# 	documents = f.read().split("\n")

with open("text.txt", encoding="utf-8") as f:
    documents = [ligne.strip() for ligne in f if ligne.strip()]
question = "C'est quoi la différence entre un LLM et un modèle qui fait des vecteurs ?"
emb_doc = model.encode(documents, convert_to_tensor=True)
emb_quest = model.encode(question, convert_to_tensor=True)

hits = util.semantic_search(emb_quest, emb_doc, top_k=3)[0]

print(f"Question : {question}\n")
print("Documents les plus pertinents :")
for hit in hits:
	score = hit["score"]
	texte = documents[hit["corpus_id"]]
	print(f"  [{score:.3f}] {texte}")
