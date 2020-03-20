from IPython.display import Image
import numpy as np
from scipy.stats import pearsonr


def answer_one(your_answer):
    '''
    your answer should be a list of letters a to e
    '''
    if your_answer == ["using the train results, the best model is the matrix factorization model"]:
        print("That's right - lower RMSEs are best.  The lowest training RMSE can be found in relation to the matrix factorization recommender, which makes it the best.  However, the best training score doesn't mean this is the model we should use in production necessarily!")
        return Image(filename='../../../images/you_right.png')

    else:
        print("Sorry, that's not correct.  Actually only one of the above statements is true.  Try to figure out which one!")


def answer_two(your_answer):
    '''
    your answer should be a list of letters a to d
    '''
    if your_answer == ["using the test results, the best model is the popularity model", "the recommender that works best for the test data is the one we should use in the real world"] or your_answer = ["using the test results, the best model is the popularity model"]:
        print("That's right the popularity model performed best in relation to the test data.  You could argue that the recommender that performed best with the test data should be used, or that we should do more rigorous testing with cross-validation to determine which model goes to production.  Eitherway, more testing should be done once the model is in production.")
        return Image(filename='../../../images/you_right.png')

    else:
        print("Sorry, that's not correct.  Remember the model with the lowest RMSE is best.")


def answer_three(your_answer):
    '''
    your answer should be a list of letters a to d
    '''
    
