# from transformers import pipeline
# from transformers import AutoProcessor, AutoModelForSeq2SeqLM , TFAutoModelForSeq2SeqLM

# import os
# from dotenv import load_dotenv
# load_dotenv()
# hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
# model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file
# pipeline_task = os.getenv('PIPELINE_TASK') # pipeline task for huggingface.co in .env file
# os.environ['TOKENIZERS_PARALLELISM'] = 'true'


# def hf_local(image_path):
#     # This will download the model and tokenizer to your local machine and run on your local machine. 
#     # saved and cached ~/.cache/huggingface
#     processor = AutoProcessor.from_pretrained(model_name) # return_tensors="pt" or "tf"
#     model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
#     pipe = pipeline("image-to-text", model=model, processer=processor)
#     output = pipe(image_path)
#     return output


# def main():
#     image_path = "images/10.jpg"
#     return_value = hf_local(image_path)
#     print(return_value)


# if __name__ == "__main__":
#     main() 