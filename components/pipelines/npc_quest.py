from langchain.chains import SequentialChain
from components.chains.npc_quest.chains import quest_chain, dialogue_chain, objectives_chain, items_chain, items_details_chain
from components.pipelines.pipeline import Pipeline


""" Creates an NPC Quest Creator pipeline with it's own chaining stages """

class NpcQuestPipeline(Pipeline):
    def __init__(self, assets: dict, assets_filepath: str):
        super().__init__(assets, assets_filepath)
        self.assets = assets
        self.assets_filepath = assets_filepath

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
    
    # Chaining pipeline stage 12
    def stage_2(self):
        pass


    # Execute the pipeline stages
    def run(self):
        # Run Chain 1
        self.stage_1()
        # Run Chain 1
        self.stage_2()
        # Display message once complete
        self.display_message()