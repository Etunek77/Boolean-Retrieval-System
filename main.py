import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import sent_tokenize , word_tokenize, punkt
from nltk.corpus import stopwords
import glob
import re
import os
from nltk.stem import PorterStemmer
Stopwords = set(stopwords.words('english'))
ps= PorterStemmer()
import itertools
from helper import finding_all_unique_words_and_freq , finding_freq_of_word_in_doc , remove_special_characters , contains_star , edit_distance

query = input('Enter your query:')
query = query.lower()
query = word_tokenize(query)
query = [ps.stem(word) for word in query]
connecting_words = []
cnt = 1
different_words = []
for word in query:
    if word.lower() != "and" and word.lower() != "or" and word.lower() != "not":
        different_words.append(word.lower())
    else:
        connecting_words.append(word.lower())

perms_dict = dict()
for i,word in enumerate(different_words):

  if contains_star(word):
    perms_dict[word] = permuterm(word)


for i, word in enumerate(different_words):
  if word not in perms_dict.keys():
  
    if unique_words_all.count(word) == 0:
      spelling_score = dict()
      for word_1 in unique_words_all:
        score=edit_distance(word,word_1)
        spelling_score[word_1]=score

      spelling_score = dict(sorted(spelling_score.items(), key = lambda x: x[1]))
      new_word = list(spelling_score.keys())
      different_words[i]=new_word[0]


# print(different_words)
final_docs = set()
queries_to_be_passed = list()

for i,v in enumerate(different_words):
  if v in perms_dict.keys():
    pass
  else:
    perms_dict[v]=[v]


args = list()

for v in different_words:
  args.append(perms_dict[v])
  print(perms_dict[v])
  
print("**********")
for combination in itertools.product(*args):
  query = list(combination)
  output = set(documents(query, connecting_words))
  final_docs = final_docs.union(output)


print(final_docs)
