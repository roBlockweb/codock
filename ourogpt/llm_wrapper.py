import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from .config import Config

class LLMWrapper:
    def __init__(self, model_path=None):
        self.model_path = model_path or Config.MODEL_PATH
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        if os.path.exists(self.model_path):
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_path).to(self.device)
        else:
            # fallback to small model
            self.tokenizer = AutoTokenizer.from_pretrained('distilgpt2')
            self.model = AutoModelForCausalLM.from_pretrained('distilgpt2').to(self.device)

    def generate(self, prompt, max_tokens=100):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt').to(self.device)
        output = self.model.generate(inputs, max_length=max_tokens+len(inputs[0]), do_sample=True)
        text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return text[len(prompt):].strip()
