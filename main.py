meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РАНДОМ": "Случайность",
            "РОФЛ": "шутка",
            "ЧЕКНУТЬ": "проверить, посмотреть что-то"
            }
word = input("Введите непонятное слово: ").upper()            

if word in meme_dict.keys():         
    print('Это слово означает:', meme_dict[word])
else:
    print("Такого слова нет в нашем словаре, спросите у ребенка, что это за слово")