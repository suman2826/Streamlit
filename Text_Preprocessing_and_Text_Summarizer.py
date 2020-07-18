import streamlit as st 
from gensim.summarization import summarize

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

def main():
	st.title("Summary and Text Preprocessing")
	activity1 = ["Summarize","Text Preprocessing"]
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



if __name__ == '__main__':
	main()
