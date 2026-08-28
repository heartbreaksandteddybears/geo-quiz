questions = [
    {"question": "What is the capital of Denmark?", "answer": "copenhagen"},
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is the largest country by area?", "answer": "russia"},
]

score = 0

for q in questions:
    guess = input(q["question"] + " ")
    if guess.strip().lower() == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The answer was {q['answer'].title()}.")

print(f"\nYou scored {score}/{len(questions)}")
