from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
import sqlite3
from datetime import datetime
import streamlit as st

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

llm=ChatOpenAI(model="gpt-4o-mini")

def create_translate_table_to_db():

        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS "Machine_Translation" (
        "S.NO"	INTEGER,
        "Original_Text"	TEXT,
        "Translated_Text"	TEXT,
        "Date"	TEXT DEFAULT CURRENT_TIMESTAMP,
        "Probability"	REAL,
        "Targeted_Language"	TEXT,
        PRIMARY KEY("S.NO" AUTOINCREMENT)
        );
        """)
        con.commit()
        con.close()

def machine_translation(Input_Text,targeted_language):

    


    def insert_to_db(Input_Text,machine_translation,probability,target_language):
        con=sqlite3.connect(database="multi_project.db")
        cur=con.cursor()
        cur.execute("insert into Machine_Translation values(?,?,?,?,?,?)",(None,Input_Text,machine_translation,date,probability,target_language))
        con.commit()
        con.close()
        

    

    class machine_translation(BaseModel):
        machine_translation:str=Field(description="""
           You are a Machine Translation System.

            Translate the given input text into the user-specified target language.

            Rules:
            - Detect the source language automatically.
            - Translate the text into the target language provided by the user.
            - Preserve the original meaning, context, and intent.
            - Do not add explanations, notes, or extra information.
            - Do not summarize or modify the content.
            - Return only the translated text.
            - If the source language and target language are the same, return the original text.
            - If the input is invalid or meaningless, return: Invalid Text.

            Example:
            Input Text: My name is Dev.
            Target Language: Hindi
            Output: मेरा नाम देव है।

            Input Text: मेरा नाम देव है।
            Target Language: English
            Output: My name is Dev.
                    
            """)
        Probability:float=Field(description="Confidence score of the predicted Translated Text  between 0 and 100 .")

    llm_structured_translation=llm.with_structured_output(machine_translation)

    translation_template=PromptTemplate(template="Give machine Translation of prompt {Prompt} into this targeted language {target_language}",input_variables=["prompt","target_language"])
    chain=translation_template|llm_structured_translation
    resp=chain.invoke({"Prompt":Input_Text,"target_language":targeted_language})
    print(resp.machine_translation)
    print(resp.Probability)
    insert_to_db(Input_Text,resp.machine_translation,resp.Probability,targeted_language)
    
    
    return resp.machine_translation, resp.Probability


