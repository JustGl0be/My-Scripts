pyg = 'ay'

original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    print (original + " in pig latin is:")
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_new_word = new_word[1:len(new_word)]
    print (new_new_word)
else:
    print ('empty')
