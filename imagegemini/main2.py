########### Import the required packages ############
import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

####### Provide your API key ###################
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

######## Choose the heading ###############
st.header("Analisis Gambar dengan AI Chat")

########## Upload a file ##################
uploaded_file = st.file_uploader("Masukkan Gambar", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))

############ What you want to ask ####################
prompt = st.text_input("Masukkan Pertanyaan")

######### Initialize Session State ########
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'conversation_active' not in st.session_state:
    st.session_state.conversation_active = True  # Set initial state for conversation

if 'image' not in st.session_state:
    st.session_state.image = None  # To store the uploaded image for follow-up questions

######### Use genai skill ##########################
if st.button("GET RESPONSE") and uploaded_file and prompt:
    st.session_state.image = Image.open(uploaded_file)  # Store the image in session state
    model = genai.GenerativeModel("gemini-1.5-pro")
    
    # Generate response using the model, combining the image and the prompt
    response = model.generate_content([prompt, st.session_state.image])
    
    # Add AI's first response to the chat history
    st.session_state.chat_history.append(f"AI: {response.text}")
    
    # Display AI response
    st.markdown(response.text)

    ######## Conversation of Results ########
    st.subheader("AI Response Summary:")
    st.write("The AI has analyzed your image and provided insights based on your query.")

    # Example of how you can extract insights (modify based on response.text structure)
    if "pattern" in response.text.lower():
        st.write("The AI detected patterns in the image relevant to your query.")
    else:
        st.write("The AI did not detect any specific patterns. Feel free to ask follow-up questions.")

    # Display the chat history
    # for msg in st.session_state.chat_history:
    #    st.markdown(msg)

######## Follow-up Chat Mode ########
if len(st.session_state.chat_history) > 0 and st.session_state.conversation_active:
    user_message = st.text_input("Your follow-up question (type 'cukup' to end):", key="follow_up")

    if user_message:
        if user_message.lower() == "cukup":
            st.session_state.conversation_active = False  # End conversation
            st.write("Percakapan telah berakhir. Terima kasih!")
        else:
            # Add user's follow-up message to the chat history
            st.session_state.chat_history.append(f"You: {user_message}")
            
            # Generate AI response for follow-up, including the initial image
            follow_up_response = genai.GenerativeModel("gemini-1.5-pro").generate_content([user_message, st.session_state.image])
            
            # Add AI's follow-up response to the chat history
            st.session_state.chat_history.append(f"AI: {follow_up_response.text}")
            
            # Display updated chat history
            for msg in st.session_state.chat_history:
                st.markdown(msg)

######## Reset Button ########
if st.button("Reset All"):
    # Clear session state variables to reset the conversation
    st.session_state.chat_history = []
    st.session_state.conversation_active = True
    st.session_state.image = None

    st.write("All data has been reset. You can start a new conversation by uploading a new image.")
