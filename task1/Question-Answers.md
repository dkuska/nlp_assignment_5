# NLP SoSe 2023 - Assignment 5 - Task 1

## Participants: Kevin Klein, David Kuska, Yorick Scheffer

## Question 2 - Do you need to replace the padding token pad with the end of the sequence eos token? Why or why not?

- No, we don't need to do that. 
- If we were to do that, we would confuse the model in regards to handling of the padding token.
- It would introduce patterns that could negatively affect performance.

## Question 9 - What is the best validation loss you achieved after training? Describe your setup including final choices of hyper-parameters, optimizer, etc

- Best validation loss we achieved was 1.576270
- Final hyperparameters:
  - number of epochs: 12
  - batch size: 32
  - learning rate: 3e-4
  - weight decay: 0.001
  - learning rate scheduler type: cosine
  - optimizer: Adam

## Question 10 - Calculate the perplexity on validation and test splits and report them separately. Do you think there is a relationship between perplexity and cross-entropy?

- TODO

## Question 11 - As an explicit inference, use your model to predict the <mask> token in the following text (taken from ag news) and report the top 5 probable tokens predicted. Do you think these predictions make sense? Why or why not?

Predictions were: spam, attacks, threats, fraud, attack
These all make perfect sense, except for the last one which is in singular and not plural.
From the context the model was able to detect that it is in some way related to crime, which is very good.
