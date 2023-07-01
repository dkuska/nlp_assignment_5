# TODOs

1. Load the QASPER dataset: dataset = load_dataset("allenai/qasper")
The dataset comes with train and test splits. Print the first sample from the train split and famil-
iarize yourself with the structure of this dataset. Notice the nested structure of the data where on
the first level, you have the id, title, abstract, qas and other attributes. In the second level,
e.g., under the qas attribute, you see for example question, answers. On the third level, e.g.,
under answers, you should be able to see unanswerable, extractive_spans, free_form_answer
and other attributes.
You will be mainly working with the qas and abstract features in this task.

2. (6 points) Perform an explanatory data analysis (EDA) on the train split of the dataset. Your
EDA should include the distribution of number of questions per article (i.e., how many articles
have x number of questions, how many article have y number of questions, etc), the average
number of answers per question (notice that in the dataset, a question can have multiple answers
associated with it), the number of free-form answers in this split, the number of extractive
answers in the training split, the number of unanswerable questions, and the distribution of
abstract lengths. You can use assignments 1 and 2 from the beginning of the semester to get
inspired.

3. (4 points) Repeat step 2 for the test split.

4. (10 points) For the open-book QA task, T5 expects the inputs to be in the form of:
question: {q} context: {c}
For example, for the question “what are the main contributions in this paper?” from a paper
with the abstract “This paper is proposing the S55-dummy model in order to solve question
answering.”, the final input text for T5 should be:
“question: what the main contributions in this paper? context: This paper is proposing
S5-dummy model in order to solve question answering.”1 .
In this task, we will be using the abstract sections of papers as contexts. Notice that we have
multiple questions for each paper and therefore, each abstract. So, the same abstract must be
used for each of the questions from the same article.
Furthermore, some questions can have multiple answers associated to them. For simplicity, ran-
domly select just one answer as the ground truth in these cases. Notice that for extractive
questions, the answer is provided by the:
1These examples are synthetically generated and not real.
sample[’qas’][’answers’][’answer’][’extractive spans’]
.
In contrast, for the free-form questions, the answer is provided by the:
sample[’qas’][’answers’][’answer’][’free form answer’].
You can treat both cases simply as answers, regardless of extractive or free-form types.
In this step, you will be flattening the hierarchical structure of the dataset so that parallelism
of the text pre-processing function on the dataset becomes possible. You can use the following
structure for flattening. You can also propose other structures if you want. :)
Perform flattening for both train and test splits.
train = { ' abstract ' : train abstracts , ' question ' : train questions ,
' answer ' : t r a i n a n s w e r s }
test = { ' abstract ' : test abstracts , ' question ' : test questions ,
' answer ' : t e s t a n s w e r s }
t r a i n d a t a s e t = d a t a s e t s . Dataset . f r o m d i c t ( t r a i n )
t e s t d a t a s e t = d a t a s e t s . Dataset . f r o m d i c t ( t e s t )
f l a t t e n e dd a t a s e t = datasets . DatasetDict (
{ ' train ' : train dataset ,
' t e s t ' : t e s t d a t a s e t } )
Notice that the lengths of the abstracts collection and questions and answers should be the same,
i.e.,:
a s s e r t len ( t r a i n a b s t r a c t s ) == len ( t r a i n q u e s t i o n s )
len ( t r a i n a b s t r a c t s == len ( t r a i n a n s w e r s )
The same condition applies for the test split. The goal is to have a 1:1:1 relationship between
abstract:question:answer for simplicity.

5. (2 points) From this step, you should be only working with your flattened dataset. Randomly
choose 10% of the train split to be used as the validation set.

6. (10 points) Define your pre-processing function. Set the maximum input length (i.e., concate-
nated question and abstract) to 128 and the maximum target length (i.e., answer sequence) to 32.  
Do these maximum sequence values result in truncating a lot of your sequences? Hint: Use
the EDA on length distribution from the step 2 for answering this.
Notice that since we are working with an encoder-decoder model here, you need to tokenize,
truncate and pad the input sequence, i.e., question: {question} context: {abstract}, as
well as the output sequence, i.e., answer.
Note: Choice of 128 and 32 for sequence lengths is due to GPU resource limitations. Longer
sequences might result in out of memory issues.

7. (2 points) Apply the pre-processing function to all of the data using the HuggingFace Dataset
map function.

8. (2 points) Load the google/t5-efficient-tiny model with pre-trained weights. For the
generative QA task, you need to use T5ForConditionalGeneration. Different versions of T5
checkpoints with different numbers of parameters are publicly available for you to use, e.g., this
link provides all the pre-trained checkpoints provided by Google. Due to the GPU resource
limitations on the Kaggle notebook, we encourage you to use the tiny model.

9. (10 points) Define your Seq2SeqTrainingArguments2 with learning rate scheduling and weight
decay. Notice that this task requires many more calculations as well as GPU memory in com-
parison to all the tasks you have experienced so far in this course. Therefore, you are required
to carefully follow the instructions provided by HuggingFace in this link for efficient training.
Otherwise, you might encounter CUDA Out Of Memory errors, which means that training your
model requires more virtual RAM than you have on your notebook, i.e., 16GB if you’re using a
single GPU on Kaggle.
Hint: You might even need to set your batch size to 1. But what can you do to still reach a
larger effective batch size? The HuggingFace tips should help you with the answer!

10.  (10 points) Define your Seq2SeqTrainer. Choose the best model on the validation set, i.e.,
the model achieving the best loss value. You do not have to reach a specific performance goal
for this task. It is rather about building an understanding of how the text generation procedure
happens using T5. However, a validation loss value higher than 2.5 after 3 epochs potentially
means things are not working as intended!
For logging, store the train and validation loss values for each step to your Weights & Biases
https://wandb.ai/site profile and provide us with these plots. You can simply provide us
screenshots of these plots.
Optional: You can use the BLEU score for evaluating the sequence generation performance on
the validation set. That means, you can define compute_metrics to return BLUE scores using
the evaluate library from HuggingFace. Notice that BLEU from evaluate requires to strings
as inputs. But the outcome of your model is a sequence of token id. Therefore, you would need
to decode them using your tokenizer and generate the text string first.
Note: If you’re using the Kaggle notebook, make sure to check out this tutorial on how to add
your wandb API key to the Kaggle environment.

11.  (4 points) As an example inference, select a single sample from the test split of your flattened
dataset and use your model for the question answering task. Notice that the outcome of your
model is a sequence of token id and you need to use your tokenzier for decoding these ids, i.e.,
converting each id to a token using the vocabulary. You are free to choose any sample from the
test split.
Explain your observations. How does your model perform when answering? Does the output
make sense? What do you think should be done for improving the prediction?
Note: The goal here is that you start critical thinking about your results and try to analyze
3what your results mean . Even if you get empty strings generated by your model, start thinking
about potential issues, suspect what could be improved, what more does the model need for
better predictions, etc. In research, we often times have an iterative process of analysing results
and implementing for improving until we achieve reasonable observations! :)