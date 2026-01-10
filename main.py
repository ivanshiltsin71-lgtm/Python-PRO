

slang = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ТОП": "Что-то лучшее во всём классе"

}

while True:
    word = input('Введите слово')
    if word in slang.keys():
        print(slang[word])
    else:
        print('Такое слово не прописано в slang!')
