#  Задание 1

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

text = text.split()

new_text = []
for word in text:
    if word.endswith('.'):
        index_point = (word.index('.'))
        new_word_p = word[:index_point] + 'ing' + '.'
        new_text.append(new_word_p)
    elif word.endswith(','):
        index_comma = (word.index(','))
        new_word_c = word[:index_comma] + 'ing' + ","
        new_text.append(new_word_c)
    else:
        new_word = word + 'ing'
        new_text.append(new_word)

print(' '.join(new_text))
