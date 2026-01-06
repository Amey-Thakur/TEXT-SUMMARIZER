"""
@file nltk_summarization.py
@description Implementation of text summarization logic using the NLTK library. 
Provides functions to calculate sentence scores based on word frequency.

@author Amey Thakur <https://github.com/Amey-Thakur>
@author Mega Satish <https://github.com/msatmod>
@created 2022-08-09
@repository https://github.com/Amey-Thakur/TEXT-SUMMARIZER
@license MIT
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq  

def nltk_summarizer(raw_text):
	"""
	Generates an extractive text summary using NLTK based on word frequency distribution.
	
	@param raw_text (str): The original text content to be summarized.
	@return summary (str): The concatenated string of the top 7 ranked sentences.
	"""
	stopWords = set(stopwords.words("english"))
	word_frequencies = {}  

	# 1. Calculate Word Frequencies
	# Tokenize the text and count occurrences of non-stop words
	for word in nltk.word_tokenize(raw_text):  
	    if word not in stopWords:
	        if word not in word_frequencies.keys():
	            word_frequencies[word] = 1
	        else:
	            word_frequencies[word] += 1

	# 2. Normalize Frequencies
	# Scale word frequencies by dividing by the maximum frequency to get weighted scores
	maximum_frequncy = max(word_frequencies.values())

	for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

	# 3. Calculate Sentence Scores
	# Score sentences by summing the weighted frequencies of their constituent words
	sentence_list = nltk.sent_tokenize(raw_text)
	sentence_scores = {}  
	for sent in sentence_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_frequencies.keys():
	            # Restrict to sentences with fewer than 30 words to avoid excessive length
	            if len(sent.split(' ')) < 30:
	                if sent not in sentence_scores.keys():
	                    sentence_scores[sent] = word_frequencies[word]
	                else:
	                    sentence_scores[sent] += word_frequencies[word]

	# 4. Generate Summary
	# Select the top 7 sentences with the highest cumulative scores
	summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

	summary = ' '.join(summary_sentences)  
	return summary