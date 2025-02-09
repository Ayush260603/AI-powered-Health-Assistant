import streamlit as st
import nltk 
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('punkt')
# nltk.download('stopwords')

chatbot=pipeline("text-generation",model="distilgpt2")

# def preprocess_input(user_input):
    # stop_words = set(stopwords.words('english'))
    # words = word_tokenize(user_input)
    # filtered_words = [word for word in words if word.lower() not in stop_words]
    # return ' '.join(filtered_words)

def healthcare_chatbot(user_input):
    # user_input = preprocess_input(user_input).lower()
    if "symptom" in user_input:
        return "please consult any specialised doc"
    elif "appointment" in user_input:
        return "would you like to schedule appointment with the doc"
    elif "medication" in user_input:
        return "its advised to take prescribed medicines only. if you have any further concerns consult your doctor"
    else:
        response=chatbot(user_input,max_length=500,num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("HEALTHCARE ASSISTANCE CHATBOT")
    user_input=st.text_input("How can I assist you today")
    print(user_input)
    if st.button("Submit"):
        if user_input:
            st.write("User: ",user_input)
            # with st.spinner("processing your query. please wait for sometime")
            response=healthcare_chatbot(user_input)
            st.write("Healthcare assistant:",response)
        else:
            st.write("please enter your query")    

main()    
