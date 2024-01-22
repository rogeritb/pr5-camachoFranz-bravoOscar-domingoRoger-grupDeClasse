def get_input(prompt):
    return input(prompt).strip()

def translate_to_castellano(insult):
    # Translate insult to Castellano using the Softcatala Translator API
    # Documentation: https://www.softcatala.org/traductor/API/traduccio
    pass

def translate_to_english(insult):
    # Translate insult to English using the DeepL Translator API
    # Documentation: https://www.deepl.com/docs-api/translating-text/
    pass

def translate_to_klingon(insult):
    # Translate insult to Klingon using the Tradukka Translator API
    # Documentation: https://tradukka.com/docs/index.html#translation
    pass

def translate_insult(insult):
    castellano = translate_to_castellano(insult)
    ingles = translate_to_english(insult)
    klingon = translate_to_klingon(insult)
    return castellano, ingles, klingon

def main():
    print("Programa de traducció d'insults en català a castellà, anglès i klingon.")
    print("Per favor, escriu per teclat un insult en català:")
    insult = get_input("")
    castellano, ingles, klingon = translate_insult(insult)
    print("\nInsult en català:", insult)
    print("Insult en castellà:", castellano)
    print("Insult en inglés:", ingles)
    print("Insult en klingon:", klingon)

if __name__ == "__main__":
    main()