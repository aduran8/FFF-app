from flask import Flask, render_template_string, request, url_for

app = Flask(__name__)

lessons = [
    {
        "title": "Objective of the Game",
        "content": "The objective of American football is to score more points than the opposing team...",
        "image": "objective.jpg",
        "video": "https://www.youtube.com/embed/AkU-_i-NThk"
    },
    {
        "title": "Basic Rules",
        "content": "Each team has four downs to advance the ball 10 yards...",
        "image": "rules.jpg",
        "video": "https://www.youtube.com/embed/cL4uhaQ58Rk"
    },
    {
        "title": "Player Positions",
        "content": "Key positions include quarterback, running back, wide receiver...",
        "image": "positions.jpg",
        "video": "https://www.youtube.com/embed/kT5ZRsCd3yE"
    },
    {
        "title": "Scoring",
        "content": "Touchdown: 6 points. Extra point: 1 or 2. Field goal: 3. Safety: 2.",
        "image": "scoring.jpg",
        "video": "https://www.youtube.com/embed/hy8aStpWmGo"
    },
    {
        "title": "Field Layout",
        "content": "A football field is 100 yards long with two 10-yard end zones.",
        "image": "field.jpg",
        "video": "https://www.youtube.com/embed/pvNq2V_EzH0"
    },
    {
        "title": "Offensive Formations",
        "content": "Offensive formations like the I-Formation, Shotgun, and Spread are used to space out defenders and create advantages in blocking or passing.",
        "image": "offense.jpg",
        "video": "https://www.youtube.com/embed/oRpZ3nJhgyw"
    },
    {
        "title": "Defensive Formations",
        "content": "Common defensive formations include the 4-3, 3-4, and Nickel. These vary in how many linemen and linebackers are used to defend the run or pass.",
        "image": "defense.jpg",
        "video": "https://www.youtube.com/embed/Jd3yP_lfV40"
    }
]

template = """
<!DOCTYPE html>
<html>
<head>
    <title>Football Fundamentals</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 20px; }
        h1 { text-align: center; }
        .card { border: 1px solid #ccc; border-radius: 12px; padding: 20px; margin-bottom: 20px; }
        .buttons { display: flex; justify-content: space-between; margin-top: 20px; }
        button {
            padding: 10px 20px;
            border-radius: 6px;
            border: none;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
        }
        button:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
        img { max-width: 100%; margin: 20px 0; border-radius: 8px; }
        iframe { width: 100%; height: 360px; border: none; margin-top: 10px; border-radius: 8px; }
    </style>
</head>
<body>
    <h1>Football Fundamentals</h1>
    <div class="card">
        <h2>{{ lesson['title'] }}</h2>
        <p>{{ lesson['content'] }}</p>
        {% if lesson['image'] %}
            <img src="{{ url_for('static', filename=lesson['image']) }}" alt="Lesson image">
        {% endif %}
        {% if lesson['video'] %}
            <iframe src="{{ lesson['video'] }}" allowfullscreen></iframe>
        {% endif %}
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
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    index = int(request.form.get("lesson_index", 0))
    index = max(0, min(index, len(lessons) - 1))
    return render_template_string(
        template,
        lesson=lessons[index],
        current_index=index,
        prev_index=max(0, index - 1),
        next_index=min(len(lessons) - 1, index + 1),
        max_index=len(lessons) - 1
    )

if __name__ == "__main__":
    app.run(debug=True)