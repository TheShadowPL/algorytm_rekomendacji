import numpy as np

# Przykładowa baza artykułów z ich meta tagami
articles = {'Artykuł 1': ['kuchnia włoska', 'kuchnia azjatycka', 'ciastka', 'soki świeżo wyciskane', 'tacos', 'fast foody', 'herbata', 'pieczywo'], 'Artykuł 2': ['dieta wegańska', 'zupy', 'zdrowe odżywianie', 'japońskie jedzenie', 'kuchnia rosyjska', 'dania fit', 'soki świeżo wyciskane', 'kuchnia karaibska'], 'Artykuł 3': ['ciastka', 'grillowana warzywa', 'chleb', 'koktajle'], 'Artykuł 4': ['kuchnia rosyjska', 'sztuka gotowania', 'ciasteczka', 'sushi', 'wegańskie przepisy', 'chleb', 'smażone dania', 'kawa', 'przetwory', 'pasta i pizze', 'kuchnia włoska', 'dania świąteczne', 'grillowana kaczka', 'soki świeżo wyciskane'], 'Artykuł 5': ['tapas', 'kulinaria', 'makarony', 'ryby'], 'Artykuł 6': ['koktajle', 'fast foody', 'kuchnia azjatycka', 'dania fit'], 'Artykuł 7': ['bezmięsne dania', 'sztuka gotowania', 'kokosowe przepisy', 'kuchnia grecka', 'chleb', 'słodkie przekąski', 'sery', 'kuchnia chińska', 'fast foody', 'naleśniki', 'zupy'], 'Artykuł 8': ['kuchnia rosyjska'], 'Artykuł 9': ['desery', 'zdrowe odżywianie', 'dieta wegańska', 'kuchnia chińska', 'kuchnia indyjska', 'owoce morza', 'pieczywo', 'grillowana kaczka', 'sztuka gotowania', 'kuchnia azjatycka', 'alkohol', 'chleb', 'smażone dania'], 'Artykuł 10': ['chleb', 'dania świąteczne', 'pasta i pizze', 'dieta wegańska', 'kuchnia chińska', 'fast foody', 'zdrowe odżywianie', 'słodkie przekąski', 'dania z ryżem', 'kuchnia rosyjska', 'soki świeżo wyciskane', 'naleśniki'], 'Artykuł 11': ['tajskie curry', 'grillowana warzywa', 'tacos', 'kawa', 'sushi', 'ciasteczka', 'grillowana kaczka', 'dieta wegańska'], 'Artykuł 12': ['dieta wegańska', 'wege kotlety', 'bezglutenowe przepisy', 'dania fit', 'bezalkoholowe drinki', 'chleb'], 'Artykuł 13': ['grillowana kaczka', 'dieta wegańska', 'zdrowe odżywianie', 'wege kotlety', 'wege burgery'], 'Artykuł 14': ['ciasteczka', 'pasta i pizze', 'grillowana kaczka', 'desery', 'dania świąteczne', 'kokosowe przepisy', 'kuchnia chińska', 'wegetariańskie dania', 'kuchnia azjatycka', 'koktajle', 'wege burgery', 'bezalkoholowe drinki'], 'Artykuł 15': ['naleśniki', 'jajecznica', 'bezmięsne dania', 'dania fit', 'kawa', 'tacos', 'pasta i pizze', 'wege burgery', 'wege kotlety'], 'Artykuł 16': ['sushi', 'kuchnia turecka', 'kuchnia grecka', 'tapas', 'pieczywo', 'wegetariańskie dania', 'zupy', 'japońskie jedzenie', 'bezglutenowe przepisy', 'herbata', 'ciastka', 'ciasteczka', 'sery', 'kuchnia chińska', 'desery'], 'Artykuł 17': ['owoce morza', 'wege burgery', 'kawa', 'kuchnia indyjska', 'kuchnia rosyjska', 'pikantne potrawy', 'pasta i pizze', 'pieczywo', 'wegańskie przepisy', 'grillowana kaczka', 'naleśniki', 'kuchnia azjatycka', 'zupy', 'dieta wegańska'], 'Artykuł 18': ['słodkie przekąski', 'ciastka', 'przetwory', 'wegetariańskie dania', 'bezmięsne dania', 'desery', 'sztuka gotowania'], 'Artykuł 19': ['wegetariańskie dania', 'dania fit', 'sztuka gotowania', 'wege kotlety', 'jajecznica', 'dania z ryżem', 'zdrowe odżywianie', 'herbata', 'sushi', 'zupy', 'ciastka', 'fast foody', 'kuchnia azjatycka', 'pasta i pizze'], 'Artykuł 20': ['sery', 'desery'], 'Artykuł 21': ['alkohol', 'smażone dania', 'ciastka'], 'Artykuł 22': ['naleśniki', 'słodkie przekąski', 'tajskie curry', 'zupy', 'sery', 'kuchnia azjatycka', 'alkohol', 'soki świeżo wyciskane'], 'Artykuł 23': ['bezglutenowe przepisy', 'smażone dania', 'alkohol', 'pieczywo', 'dania fit'], 'Artykuł 24': ['dania z ryżem'], 'Artykuł 25': ['dania świąteczne', 'smażone dania', 'ciasteczka', 'dieta wegańska', 'wege burgery', 'alkohol', 'tacos', 'kuchnia karaibska', 'kuchnia grecka', 'kuchnia azjatycka', 'ciasta'], 'Artykuł 26': ['smażone dania', 'bezmięsne dania'], 'Artykuł 27': ['ciasta', 'ciastka', 'japońskie jedzenie', 'dania świąteczne', 'bezmięsne dania', 'smażone dania', 'tajskie curry', 'kuchnia indyjska'], 'Artykuł 28': ['soki świeżo wyciskane', 'kuchnia chińska', 'chleb', 'pasta i pizze', 'kawa', 'zdrowe odżywianie', 'herbata', 'kuchnia francuska', 'alkohol', 'kuchnia rosyjska', 'słodkie przekąski', 'ryby', 'zupy'], 'Artykuł 29': ['tajskie curry', 'dania fit', 'kuchnia indyjska', 'kuchnia włoska', 'dieta wegańska', 'fast foody'], 'Artykuł 30': ['pieczywo', 'wege burgery', 'soki świeżo wyciskane'], 'Artykuł 31': ['bezglutenowe przepisy', 'smażone dania', 'kuchnia turecka', 'kuchnia indyjska', 'sztuka gotowania', 'sałatki', 'sushi', 'kuchnia rosyjska', 'wege burgery', 'tacos', 'makarony'], 'Artykuł 32': ['soki świeżo wyciskane', 'grillowana kaczka', 'japońskie jedzenie', 'grillowana warzywa', 'kuchnia karaibska', 'tapas', 'kuchnia indyjska', 'sztuka gotowania', 'dania fit', 'bezglutenowe przepisy', 'alkohol', 'kuchnia chińska'], 'Artykuł 33': ['zdrowe odżywianie', 'makarony', 'herbata'], 'Artykuł 34': ['dieta wegańska', 'tapas', 'pieczywo', 'kuchnia francuska', 'grillowana warzywa', 'naleśniki'], 'Artykuł 35': ['zdrowe odżywianie', 'sushi', 'grillowana kaczka', 'fast foody', 'przetwory', 'tajskie curry', 'herbata', 'ciasteczka', 'jajecznica', 'dania fit', 'owoce morza', 'kuchnia grecka', 'pikantne potrawy', 'sery'], 'Artykuł 36': ['sushi', 'kulinaria', 'kuchnia włoska', 'ciastka', 'chleb'], 'Artykuł 37': ['fast foody', 'wegetariańskie dania', 'dania z ryżem', 'kuchnia indyjska', 'tajskie curry'], 'Artykuł 38': ['grillowana kaczka', 'wege kotlety', 'bezglutenowe przepisy', 'bezalkoholowe drinki', 'wege burgery', 'kuchnia rosyjska', 'kulinaria', 'pieczywo', 'kuchnia grecka', 'grillowana warzywa', 'kuchnia francuska', 'tacos', 'naleśniki', 'sery'], 'Artykuł 39': ['kuchnia azjatycka', 'bezalkoholowe drinki', 'naleśniki', 'ryby', 'bezmięsne dania'], 'Artykuł 40': ['grillowana kaczka', 'bezmięsne dania', 'chleb', 'ciasteczka', 'ciasta', 'kuchnia indyjska', 'kuchnia włoska', 'zupy', 'herbata', 'koktajle', 'bezglutenowe przepisy', 'zdrowe odżywianie'], 'Artykuł 41': ['wege kotlety', 'japońskie jedzenie', 'kokosowe przepisy', 'bezmięsne dania', 'dania z ryżem', 'kuchnia azjatycka', 'kuchnia chińska', 'kuchnia włoska', 'makarony', 'wegańskie przepisy', 'fast foody', 'kuchnia turecka', 'zupy', 'kuchnia rosyjska'], 'Artykuł 42': ['soki świeżo wyciskane', 'kuchnia chińska', 'kuchnia włoska', 'kulinaria', 'kuchnia francuska', 'zdrowe odżywianie', 'ciastka', 'tapas', 'dania świąteczne', 'meksykańskie dania', 'wegetariańskie dania', 'jajecznica', 'ciasteczka', 'kokosowe przepisy', 'sztuka gotowania'], 'Artykuł 43': ['sery', 'kuchnia włoska', 'meksykańskie dania', 'wege burgery', 'kuchnia turecka', 'przetwory', 'kuchnia chińska', 'bezmięsne dania', 'tajskie curry', 'wegańskie przepisy', 'sałatki', 'dania fit', 'dieta wegańska', 'tacos', 'ciasteczka'], 'Artykuł 44': ['naleśniki', 'grillowana warzywa'], 'Artykuł 45': ['dania świąteczne', 'herbata', 'zupy', 'kokosowe przepisy', 'pikantne potrawy', 'pieczywo', 'bezglutenowe przepisy', 'ciastka', 'sery', 'ciasta', 'sztuka gotowania', 'wege kotlety', 'dieta wegańska', 'kuchnia chińska'], 'Artykuł 46': ['kuchnia włoska', 'alkohol', 'pasta i pizze', 'słodkie przekąski', 'tacos', 'bezalkoholowe drinki', 'chleb', 'kuchnia rosyjska', 'ciasteczka', 'wege kotlety', 'wegetariańskie dania', 'ryby', 'tapas'], 'Artykuł 47': ['jajecznica', 'soki świeżo wyciskane', 'kulinaria', 'dania świąteczne', 'grillowana warzywa', 'herbata', 'grillowana kaczka', 'tajskie curry'], 'Artykuł 48': ['wege kotlety', 'kulinaria', 'jajecznica', 'soki świeżo wyciskane', 'bezmięsne dania', 'sushi', 'owoce morza', 'zdrowe odżywianie', 'pasta i pizze', 'meksykańskie dania', 'kawa', 'smażone dania'], 'Artykuł 49': ['sushi', 'kawa', 'sałatki'], 'Artykuł 50': ['przetwory', 'kuchnia azjatycka', 'naleśniki', 'kulinaria', 'dania fit'], 'Artykuł 51': ['alkohol', 'kuchnia rosyjska'], 'Artykuł 52': ['meksykańskie dania', 'desery', 'tacos', 'zdrowe odżywianie'], 'Artykuł 53': ['naleśniki', 'przetwory', 'bezglutenowe przepisy', 'smażone dania', 'kuchnia turecka', 'dieta wegańska', 'herbata', 'jajecznica', 'wege burgery', 'zupy', 'chleb', 'sushi', 'sery', 'kuchnia chińska', 'kulinaria'], 'Artykuł 54': ['tajskie curry', 'bezalkoholowe drinki', 'zdrowe odżywianie', 'soki świeżo wyciskane', 'wege burgery', 'kuchnia rosyjska', 'bezmięsne dania', 'przetwory', 'owoce morza', 'tapas', 'grillowana warzywa', 'kulinaria', 'herbata', 'kuchnia chińska', 'dania świąteczne'], 'Artykuł 55': ['smażone dania', 'kulinaria', 'chleb', 'ciasteczka', 'dania fit'], 'Artykuł 56': ['pikantne potrawy', 'dania fit', 'koktajle'], 'Artykuł 57': ['jajecznica', 'naleśniki', 'ciasta', 'ciastka', 'kuchnia turecka', 'pikantne potrawy', 'kuchnia indyjska', 'kawa', 'kuchnia grecka', 'wegetariańskie dania', 'koktajle', 'sery', 'bezalkoholowe drinki', 'smażone dania'], 'Artykuł 58': ['ryby', 'wegetariańskie dania', 'dania fit', 'wege burgery', 'sery', 'pikantne potrawy'], 'Artykuł 59': ['dania świąteczne', 'dania z ryżem', 'tajskie curry', 'kuchnia grecka', 'chleb', 'kuchnia francuska', 'japońskie jedzenie', 'słodkie przekąski', 'kuchnia karaibska', 'dieta wegańska', 'jajecznica', 'bezglutenowe przepisy', 'owoce morza'], 'Artykuł 60': ['japońskie jedzenie', 'wegetariańskie dania', 'zdrowe odżywianie', 'pikantne potrawy', 'sery', 'bezalkoholowe drinki', 'grillowana warzywa', 'kuchnia turecka', 'smażone dania', 'chleb', 'kuchnia indyjska', 'wegańskie przepisy', 'kuchnia włoska'], 'Artykuł 61': ['kuchnia rosyjska', 'bezglutenowe przepisy', 'wegetariańskie dania', 'sztuka gotowania', 'meksykańskie dania', 'makarony', 'dania fit', 'kokosowe przepisy', 'kuchnia chińska', 'grillowana warzywa', 'ryby', 'dania z ryżem', 'przetwory', 'tapas'], 'Artykuł 62': ['tajskie curry', 'smażone dania', 'naleśniki', 'bezmięsne dania', 'koktajle', 'kuchnia indyjska', 'ryby', 'kuchnia włoska', 'kuchnia francuska', 'soki świeżo wyciskane', 'grillowana kaczka', 'owoce morza', 'kawa', 'bezalkoholowe drinki'], 'Artykuł 63': ['wege burgery', 'kuchnia grecka'], 'Artykuł 64': ['herbata', 'pasta i pizze', 'kuchnia azjatycka', 'wegetariańskie dania', 'kuchnia indyjska', 'sery', 'koktajle', 'tapas', 'bezalkoholowe drinki', 'grillowana warzywa', 'dania z ryżem', 'dania fit', 'ciasta'], 'Artykuł 65': ['jajecznica'], 'Artykuł 66': ['naleśniki', 'dieta wegańska', 'kokosowe przepisy', 'tacos', 'wegańskie przepisy', 'ryby', 'alkohol', 'zupy', 'koktajle'], 'Artykuł 67': ['makarony', 'chleb', 'herbata', 'sztuka gotowania', 'grillowana warzywa', 'ciastka', 'tajskie curry', 'sushi', 'ryby', 'meksykańskie dania', 'jajecznica', 'wege kotlety', 'grillowana kaczka', 'tacos'], 'Artykuł 68': ['zupy', 'tacos', 'zdrowe odżywianie', 'tajskie curry', 'alkohol', 'kulinaria', 'kuchnia turecka', 'kuchnia włoska', 'dania z ryżem', 'soki świeżo wyciskane'], 'Artykuł 69': ['sery'], 'Artykuł 70': ['kuchnia karaibska', 'dania z ryżem', 'desery', 'zupy', 'naleśniki', 'bezmięsne dania', 'pikantne potrawy', 'owoce morza', 'zdrowe odżywianie', 'koktajle'], 'Artykuł 71': ['koktajle', 'tacos', 'bezmięsne dania', 'pasta i pizze', 'przetwory', 'kuchnia grecka', 'sztuka gotowania', 'tajskie curry', 'ciastka', 'ryby', 'dieta wegańska'], 'Artykuł 72': ['dieta wegańska', 'sztuka gotowania', 'ryby', 'pasta i pizze', 'grillowana warzywa', 'kuchnia turecka', 'pikantne potrawy', 'tapas', 'naleśniki'], 'Artykuł 73': ['ciasta', 'kuchnia turecka', 'kuchnia grecka', 'wegańskie przepisy', 'soki świeżo wyciskane'], 'Artykuł 74': ['chleb', 'kuchnia rosyjska', 'kawa', 'makarony', 'dania z ryżem', 'jajecznica', 'dania świąteczne'], 'Artykuł 75': ['dieta wegańska', 'dania z ryżem', 'dania fit', 'alkohol', 'kulinaria', 'ciasteczka', 'sery', 'soki świeżo wyciskane', 'kuchnia francuska'], 'Artykuł 76': ['sery', 'kuchnia turecka', 'sztuka gotowania', 'kuchnia indyjska', 'jajecznica', 'fast foody', 'owoce morza', 'sushi', 'wegetariańskie dania', 'makarony', 'bezalkoholowe drinki', 'słodkie przekąski'], 'Artykuł 77': ['pieczywo', 'słodkie przekąski', 'dania z ryżem'], 'Artykuł 78': ['ciastka', 'sery', 'pasta i pizze', 'kuchnia grecka', 'sałatki'], 'Artykuł 79': ['dania fit', 'kokosowe przepisy', 'meksykańskie dania', 'przetwory', 'grillowana kaczka', 'wege burgery', 'kuchnia indyjska', 'dieta wegańska', 'alkohol'], 'Artykuł 80': ['wegetariańskie dania', 'koktajle'], 'Artykuł 81': ['koktajle', 'ciasta', 'alkohol'], 'Artykuł 82': ['kuchnia karaibska', 'bezmięsne dania', 'soki świeżo wyciskane', 'naleśniki', 'alkohol', 'kuchnia francuska', 'wegańskie przepisy'], 'Artykuł 83': ['przetwory', 'japońskie jedzenie', 'sushi', 'ciastka', 'ciasteczka', 'kuchnia turecka', 'bezmięsne dania', 'dania fit', 'grillowana kaczka'], 'Artykuł 84': ['herbata', 'tacos', 'kuchnia turecka', 'naleśniki', 'bezalkoholowe drinki', 'makarony', 'owoce morza'], 'Artykuł 85': ['kuchnia grecka', 'bezmięsne dania', 'alkohol', 'sery', 'sztuka gotowania', 'wegańskie przepisy', 'tapas', 'ciastka', 'grillowana kaczka', 'tajskie curry', 'herbata', 'ryby', 'japońskie jedzenie', 'zupy', 'makarony'], 'Artykuł 86': ['zdrowe odżywianie', 'japońskie jedzenie', 'tajskie curry', 'kuchnia indyjska', 'wege burgery', 'ciasta', 'owoce morza', 'smażone dania', 'tacos', 'pikantne potrawy', 'sushi', 'alkohol', 'kuchnia rosyjska'], 'Artykuł 87': ['bezglutenowe przepisy', 'smażone dania', 'kokosowe przepisy', 'kuchnia rosyjska', 'fast foody', 'wege kotlety', 'chleb', 'japońskie jedzenie'], 'Artykuł 88': ['herbata', 'sztuka gotowania'], 'Artykuł 89': ['tacos', 'koktajle', 'kulinaria', 'kuchnia francuska', 'kuchnia chińska', 'alkohol', 'desery', 'jajecznica', 'meksykańskie dania'], 'Artykuł 90': ['słodkie przekąski', 'dieta wegańska', 'kuchnia chińska', 'dania fit', 'kuchnia francuska', 'koktajle', 'kuchnia grecka'], 'Artykuł 91': ['grillowana warzywa', 'kawa', 'przetwory', 'dieta wegańska', 'zupy', 'smażone dania', 'kuchnia chińska'], 'Artykuł 92': ['dania świąteczne', 'japońskie jedzenie', 'kuchnia karaibska', 'wegetariańskie dania', 'sery', 'herbata', 'kuchnia indyjska', 'tapas', 'ciasta', 'alkohol', 'dania z ryżem', 'zdrowe odżywianie'], 'Artykuł 93': ['bezalkoholowe drinki', 'owoce morza', 'tapas'], 'Artykuł 94': ['herbata'], 'Artykuł 95': ['bezalkoholowe drinki', 'chleb', 'kuchnia grecka', 'sztuka gotowania', 'ryby', 'pikantne potrawy', 'ciasta', 'kulinaria', 'meksykańskie dania', 'grillowana warzywa', 'kawa'], 'Artykuł 96': ['przetwory', 'ryby', 'wegańskie przepisy'], 'Artykuł 97': ['słodkie przekąski'], 'Artykuł 98': ['bezmięsne dania', 'ciastka', 'jajecznica'], 'Artykuł 99': ['kuchnia karaibska', 'zdrowe odżywianie', 'ciastka', 'ryby', 'bezglutenowe przepisy', 'ciasteczka', 'tapas', 'japońskie jedzenie', 'sery', 'wege kotlety', 'przetwory'], 'Artykuł 100': ['sztuka gotowania', 'przetwory', 'kuchnia turecka', 'wegańskie przepisy', 'kuchnia azjatycka', 'kulinaria', 'tapas', 'sushi', 'pieczywo', 'ciastka', 'wegetariańskie dania', 'smażone dania']}

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
article_title = "Artykuł 1"
recommended_articles = recommend_similar_articles(article_title)
print(f"Rekomendowane artykuły podobne do '{article_title}':")
for title, similarity in recommended_articles:
    print(f"- {title} (podobieństwo: {similarity:.2f})")