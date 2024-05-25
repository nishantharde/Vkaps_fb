#  branch main app.py

from openai import OpenAI
import streamlit as st
client =OpenAI(api_key=OPENAI_API_KEY) 
# Upload a file with an "assistants" purpose
file = client.files.create(
  file=open("speech.py", "rb"),
  purpose='assistants'
)

# Create an assistant using the file ID
assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-4-turbo-preview",
  tools=[{"type": "code_interpreter"}],
  file_ids=[file.id]
) 