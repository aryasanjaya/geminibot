########### Import the required packages ############
import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader  # To read PDF files
from dotenv import load_dotenv
import os

load_dotenv()

####### Provide your API key ###################
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

######## Choose the heading ###############
st.header("Analisis PDF dengan AI Chat")

########## Upload a file ##################
uploaded_file = st.file_uploader("Masukkan File PDF", type=["pdf"])

if uploaded_file is not None:
    # Read and extract text from the PDF
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page_num in range(len(reader.pages)):
        pdf_text += reader.pages[page_num].extract_text()

    # Display extracted text from the PDF
    st.subheader("Isi PDF yang Ditemukan:")
    st.text_area("Teks PDF", pdf_text, height=200)

############ What you want to ask ####################
prompt = st.text_input("Masukkan Pertanyaan")

######### Initialize Session State ########
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'conversation_active' not in st.session_state:
    st.session_state.conversation_active = True  # Set initial state for conversation

if 'pdf_text' not in st.session_state:
    st.session_state.pdf_text = None  # To store the uploaded PDF text for follow-up questions

######### Use genai skill ##########################
if st.button("GET RESPONSE") and uploaded_file and prompt:
    st.session_state.pdf_text = pdf_text  # Store the PDF text in session state
    model = genai.GenerativeModel("gemini-1.5-pro")
    
    # Generate response using the model, combining the prompt and the extracted PDF text
    response = model.generate_content([prompt, st.session_state.pdf_text])
    
    # Add AI's first response to the chat history
    st.session_state.chat_history.append(f"AI: {response.text}")
    
    # Display AI response
    st.markdown(response.text)

    ######## Conversation of Results ########
    st.subheader("AI Response Summary:")
    st.write("The AI has analyzed your PDF and provided insights based on your query.")

    # Display the chat history
    for msg in st.session_state.chat_history:
        st.markdown(msg)

######## Follow-up Chat Mode ########
if len(st.session_state.chat_history) > 0 and st.session_state.conversation_active:
    user_message = st.text_input("Pertanyaan lanjutan (ketik 'cukup' untuk mengakhiri):", key="follow_up")

    if user_message:
        if user_message.lower() == "cukup":
            st.session_state.conversation_active = False  # End conversation
            st.write("Percakapan telah berakhir. Terima kasih!")
        else:
            # Add user's follow-up message to the chat history
            st.session_state.chat_history.append(f"You: {user_message}")
            
            # Generate AI response for follow-up, including the initial PDF text
            follow_up_response = genai.GenerativeModel("gemini-1.5-pro").generate_content([user_message, st.session_state.pdf_text])
            
            # Add AI's follow-up response to the chat history
            st.session_state.chat_history.append(f"AI: {follow_up_response.text}")
            
            # Display updated chat history
            for msg in st.session_state.chat_history:
                st.markdown(msg)

######## Reset Button ########
if st.button("Reset Semua"):
    # Clear session state variables to reset the conversation
    st.session_state.chat_history = []
    st.session_state.conversation_active = True
    st.session_state.pdf_text = None

    st.write("Semua data telah direset. Anda bisa memulai percakapan baru dengan mengunggah PDF.")
