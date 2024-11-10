from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama 
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#promt temp

promt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respomd to the user queries"),
        ("user","Question:{question}") 
    ]
)

#streamlit framework

st.title('Langchain Demo with OpenAI API')
input_text=st.text_input("search the topic you want")

#Ollama LLama2 llm
llm=ollama(model="llama2")
output_parser=StrOutputParser()
chain=promt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

import os

# Set the API key manually (use your actual API key here)
os.environ["LANGCHAIN_API_KEY"] = "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"

# Now use the environment variable
api_key = os.getenv("LANGCHAIN_API_KEY")
print(api_key)  # This should print the correct key    




                         
