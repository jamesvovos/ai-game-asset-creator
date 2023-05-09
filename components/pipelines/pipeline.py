from abc import ABC
import json
import streamlit as st


""" Pipelines with stages to execute LangChain chaining events, based on the type of asset creation method the user chooses (for example: autopilot mode, create items, create tilemaps, etc). """


# Abstract base class
class Pipeline(ABC):
    def __init__(self, assets: dict, assets_filepath: str):
        self.assets = assets
        self.assets_filepath = assets_filepath

    def write_data_to_file(self, assets):
        # Append data from pipeline to file.
        with open(self.assets_filepath, "w") as f:
            json.dump(assets, f, indent=4)
        f.close()
    
    def run(self):
        pass

    def display_message(self):
        # Display success message once completed.
        st.info('Game assets created successfully.')
        st.balloons()