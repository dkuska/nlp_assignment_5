# NLP SoSe 2023 - Assignment 5 - Task 2

## Participants: Kevin Klein, David Kuska, Yorick Scheffer

## Question 2

- Question: Perform EDA on the train split and include
  - distribution of number of questions per article (i.e., how many articles have x number of questions, how many article have y number of questions, etc)
  - number of answers per question (notice that in the dataset, a question can have multiple answers associated with it)
  - the number of free-form answers in this split
  - the number of extractive answers in the training split
  - the number of unanswerable questions
  - the distribution of abstract lengths

## Question 3

- Question: Repeat step 2 for the test split.

## Question 6

- Set the maximum input length (i.e., concatenated question and abstract) to 128 and the maximum target length (i.e., answer sequence) to 32.  
- Do these maximum sequence values result in truncating a lot of your sequences?
- Hint: Use the EDA on length distribution from the step 2 for answering this.

## Question 10

- Question: For logging, store the train and validation loss values for each step to your Weights & Biases https://wandb.ai/site profile and provide us with these plots. You can simply provide us screenshots of these plots.

## Question 11

- Question: How does your model perform when answering? Does the output make sense? What do you think should be done for improving the prediction?