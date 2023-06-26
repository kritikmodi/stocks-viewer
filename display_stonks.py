import streamlit as st
import requests

def main():
    st.title('Text Input')
    text = st.text_input('Enter some text')
    
    if st.button('Submit'):
        response = send_request(text)
        if response is not None:
            st.write('Response:', response)
        else:
            st.write('Error: Failed to connect to Flask service.')

def send_request(text):
    try:
        url = 'http://127.0.0.1:5000'
        payload = {'text': text}
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

if __name__ == '__main__':
    main()
