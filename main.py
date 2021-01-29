def palidrony(word):
    word_revers = ""
    for i in range(len(word)-1,-1,-1):
        word_revers += word[i]

    if word_revers == word:
        return True
    else:
        return False

while True:
  word = input("give me your word\n")
  if bool(word) == True:
    print(palidrony(word))
  else:
    break
