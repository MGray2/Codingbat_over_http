def word_splosion(word):
    new_word = list(word)
    answer = ""
    answer2 = ""
    i = 1
    while i < len(word) + 1:
        fragment = slice(0, i)
        parts = answer.join(new_word[fragment])
        answer2 += parts
        i += 1
    print(answer2)


word_splosion("white")
