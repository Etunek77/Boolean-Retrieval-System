def make_permuterm():
  ind = 1
  inverted_index = {}
  files_ind = {}
  for file in glob.iglob(f'{file_folder}/*'):
      fname = file
      file = open(file, "r")
      text = file.read()
      files_ind[ind] = os.path.basename(fname)
      text = remove_special_characters(text)
      text = re.sub(re.compile('\d'),'',text)
      # sentences = sent_tokenize(text)                                  # Refer above
      words = word_tokenize(text)
      words = [word for word in words if len(words)>1]
      words = [word.lower() for word in words]
      words = [word for word in words if word not in Stopwords]
      words = [ps.stem(word) for word in words]
      words = [word.lower() for word in words]

      for word in words:                                    
        perms = list()                              # List for all permutations of that word
        n = len(word)                               #
        temp = list(word)                           # Conver word to list
        temp.append("$")                            # and append $

        i = 1                                       
        while i<=n+1:                               
          ans = "".join(temp)                       # Convert list to word
          perms.append(ans)                         # Append to perms list
          r = temp.pop()                            # Do for all permutations
          temp.insert(0,r)                          
          i+=1

        for word in perms:
          if word not in inverted_index.keys():     # Build inverted index 
            inverted_index[word] = {ind}            # for all permuatations
          else:
            inverted_index[word].add(ind) 

      ind+=1
    
    
    
def permuterm(query):                # Parameter is single query term

  query = list(query)                # Convert term to list
  temp = query.copy()                      

  query.append("$")                  # Append $ to query


  if temp[-1]=="*" and temp[0] == "*":  # If * is present at first and last pos, remove * from first pos
    query.pop(0)                        
    temp.pop(0)

  elif temp[0]=="*":                    # If * is present at first pos, append at end
    t = query.pop(0)
    query.append(t)

  elif temp[-1]=="*":
    pass

  else:
    while query[-1] != "*":             # Move to last if it is somewhere in the middle
      t = query.pop(0)
      query.append(t)

  ans = list()                          # Store all words which satisfy the query (in rotated form)
  query.pop()                           # Pop *
  query = "".join(query)                # Convert to string
  print(query)                    
  n = len(query)                  
  check_list = list(inverted_index.keys())   # All words in the inverted index
  final_list = list()                        # Store all words which satisfy the query

  for word in check_list:                    # Convert words to original form
    if query == word[0:n]:
      ans.append(word)

  for word in ans:
    temp = list(word)
    if word[0]=="$":
      temp.pop(0)
    elif word[-1]=="$":
      temp.pop()

    else:
      temp = list(word)
      while temp[-1]!="$":
        t = temp.pop(0)
        temp.append(t)

      temp.pop()
      word = "".join(temp)
    word = "".join(temp)
    final_list.append(word)

  return final_list  
