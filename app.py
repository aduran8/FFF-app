from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your-secret-key"

lessons = [
    {"title": "Objective of the Game", "content": "The objective of American football is to score more points than the opposing team by advancing the ball into the opponent's end zone for a touchdown or kicking the ball through the opponent's goalposts for a field goal."},
    {"title": "Basic Rules", "content": "Each team has four downs (plays) to advance the ball 10 yards. If successful, they earn a new set of four downs. If not, the opposing team takes possession."},
    {"title": "Positions", "content": "Key positions include quarterback (throws or hands off the ball), running back (runs with the ball), wide receiver (catches passes), and linemen (block or tackle)."},
    {"title": "Scoring", "content": "Touchdown: 6 points. Extra point: 1 point (kick) or 2 points (conversion). Field goal: 3 points. Safety: 2 points."},
    {"title": "Field Layout", "content": "A football field is 100 yards long with end zones at each end. Yard lines and hash marks help track the ball's position."}
]

quiz_questions = [
    {"question": "How many points is a touchdown worth?", "options": ["3", "6", "1", "2"], "answer": "6", "lesson": "Scoring"},
    {"question": "What is the main job of a quarterback?", "options": ["Catch passes", "Kick field goals", "Tackle runners", "Throw or hand off the ball"], "answer": "Throw or hand off the ball", "lesson": "Positions"},
    {"question": "How long is a standard football field (excluding end zones)?", "options": ["50 yards", "100 yards", "120 yards", "80 yards"], "answer": "100 yards", "lesson": "Field Layout"},
    {"question": "What is a field goal worth?", "options": ["2 points", "3 points", "6 points", "1 point"], "answer": "3 points", "lesson": "Scoring"},
    {"question": "What is the objective of American football?", "options": ["Run the ball", "Score touchdowns or field goals", "Possession time", "Prevent injuries"], "answer": "Score touchdowns or field goals", "lesson": "Objective of the Game"},
    {"question": "How many downs does a team get to gain 10 yards?", "options": ["3", "2", "5", "4"], "answer": "4", "lesson": "Basic Rules"},
    {"question": "What happens if a team fails to advance 10 yards in 4 downs?", "options": ["2 more downs", "Field goal", "Opposing team gains possession", "Safety"], "answer": "Opposing team gains possession", "lesson": "Basic Rules"},
    {"question": "What is located at each end of the football field?", "options": ["Benches", "End zones", "Goal lines", "Stands"], "answer": "End zones", "lesson": "Field Layout"}
]

html_template = """<!DOCTYPE html>
<html>
<head>
    <title>Football Fundamentals</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 700px; margin: auto; padding: 20px; }
        h1 { text-align: center; }
        .card { border: 1px solid #ccc; border-radius: 12px; padding: 20px; margin-bottom: 20px; }
        .buttons { display: flex; justify-content: space-between; }
        button { padding: 10px 20px; border-radius: 8px; border: none; background-color: #007BFF; color: white; cursor: pointer; }
        button:disabled { background-color: #ccc; cursor: not-allowed; }
    </style>
</head>
<body>
    <h1>Learn the Fundamentals of American Football</h1>
    <div class="card">
        <h2>{{ lesson['title'] }}</h2>
        <p>{{ lesson['content'] }}</p>
    </div>
    <div class="buttons">
        <form method="post">
            <input type="hidden" name="lesson_index" value="{{ prev_index }}">
            <button type="submit" {% if current_index == 0 %}disabled{% endif %}>Previous</button>
        </form>
        <form method="post">
            <input type="hidden" name="lesson_index" value="{{ next_index }}">
            <button type="submit" {% if current_index == max_index %}disabled{% endif %}>Next</button>
        </form>
    </div>
    <div style="text-align:center; margin-top:30px;">
        <form action="{{ url_for('quiz') }}">
            <button type="submit" style="background-color:#28a745;">Start Quiz</button>
        </form>
    </div>
</body>
</html>"""

quiz_template = """<!DOCTYPE html>
<html>
<head>
    <title>Quiz</title>
    <style>
        body { font-family: Arial; max-width: 700px; margin: auto; padding: 20px; }
        .question { margin-bottom: 20px; }
        h1 { text-align: center; }
        input[type=submit] {
            padding: 10px 20px;
            background: #28a745;
            border: none;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
<h1>Football Quiz</h1>
<form method="post">
{% for i, q in enumerate(questions) %}
    <div class="question">
        <p><strong>{{ i+1 }}. {{ q.question }}</strong></p>
        {% for option in q.options %}
            <label><input type="radio" name="q{{ i }}" value="{{ option }}" required> {{ option }}</label><br>
        {% endfor %}
    </div>
{% endfor %}
    <input type="submit" value="Submit Quiz">
</form>
</body>
</html>"""

review_template = """<!DOCTYPE html>
<html>
<head>
    <title>Quiz Results</title>
    <style>
        body { font-family: Arial; max-width: 700px; margin: auto; padding: 20px; }
        h1 { text-align: center; }
        ul { padding-left: 20px; }
    </style>
</head>
<body>
<h1>Quiz Results</h1>
{% if review_lessons %}
    <p>You should review the following topics:</p>
    <ul>
        {% for lesson in review_lessons %}
            <li>{{ lesson }}</li>
        {% endfor %}
    </ul>
{% else %}
    <p>Excellent! You answered all questions correctly!</p>
{% endif %}
</body>
</html>"""

@app.route('/', methods=['GET', 'POST'])
def index():
    index = int(request.form.get('lesson_index', 0))
    index = max(0, min(index, len(lessons) - 1))
    return render_template_string(
        html_template,
        lesson=lessons[index],
        current_index=index,
        prev_index=max(0, index - 1),
        next_index=min(len(lessons) - 1, index + 1),
        max_index=len(lessons) - 1
    )

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        incorrect_lessons = set()
        for i, question in enumerate(quiz_questions):
            user_answer = request.form.get(f"q{i}")
            if user_answer != question['answer']:
                incorrect_lessons.add(question['lesson'])
        session['quiz_results'] = list(incorrect_lessons)
        return redirect(url_for('review'))
    return render_template_string(quiz_template, questions=quiz_questions)

@app.route('/review')
def review():
    review_lessons = session.get('quiz_results', [])
    return render_template_string(review_template, review_lessons=review_lessons)

if __name__ == '__main__':
    app.run(debug=True)