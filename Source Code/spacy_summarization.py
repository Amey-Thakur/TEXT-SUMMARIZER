# NLP Pkgs
"""
@file spacy_summarization.py
@description Implementation of text summarization logic using the SpaCy library. 
Utilizes tokenization, stop-word removal, and sentence weighting for summary generation.

@author Amey Thakur <https://github.com/Amey-Thakur>
@author Mega Satish <https://github.com/msatmod>
@created 2022-08-09
@repository https://github.com/Amey-Thakur/TEXT-SUMMARIZER
@license MIT
"""

import spacy 
nlp = spacy.load("en_core_web_sm")
# Pkgs for Normalizing Text
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
# Import Heapq for Finding the Top N Sentences
from heapq import nlargest



def text_summarizer(raw_docx):
    """
    Generates an extractive summary using SpaCy NLP pipeline.
    Calculates word importance based on inverse frequency and ranks sentences accordingly.
    
    @param raw_docx (str): The raw input text string to be summarized.
    @return summary (str): The final extractive summary composed of top-ranked sentences.
    """
    raw_text = raw_docx
    docx = nlp(raw_text) # Process text through SpaCy pipeline
    stopwords = list(STOP_WORDS)
    
    # 1. Build Word Frequency Distribution
    # Iterate over tokens to count non-stopword occurrences
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    # 2. Normalize Word Frequencies
    # Scale frequencies to [0, 1] range to determine relative word importance
    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
        
    # 3. Sentence Tokenization
    # Extract sentence objects from the SpaCy Doc object
    sentence_list = [ sentence for sentence in docx.sents ]

    # 4. Calculate Sentence Scores
    # Aggregate weighted word scores to determine overall sentence significance
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                # Filter out long sentences (>30 words) to maintain summary conciseness
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    # 5. Extract Top Sentences
    # Select the top 7 highest-scoring sentences for the final summary
    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    return summary
    
