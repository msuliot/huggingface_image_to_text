from transformers import pipeline

import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file
pipeline_task = os.getenv('PIPELINE_TASK') # pipeline task for huggingface.co in .env file
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def hf_pipeline(image_path):
    pipe = pipeline(pipeline_task, model=model_name, max_new_tokens=100)
    output = pipe(image_path)
    return output


def main():
    image_path = "images/10.jpg"
    return_value = hf_pipeline(image_path)
    print(return_value)


if __name__ == "__main__":
    main() 