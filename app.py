from flask import Flask, render_template_string, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string(home_template)


lessons = [
    {
        "title": "American Football: The Objective of the Game",
        "content": "The overall objective of American football is to score more points than the opposing team by advancing the ball into the opponent's end zone or kicking field goals into the opponent goal posts (sometimes referred to as 'uprights'). There are other ways one can score points as well; through defense, or special teams plays that do not include field goals. The sport of American football varies only a little depending on the level that it is played;"
        "whether it is high school, college, or at the professional level. The concept of it does not change, there are only a few changes as the level of complexity grows.",
    },
    {
        "title": "A Brief Overview of the Basics of the Game: Courtesy of the NFL",
        "video": "https://www.youtube.com/embed/3t6hM5tRlfA"
    },
    {
        "title": "The Basic Rules of Football",
        "content": "Each team has four downs (or also referred to as 'plays') to advance the ball 10 yards. If successful, they earn a new set of downs; otherwise, the other team gains possession of the ball, at the location of where the team with the ball failed to gain 10 yards."
        "Once a team has achieved a first down after passing the opponent's 10 yard line, there is no opportunity to achieve a fresh set of downs. The term '1st & Goal' then comes into play. Followed by '2nd & Goal', and so forth. Usually, if a team is facing a '4th & Goal' situation, the team will elect to kick a field goal."

    },
    {
        "title": "The Different Positions of Football",
        "content": "Football players are grouped into either offense, defense, and/or special teams. Normally, a player plays either offense or defense, it is uncommon for a specific player to play both sides of the ball.  There are a total of 11 players for all three sections of the game; any more than that results in a penalty to the team with 11 players. The position on offense include quarterback, running back, wide receiver, offensive linemen, and defensive backs.",
        "video": "https://www.youtube.com/embed/kT5ZRsCd3yE"
    },
    {
        "title": "Scoring",
        "content": "Scoring a Touchdown awards a team 6 points. Extra point (kick): 1 point. Two-point conversion: 2 points. Field goal: 3 points. Safety: 2 points.",
        "video": "https://www.youtube.com/embed/hy8aStpWmGo"
    },
    {
        "title": "Field Layout",
        "content": "A football field is 100 yards long (120 when you include the two 10-yard end zones). Yard lines and hash marks divide the field for precise positioning.",
        "video": "https://www.youtube.com/embed/pvNq2V_EzH0"
    },
    {
        "title": "Offensive Formations",
        "content": "Common offensive formations include the I-Formation, Shotgun, and Spread. These affect play options and spacing.",
        "video": "https://www.youtube.com/embed/oRpZ3nJhgyw"
    },
    {
        "title": "Defensive Formations",
        "content": "Typical formations like 4-3, 3-4, and Nickel adjust the number of linemen and backs based on pass/run defense strategy.",
        "video": "https://www.youtube.com/embed/Jd3yP_lfV40"
    }
]

template = """


<!DOCTYPE html>
<html>
<head>
    <title> FFF (Fun Fundamentals of Football)</title>
    <style>
        body {
            font-family: Varsity, sans-serif;
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #0b6623;
            color: white;
        }
        h1 { text-align: center; }
        .card {
            border: 1px solid #ccc;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: #14532d;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
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
        iframe {
            width: 100%;
            height: 360px;
            border: none;
            margin-top: 20px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <h1>FFF (Fun Fundamentals of Football)</h1>
    <div class="card">
        <h2>{{ lesson['title'] }}</h2>
        <p>{{ lesson['content'] }}</p>
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
home_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Football Fundamentals - Home</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: auto;
            padding: 40px;
            background-color: #0b6623;
            color: white;
            text-align: center;
        }
        h1 { font-size: 36px; margin-bottom: 10px; }
        p { font-size: 18px; }
        a.button {
            display: inline-block;
            margin-top: 30px;
            padding: 12px 24px;
            background-color: #007BFF;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-size: 18px;
        }
        a.button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Welcome to Football Fundamentals</h1>
    <p>Learn the basics of American football, one step at a time — including scoring, rules, positions, and formations.</p>
    <a href="{{ url_for('index') }}" class="button">Start Learning</a>
</body>
</html>
"""


@app.route("/lessons", methods=["GET", "POST"])
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
