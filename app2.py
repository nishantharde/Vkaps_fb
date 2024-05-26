import streamlit as st
from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
load_dotenv()
#  testing app2.py for git diff command 
st.set_page_config(page_title="URL Summirazer", page_icon=":face:")
st.markdown("<h1 style='text-align: center;'>URL TO MEDIA_POST</h1>", unsafe_allow_html=True)
st.session_state['URL']=st.text_input("Past  URL Here ",type="default")

with open('scraped_data.txt', 'r') as file:
    # Read the entire contents of the file into a string
    data = file.read()

llm = ChatOpenAI(model_name="gpt-4-0125-preview")
chain = load_summarize_chain(llm, chain_type="stuff")
summarise_button = st.button("Summarise the URL", key="summarise")
std = ""
if st.session_state['URL'] !="":
  url = st.session_state['URL']
  loader = WebBaseLoader(url)
  docs = loader.load()
  summarize_text=chain.invoke(docs)
  std = summarize_text.get("output_text")
