import random

from flask import Flask, render_template, request

app = Flask(__name__)

QUESTIONS = [
    {"question": "What is the capital of Denmark?", "answer": "copenhagen"},
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is the largest country by area?", "answer": "russia"},
    {"question": "What is the capital of Japan?", "answer": "tokyo"},
    {"question": "Which continent is Egypt in?", "answer": "africa"},
]


@app.route("/")
def index():
    shuffled = random.sample(QUESTIONS, len(QUESTIONS))
    return render_template("quiz.html", questions=shuffled)


@app.route("/submit", methods=["POST"])
def submit():
    score = 0
    total = 0

    while f"answer_{total}" in request.form:
        guess = request.form[f"answer_{total}"].strip().lower()
        correct = request.form[f"correct_{total}"]
        if guess == correct:
            score += 1
        total += 1

    percentage = round(score / total * 100)
    return render_template("result.html", score=score, total=total, percentage=percentage)


if __name__ == "__main__":
    app.run(debug=True)
