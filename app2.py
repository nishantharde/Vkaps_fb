import streamlit as st
from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
import facebook
import os
load_dotenv()

Open_AI_Key = os.environ["OPENAI_API_KEY"] 
FB_Access_Token = os.environ["FB_GRAPH_ACCESS_TOKEN"]
FB_Page_ID = os.environ["FB_Page_ID"]

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

send_button = st.button("Post on Facebook page",key="Post")

if summarise_button:
  summarise_placeholder = st.write(std)
if send_button:
  access_token = 'FB_GRAPH_ACCESS_TOKEN'
  graph = facebook.GraphAPI(access_token)
  page_id = "FB_Page_ID" 
  post_message = std
  graph.put_object(page_id, "feed", message=post_message)

  # print("Post successfully sent to Facebook.")
  st.write("Post successfully sent to Facebook.")