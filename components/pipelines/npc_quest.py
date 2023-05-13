from langchain.chains import SequentialChain
from components.chains.npc_quest.chains import quest_chain, dialogue_chain, objectives_chain, items_chain, items_details_chain
from components.pipelines.pipeline import Pipeline
from components.leonardo.endpoints import generate_image
from components.leonardo.prompts import ItemPrompt


""" Creates an NPC Quest Creator pipeline with it's own chaining stages """

class NpcQuestPipeline(Pipeline):
    def __init__(self, assets: dict, assets_filepath: str):
        super().__init__(assets, assets_filepath)
        self.assets = assets
        self.assets_filepath = assets_filepath


    # Help from ChatGPT here to help split data:
    # NOTE: Make this multi-threaded later
    # NOTE: Steps:
        # 1. Grab the string entry from file
        # 2. Split the data
        # 3. Create list of objects
        # 4. Write data to file
    def split_data(self):

        # Items
        items_string = self.assets['items']

        items_list = items_string.split("\n")
        items_list = [item[3:] for item in items_list]
        self.assets['items'] = items_list

        # Objectives
        objectives_string = self.assets['objectives']
        objectives_list = objectives_string.split("\n")
        self.assets['objectives'] = objectives_list

        # Items Details
        item_details_string = self.assets['items_details']
        items_details_list = item_details_string.split("\n\n")
        item_details = []

        for item in items_details_list:
            item_info = item.split("\n")
            item_desc = item_info[0][3:] # remove the item number and the colon
            item_details.append({"description": item_desc}) # append the dictionary to the list

        self.assets['items_details'] = item_details

        # Write the data to file
        self.write_data_to_file(self.assets)



    # Chaining pipeline stage 1
    def stage_1(self):
        # Get required input data from JSON file
        name = self.assets['name']
        description = self.assets['description']
        tone = self.assets['tone']

        # Chain the data together in sequential order
        chain_1 = SequentialChain(chains=[quest_chain, dialogue_chain, objectives_chain, items_chain, items_details_chain], verbose=True, input_variables=["name", "description", "tone"], output_variables=["quest", "dialogue", "objectives", "items", "items_details"])
        
        # Get AI model output response
        output = chain_1(({'name': name, 'description': description, 'tone': tone}))

        # Grab the values from the first chain that ran
        quest = output['quest']
        dialogue = output['dialogue']
        objectives = output['objectives']
        items = output['items']
        items_details = output['items_details']

        # Add assets to JSON file to be retrieved by other chains
        self.assets['quest'] = quest
        self.assets['dialogue'] = dialogue
        self.assets['objectives'] = objectives
        self.assets['items'] = items
        self.assets['items_details'] = items_details

        # Write the updated data back to the assets file
        self.write_data_to_file(self.assets)

        # Split the raw data to convert into JSON objects
        self.split_data()

    
    # Chaining pipeline stage 2
    def stage_2(self):
        # Generate Asset Images

        # Step 1: Create Item Assets
        for item in self.assets['items_details']:
                asset = ItemPrompt(item['description'], descriptors="", type="quest")
                prompt = asset.create()

                # Generate the asset's Image using Leonardo.ai API endpoint
                image = generate_image(prompt, asset.model_id)

                # Grab the Image URL from the response
                image_url = image['generations_by_pk']['generated_images'][0]['url']

                # Add the Item Image URL to the list of items_details in the JSON file
                item['url'] = image_url

                # Write the updated data back to the Items data file
                self.write_data_to_file(self.assets)


    # Execute the pipeline stages
    def run(self):
        # Run Chain 1
        self.stage_1()
        # Run Chain 2
        self.stage_2()
        # Display message once complete
        self.display_message()