import streamlit as st
from st_pages import add_page_title, hide_pages
from st_audiorec import st_audiorec
from streamlit_extras.stateful_button import button
import time
from utils import upload_to_drive

import torch
from transformers import pipeline

add_page_title() 

st.markdown(
    """
    **Windanam** is Cawoylel's first multidialectal speech recognition model. 
    As with all AI systems, there are inherent risks that the model coud mis-transcribe what a person wants to say, or generate inaccurate outputs.
    We encourage you to test it and provides us some feedbacks on the model outputs.
"""
)

if "transcription" not in st.session_state:
    st.session_state.transcription = None

if "audio" not in st.session_state:
    st.session_state.audio = None

@st.cache_resource(show_spinner="Downloading model from Hugging Face...")
def load_model(model_name = "cawoylel/windanam_mms-1b-tts_v2"):
  """
  Function to load model from hugging face
  """
  pipe = pipeline("automatic-speech-recognition", model=model_name)
  return pipe

pipeline = load_model()

st.cache_data(show_spinner="Running model. This can take some some time")
def transcribe_audio(sample):
  """
  Transcribe audio
  """
  transcription = pipeline(sample)
  return transcription["text"]

def main():
    """
    Main function to record audio from browser
    """
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
      st.audio(wav_audio_data, format='audio/wav')
      st.session_state.audio = wav_audio_data
      if button("Transcribe recording", key="transcribe"):
        st.session_state.transcription = transcribe_audio(st.session_state.audio)
        with st.spinner("Fetching output"):
            st.text_area(label = "Model Output", 
                             value=st.session_state.transcription, height = 100)
                
        with st.container():
          st.info("The results might not be perfect yet. In order to improve the model, would you allow us to use your recordings?", icon="ℹ️") 
          if button("Allow my recordings to be used", key="saved"):
            upload_to_drive(wav_audio_data)
            #Display a message indicating successful upload
            st.success(f"Your recording has been saved to improve the model. A jaaraama")

                
    else:
      st.info("Make sure you have recorded yourself by clicking on Start Recording button. Once recorded, you will be able to listen to the recording. Wait some seconds for the Transcribe button to appear. Click on it and wait for the output")
      st.warning("The process might induce some latencies", icon="⚠️")   


if __name__ == "__main__":
    main()
