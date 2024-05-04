#EXTRACTIVE SUMMARIZER
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, particularly computer systems, as opposed to the natural intelligence of living beings. It is a field of research in computer science that develops and studies methods and software which enable machines to perceive their environment and uses learning and intelligence to take actions that maximize their chances of achieving defined goals. Such machines may be called AIs.
AI technology is widely used throughout industry, government, and science. Some high-profile applications include advanced web search engines (e.g., Google Search); recommendation systems (used by YouTube, Amazon, and Netflix); interacting via human speech (e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo); generative and creative tools (e.g., ChatGPT and AI art); and superhuman play and analysis in strategy games (e.g., chess and Go). However, many AI applications are not perceived as AI: "A lot of cutting edge AI has filtered into general applications, often without being called AI because once something becomes useful enough and common enough it's not labeled AI anymore.
Alan Turing was the first person to conduct substantial research in the field that he called machine intelligence. Artificial intelligence was founded as an academic discipline in 1956.[6] The field went through multiple cycles of optimism, followed by periods of disappointment and loss of funding, known as AI winter. Funding and interest vastly increased after 2012 when deep learning surpassed all previous AI techniques, and after 2017 with the transformer architecture. This led to the AI boom of the early 2020s, with companies, universities, and laboratories overwhelmingly based in the United States pioneering significant advances in artificial intelligence."""

def summarizer(rawdocs):
	stopwords = list(STOP_WORDS)
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(rawdocs)
	tokens = [token.text for token in doc] 
	word_freq={}  
	for word in doc:
		if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
			if word.text not in word_freq.keys():
				word_freq[word.text]=1
			else:
				word_freq[word.text]+=1

	max_freq = max(word_freq.values())
	for word in word_freq.keys():
		word_freq[word] = word_freq[word]/max_freq #normalized
		
	sent_token = [sent for sent in doc.sents]
	sent_scores={}
	for sent in sent_token:
		for word in sent:
			if word.text in word_freq.keys():
				if sent not in sent_scores:
					sent_scores[sent]=word_freq[word.text]
				else:
					sent_scores[sent]+=word_freq[word.text]

	select_len = int(len(sent_token)*0.3)
	summary = nlargest(select_len, sent_scores,key=sent_scores.get)
	final_summary = [word.text for word in summary]
	summary = ' '.join(final_summary)
	return summary

#,doc,len(rawdocs.split(' ')),len(summary.split(' '))
