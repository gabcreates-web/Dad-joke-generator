import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Dad Joke Generator", page_icon="😂", layout="wide")

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        padding: 20px 40px;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        display: block;
        margin: 0 auto;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTitle {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 40px;
        color: #FF5733;
        text-align: center;
    }
    .stText {
        font-family: 'Arial', sans-serif;
        font-size: 20px;
        text-align: center;
        color: #555;
    }
    .stMarkdown {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #333;
        padding: 20px;
        background-color: #f4f4f4;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='stTitle'>Dad Joke Generator</h1>", unsafe_allow_html=True)

st.markdown("<p class='stText'>Click the button below to hear a random dad joke that will surely make you groan!</p>", unsafe_allow_html=True)

df = pd.read_csv('dad_jokes.csv')

def get_random_joke():
    return random.choice(df['joke'].tolist())

st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)

if st.button("Tell Me a Joke"):
    joke = get_random_joke()
    st.markdown(f"<p class='stMarkdown'>{joke}</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
