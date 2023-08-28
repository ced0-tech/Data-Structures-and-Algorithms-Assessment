def clean_word(word):
    cleaned_word = ""
    for char in word:
        if char.isalnum():
            cleaned_word += char.lower()
    return cleaned_word

def word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        cleaned_word = clean_word(word)
        if cleaned_word:
            if cleaned_word in frequency:
                frequency[cleaned_word] += 1
            else:
                frequency[cleaned_word] = 1
    
    return frequency

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
