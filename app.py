import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from PIL import Image

API_KEY = 'AIzaSyAmNZj1Igm_qhu_k4vdStcNVPV_YYtWiKM'
genai.configure(api_key=API_KEY)

#setting the page configuration
st.set_page_config(page_title="Bluesense",
                   page_icon="📸",
                   layout="wide",
                   initial_sidebar_state='collapsed')

#setting the title and description
st.header("Bluesense")


st.write("This app uses Gemini pro vision to generate text from the image provided.")

st.image(r"C:\Users\user\Desktop\Bluesense\image\image.jpg", width=300)

#to upload file and display image 
uploaded_file = st.file_uploader(
    "Choose an Image file", accept_multiple_files=False, type=['jpg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption='Uploaded Image', width=300)
    bytes_data = uploaded_file.getvalue()


#to generate the text from the image using gemini pro vision
generate = st.button("Generate!")

if generate:
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(
        glm.Content(
            parts=[
                glm.Part(
                    text="From the provided image, Please Extract the parameters neede for claiming insurance amount and determine the money that the individual may be entitled to claim from insurance for their injuries accurately. Specifying the amount in dollars and the output should be in less than 20 tokens only."),
                glm.Part(
                    inline_data=glm.Blob(
                        mime_type='image/jpeg',
                        data=bytes_data
                    )
                ),
            ],
        ),
        stream=True)
    
    response.resolve()

#displaying the output text generated
    st.write(response.text)
    