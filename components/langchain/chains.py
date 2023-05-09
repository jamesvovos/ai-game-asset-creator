import os
from dotenv import load_dotenv
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from .templates import storyline_template, characters_template, backstories_template, quests_template, dialogue_template, items_template, item_descriptions_template, dialogue_tree_template

# get ChatGPT API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LLMS

#OpenAI
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
# API model costs: https://openai.com/pricing

# NOTE: Chain 1

storyline_chain = LLMChain(
    llm=llm,
    prompt=storyline_template,
    verbose=True,
    output_key="storyline"
)

characters_chain = LLMChain(
    llm=llm,
    prompt=characters_template,
    verbose=True,
    output_key="characters"
)

# NOTE: Chain 2

backstories_chain = LLMChain(
    llm=llm,
    prompt=backstories_template,
    verbose=True,
    output_key="backstories"
)

# NOTE: Chain 3

quests_chain = LLMChain(
    llm=llm,
    prompt=quests_template,
    verbose=True,
    output_key="quests"
)

# NOTE: Chain 4

dialogue_chain = LLMChain(
    llm=llm,
    prompt=dialogue_template,
    verbose=True,
    output_key="dialogue"
)

# NOTE: Chain 5

items_chain = LLMChain(
    llm=llm,
    prompt=items_template,
    verbose=True,
    output_key="items"
)

item_descriptions_chain = LLMChain(
    llm=llm,
    prompt=item_descriptions_template,
    verbose=True,
    output_key="item_descriptions"
)

# NOTE: Chain 6

dialogue_tree_chain = LLMChain(
    llm=llm,
    prompt=dialogue_tree_template,
    verbose=True,
    output_key="dialogue_tree"
)