from datasets import (
    load_dataset, 
    DatasetDict, 
)
import torch
from typing import Dict, Any
from transformers import (
    AutoModelForMaskedLM,
    AutoTokenizer,
    DataCollatorForLanguageModeling,
    TrainingArguments, 
    Trainer,
    pipeline
)

model_checkpoint = "distilroberta-base"
path_to_model = '/models/'

tokenizer = AutoTokenizer().from_pretrained(model_checkpoint)
model = AutoModelForMaskedLM().from_pretrained(path_to_model)

### Task 10
### TODO:

### Task 11
### TODO:
text = "E-mail scam targets police chief Wiltshire Police warns about <mask> after its fraud squad chief was targeted."