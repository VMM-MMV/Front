import streamlit as st
import cv2  # Import OpenCV for potential video processing

def main():
    st.title("DeepFake Detector")

    # uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])

    # option = st.radio("Upload a video or add a link:", options=["Upload Video", "Add Link"])

    # if option == "Upload Video":
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])
    # st.header("or:")
    st.subheader("or:")
    # elif option == "Add Link":
    link = st.text_input("Enter the video link:")
    if link:
        st.markdown(f"You entered: {link}")  # Display the entered link
    
    # if uploaded_file is not None:
    #     file_bytes = uploaded_file.getvalue()

    #     st.video(file_bytes)


        

if __name__ == "__main__":
    main()
