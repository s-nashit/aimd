import streamlit as st
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Streamlit UI
st.title("Speech-to-Text App")
st.write("Click the button and start speaking!")

# Button to record audio
if st.button("Record"):
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Convert speech to text
    try:
        text = recognizer.recognize_google(audio)
        st.success(f"You said: {text}")

        # Print the recognized text
        print("Transcribed Text:", text)

        # Save to a text file
        with open("transcription.txt", "w") as file:
            file.write(text)
        st.write("Transcription saved to `transcription.txt`!")

    except sr.UnknownValueError:
        st.error("Sorry, could not understand the audio.")
    except sr.RequestError:
        st.error("Request error, check your internet connection.")
