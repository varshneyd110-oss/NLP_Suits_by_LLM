from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3
from datetime import datetime
import streamlit as st

date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

llm=ChatOpenAI(model="gpt-4o-mini")

def create_news_table_to_db():

        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS "News_classification" (
        "S.NO"	INTEGER,
        "News Headline"	TEXT,
        "Category"	TEXT,
        "Date"	TEXT DEFAULT CURRENT_TIMESTAMP,
        "Probability"	REAL,
        PRIMARY KEY("S.NO" AUTOINCREMENT)
    );
""")
        con.commit()
        con.close()

def news_classification(headline):

    

    def insert_to_db(headline,news_classification,Probability):
        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("insert into News_classification values(?,?,?,?,?)",(None,headline,news_classification,date,Probability))
        con.commit()
        con.close()
        

    

    class News_classification(BaseModel):
        news_classification:str=Field(description="""
            Analyze the given news headline or news article and classify it into one of the following categories:
            SPORTS
            POLITICS
            ENTERTAINMENT
            BUSINESS
            TECHNOLOGY
            RELIGIOUS
            Category Definitions:
            SPORTS:
            News related to sports events, matches, tournaments, players, teams, and athletic activities.
            POLITICS:
            News related to government, elections, political parties, policies, ministers, and international relations.
            ENTERTAINMENT:
            News related to movies, television, celebrities, music, web series, and the entertainment industry.
            BUSINESS:
            News related to companies, stock markets, economy, finance, trade, and investments.
            TECHNOLOGY:
            News related to software, hardware, AI, gadgets, cybersecurity, and technological innovations.
            RELIGIOUS:
            News related to religions, temples, mosques, churches, spiritual events, festivals, and religious activities.

            If the input is not a valid news headline or news content,
            return: Invalid News.
    """)
        Probability:float=Field(description="Confidence score of the predicted News Headline between 0 and 100 .")

    llm_structured_News=llm.with_structured_output(News_classification)

    News_template=PromptTemplate(template="{Prompt}",input_variables=["prompt"])
    chain=News_template|llm_structured_News
    resp=chain.invoke({"Prompt":headline})
    
    insert_to_db(headline,resp.news_classification,resp.Probability)
    


    return resp.news_classification, resp.Probability
