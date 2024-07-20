from urllib import response
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import sqlite3

import google.generativeai as genai

## Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

## Function to produce SQL query from prompt
def get_gemini_respone(question, prompt):
    
    llm = genai.GenerativeModel("gemini-pro")
    response = llm.generate_content([prompt[0], question])
    return response.text

## Function to execute SQL query in the database
def execute_query(sql,db):
    
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    connection.commit()
    connection.close()
    
    # for row in rows:
    #     print(row)

    return rows

## Input Prompt [Taken verbatim from Krish Naik]
## WRITE AS MANY EXAMPLES AS POSSIBLE TO TRAIN THE MODEL BETTER
## THIS WILL HELP US ACHIEVE COMPLEX QUERIES
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, STREAM, MARKS, SUBJECT
    \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science stream?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where STREAM="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""
]

## Streamlit Application

st.set_page_config(page_title="Text to SQL queries")
st.header("Gemini Pro as the underlying LLM")
question = st.text_input("Input: ",key="input")
submit = st.button("Ask this question")

if submit:
    response = get_gemini_respone(question,prompt)
    # print(f"The sequel query generated is {response}")
    st.subheader("The following query is generated:")
    st.subheader(response)

    data = execute_query(response,"student.db")
    st.subheader("Upon executing this query, we get:")
    for row in data:
        st.subheader(row)