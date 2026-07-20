from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3
from datetime import datetime
import streamlit as st

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

llm=ChatOpenAI(model="gpt-4o-mini")

def create_detect_table_to_db():

        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS "Language_Detection" (
        "S.NO"	INTEGER,
        "Input_Text"	TEXT,
        "Detected_Language"	TEXT,
        "Date"	TEXT DEFAULT CURRENT_TIMESTAMP,
        "Probability"	REAL,
        PRIMARY KEY("S.NO" AUTOINCREMENT)
        );
        """)
        con.commit()
        con.close()

def language_detection(Sentence):

    

    def insert_to_db(Sentence,Language_Detect,probability):
        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("insert into Language_Detection values(?,?,?,?,?)",(None,Sentence,Language_Detect,date,probability))
        con.commit()
        con.close()
        

    

    class language_detection(BaseModel):
        Language_Detect:str=Field(description="""
            Analyze the given text and identify the language in which it is written.

                    Possible languages may include:
                    English
                    Hindi
                    French
                    German
                    Spanish
                    Italian
                    Portuguese
                    Russian
                    Chinese
                    Japanese
                    Korean
                    Arabic
                    and other supported languages.

                    Return only the detected language name.

                    If the input is empty, meaningless, contains only symbols/numbers,
                    or is not valid text, return: Invalid Text.
            """)
        Probability:float=Field(description="Confidence score of the predicted Language Detection between 0 and 100 .")

    llm_structured_language=llm.with_structured_output(language_detection)

    language_template=PromptTemplate(template="{Prompt}",input_variables=["prompt"])
    chain=language_template|llm_structured_language
    resp=chain.invoke({"Prompt":Sentence})
    
    insert_to_db(Sentence,resp.Language_Detect,resp.Probability)
    
    return resp.Language_Detect, resp.Probability


