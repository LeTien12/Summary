import streamlit as st
from tool.funtions import summarize


def main():

    st.title('Wellcom to here')
    user = st.chat_input()

    if user:
        with st.spinner("Prosessing..."):
            text = summarize(user)
            st.write(text)
            
if __name__ == '__main__':
    main()

