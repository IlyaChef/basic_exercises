# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове: {word[-1]}')


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f'количество букв "а" в слове: {word.lower().count("а")}')


# Вывести количество гласных букв в слове

word = 'Архангельск'.lower()
vowels = ['а','и','е','ё','о', 'у', 'ы', 'э', 'ю', 'я']
total = 0
for s in word:
    if s in vowels:
        total += 1
print(f'количество гласных букв в слове: {total}')



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'количество слов в предложении: {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'.split()
for s in sentence:
    print(s[0])



# Вывести усреднённую длину слова в предложении

sentence = 'Мы приехали в гости'.split()
amount = 0
lenght = 0
for i in sentence:
    amount += 1
for j in sentence:
    lenght += len(j)
middle = lenght / amount
print(f'Усредненная длина слова: {int(middle)}')
    