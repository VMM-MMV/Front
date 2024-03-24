import streamlit as st
import cv2, requests

def style_button(col, label, color):
        st.write(f"""
            <style>
            div.stButton > button:nth-child(1) {{
                width: 100%;
                height: 100%;
                background-color: {color};
                color: white;
                border: 1px solid #aaa;
                border-radius: 5px;
                padding: 15px 30px;
                text-align: center;
                cursor: pointer;
            }}
            </style>
            """, unsafe_allow_html=True)

def main():

    data = {
        "type": None,  # Will store 'Video' or 'Audio'
        "url": None  # Will store the URL or file path
    }

    st.markdown("""
    <style>
    div[data-testid="stMarkdownContainer"] h1 { /* Target the title element */
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("DeepFake Detector")

    col1, col2 = st.columns(2)

    if "type" not in st.session_state:
        st.session_state["type"] = None

    style_button(col1, "Button 1", "#FF4B4B") 
    if col1.button("Video", key="unique_button_1"): 
        # st.write("Button 1 clicked")
        st.session_state["type"] = "video"

    style_button(col2, "Button 2", "#4B74FF")  
    if col2.button("Audio", key="unique_button_2"):
        # st.write("Button 2 clicked")
        st.session_state["type"] = "video"

    data["type"] = st.session_state["type"] 

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])
    st.subheader("or:")
    link = st.text_input("Enter the video link:")

    if link:
        data["url"] = link

    st.write("---")
    col1, col2, col3 = st.columns(3)

    if uploaded_file or link:    
        with col2:
            if st.button("Analyze Video"):
                endpoint = "http://127.0.0.1:5000"
                print(data)
                response = requests.post(endpoint, json=data)

                if response.status_code == 200:
                    st.write("Data sent successfully!")
                else:
                    st.write("Error sending data.")


    # Style the button using CSS
    with st.container():
        st.markdown("""
        <style>
            .stButton > button {
                font-size: 20px; 
                width: 100%; 
            }
        </style>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

