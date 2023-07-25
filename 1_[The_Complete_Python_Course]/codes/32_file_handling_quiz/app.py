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


correct_answers = 0
for question in questions:
    [ques, answer] = question.split("=")
    user_input = input(f"{ques}=")
    if user_input == answer:
        correct_answers += 1

results_file = open("result.txt", "w")
results_file.write(f"Your final score is {correct_answers}/{len(questions)}.")
results_file.close()
# print(correct_answers, incorrect_answers)
