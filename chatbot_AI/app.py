#%%
## import required libraries
from langchain_openai import ChatOpenAI                   ## The LLM model
from langchain_core.prompts import ChatPromptTemplate     ## Required to give input prompt
from langchain_core.output_parsers import StrOutputParser ## Default output parser

import streamlit as st
import os
from dotenv import load_dotenv
#%%
## Get environment variables

os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")
## Langsmith tracking
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

st.title("Langchain demo with OpenAI API")
input = st.text_input("Search -> ")

#%%
## OpenAI LLM 
llm = ChatOpenAI(model="gpt-3.5-turbo")

## Output Parser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser    ## **IMP**

#%%
if input!=None:
    st.write(chain.invoke({'question':input}))