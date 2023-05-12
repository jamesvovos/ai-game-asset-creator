import os
from dotenv import load_dotenv
import requests
import time

# Get Leonardio.ai API key, User ID and Model ID from .env file
load_dotenv()
LEONARDO_AI_API_KEY = os.environ.get('LEONARDO_AI_API_KEY')
LEONARDO_AI_USER_ID = os.environ.get('LEONARDO_AI_USER_ID')


# NOTE: Create a Generation of Images

def generate_image(prompt: str, model_id: str):
    url = "https://cloud.leonardo.ai/api/rest/v1/generations"

    payload = {
    "prompt": prompt,
    "modelId": model_id,
    "presetStyle": "LEONARDO",
    "width": 512,
    "height": 512,
    "num_images": 1,
    "guidance_scale": 7,
    "public": False,
    "sd_version": "v2",
    "scheduler": "LEONARDO"
    }

    headers = {
    "Authorization": f"Bearer {LEONARDO_AI_API_KEY}",
    "content-type": "application/json",
    "accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    generation_id = response_json['sdGenerationJob']['generationId']
    
    # Give the URL enough time to populate
    time.sleep(10)
    image_url = get_image_by_id(generation_id)
    return image_url



# NOTE: Get ALL Image Generations by User ID, returns the URL to display image after creation.

def get_images_by_user_id():
    url = f"https://cloud.leonardo.ai/api/rest/v1/generations/user/{LEONARDO_AI_USER_ID}"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {LEONARDO_AI_API_KEY}"
    }

    response = requests.get(url, headers=headers)
    print(response.text)


# NOTE: Get Single Image by ID

def get_image_by_id(id: str):
    url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{id}"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {LEONARDO_AI_API_KEY}"
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()

    return response_json


# NOTE: Delete Single Image by ID

def delete_image_by_id(id: str):
    url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{id}"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {LEONARDO_AI_API_KEY}"
    }

    response = requests.delete(url, headers=headers)
    print(response.text)


# NOTE: Upscale Image by ID (Increase resolution & quality)

def upscale_image(id: str):
    url = "https://cloud.leonardo.ai/api/rest/v1/variations/upscale"

    payload = {"id": id}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {LEONARDO_AI_API_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

    


