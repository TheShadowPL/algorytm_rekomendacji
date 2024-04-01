import numpy as np, time


# Przykładowa baza artykułów z ich meta tagami
articles = {}


# Funkcja do przetwarzania meta tagów na wektor cech
def vectorize_tags(tags, all_tags):
    vector = np.zeros(len(all_tags))
    for tag in tags:
        vector[all_tags.index(tag)] = 1
    return vector

# Zbierz wszystkie unikalne tagi
all_tags = list(set(tag for tags in articles.values() for tag in tags))

# Przetwórz meta tagi na wektory cech
article_vectors = {title: vectorize_tags(tags, all_tags) for title, tags in articles.items()}

# Funkcja do obliczania podobieństwa między artykułami
def calculate_similarity(article1, article2):
    return np.dot(article1, article2) / (np.linalg.norm(article1) * np.linalg.norm(article2))

# Funkcja rekomendująca artykuły na podstawie podobieństwa z podanym artykułem
def recommend_similar_articles(article_title, n=3):
    similarities = {title: calculate_similarity(article_vectors[article_title], vector) for title, vector in article_vectors.items() if title != article_title}
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    return sorted_similarities[:n]

# Testowanie
start_time = time.time()
article_title = "Artykuł 24"
recommended_articles = recommend_similar_articles(article_title)
print(f"Rekomendowane artykuły podobne do '{article_title}':")
for title, similarity in recommended_articles:
    print(f"- {title} (podobieństwo: {similarity:.2f})")

end_time = time.time()
execution_time = end_time - start_time
print(f"Czas wykonania operacji: {execution_time} sekund")