from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer(("sentence-transformers/all-MiniLM-L6-v2"))

documents = [
    "Un embedding est un vecteur de nombres qui capture le sens d'un texte. Deux textes au sens proche ont des vecteurs proches.",
    "La similarité cosinus mesure l'angle entre deux vecteurs. Un score proche de 1 signifie que les textes sont très similaires.",
    "Le RAG (Retrieval Augmented Generation) combine une recherche de documents pertinents avec un LLM qui génère la réponse finale.",
    "pgvector est une extension de PostgreSQL qui permet de stocker des vecteurs et de faire des recherches de similarité directement en SQL.",
    "sentence-transformers est une bibliothèque Python qui transforme des phrases en vecteurs, en local et gratuitement.",
    "Le chunking consiste à découper un document en petits morceaux avant de les transformer en vecteurs pour l'indexation.",
    "Un transformer est une architecture de réseau de neurones basée sur le mécanisme d'attention, qui traite tous les mots d'une séquence en parallèle.",
    "Un LLM génératif comme GPT ou Claude produit du texte token par token, tandis qu'un embedding model produit un vecteur représentant le sens d'un texte.",
    "Ollama permet de faire tourner des modèles de langage localement sur sa machine, gratuitement, sans appeler une API externe.",
    "La recherche sémantique compare le sens d'une requête aux documents, contrairement à la recherche par mots-clés qui cherche des correspondances exactes."
]

question = "C'est quoi la différence entre un LLM et un modèle qui fait des vecteurs ?"

emb_documents = model.encode(documents, convert_to_tensor=True)
emb_question = model.encode(question, convert_to_tensor=True)

hits = util.semantic_search(emb_question, emb_documents, top_k=3)[0]

print(f"Question : {question}\n")
print("Documents les plus pertinents :")
for hit in hits:
	score = hit["score"]
	texte = documents[hit["corpus_id"]]
	print(f"  [{score:.3f}] {texte}")

