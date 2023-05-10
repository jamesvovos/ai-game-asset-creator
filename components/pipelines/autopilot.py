from langchain.chains import SequentialChain
from components.chains.autopilot.chains import storyline_chain, characters_chain, backstories_chain, quests_chain, dialogue_chain, items_chain, item_descriptions_chain, dialogue_tree_chain
from components.pipelines.pipeline import Pipeline
import json


""" Creates an AutoPilot pipeline with it's own chaining stages """

class AutoPilotPipeline(Pipeline):
    def __init__(self, assets: dict, assets_filepath: str, dialog_tree_filepath: str):
        super().__init__(assets, assets_filepath)
        self.assets = assets
        self.assets_filepath = assets_filepath
        self.dialogue_tree_filepath = dialog_tree_filepath

    # Write the branching-dialogue into seperate JSON file to display tree.
    def write_dialogue_tree_to_file(self, dialogue_tree):
        with open(self.dialogue_tree_filepath, 'w') as f:
            json.dump(dialogue_tree, f, indent=4)
        f.close()


    # Chaining pipeline stage 1
    def stage_1(self):
        # Get required input data from JSON file
        theme = self.assets['theme']
        details = self.assets['details']

        # Chain the data together in sequential order
        chain_1 = SequentialChain(chains=[storyline_chain, characters_chain], verbose=True, input_variables=["theme", "details"], output_variables=["storyline", "characters"])
        
        # Get AI model output response
        output = chain_1({'theme': theme, 'details': details})

        # Grab the values from the first chain that ran
        storyline = output['storyline']
        characters = output['characters']

        # Add assets to JSON file to be retrieved by other chains
        self.assets['storyline'] = storyline
        self.assets['characters'] = characters

        # Write the updated data back to the assets file
        self.write_data_to_file(self.assets)


    # Chaining pipeline stage 2
    def stage_2(self):
        # Get required input data from JSON file
        storyline = self.assets['storyline']
        characters = self.assets['characters']

        # Chain the data together in sequential order
        chain_2 = SequentialChain(chains=[backstories_chain], verbose=True, input_variables=["storyline", "characters"], output_variables=["backstories"])

        # Get AI model output response
        output = chain_2({'storyline': storyline, 'characters': characters})

        # Add assets to JSON file to be retrieved by other chains
        self.assets['backstories'] = output['backstories']
        
        # Write the updated data back to the assets file
        self.write_data_to_file(self.assets)


    # Chaining pipeline stage 3
    def stage_3(self):
        # Get required input data from JSON file
        backstories = self.assets['backstories']
        storyline = self.assets['storyline']

        # Chain the data together in sequential order
        chain_3 = SequentialChain(chains=[quests_chain], verbose=True, input_variables=["backstories", "storyline"], output_variables=["quests"])

        # Get AI model output response
        output = chain_3({'backstories': backstories, 'storyline': storyline})

        # Add assets to JSON file to be retrieved by other chains
        self.assets['quests'] = output['quests']
        
        # Write the updated data back to the assets file
        self.write_data_to_file(self.assets)


    # Chaining pipeline stage 4
    def stage_4(self):
        # Get required input data from JSON file
        quests = self.assets['quests']
        backstories = self.assets['backstories']

        # Chain the data together in sequential order
        chain_4 = SequentialChain(chains=[dialogue_chain], verbose=True, input_variables=["quests", "backstories"], output_variables=["dialogue"])

        # Get AI model output response
        output = chain_4({'quests': quests, 'backstories': backstories})

        # Add assets to JSON file to be retrieved by other chains
        self.assets['dialogue'] = output['dialogue']
        
        # Write the updated data back to the assets file
        self.write_data_to_file(self.assets)
    

    # Chaining pipeline stage 5
    def stage_5(self):
        # Get required input data from JSON file
        dialogue = self.assets['dialogue']
        quests = self.assets['quests']

        # Chain the data together in sequential order
        chain_5 = SequentialChain(chains=[items_chain, item_descriptions_chain], verbose=True, input_variables=["dialogue", "quests"], output_variables=["items", "item_descriptions"])

        # Get AI model output response
        output = chain_5({'dialogue': dialogue, 'quests': quests})

        # Add assets to JSON file to be retrieved by other chains
        self.assets['items'] = output['items']
        self.assets['item_descriptions'] = output['item_descriptions']
        
        # Write the updated data back to the assets file
        self.write_data_to_file(self.assets)


    # Chaining pipeline stage 6
    def stage_6(self):
        # Get required input data from JSON file
        dialogue = self.assets['dialogue']

        # Chain the data together in sequential order
        chain_6 = SequentialChain(chains=[dialogue_tree_chain], verbose=True, input_variables=["dialogue"], output_variables=["dialogue_tree"])

        # Get AI model output response
        output = chain_6({'dialogue': dialogue})

        # Add assets to JSON file to be retrieved by other chains
        dialogue_tree = output['dialogue_tree']
        
        # Conver the dialogue text into JSON format for branching-dialogue tree view
        self.write_dialogue_tree_to_file(dialogue_tree)


    # Execute the pipeline stages
    def run(self):
        # Run Chain 1
        self.stage_1()
        # Run Chain 2
        self.stage_2()
        # Run Chain 3
        self.stage_3()
        # Run Chain 4
        self.stage_4()
        # Run Chain 5
        self.stage_5()
        # Run Chain 6
        self.stage_6()
        # Display message once complete
        self.display_message()