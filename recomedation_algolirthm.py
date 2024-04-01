import numpy as np
import json
import time

def load_data(articles_file, users_file):
    with open(articles_file, 'r', encoding='utf-8') as f:
        articles_data = json.load(f)
    with open(users_file, 'r', encoding='utf-8') as f:
        users_data = json.load(f)
    return articles_data, users_data

# Przetwarzanie artykułów na słownik
def process_articles(articles_data):
    articles = {}
    for title, tags in articles_data.items():
        articles[title] = tags
    return articles

# Przetwarzanie użytkowników na słownik
def process_users(users_data):
    users = {}
    for user in users_data['users']:
        users[user['name']] = user['articles_read']
    return users

# Funkcja do przetwarzania meta tagów na wektor cech
def vectorize_tags(tags, all_tags):
    vector = np.zeros(len(all_tags))
    for tag in tags:
        vector[all_tags.index(tag)] = 1
    return vector

# Funkcja rekomendująca artykuły na podstawie podobieństwa z podanym artykułem
def recommend_similar_articles(user, articles, all_tags, n=10):
    user_read_articles = users[user]
    user_read_tags = [tag for article in user_read_articles for tag in articles[article]]
    user_vector = vectorize_tags(user_read_tags, all_tags)
    similarities = {title: calculate_similarity(user_vector, vector) for title, vector in article_vectors.items() if title not in user_read_articles}
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    return sorted_similarities[:n]

# Funkcja do obliczania podobieństwa między artykułami
def calculate_similarity(article1, article2):
    return np.dot(article1, article2) / (np.linalg.norm(article1) * np.linalg.norm(article2))

articles_data, users_data = load_data('articles_base.json', 'users_base.json')

# Przetwarzanie artykułów i użytkowników
articles = process_articles(articles_data)
users = process_users(users_data)

# Zbierz wszystkie unikalne tagi
all_tags = list(set(tag for tags in articles.values() for tag in tags))

# Przetwórz meta tagi na wektory cech
article_vectors = {title: vectorize_tags(tags, all_tags) for title, tags in articles.items()}


start_time = time.time()

for user in users:
    recommended_articles = recommend_similar_articles(user, articles, all_tags)
    print(f"Rekomendowane artykuły dla użytkownika '{user}':")
    for title, similarity in recommended_articles:
        print(f"- {title} (podobieństwo: {similarity:.2f})")
    print()

end_time = time.time()
execution_time = end_time - start_time
print(f"Czas wykonania operacji: {execution_time} sekund")
