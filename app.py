from flask import Flask, render_template_string, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def init_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            progress INTEGER DEFAULT 0,
                            quiz_score INTEGER DEFAULT -1)''')
init_db()

lessons = [
    {"title": "Objective of the Game", "content": "The objective of American football is to score more points...", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/American_football_positions.svg/800px-American_football_positions.svg.png", "video": "https://www.youtube.com/embed/5YQ5oC_PZL8"},
    {"title": "Basic Rules", "content": "Each team has four downs (plays)...", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/NFL_down_marker_2010.jpg/640px-NFL_down_marker_2010.jpg", "video": "https://www.youtube.com/embed/-P3kT6gQ1i8"},
    {"title": "Positions", "content": "Key positions include quarterback...", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/American_football_positions_2.svg/800px-American_football_positions_2.svg.png", "video": "https://www.youtube.com/embed/7r9hEZkUYtU"},
    {"title": "Scoring", "content": "Touchdown: 6 points...", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Football_Field_Goalposts.jpg/640px-Football_Field_Goalposts.jpg", "video": "https://www.youtube.com/embed/CXJ1j3GxWDI"},
    {"title": "Field Layout", "content": "A football field is 100 yards...", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/American_Football_Field_diagram.svg/800px-American_Football_Field_diagram.svg.png", "video": "https://www.youtube.com/embed/QYvYm4D9OHk"}
]

quiz_questions = [
    {"question": "How many points is a touchdown worth?", "options": ["3", "6", "7", "2"], "answer": "6"},
    {"question": "What is the job of the quarterback?", "options": ["Tackle the runner", "Kick field goals", "Throw or hand off the ball", "Catch passes"], "answer": "Throw or hand off the ball"},
    {"question": "How many downs does a team get to advance 10 yards?", "options": ["2", "4", "3", "6"], "answer": "4"}
]

html_template = '''...'''  # Omitted for brevity (same as previous UI with login and lessons)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return render_template_string(html_template, session=session)
    username = session['username']
    with sqlite3.connect('users.db') as conn:
        user = conn.execute('SELECT progress, quiz_score FROM users WHERE username = ?', (username,)).fetchone()
    if user and user[1] == -1:
        return redirect(url_for('quiz'))
    index = int(request.form.get('lesson_index', user[0] if user else 0))
    index = max(0, min(index, len(lessons) - 1))
    with sqlite3.connect('users.db') as conn:
        conn.execute('UPDATE users SET progress = ? WHERE username = ?', (index, username))
    return render_template_string(html_template, lessons=lessons, lesson=lessons[index], current_index=index, session=session)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(quiz_questions):
            user_answer = request.form.get(f'q{i}')
            if user_answer == q['answer']:
                score += 1
        with sqlite3.connect('users.db') as conn:
            conn.execute('UPDATE users SET quiz_score = ? WHERE username = ?', (score, session['username']))
        return redirect(url_for('index'))
    quiz_form = '<h2>Quick Quiz</h2><form method="post">'
    for i, q in enumerate(quiz_questions):
        quiz_form += f'<p>{q["question"]}</p>'
        for option in q['options']:
            quiz_form += f'<input type="radio" name="q{i}" value="{option}"> {option}<br>'
    quiz_form += '<br><input type="submit" value="Submit Quiz"></form>'
    return quiz_form

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        with sqlite3.connect('users.db') as conn:
            try:
                conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return 'Username already exists.'
    return '''<form method="post"><h2>Register</h2>Username: <input name="username"><br>Password: <input type="password" name="password"><br><input type="submit"></form>'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('users.db') as conn:
            user = conn.execute('SELECT password FROM users WHERE username = ?', (username,)).fetchone()
            if user and check_password_hash(user[0], password):
                session['username'] = username
                return redirect(url_for('index'))
        return 'Invalid credentials.'
    return '''<form method="post"><h2>Login</h2>Username: <input name="username"><br>Password: <input type="password" name="password"><br><input type="submit"></form>'''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

