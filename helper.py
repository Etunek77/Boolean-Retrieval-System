def finding_all_unique_words_and_freq(words):
    # words - array of strings
    words_unique = []   # array to store unique words in 'words'
    word_freq = {}      # dictionary to store frequency of each word in 'words'

    for word in words:               
        if word not in words_unique:        # Fill words_unique array
            words_unique.append(word)
    
    for word in words_unique:
        word_freq[word] = words.count(word)  # Fill word_freq dict
    return word_freq

def finding_freq_of_word_in_doc(word,words):  # Find count of 'word' in 'words'
    return words.count(word)
        
def remove_special_characters(text):          # Remove all chars
    regex = re.compile('[^a-zA-Z0-9\s]')      # except alphanumeric and spaces
    text_returned = re.sub(regex,'',text)
    return text_returned

def contains_star(word):                      # Check if the word contains a *
  for v in word:
    if v=="*":
      return True

  return False

  
def edit_distance(word1, word2):              # edit distance b/w word1 and word2
  l1 = len(word1)
  l2 = len(word2)
  if l1 == 0:
    return l2
  if l2 == 0:
    return l1

  dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]

  for x in range(l2 + 1):
    dp[0][x] = x
  for x in range(l1 + 1):
    dp[x][0] = x
  
  for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
      if word1[i-1] == word2[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
  
  return dp[l1][l2]
