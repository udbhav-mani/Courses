"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

questions_file = open("questions.txt", "r")
questions = questions_file.read().split("\n")
questions_file.close()

questions_list = list()
for question in questions:
    question = question.split("=")
    questions_list.append(question)

correct_answers = 0
incorrect_answers = 0
for question in questions_list:
    user_input = int(input(f"{question[0]} = "))
    if user_input == int(question[1]):
        correct_answers += 1
    else:
        incorrect_answers += 1

results_file = open("results.txt", "w")
results_file.write(f"Your final score is {correct_answers}/{incorrect_answers}.")
# print(correct_answers, incorrect_answers)
