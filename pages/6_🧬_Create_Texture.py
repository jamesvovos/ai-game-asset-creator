import json
import time
import streamlit as st
from components.midjourney.prompts import TexturePrompt


# Load the common knowledge training data from JSON file
with open('./data/texture/data.json', 'r') as f:
    textures = json.load(f)

def show_midjourney_prompt():
        prompt = TexturePrompt(colour, item, type, style)
        midjourney_prompt = prompt.create()
        time.sleep(1)
        with st.expander("Midjourney Prompt:", expanded=True):
            st.info(midjourney_prompt)

# Display UI Spinner
def display_spinner():
    with st.spinner(text='Creating 2D Game Asset...'):
        show_midjourney_prompt()

# Web App UI
st.title("🧬Texture Creator🧵")
# Insert containers separated into tabs:
create_tab, view_tab = st.tabs(["Create Texture", "View Textures"])
with create_tab:
    st.subheader("Create Texture Game Asset:")
    item = st.selectbox("Item to be textured:", [str(item) for item in textures['items']])
    type = st.selectbox("Texture pattern:", [str(type) for type in textures['types']])
    colour = st.selectbox("Texture colour:", [str(colour) for colour in textures['colours']])
    style = st.selectbox('Texture style:', [str(style) for style in textures['styles']])

    st.button(label="Create Texture", on_click=display_spinner)

with view_tab:
    # API call here later to retrieve images from database
    st.subheader("Textures Asset Library:")
    st.image('./assets/images/blue-rocks-texture.png', caption="Blue Soil with Rocks Texture")
    st.image('./assets/images/purple-bricks-cracked-texture.png', caption="Blue Soil with Rocks Texture")