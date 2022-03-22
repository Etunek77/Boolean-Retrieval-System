def documents(different_words, connecting_words):             # different words - query terms, connecting words - boolean oper
  print(connecting_words)                                    
  total_files = len(files_with_index)                         
  zeroes_and_ones = []                                        # Result vector
  zeroes_and_ones_of_all_words = []                           # Result vector for all words stored as a list
  for word in (different_words):                              # process each word in query terms                             
      if word.lower() in unique_words_all:                    # if word exists in corpus
          zeroes_and_ones = [0] * total_files                 # Initialise bitmap with all 0s
          linkedlist = linked_list_data[word].head            # Head of inverted index of that word
          # print(word) 
          while linkedlist.nextval is not None:                 # Put 1 in the bitmap
              zeroes_and_ones[linkedlist.nextval.doc - 1] = 1   # if the word exists in the corresponding
              linkedlist = linkedlist.nextval                   # document and advance pointer
          zeroes_and_ones_of_all_words.append(zeroes_and_ones)  # Append bitmap for that word to list of all bitmaps
      else:
          zeroes_and_ones_of_all_words.append([0] * total_files)

  # print(zeroes_and_ones_of_all_words)
  for word in connecting_words:                                  # Processing boolean operators
      word_list1 = zeroes_and_ones_of_all_words[0]              
      word_list2 = zeroes_and_ones_of_all_words[1]               
      if word == "and":                                          
          bitwise_op = [w1 & w2 for (w1,w2) in zip(word_list1,word_list2)]
          zeroes_and_ones_of_all_words.remove(word_list1)
          zeroes_and_ones_of_all_words.remove(word_list2)
          zeroes_and_ones_of_all_words.insert(0, bitwise_op);
      elif word == "or":
          bitwise_op = [w1 | w2 for (w1,w2) in zip(word_list1,word_list2)]
          zeroes_and_ones_of_all_words.remove(word_list1)
          zeroes_and_ones_of_all_words.remove(word_list2)
          zeroes_and_ones_of_all_words.insert(0, bitwise_op);
      elif word == "not":
          bitwise_op = [not w1 for w1 in word_list2]
          bitwise_op = [int(b == True) for b in bitwise_op]
          zeroes_and_ones_of_all_words.remove(word_list2)
          zeroes_and_ones_of_all_words.remove(word_list1)
          bitwise_op = [w1 & w2 for (w1,w2) in zip(word_list1,bitwise_op)]

  zeroes_and_ones_of_all_words.insert(0, bitwise_op);              # Final bitmap
          
  files = []                                                                             
  # print(zeroes_and_ones_of_all_words)
  lisa = zeroes_and_ones_of_all_words[0]
  cnt = 1
  for index in lisa:
      if index == 1:
          files.append(files_with_index[cnt])
      cnt = cnt+1
      
  return files
