import json
import time
import streamlit as st
from streamlit_tags import st_tags
from components.leonardo.endpoints import generate_image
from components.leonardo.prompts import IsometricPrompt

# NOTE: Filepaths
isometric_data_path = "./data/isometrics/data.json"
ui_data_path ="./data/isometrics/ui.json"

# load the UI data from JSON file
with open(ui_data_path, 'r') as f:
    ui = json.load(f)

# load the Textures data from JSON file
with open(isometric_data_path, 'r') as f:
    isometrics = json.load(f)

# Create Texture Asset
def create_isometric_world():
    with st.spinner(text='Creating 2D Game Asset...'):
        time.sleep(2)

        # Create Isometric asset prompt
        asset = IsometricPrompt(location, descriptors)
        prompt = asset.create()

        # Generate the asset's Image using Leonardo.ai API endpoint
        image = generate_image(prompt, asset.model_id)

        # Grab the Image URL from the response
        image_url = image['generations_by_pk']['generated_images'][0]['url']

        # Add the Isometric World to the list of Isometrics in JSON file
        isometric = {"name": location, "url": image_url}
        isometrics.append(isometric)

        # Write the updated data back to the Isometrics data file
        with open(isometric_data_path, 'w') as f:
            json.dump(isometrics, f, indent=4)




# Web App UI
st.title("🌃Isometric World Creator🌏")
# Insert containers separated into tabs:
create_tab, view_tab = st.tabs(["🌃Create Isometric World", "🌏View Isometric Worlds"])
with create_tab:
    st.subheader("Create Isometric World Game Asset:")
    location = st.text_input("Isometric world location:", placeholder="For example: dark cave, dark forest, beach island, snowy cabins, etc")

    descriptors = [str(descriptor) for descriptor in ui['descriptors']]

    descriptors = st_tags(
        label='Isometric descriptors:',
        text='Press enter to add.',
        value=descriptors,
        maxtags = 5,
        key='descriptortags')

    st.button(label="Create Isometric World", on_click=create_isometric_world)

with view_tab:
    # API call here later to retrieve images from database
    st.subheader("Isometric Worlds Asset Library:")

    # Loop throught the Isometrics assets created and render the Images
    for iso in isometrics:
        with st.expander(iso['name'], expanded=True):
            st.image(iso['url'], caption=iso['name'], use_column_width=True)