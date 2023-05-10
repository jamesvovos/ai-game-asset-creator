import os
from dotenv import load_dotenv
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from .templates import quest_template, dialogue_template, objectives_template, items_template, items_details_template

# get ChatGPT API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LLMS

#OpenAI
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
# API model costs: https://openai.com/pricing

# NOTE: Chain 1

quest_chain = LLMChain(
    llm=llm,
    prompt=quest_template,
    verbose=True,
    output_key="quest"
)

dialogue_chain = LLMChain(
    llm=llm,
    prompt=dialogue_template,
    verbose=True,
    output_key="dialogue"
)

objectives_chain = LLMChain(
    llm=llm,
    prompt=objectives_template,
    verbose=True,
    output_key="objectives"
)

items_chain = LLMChain(
    llm=llm,
    prompt=items_template,
    verbose=True,
    output_key="items"
)

items_details_chain = LLMChain(
    llm=llm,
    prompt=items_details_template,
    verbose=True,
    output_key="items_details"
)