from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit  as st
from dotenv import load_dotenv 

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANCHAIN_TRACING_V2"]="true"
os.environ["LANCHAIN_API_KEY"]=os.getev("LANHCHAIN_API_KEY")

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

#openai llm
llm=ChatOpenAI(model="get-3")
