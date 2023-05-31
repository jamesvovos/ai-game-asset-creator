# AI 2D Game Asset Creator.
## _Generate 2D Game Assets utilising artificial intelligence, natural language processing and fine-tuned text-to-image deep learning models._

![DashboardImage](https://i.postimg.cc/prD74QKy/ui.png)

## Installation Guide
- OpenAI installation instructions [OpenAI docs](https://platform.openai.com/docs/api-reference?lang=python)
- LangChain installation instructions [LangChain website](https://python.langchain.com/en/latest/getting_started/getting_started.html)
- Streamlit installation instructions [Streamlit docs](https://streamlit.io/)
- Dotenv installation instructions [Dotenv docs](https://pypi.org/project/python-dotenv/)

## 1. Install OpenAI

Install OpenAPI:
```sh
pip install openai
```

Add your OpenAI API key to a `.env` file like so: `OPENAI_API_KEY=yourapikeyhere`.

## 2. Install LangChain

Install LangChain:
```sh
pip install langchain
```

## 3. Install Streamlit
Install Streamlit:
```sh
pip install streamlit
```

## 4. Install Dotenv

Install Dotenv:
```sh
pip install python-dotenv
```

## 5. Run the server

CD/ into the project directory and run the command:
```sh
streamlit run app.py
```

## Sample Responses:
![SampleOutputImage](https://i.postimg.cc/3JxCPCX6/ui2.png)
![SampleOutputImage2](https://i.postimg.cc/3Jk0XLCK/renders.png)

## Features

- Chain together LLM generated output via pipeline architecture in order to create 2D game assets such as quests, items, storyline, character dialogue, etc.
- Customise and fine-tune deeplearning text-to-image models to suit sylistic preferences.
- Export 2D generated assets created by simple prompts.


## .env 
Create a `.env` file in the root project directory. Add the following variables with their relevant API keys: `OPENAI_API_KEY`, `LEONARDO_AI_API_KEY`, `LEONARDO_AI_USER_ID`.
Refer to Leonardo AI's API documentation https://docs.leonardo.ai/reference
NOTE: WIP - Creating database & API to store data.

```sh
# API Keys
OPENAI_API_KEY=""
LEONARDO_AI_API_KEY=""
LEONARDO_AI_USER_ID=""
```

## License

MIT
