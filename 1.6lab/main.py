#вар9
def count_words(sentence):
    words=sentence.lower().split()
    word_count={}
    for word in words:
        word=word.strip('.,!?:;"()[]')
        if word:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
    return word_count
sentence= "Сегодня шестоя ноября. Сегодня холодно."
result = count_words(sentence)
print(f"Предложение: '{sentence}'")
print("Результат:",result)
