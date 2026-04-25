import time

# Dados da música
LYRICS_DATA = {
    "title": "Weight Watcher",
    "artist": "Melanie Martinez",
    "lyrics": [
        # COLE A LETRA AQUI (uma frase por linha)
        "How normal it is to skip lunch and dessert",
        "And yet somehow my stomach",
        "sticks out of my skirt",
        "So I work out each day, "
        "but I don't think it works",
        "So I research to see ",
        "if the surgery hurts",
        "Spent so many years ",
        "being cute on the TV",
        "Before I could blink,",
        "I became nearly thirty",
        "And I got bigger boobs ",
        "so that I could transcend it",
        "Now all that I read is: ",
        "Hey, I think she's pregnant!",
    ]
}

# Função para mostrar a letra
def print_lyrics():
    print(LYRICS_DATA["title"])
    print(LYRICS_DATA["artist"])
    print()

    # Mostra a letra com pausa
    for line in LYRICS_DATA["lyrics"]:
        print(line)
        time.sleep(5)  # espera de 5 segundos

# Executar
print_lyrics()