from transformers import (
    AutoModelForMaskedLM,
    AutoTokenizer,
    pipeline
)

model_checkpoint = "distilroberta-base"
path_to_model = './model/'

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForMaskedLM.from_pretrained(path_to_model)

### Task 10
### TODO:

### Task 11
text = "E-mail scam targets police chief Wiltshire Police warns about <mask> after its fraud squad chief was targeted."
unmasker = pipeline('fill-mask', tokenizer=tokenizer, model=model)
for i, result in enumerate(unmasker(text)):
    print(f"Prediction #{i+1} - {result['token_str']} - score: {result['score']:.4f}")
