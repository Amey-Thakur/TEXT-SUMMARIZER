"""
@file app.py
@description Main application entry point for the Text Summarizer. Handles Flask routes, 
integrates summarization algorithms (SpaCy, NLTK, Gensim, Sumy), and manages data processing 
for text and URL inputs.

@author Amey Thakur <https://github.com/Amey-Thakur>
@author Mega Satish <https://github.com/msatmod>
@created 2022-08-09
@repository https://github.com/Amey-Thakur/TEXT-SUMMARIZER
@license MIT
"""

from __future__ import unicode_literals
from flask import Flask,render_template,url_for,request

# Import proprietary and third-party summarization modules
from spacy_summarization import text_summarizer  # SpaCy-based summarization logic
from summa.summarizer import summarize       # Summa (Gensim TextRank fork) implementation
from nltk_summarization import nltk_summarizer   # NLTK frequency-based summarization
import time
import spacy

# Initialize SpaCy's English model for Natural Language Processing task
nlp = spacy.load("en_core_web_sm")
app = Flask(__name__)

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen


# Sumy Package Imports for LexRank Algorithm
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def sumy_summary(docx):
	"""
	Generates a text summary using the LexRank algorithm provided by Sumy.
	
	@param docx (str): The input text document to be summarized.
	@return result (str): The concatenated summary string containing top-ranked sentences.
	"""
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3) # Extract top 3 sentences
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result


def readingTime(mytext):
	"""
	Estimates the reading time for a given text based on average reading speed.
	
	@param mytext (str): The input text to analyze.
	@return estimatedTime (float): The estimated reading time in minutes (assuming 200 wpm).
	"""
	total_words = len([ token.text for token in nlp(mytext)]) # Tokenize and count words
	estimatedTime = total_words/200.0
	return estimatedTime

# Fetch Text From Url
def get_text(url):
	"""
	Scrapes and processes textual content from a valid URL.
	
	@param url (str): The HTTP URL of the target webpage.
	@return fetched_text (str): The cleaned text content extracted from paragraph tags.
	"""
	page = urlopen(url)
	soup = BeautifulSoup(page, "html.parser") # Parse HTML content
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p'))) # Extract text from <p> tags
	return fetched_text

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyze',methods=['GET','POST'])
def analyze():
	"""
	Route to handle direct text input for summarization.
	Processes the input text, calculates reading times, and returns the simplified summary.
	"""
	start = time.time()
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		# Calculate metrics for original text
		final_reading_time = readingTime(rawtext)
		# Generate summary using SpaCy-based custom algorithm
		final_summary = text_summarizer(rawtext)
		summary_reading_time = readingTime(final_summary)
		end = time.time()
		final_time = end-start
	return render_template('index.html',ctext=rawtext,final_summary=final_summary,final_time=final_time,final_reading_time=final_reading_time,summary_reading_time=summary_reading_time)

@app.route('/analyze_url',methods=['GET','POST'])
def analyze_url():
	"""
	Route to handle URL-based input for summarization.
	Fetches content from the URL, extracts text, and performs summarization.
	"""
	start = time.time()
	if request.method == 'POST':
		raw_url = request.form['raw_url']
		rawtext = get_text(raw_url)
		final_reading_time = readingTime(rawtext)
		final_summary = text_summarizer(rawtext)
		summary_reading_time = readingTime(final_summary)
		end = time.time()
		final_time = end-start
	return render_template('index.html',ctext=rawtext,final_summary=final_summary,final_time=final_time,final_reading_time=final_reading_time,summary_reading_time=summary_reading_time)



@app.route('/compare_summary')
def compare_summary():
	return render_template('compare_summary.html')

@app.route('/comparer',methods=['GET','POST'])
def comparer():
	"""
	Comparative analysis route.
	Runs multiple summarization algorithms (SpaCy, Gensim, NLTK, Sumy) on the same input 
	to allow side-by-side performance and quality comparison.
	"""
	start = time.time()
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		final_reading_time = readingTime(rawtext)
		
		# 1. SpaCy Summarizer
		try:
			final_summary_spacy = text_summarizer(rawtext)
			summary_reading_time = readingTime(final_summary_spacy)
		except Exception:
			final_summary_spacy = "Error: Text too short or processing failed."
			summary_reading_time = 0

		# 2. Gensim Summarizer (Summa)
		try:
			final_summary_gensim = summarize(rawtext)
			summary_reading_time_gensim = readingTime(final_summary_gensim)
		except Exception:
			final_summary_gensim = "Error: Text too short or processing failed."
			summary_reading_time_gensim = 0

		# 3. NLTK Summarizer (Frequency Dist)
		try:
			final_summary_nltk = nltk_summarizer(rawtext)
			summary_reading_time_nltk = readingTime(final_summary_nltk)
		except Exception:
			final_summary_nltk = "Error: Text too short or processing failed."
			summary_reading_time_nltk = 0

		# 4. Sumy Summarizer (LexRank)
		try:
			final_summary_sumy = sumy_summary(rawtext)
			summary_reading_time_sumy = readingTime(final_summary_sumy)
		except Exception:
			final_summary_sumy = "Error: Text too short or processing failed."
			summary_reading_time_sumy = 0 

		end = time.time()
		final_time = end-start
	return render_template('compare_summary.html',ctext=rawtext,final_summary_spacy=final_summary_spacy,final_summary_gensim=final_summary_gensim,final_summary_nltk=final_summary_nltk,final_time=final_time,final_reading_time=final_reading_time,summary_reading_time=summary_reading_time,summary_reading_time_gensim=summary_reading_time_gensim,final_summary_sumy=final_summary_sumy,summary_reading_time_sumy=summary_reading_time_sumy,summary_reading_time_nltk=summary_reading_time_nltk)



@app.route('/about')
def about():
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)