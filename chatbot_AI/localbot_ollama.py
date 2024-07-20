#%%
## import required libraries
from langchain_openai import ChatOpenAI                   ## The LLM model
from langchain_core.prompts import ChatPromptTemplate     ## Required to give input prompt
from langchain_core.output_parsers import StrOutputParser ## Default output parser

## for third party integrations: langchain community
from langchain_community.llms.ollama import Ollama

import os
import streamlit as st
from dotenv import load_dotenv

#%%
## Get environment varaibles
os.environ["LANGCHAIN_TRACING_V2"] = "true"                         ## to capture monitoring results
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")    ## where monitoring results will be stored (dashboard)

#%%
## Define the prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Please respond to the queries:"),
        ("user","Question:{question}")
    ]
)

#%%
## Streamlit framework

st.title("Langchain demo with Ollama and LLAMA3 LLM")
input = st.text_input("Search -> ")

#%%

## LLAMA2 LLM 
llm = Ollama(model="llama3")

## Output Parser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser    ## **IMP**

#%%
if input!=None:
    st.write(chain.invoke({'question':input}))