from PIL import Image
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    image = Image.open("images/myphoto.png")
    resized_image = image.resize((600, 400))  # Width = 600, Height = 400

    # Display the resized image
    st.image(resized_image)

with col2:
    st.title("Sumit Dangi")
    content = """
    I am Sumit Dangi!
    Done my bachelors of engineering in Information Technology in 2008.
    Currently working in Coforge Ltd. as a Test Architect.
    """
    st.info(content)
st.write(
    "Below you can find some of the apps I have build in python.Feel free to contact me!.I will love to help you to create similar Apps using python")
col3,empty_col ,col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv("data.csv", sep=";")
print(int(df.shape[0] / 2))
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(f"**{row['description']}**")
        st.image(f"images/{row['image']}")
        st.write(f"[Source]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(f"**{row['description']}**")
        st.image(f"images/{row['image']}")
        st.write(f"[Source]({row['url']})")

