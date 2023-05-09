import json
import time
import streamlit as st
from components.midjourney.prompts import TileMapPrompt


# Load the common knowledge training data from JSON file
with open('./data/tilemaps/tilemaps.json', 'r') as f:
    tilemaps = json.load(f)

def show_midjourney_prompt():
        prompt = TileMapPrompt(location, style)
        midjourney_prompt = prompt.create()
        time.sleep(1)
        with st.expander("Midjourney Prompt:", expanded=True):
            st.info(midjourney_prompt)

# Display UI Spinner
def display_spinner():
    with st.spinner(text='Creating 2D Game Asset...'):
        show_midjourney_prompt()

# Web App UI
st.title("🌃Tilemap Creator👾")
# Insert containers separated into tabs:
create_tab, view_tab = st.tabs(["Create Tilemap", "View Tilemaps"])
with create_tab:
    st.subheader("Create Tilemap Game Asset:")
    location = st.text_input("Tilemap location:", placeholder="For example: farm, pond, delve, etc.")
    style = st.selectbox('Tilemap style:', [str(style) for style in tilemaps['styles']])
    st.button(label="Create Tilemap", on_click=display_spinner)

with view_tab:
    # API call here later to retrieve images from database
    st.subheader("Tilemap Asset Library:")
    st.image('./assets/images/tilemap.png', caption="Tilemap Example")
    st.image('./assets/images/zelda-pond-tilemap.png', caption="Zelda Pond Scene Tilemap")

    st.file_uploader('Upload an Image:')