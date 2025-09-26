import streamlit as st
import base64
import yaml
import os


def display_instructions():
    # Markdown with some basic CSS styles for the box
    box_css = """
    <style>
        .instructions-box {
            background-color: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
        }
    </style>
    """

    st.sidebar.markdown(box_css, unsafe_allow_html=True)

    st.sidebar.markdown(
        """
    <div class="instructions-box">

    ### Instructions
    You can exploit this ReAct-based assistant via prompt
    injection to get two flags:

    - You'll obtain the first flag by accessing the transactions for user with ID 2
    - The second flag is DocBrown's password

    To help you finish the challenge, we suggest you familiarize yourself with the techniques
    described <a href="https://labs.withsecure.com/publications/llm-agent-prompt-injection" target="_blank">here</a>
    and <a href="https://youtu.be/43qfHaKh0Xk" target="_blank">here</a>.

    </div>

    You'll also find the database schema to be useful:

    """,
        unsafe_allow_html=True,
    )

    if st.sidebar.button('Show database schema', use_container_width=True):
        st.sidebar.info('Users(userId,username,password)\n\nTransactions(transactionId,username,reference,recipient,amount)')
