from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

SAVE_PATH = "saved_model"

print("Downloading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

print("Downloading model...")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME
)

###################################################
# SAVE LOCALLY
###################################################

tokenizer.save_pretrained(SAVE_PATH)

model.save_pretrained(SAVE_PATH)

print("Model saved successfully!")