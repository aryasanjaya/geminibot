!pip install streamlit
!pip install google.generativeai
!pip install python-dotenv

########### Import the required packages ############
import streamlit as st
import google.generativeai as genai  # Google Generative AI package for text generation
from dotenv import load_dotenv
import os

# Load environment variables (for API key)
load_dotenv()

####### Provide your API key ###################
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

######## Choose the heading ###############
st.header("AI Chat: Text and Image Generation")

############ Input Prompt ####################
prompt = st.text_input("Masukkan Pertanyaan atau Prompt untuk Menghasilkan Gambar atau Jawaban Teks")

######### Initialize Session State ########
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'conversation_active' not in st.session_state:
    st.session_state.conversation_active = True  # Set initial state for conversation

######### Generate Response or Image ##########
if st.button("Generate Response or Image") and prompt:
    # Decide if prompt is for text generation or image generation
    if "generate image" in prompt.lower():
        # Extract the image description from the prompt
        image_description = prompt.replace("generate image", "").strip()
        st.write(f"Generating image for: {image_description}")
        
        # Replace the below line with actual image generation API call or use a mockup for testing
        st.image("https://via.placeholder.com/400x300.png?text=Generated+Image", 
                 caption=f"Generated image for: {image_description}")
        
        st.session_state.chat_history.append(f"AI generated image for: {image_description}")
    else:
        # Use Gemini's content generation for text analysis
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content([prompt])
        
        # Add AI's first response to the chat history
        st.session_state.chat_history.append(f"AI: {response.text}")
        
        # Display AI response
        st.markdown(response.text)

        ######## Conversation of Results ########
        st.subheader("AI Response Summary:")
        st.write("The AI has analyzed your prompt and provided insights based on your query.")
        
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
            
            # Generate AI response for follow-up, continuing the conversation
            follow_up_response = genai.GenerativeModel("gemini-1.5-pro").generate_content([user_message])
            
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

    st.write("Semua data telah direset. Anda bisa memulai percakapan baru.")
