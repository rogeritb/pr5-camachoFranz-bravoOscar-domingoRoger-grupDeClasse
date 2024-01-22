def tradueix_catala(insult):
    # Funció que tradueix l'insult en català a castellà
    traductors = {
        "Mocós": "Mocoso",
        "Capsigrany": "Cabezón",
        # Afegir aquí la resta d'insults en català
    }
    return traductors.get(insult, "No trobat")

def tradueix_angles(insult):
    # Funció que tradueix l'insult en català a anglès
    # Implementar aquí la traducció utilitzant l'API de traducció DeepL
    pass

def tradueix_klingon(insult):
    # Funció que tradueix l'insult en català a klingon
    # Implementar aquí la traducció utilitzant l'API de traducció Tradukka
    pass

insults = {
    "CAT": ["Mocós", "Capsigrany"],
    # Afegir aquí la resta d'insults en català
}

traduccions = {
    "ESP": [],
    "ENG": [],
    "KLI": [],
}

# Obtenir l'insult en català de l'usuari
insult_catala = input("Escriu un insult en català: ")

# Traducir l'insult a castellà, anglès i klingon
for lang, trad in zip(["ESP", "ENG", "KLI"], [tradueix_catala, tradueix_angles, tradueix_klingon]):
    traduccion = trad(insult_catala)
    traduccions[lang].append(traduccion)

# Mostrar les traduccions a l'usuari
for lang, traduccions_lang in traduccions.items():
    print(f"Traduccions a {lang}: {traduccions_lang}")