import random


def print_poem(number_of_lines=5):
    articles = ("the", "a")
    subjects = ('cat', 'dog', 'man', 'woman')
    verbs = ('sang', 'ran', 'jumped')
    adverbs = ('loudly', 'quietly', 'well', 'badly')
    structures = ((articles, subjects, verbs, adverbs), (articles, subjects, verbs))

    for i in range(number_of_lines):
        variant = random.randint(0, 1)
        new_line = ''
        for list_of_words in structures[variant]:
            new_line += ' ' + random.choice(list_of_words)
        print(new_line)


while True:
    try:
        line = input('введите число от 1 до 10 или простонажмите Enter:')
        if not line:
            print_poem()
            break
        n = int(line)
        if 1 <= n <= 10:
            print_poem(n)
            break
        else:
            print(' число должно быть между 1 и 10')
    except ValueError as err:
        print(f'Ошибка: {err}')
