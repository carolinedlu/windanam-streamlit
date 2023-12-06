import streamlit as st
from st_pages import add_page_title, hide_pages
from st_audiorec import st_audiorec
from streamlit_extras.stateful_button import button
import time
from utils import upload_to_drive


add_page_title() 

st.markdown(
    """
    Windanam is Cawoylel's first multidialectal speech recognition model. 
    We encourage you test it and provides us some feedbacks on the model outputs
"""
)
#https://drive.google.com/drive/folders/1bkxELyDOA98Ok5uZP3Q0yBoMFE4jy0q5?usp=share_link

# import asr function from pages/models
st.cache_data()
def transcribe_audio():
    transcription = " This is a test for asr model"
    return transcription

def main():
    """
    Main function to record audio from browser
    """
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        if button("Transcribe recording", key="transcribe"):
            transcription = transcribe_audio()
            with st.spinner("Model is loading"):
                st.text_area(label = "Model Output", 
                             value=transcription, height =100)
                
            with st.container():
                st.info("As you can see, the results are not yet perfect. In order to improve the model, would you allow us to use your recordings?", icon="ℹ️")
                if button("Allow my recordings to be used", key="saved"):
                    upload_to_drive(wav_audio_data)
                    #Display a message indicating successful upload
                    st.success(f"Your recording has been uploaded to Google Drive")

                
    else:
        st.warning("Make sure you have recorded yourself by clicking on Start Recording button")
  


if __name__ == "__main__":
    main()
