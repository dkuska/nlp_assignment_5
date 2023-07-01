# TODOs

1. (2 points) Load the train and test splits from ag_news. Randomly select 10% of the training
set as validation.

2. (3 points) Prepare your data pipeline including the text pre-processing. Set the maximum
sequence length to 256. Do you need to replace the padding token pad with the end of the
sequence eos token? Why or why not?

3. (2 points) Apply your pre-processing function to all data in all splits using the HuggingFace
Dataset map function. Are there any columns in the ag_news dataset that is not required for the
MLM task? If yes, remove it by defining it in the remove_columns in the map function.

4. (4 points) Define the suitable data collator for MLM with a masking probability of 0.1.

5. (2 points) Load the distilroberta-base model with pre-trained weights.

6. (2 points) If you print the model, you notice that it has 6 layers in its encoder module. Each
of these layers has an attention, intermediate and output layer. Update the dropout prob-
ability of the output layer in each of the 6 encoder layers (from 0.1) to 0.15.
Hint: You can do this by either using torch.nn.Dropout or updating the pre-trained Hugging-
Face config for your model.

7. (5 points) Define the TrainingArguments with learning rate scheduler and weight decay.

8. (5 points) Define the Trainer with your updated model, training arguments, train and valida-
tion splits, and the data collator you defined in step 4.

9. (5 points) Train the model and try to tune the hyper-parameters, e.g., batch size, number of
epochs, weight decay and learning rate. You do not have to reach a specific performance goal
for this task. It is rather about building an understanding of how to perform masked language
modeling. Although, a validation loss of more than 0.3 after epoch 3 means that things are
probably not working as intended.
What is the best validation loss you achieved after training? Describe your setup including final
choices of hyper-parameters, optimizer, etc.

10. (5 points) Select the best model from step 7 where the minimum validation loss is achieved.
Calculate the perplexity on validation and test splits and report them separately. Do you think
there is a relationship between perplexity and cross-entropy?
Hint: HuggingFace’s tutorial on perplexity can help you! :)

11. (5 points) As an explicit inference, use your model to predict the <mask> token in the following
text (taken from ag news) and report the top 5 probable tokens predicted. Do you think these
predictions make sense? Why or why not?
text = "E-mail scam targets police chief Wiltshire Police warns about <mask> after
its fraud squad chief was targeted."
