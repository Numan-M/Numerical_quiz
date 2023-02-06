# Numerical_quiz

This code creates a simple math quiz program that allows a user to answer 10 random questions. The questions can be Addition, Multiplication, or Subtraction and the numbers used for the calculation are randomly generated between 1 and 10.

### Classes

The code defines several classes:

* Question: The base class for all mathematical questions. It has two attributes: answer and text.
* Add, Multiply, Subtract: Subclasses of Question that generate a specific type of question (addition, multiplication, or subtraction).
* Quiz: The main class that manages the quiz. It generates the 10 random questions and allows the user to take the quiz.

### Quiz Method

* __init__: This method initializes an instance of the Quiz class and generates 10 random questions (Add, Multiply, or Subtract).
* take_quiz: This method starts the quiz and asks the user to answer each of the 10 questions. It also keeps track of the start and end time of the quiz.
* ask: This method asks a single question and returns a tuple of the form (correct, elapsed_time), where correct is a Boolean indicating whether the user's answer was correct and elapsed_time is the time taken by the user to answer the question.
* total_correct: This method returns the total number of correct answers.
* summary: This method prints a summary of the quiz, including the number of correct answers and the completion time.

## Running the Quiz

To run the quiz, simply run the script in the terminal. You will be asked 10 random questions, and after you have answered all of them, you will see a summary of your performance.

Requirements

    Python 3.x

## Usage

1. Clone the repository to your local machine.

```
$ git clone https://github.com/Numan-M/Numerical_quiz.git
```

2. Change your current directory to the newly cloned repository.

```
$ cd Numerical_quiz
```
3. Run the main python script.

```
$ python3 quiz.py
```

4. Follow the prompt and enter your answers.

5. Once you have answered all the questions, the application will display the results, including the number of correct answers and the total time taken to complete the quiz.

## Contributing

If you'd like to contribute to this project, please open an issue or a pull request with your suggestions.

## Contact:
* [LinkedIn](https://www.linkedin.com/in/numan-mahmood-197951242/)
