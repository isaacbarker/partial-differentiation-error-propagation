# 🔬 Physics Lab Scripts

## About 📁

This site provides scripts used for practical physics and physical computing. This site uses [streamlit](https://streamlit.io) to convert python programs to web applications.

## Libraries 📚
- Sympy
- Pandas
- Streamlit
- Requests

## Running 🏃‍♀️

To run tshis site pull the repo. 

To run using docker build using the provided `Dockerfile`. using `docker build -t phys-labs`.  Then run the container with `docker run -p 8501:8501 phys-labs`. See more on streamlit deployment using Docker [here]("https://docs.streamlit.io/deploy/tutorials/docker").

To run using python install the dependencies using `pip install -r requirements.txt` and then run using `streamlit run Home.py`.

*See the example.env file for deployment secrets.*