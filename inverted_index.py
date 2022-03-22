dict_global = {}   # dict_global dictionary 
file_folder = '/content/drive/MyDrive/DATASET'  # folder containing all documents
idx = 1   # number the documents starting from 1
files_with_index = {}    # dictionary having filename and its index {filename, file index}
for file in glob.iglob(f'{file_folder}/*'):
    print(file)
    fname = file
    file = open(file , "r")                  # Open and
    text = file.read()                       # read file
    text = remove_special_characters(text)   # Remove special characters
    text = re.sub(re.compile('\d'),'',text)  # Remove digits from text
    # sentences = sent_tokenize(text)          
    words = word_tokenize(text)              # Tokenized 'words' array
    words = [word for word in words if len(words)>1]  # Remove words with length = 1
    words = [word.lower() for word in words]          # Convert word to lowercase
    words = [word for word in words if word not in Stopwords]  # Remove stopwords
    words = [ps.stem(word) for word in words]                  # Stemming 
    # words = [word.lower() for word in words]                  
    dict_global.update(finding_all_unique_words_and_freq(words)) # Update global dictionary
    files_with_index[idx] = os.path.basename(fname)              # Put file into files_with_index array
    idx = idx + 1                                                # and update index
    
unique_words_all = list(set(dict_global.keys()))

class Node:                                       # Node in the inverted index
    def __init__(self ,docId, freq = None):
        self.freq = freq
        self.doc = docId
        self.nextval = None
    
class SlinkedList:                                 # Head of inverted index
    def __init__(self ,head = None):
        self.head = head
        
        
linked_list_data = {}                              # Initialise inverted index for each word
for word in unique_words_all:                      # For each word,
    linked_list_data[word] = SlinkedList()         # create head
    linked_list_data[word].head = Node(1,Node)     # and head is pointing to a dummy node
word_freq_in_doc = {}                              # Word freq in a particular document
idx = 1                                            # idx = idx of document
for file in glob.iglob(f'{file_folder}/*'):        # For each file,
    file = open(file, "r")                         # open
    text = file.read()                             # read
    text = remove_special_characters(text)         # remove spc char
    text = re.sub(re.compile('\d'),'',text)        # remove digits
    # sentences = sent_tokenize(text)
    words = word_tokenize(text)                    # return list of words
    words = [word for word in words if len(words)>1] # remove words of len 1
    words = [word.lower() for word in words]         # convert words to lowercase
    words = [word for word in words if word not in Stopwords] # remove stopwords
    words = [ps.stem(word) for word in words]             # stemming            
    # words = [word.lower() for word in words]              
    word_freq_in_doc = finding_all_unique_words_and_freq(words) # Find word freq in a particular file
    for word in word_freq_in_doc.keys():                        # Populate word_freq_in_doc
        linked_list = linked_list_data[word].head               # Get head of inverted index of that word
        while linked_list.nextval is not None:                  # Go to end of inverted index
            linked_list = linked_list.nextval                   
        linked_list.nextval = Node(idx ,word_freq_in_doc[word]) # Create new node with doc idx and freq in doc
    idx = idx + 1 
