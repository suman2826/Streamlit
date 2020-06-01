import streamlit as st 
from gensim.summarization import summarize

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import spacy
from spacy import displacy
nlp = spacy.load('en')
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

#@st.cache(allow_output_mutation=True)
def analyze_text(text):
	return nlp(text)

def main():
	st.title("Summary and Text Preprocessing")
	activity1 = ["Summarize","Named Entity Recognition","Text Preprocessing"]
	choice = st.sidebar.selectbox("Select Function",activity1)
	if choice == 'Summarize':
		st.subheader("Summary with NLP")
		raw_text = st.text_area("Enter Text Here","Type Here")
		summary_choice = st.selectbox("Summary Choice",["Genism","Sumy Lex Rank"])

		if st.button("Summarize"):
			if summary_choice == "Genism":
				summary_result = summarize(raw_text)
			elif summary_choice == "Sumy Lex Rank":
				summary_result = sumy_summarizer(raw_text)

			st.write(summary_result)
	if choice == 'Named Entity Recognition':
		st.subheader("Named Entity Recog with Spacy")
		raw_text = st.text_area("Enter Text Here","Type Here")
		if st.button("Analyze"):
			docx = analyze_text(raw_text)
			html = displacy.render(docx,style="ent")
			html = html.replace("\n\n","\n")
			st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)

	if choice == 'Text Preprocessing':
		st.subheader("Text Preprocessing")
		raw_text = st.text_area("Enter Text Here")
		c1 = "Convert to Lower Case"
		c2 = "Remove Punctuation"
		c3 = "Convert sentence into words"
		choice2 = [c1,c2,c3]
		choiceOperations = []
		choiceOperations = st.multiselect("Operations",choice2)
		print(choiceOperations)
		out, flag = '',True
		if st.button("Process"):
			if c1 in choiceOperations:
				if flag:
					out = raw_text.lower()
					flag = False
				else:
					out = out.lower()
			if c2 in choiceOperations:
				punctuations = '''!()-[]{};:'"\,>./?@#$%^&*_~'''
				if flag:
					for x in raw_text:
						if x in punctuations:
							out = raw_text.replace(x,"")
					flag = False
				else:
					for x in out:
						if x in punctuations:
							out = out.replace(x,"")
			if c3 in choiceOperations:
				if flag:
					out = raw_text.split()
					flag = False
				else:
					out = out.split()
		st.write(out)



if __name__ == '__main__':
	main()
