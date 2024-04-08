
import streamlit as st
import requests
import mimetypes

def main():

    st.title('Concrete Crack Classification App')

    col1, col2, col3 = st.columns([1, 5, 1])  

    with col1:
        st.write("") 

    with col2:
        st.write("")  
        st.image(r'C:/Users/dskapinakis/Documents/computer_vision_concrete/crack_images/Positive/00030.jpg', width=300, caption="", use_column_width=True)
        uploaded_file = st.file_uploader("Upload a concrete image", type=['png', 'jpg'])
        if uploaded_file is not None:
            if st.button('Probability of concrete having a crack'):
                files = {'file': uploaded_file}
                response = requests.post("http://127.0.0.1:8000/prediction", files=files)
                response.raise_for_status()
                prediction = response.json()
                st.write("Probability of concrete being cracked:", prediction['prediction'])
        
    with col3:
        st.write("") 

if __name__ == "__main__":
    main()

