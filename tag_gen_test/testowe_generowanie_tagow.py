from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def load_stop_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stop_words = file.readlines()
    return [word.strip() for word in stop_words]

def load_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        article = file.read()
    return article

def generate_tags(article, stop_words):
    # Tokenizacja tekstu na słowa
    words = word_tokenize(article.lower())
    
    # Wykluczenie słów z listy stop words
    words = [word for word in words if word not in stop_words]
    
    # Obliczanie częstości występowania słów
    fdist = FreqDist(words)
    
    # Wybór słów kluczowych
    keywords = fdist.most_common(10)  # Wybierz 10 najczęściej występujących słów
    
    # Utwórz listę tagów
    tags = [keyword[0] for keyword in keywords]
    
    return tags

# Ścieżki do plików
stop_words_path = 'stop_words.txt'
article_path = 'article.txt'

# Wczytaj listę stop words i artykuł
stop_words = load_stop_words(stop_words_path)
article = load_article(article_path)

# Generowanie tagów dla artykułu
tags = generate_tags(article, stop_words)
print("Wygenerowane tagi:")
print(tags)
