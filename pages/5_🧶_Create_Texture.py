import json
import time
import streamlit as st
from components.leonardo.endpoints import generate_image
from components.leonardo.prompts import TexturePrompt

# NOTE: Filepaths
textures_data_path = "./data/textures/data.json"
ui_data_path ="./data/textures/ui.json"

# load the UI data from JSON file
with open(ui_data_path, 'r') as f:
    ui = json.load(f)

# load the Textures data from JSON file
with open(textures_data_path, 'r') as f:
    textures = json.load(f)

# Create Texture Asset
def create_texture():
    with st.spinner(text='Creating 2D Game Asset...'):
        time.sleep(2)

        # Create Texture asset prompt
        asset = TexturePrompt(colour, item, type, style)
        prompt = asset.create()

        # Generate the asset's Image using Leonardo.ai API endpoint
        image = generate_image(prompt, asset.model_id)

        # Grab the Image URL from the response
        image_url = image['generations_by_pk']['generated_images'][0]['url']

        # Add the Texture to the list of Textures in JSON file
        texture = {"name": item, "url": image_url}
        textures.append(texture)

        # Write the updated data back to the Textures data file
        with open(textures_data_path, 'w') as f:
            json.dump(textures, f, indent=4)




# Web App UI
st.title("🧶Texture Creator🧵")
# Insert containers separated into tabs:
create_tab, view_tab = st.tabs(["🧶Create Texture", "🧵View Textures"])
with create_tab:
    st.subheader("Create Texture Game Asset:")
    item = st.selectbox("Item to be textured:", [str(item) for item in ui['items']])
    type = st.selectbox("Texture pattern:", [str(type) for type in ui['types']])
    colour = st.selectbox("Texture colour:", [str(colour) for colour in ui['colours']])
    style = st.selectbox('Texture style:', [str(style) for style in ui['styles']])

    st.button(label="Create Texture", on_click=create_texture)

with view_tab:
    # API call here later to retrieve images from database
    st.subheader("2D Textures Asset Library:")

    # Loop throught the Textures assets created and render the Images
    for txt in textures:
        with st.expander(txt['name'], expanded=True):
            st.image(txt['url'], caption=txt['name'], use_column_width=True)