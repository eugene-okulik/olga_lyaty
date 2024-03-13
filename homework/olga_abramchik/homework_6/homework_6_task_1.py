text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
text = text.split()

for i in range(len(text)):
    if text[i][-1] in ',.':
        text[i] = text[i][0:-1] + 'ing' + text[i][-1]
    else:
        text[i] += 'ing'

text_new = ' '.join(text)
print(text_new)
