import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def process_text(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return []
    
    with open(file_path, "r") as file:
        content = file.read()

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(content)
    filtered_words = [word for word in word_tokens if word.lower() not in stop_words]
    
    return filtered_words
