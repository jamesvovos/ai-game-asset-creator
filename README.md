# ChatGPT NPC Creator.
## _Create and train NPC characters using ChatGPT - output dialogue and conversation based on what you've said._

![DashboardImage](https://i.postimg.cc/kMRZxxPS/streamlit.png)

## Installation Guide
- OpenAI installation instructions [OpenAI docs](https://platform.openai.com/docs/api-reference?lang=python)
- LangChain installation instructions [LangChain website](https://python.langchain.com/en/latest/getting_started/getting_started.html)
- Streamlit installation instructions [Streamlit docs](https://streamlit.io/)

## 1. Install OpenAI

Install FastAPI:
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

## 4. Run the server
CD/ into the project directory and run the command:
```sh
streamlit run app.py
```

## Sample Response:
![SampleOutputImage](https://i.postimg.cc/HLf0H8vG/output.png)

## Features

- Chain together NPC character training tasks by feeding ChatGPT AI model via API and LangChain.
- Customise AI text-to-speech responses including: tone, personality, name, voice, etc.
- Export NPC character to game engines such as Unity or UE5, have text-to-text or speech-to-text conversations with them.


## Customize
Modify the `characters.json` file to change attributes such as `name`, `description`, `voice`, `mood`, `actions`, `knowledge` and `hobbies` for your NPC character.
NOTE: WIP - Creating database & API to store data.

```sh
{
    "name": "Gandalf the Great",
    "description": "a powerful and wise wizard in Middle-earth. He is tall, thin, with a long white beard and hair, and carries a staff and wears a pointed hat. Gandalf is a skilled warrior, strategist, and master of magical spells. He is known for his wisdom, compassion, and love of fireworks, and plays a key role in the fight against the evil of Sauron",
    "voice": "Microsoft Azure",
    "mood": "happy",
    "actions": [
        "light fireworks",
        "put on wizard hat",
        "shout full of a took!"
    ],
    "knowledge": [
        "has an evil enemy named Sauron, that he despises",
        "needs help defeating a dragon on his farm",
        "magical glyphs sell for 300 gold each"
    ],
    "hobbies": [
        "lighting fireworks",
        "exploring middle earth",
        "casting magical spells"
    ]
}
```

## License

MIT
