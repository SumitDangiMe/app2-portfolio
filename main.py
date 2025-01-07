import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.png")

with col2:
    st.title("Sumit Dangi")
    content = """
    I am Sumit Dangi!
    Done my bachelors of engineering in Information Technology in 2008.
    Currently working in Coforge Ltd. as a Test Architect.
    """
    st.info(content)