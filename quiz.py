import random

QUESTIONS = [
    {"question": "What is the capital of Denmark?", "answer": "copenhagen"},
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is the largest country by area?", "answer": "russia"},
    {"question": "What is the capital of Japan?", "answer": "tokyo"},
    {"question": "Which continent is Egypt in?", "answer": "africa"},
]


def run_quiz():
    shuffled = random.sample(QUESTIONS, len(QUESTIONS))
    score = 0

    for q in shuffled:
        guess = input(q["question"] + " ")
        if guess.strip().lower() == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The answer was {q['answer'].title()}.")

    print(f"\nYou scored {score}/{len(shuffled)}")


def main():
    print("Welcome to the Geo Quiz! Test your geography knowledge.\n")
    play_again = "y"
    while play_again == "y":
        run_quiz()
        play_again = input("\nPlay again? (y/n) ").strip().lower()


if __name__ == "__main__":
    main()
