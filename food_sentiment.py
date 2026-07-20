from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3
from datetime import datetime
import streamlit as st

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

llm=ChatOpenAI(model="gpt-4o-mini")

def create_database():
        con = sqlite3.connect("multi_project.db")
        con.close()

def create_food_table_to_db():

        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS "Food_review" (
        "S.NO"	INTEGER,
        "Food Review"	TEXT,
        "Sentiment"	TEXT,
        "Date"	TEXT DEFAULT CURRENT_TIMESTAMP,
        "Probability"	REAL,
        PRIMARY KEY("S.NO" AUTOINCREMENT)
    );
""")
        con.commit()
        con.close()



def food_sentiment(review):

    

    
    def insert_to_db(review,food_sentiment,probability):
        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("insert into Food_review values(?,?,?,?,?)",(None,review,food_sentiment,date,probability))
        con.commit()
        con.close()
        
    

    class food_review(BaseModel):
        food_sentiment:str=Field(description="""
        Classify the sentiment of food, restaurant, dining, beverage,
        service, serving, menu, taste, quality, delivery, or eating experience reviews.

        Output only:
        - Positive
        - Negative
        - Neutral
        - Invalid Review

        Consider short review phrases such as:
        'Highly recommended'
        'Excellent service'
        'Loved it'
        'Tasty'
        'Not good'
        'Will visit again'

        as valid food reviews when they reasonably resemble customer feedback.

        Return Invalid Review only when the text is clearly unrelated to food,
        restaurant, dining, beverages, service, menu, delivery, or eating experience.
            
""")
        Probability:float=Field(description="Confidence score of the predicted sentiment between 0 and 100 .")



    llm_structured_food=llm.with_structured_output(food_review)

    food_template=PromptTemplate(template="{Prompt}",input_variables=["prompt"])
    chain=food_template|llm_structured_food

    resp=chain.invoke({"Prompt":review})
    
    insert_to_db(review,resp.food_sentiment,resp.Probability)
    
    
    return resp.food_sentiment, resp.Probability

