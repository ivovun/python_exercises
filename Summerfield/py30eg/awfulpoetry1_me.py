import random

articles = ("the", "a")
subjects = ('cat', 'dog', 'man', 'woman')
verbs = ('sang', 'ran', 'jumped')
adverbs = ('loudly', 'quietly', 'well', 'badly')
structures = ((articles, subjects, verbs, adverbs), (articles, subjects, verbs))

for i in range(5):
    variant = random.randint(0, 1)
    new_line = ''
    for list_of_words in structures[variant]:
        new_line += ' ' + random.choice(list_of_words)
    print(new_line)

