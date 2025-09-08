def longest(sentence):
    words = sentence.split()
    longest = words[0]  

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
sentence="namekkk is koushik"
print(longest(sentence))    