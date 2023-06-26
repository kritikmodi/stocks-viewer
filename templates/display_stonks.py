import streamlit as st
import yfinance as finance
import requests

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>DATATAILR STOCK APP</h1>", unsafe_allow_html=True)
    st.title('Enter company code')
    company_code = st.text_input('Enter some text')
    
    if st.button('Submit'):
        company_ticker = send_request(company_code)
        if company_ticker is not None:
            display_results(company_ticker, company_code)
        else:
            st.write('Error: Failed to connect to Flask service.')

def send_request(company_code):
    try:
        url = 'http://127.0.0.1:5000'
        payload = {'text': company_code}
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return response
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    
def display_results(company_ticker, company_code):

    company_finance_details = finance.download(company_code, start="2022-04-01", end="2022-09-01")

    company_data = company_ticker.history(period="1mo")

    st.write("\n\n\n")

    st.write("""### {company_ticker}""")
    st.write(company_ticker.info['longBusinessSummary'])
    st.write(company_finance_details)
    st.line_chart(company_data.values)
    
if __name__ == '__main__':
    main()