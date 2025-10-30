import streamlit as st
from dotenv import load_dotenv, find_dotenv
import requests
import os

load_dotenv(find_dotenv())

st.set_page_config(
    page_title="Physics Lab Scripts",
    page_icon="🔬",
)

st.title("🔬 Physics Lab Scripts")
st.write("By [Isaac Barker](https://www.isaacbarker.net).")

st.subheader("About")
st.write("This site provides scripts used for practical physics and physical computing. " \
"This site uses [streamlit](https://streamlit.io) to convert python programs to web applications. " \
"**Check out the Git repo [isaacbarker/physics-labs](https://github.com/isaacbarker/physics-labs).**")

st.subheader("Libraries")
st.write(
"- Sympy\n"
"- Pandas\n"
"- Streamlit\n"
"- Requests\n"
)

# print nasa photo of the day
@st.cache_data(ttl='1d', persist='disk', show_spinner=True)
def get_photo_of_day():
    return requests.get(f"https://api.nasa.gov/planetary/apod?api_key={os.getenv('NASA_API_KEY')}").json()

data = get_photo_of_day()

st.image(data["url"], caption=f"NASA {data['title']}, {data['copyright']}")