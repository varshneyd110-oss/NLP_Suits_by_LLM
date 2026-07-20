from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3
from datetime import datetime
import streamlit as st

date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

llm=ChatOpenAI(model="gpt-4o-mini")

def create_spam_table_to_db():

        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS  "Spam_Classifier" (
        "S.NO"	INTEGER,
        "message_text"	TEXT,
        "prediction"	TEXT,
        "date"	TEXT DEFAULT CURRENT_TIMESTAMP,
        "Probability"	REAL,
        PRIMARY KEY("S.NO" AUTOINCREMENT)
    );
""")
        con.commit()
        con.close()


def spam_classifier(message):

    
    def insert_to_db(message,spam_classifier,Probability):
        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("insert into Spam_Classifier values(?,?,?,?,?)",(None,message,spam_classifier,date,Probability))
        con.commit()
        con.close()
        

    

    class spam_classifier(BaseModel):
        
        Spam_classifier:str=Field(description="""
            Analyze the given message and classify it as:
            Spam or Ham.
            Spam:
            Messages that contain advertisements, promotions, scams, fraudulent offers, phishing attempts, or unwanted marketing content.
            Ham:
            Legitimate and normal messages intended for genuine communication.

            If the input is empty, meaningless, or not a valid message,
            return: Invalid Message.""")
        Probability:float=Field(description="Confidence score of the predicted Messages between 0 and 100 .")

    llm_structured_spam=llm.with_structured_output(spam_classifier)

    spam_template=PromptTemplate(template="{Prompt}",input_variables=["prompt"])
    chain=spam_template|llm_structured_spam
    resp=chain.invoke({"Prompt":message})
    
    insert_to_db(message,resp.Spam_classifier,resp.Probability)
    
    

    return  resp.Spam_classifier, resp.Probability
