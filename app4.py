import streamlit as st
import pickle
from time import sleep
from PIL import Image
import base64

# Function to Add Background Image
def add_background_image(image_file):
    with open(image_file, "rb") as file:
        base64_image = base64.b64encode(file.read()).decode()

    # Inject CSS for background image
    css_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css_style, unsafe_allow_html=True)

# Main Function

def main():
    add_background_image("water12.jpg")  # Replace with the name/path of your image file

    st.sidebar.title(":blue[📌Navigation]")
    page=st.sidebar.radio('Go to',['🏠Home','🔍Prediction'])
    if page == '🏠Home':
        #st.title(":blue[WATER QUALITY CLASSIFICATION]")
        st.subheader("Welcome😊" )
        st.header("Water Quality Classification App!")
        st.write(" ")
        st.write("""This app **analyzes** whether a water sample is **safe for human consumption** using **machine learning**! By examining its chemical and microbial properties, the model can accurately predict water quality — providing a valuable tool for environmental monitoring and public health!""")

    elif page=='🔍Prediction':
        st.title(":blue[🔍Prediction]")
        aluminium=st.slider("aluminium",0.0,5.05)
        ammonia=st.slider("ammonia",-0.08,29.8)
        arsenic=st.slider("arsenic",0.0,1.05)
        barium= st.slider("barium",0.0,4.94)
        cadmium=st.slider("cadmium",0.0,0.13)
        chloramine = st.slider("chloramine",0.0,8.68)
        chromium = st.slider("chromium",0.0,0.9)
        copper = st.slider("copper",0.0,2.0)
        flouride = st.slider("flouride",0.0,1.5)
        bacteria = st.slider("bacteria",0.0,1.0)
        viruses = st.slider("viruses",0.0,1.0)
        lead = st.slider("lead",0.0,0.2)
        nitrates = st.slider("nitrates",0.0,19.8)
        nitrites = st.slider("nitrites",0.0,2.93)
        mercury = st.slider("mercury",0.0,0.01)
        perchlorate = st.slider("perchlorate",0.0,60.0)
        radium = st.slider("radium",0.0,7.99)
        selenium = st.slider("selenium",0.0,0.1)
        silver = st.slider("silver",0.0,0.5)
        uranium = st.slider("uranium",0.0,0.09)
        features=[aluminium,ammonia,arsenic,barium,cadmium,chloramine,
        chromium,copper,flouride,bacteria,viruses,lead,
        nitrates,nitrites,mercury,perchlorate,radium,selenium,
        silver,uranium]

        scaler=pickle.load(open("WQ_scaler.sav",'rb'))
        model=pickle.load(open("WaterQuality_xg_os.sav",'rb'))
        pred=st.button('PREDICT')
        if pred:
            result = model.predict(scaler.transform([features]))

            if result == 1:
                st.write("Processing result...")
                #sleep(2)  # Pause for 2 seconds
                #st.write("Still analyzing...")
                sleep(3)  # Pause for another 3 seconds
                st.write(":blue[Water is safe]")
            else:
                st.write(":red[Water is not safe]")
main()