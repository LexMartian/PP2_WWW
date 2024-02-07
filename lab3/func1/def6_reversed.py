def backwards(string):
    words = string.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = input("Enter a sentence: ")
print(backwards(sentence))
