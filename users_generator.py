import random

import random
import json

def generate_users(num_users, num_articles):
    users = []
    for i in range(1, num_users + 1):
        name = f"Użytkownik {i}"
        articles_read = [f"Artykuł {random.randint(1, num_articles)}" for _ in range(random.randint(1, 10))]
        user = {
            "id": i,
            "name": name,
            "articles_read": articles_read
        }
        users.append(user)
    return users

# Generowanie użytkowników
users = generate_users(10, 300)  # generujemy 10 czytelników o bazie 300 artykulow

# Zapis do pliku JSON
with open('users_base.json', 'w', encoding='utf-8') as f:
    json.dump({"users": users}, f, ensure_ascii=False, indent=2)

print("Pomyślnie zapisano użytkowników")