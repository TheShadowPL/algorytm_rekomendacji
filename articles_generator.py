import random
import json

tags = [
    "wegańskie przepisy", "dieta wegańska", "bezmięsne dania",
    "zdrowe odżywianie", "wegetariańskie dania", "sztuka gotowania",
    "kuchnia włoska", "pasta i pizze", "desery", "słodkie przekąski",
    "kawa", "herbata", "koktajle", "owoce morza", "kuchnia azjatycka",
    "kuchnia francuska", "sushi", "sałatki", "grillowana kaczka", "tajskie curry",
    "ryby", "pieczywo", "pikantne potrawy", "smażone dania", "bezglutenowe przepisy",
    "ciasta", "soki świeżo wyciskane", "wege burgery", "meksykańskie dania",
    "japońskie jedzenie", "ciasteczka", "makarony", "dania z ryżem", "wege kotlety",
    "zupy", "fast foody", "dania świąteczne", "dania fit", "alkohol", "bezalkoholowe drinki",
    "grillowana warzywa", "przetwory", "jajecznica", "kulinaria", "naleśniki", "tacos",
    "kuchnia indyjska", "chleb", "tapas", "kuchnia grecka", "kuchnia turecka", "sery",
    "kokosowe przepisy", "ciastka", "kuchnia chińska", "kuchnia karaibska", "kuchnia rosyjska",
    "potrawy bez cukru", "dania bez laktozy", "kuchnia marokańska", "wege dania na grill",
    "potrawy z dyni", "dania z quinoa", "kuchnia koreańska", "dania z kaszy jaglanej",
    "kuchnia włoska bez glutenu", "wege dania na święta", "dania z warzyw strączkowych",
    "kuchnia libańska", "potrawy z orzechów", "dania z kaszy bulgur", "kuchnia grecka bez mięsa",
    "potrawy z suszonych owoców", "dania na bazie warzyw korzeniowych", "wege dania na grilla",
    "kuchnia libańska bez glutenu", "potrawy z soczewicy", "dania z warzyw strączkowych na obiad",
    "wege desery bez cukru", "kuchnia kubańska", "potrawy z kiełków", "dania z marchewki",
    "wege dania na śniadanie", "kuchnia meksykańska bez glutenu", "potrawy z warzyw kapustnych",
    "dania z papryki", "wege dania na szybki obiad", "kuchnia syryjska", "potrawy z warzyw korzeniowych na obiad",
    "dania z brokułów", "wege dania na romantyczną kolację"
]

articles = {}

for i in range(1, 301):
    article_tags = random.sample(tags, random.randint(1, min(15, len(tags))))
    articles[f"Artykuł {i}"] = article_tags

with open('articles_base.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False)

print("Pomyślnie zapisano artykuły")
