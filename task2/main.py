from datasets import load_dataset


def get_number_of_questions_per_article(dataset):
    pass

def get_number_of_questions_per_question(dataset):
    pass

def get_number_of_free_form_answers(dataset):
    pass

def get_number_of_extractive_answers(dataset):
    pass

def get_number_of_unanswerable_questions(dataset):
    pass

def get_length_distribution_of_abstracts(dataset):
    pass

def exploratory_data_analysis(dataset):
    get_number_of_questions_per_article(dataset)
    get_number_of_questions_per_question(dataset)
    get_number_of_free_form_answers(dataset)
    get_number_of_extractive_answers(dataset)
    get_number_of_unanswerable_questions(dataset)
    get_length_distribution_of_abstracts(dataset)


def main():
    dataset = load_dataset("allenai/qasper")
    exploratory_data_analysis(dataset)


if __name__ == '__main__':
    main()