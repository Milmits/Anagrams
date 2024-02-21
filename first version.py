print("\t\tПрограмма Кучук")
print("Анаграммы\n")


import random
WORDS = ("VLAD", "IGOR", "NIKITA", "MILAN")
word = random.choice(WORDS)
correct = word
peremeshka = ""

while word:
    position = random.randrange(len(word))
    peremeshka += word[position]
    word = word[:position] + word[(position + 1):]
print("Суть игры в том, чтобы из данных нам букв сздать слово")
print(peremeshka)
guess = input("Соберите слово\n")
help1 = 0
second_help2 = 0
triple_help3 = 0
score = 1000
while guess != correct and guess != "":
    score -= 25
    help1 += 1
    second_help2 += 1
    triple_help3 += 1
    print("Incorrect")
    if help1 == 2:
        helps = input("Нужна ли вам помощь (y,n) ?")
        if helps == "y":
            print("Первая буква нашего слова - ", correct[0:1])
            score -= 250
        else:
            print("Удачки:)")
    if second_help2 == 3:
        second_help = input("Нужна ли вам помощь (y,n) ?")
        if helps == "n" and second_help == "y":
            print("Первая буква нашего слова - ", correct[0:1])
            score -= 250
        elif second_help == "y":
            print("Вторая буква нашего слова - ", correct[1:2])
            score -= 250
        else:
            print("Удачки:))")
    if triple_help3 == 4:
        triple_help = input("Нужна ли вам помощь (y,n) ?")
        if helps == "n" and second_help == "n":
            print("Первая буква нашего слова - ", correct[0:1])
            score -= 250
        elif second_help == "n" and second_help == "y" and triple_help == "y":
            print("Вторая буква нашего слова - ", correct[1:2])
            score -= 250
        elif triple_help == "y":
            print("Третья буква нашего слова - ", correct[2:3])
            score -= 250
        else:
            print("Удачки:)))")
    guess = input("Try one more time\n")
    if score <= 0:
        print("Вы дебил")
        quit()
    if guess == correct:
        print("Поздравляем, вы угадали")


print("Молодец")
print("Вы заработали ", score, " очков!")
print("Выход\n")
