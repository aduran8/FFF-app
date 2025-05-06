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
        "content": "Football players are grouped into either offense, defense, and/or special teams. Normally, a player plays either offense or defense, it is uncommon for a specific player to play both sides of the ball.  There are a total of 11 players for all three sections of the game; any more than that results in a penalty to the team with more than 11 players on their side of the field."

    },
    {
        "title": "Offense - The Different Positions",
        "content": "There are a total of 11 players on the offense side of the ball. The way one can tell that the offense is on the field is because they are the side that have posession of the football, and are trying to score. "
        "The list of players go as follows: "
        "   -Quarterback: The 'captain' on the offense, in charge of taking the snap from the center and throwing the football to either wide receivers, tights ends, or running backs."
        "   -Fullback: This player lines up behind the quarterback. Sometimes this player will be given the ball from the quarterback on a run play, but their role is to typically serve as a blocker to the quarterback and/or the halfback."
        "   -Halfback: This player lines up behind the fullback and is responsible for running the ball when the quarterback hands them the ball. There are occasions where the running back will go past the line of scrimmage and try to catch a pass from the quarterback.There are also scenarios where the running back will protect the quarterback from players on defense that try to get to the quarterback"
        "   -Wide Receiver: This player is usually the fastest player on the offensive side of the ball. There are always two of these players (sometimes three) line up on different ends of their side of the ball. These players line up furthest from the ball to run routes to try and catch passes from the quarterback; whether they are short passes or long passes, their objective is to run and catch the ball."
        "   -Tight End: This player is similar to the wide receiver, but the only difference about these players is that they are taller and stronger than the receivers. They typically don't have to be fast, because sometimes their objective on the field is to serve as a blocker to either the quarterback or a running back running down the field."
        "   -Left Tackle: This player lines up on the left side of the football. They protect what is known as the 'blind-side' of a quarterback. One of the five positions on the line of scrimmage that is responsible for protecting the quarterback. All lineman tend to be big, tall, and muscular. It is preferred that they be somewhat fast in order to prevent fast defenders from reaching the quarterback."
        "   -Left Guard: Lineman 2 of 5. This player lines up between the left tackle and the center. They are typically smaller than the two offensive tackles on the field, but they also serve to protect the quarterback."
        "   -Center: Lineman 3 of 5. Arguably, the most important lineman. This player is responsible of 'snapping' the ball to the quarterback. This player is usually 'the brain' on the line because they communicate to the quarterback what they are seeing on the defensive line."
        "   -Right Guard: This player serves the same purpose as the left guard on the offensive line, the only difference is that they are lined up on the right side of the football."
        "   -Right Tackle: Lineman 5 of 5. Same rules apply to the right tackle and the left tackle, but some see their responsibility to be a little less, because the quarterback can usually see what is happening on the right side of the field when trying to throw the football."
    },
     {
        "title": "Defense - The Different Positions... On the other side of the Ball",
        "content": "There are a total of 11 players on the defensive side of the ball. They are on the opposite side of the football. Their goal is to stop the offense from advancing the ball down the field and scoring points. If done well enough, the defense can score points as well, if they manage to take the ball away from the offense. "
        "The list of players go as follows: "
        "   -Cornerback: The role of this player is to defend the wide receivers. They also have to be fast, in order to be able to keep up with the receivers. Their objective is to try and prevent receivers from catching the ball. If played well enough, they can intercept a throw from the quarterback and allow the offense from his team to try and score. There are always at least 2 cornerbacks lined up on the field. "
        "   -Safety: The safety positon is somewhat similar to what the cornerback does, the only difference is that they are not 'assigned' to guard a specific position. Their role is more for them to guard wherever the ball may be headed. Typically, a safety will take on the role of guarding the tight end position player. There are always 2 safeties on the field as well. Safeties do not have to be as fast as the cornerbacks, but are usually fast. Both cornerbacks and safeties are referred to as 'defensive backs'. "
        "   -Middle Linebacker: There is only one middle linebacker on the field, and they are typically the 'unofficial captain' on the field. The player in this position is usually the one who is communicating to the other players on defense to point out anything they are seeing from the offense on the field. Middle linebackers are usually strong and fast; they are assigned to protect the short passes from the offense. "
        "   -Outside Linebacker: The role of this player is to guard the areas in which the tight end can catch passes. There are always 2 outside linebackers, and they sometimes come down to try and get to the quarterback. Outside linebackers are usually not that big, not that fast, but they do tend to be strong."
        "   -Defensive End: There are two defensive ends on the defense. Each one lines up against the left tackle and the right tackle. The role of this player is to try and get to the quarterback, or 'stuff' the line of scrimmage to prevent runningbacks from gaining yards. Defensive ends are usually lean, but muscular; they are usually very fast, but not as fast as defensive backs. "
        "   -Defensive Tackle: The same as defensive ends, there are also 2 DT's on the defensive side of the field. The players filling this role are typically tall, big, and muscular players. Their job is to prevent the runningback from gaining yardage, and to disrupt the offensive line. On some occasions, the defensive tackles get to the quarterback, but ultimately, it is not really their job. "
    },
         {
        "title": "Special Teams - The Not So Man ",
        "content": "There are a total of 11 players from each team on the field. When it comes to special teams, there are a mix of players who play on different sides of the ball. There are only a few changes from offense and defense when it comes to special teams."
        "The list of players go as follows: "
        "   -Long Snapper: The player in this position kind of does what the center does, the only difference is that they are looking back, and snapping the ball at a longer distance. "
        "   -Punter (only for Punts): The punter is similar to the kicker, but the job of the punter is to catch the ball himself and kick the ball in a way that prevents the return specialist from scoring the ball, or having a big return. Punters have to calculate how far and how high they want to punt the ball when kicking it. Whereas kickers have to kick as hard as they can, in a specific direction. "
        "   -Holder (for Field Goal attempts): The player in this position is in charge of letting the long snapper know when to snap the ball. This player then proceeds to catch the ball, and position the ball correctly, so th kicker may proceed to kick a field goal. A holder not need for kickoff or for punts. This player is only needed for field goal attempts. "
        "   -Kicker: The kicker is probably the most well-known special teams player. This player is in charge of kicking the football within the goalposts. The acceptable range for a kicker to kick a field goal is usually between 10 to 45 yards. Anything more than that can still fall within their criteria, but it is usually a little harder for them to accomplish that feat. When kicking the ball off, it only matters that the kicker try to kick it as far as possible, so the return specialist doesn't have a chance to return the football. If a kicker kicks it out further than the end zone, then it is considered a touchback, and the returner does not get a chance to return the ball. "
        "   -Return Specialist: The person in this role has to catch the ball (whether it is being punted or kicked off to them) and try to run it to score a touchdown. Typically, the player witin this role has to be fast, but it is not really a strict requirement. Sometimes when the ball is punted to the return specialist, they do not get a chance to return it because a gunner has already reached them. In which case, the return specialist waves their hand to signal a 'fair catch'; meaning that nobody can tackle them, and the spot of the ball stands where the specialist caught it.   "
        "   -Gunner: The role of this player is to try and get to the return specialist as fast as they can in order to prevent the specialist from catching the ball and returning it. Once the ball is snapped, they just have to run as fast as they can. So, these players have to be very fast and smart about how they try to tackle the specialist when running at full speed."
        "   -Jammer: A player in this positon has the role of trying to prevent the guuner from getting to the player receiving the ball from a punt or a kick return. If they do their job well, then it allows the return specialist to have a chance of scoring upon catching the ball. These players have to be just as fast as the "
        "   -Blockers: This is just the category name given to the offensive lineman and the running backs who are preventing the defense from getting to the football."
    },
    {
        "title": "Scoring: How Points are Determined",
        "content": "Scoring a Touchdown awards a team 6 points. An Extra point (kick): 1 point. Or teams can try for a Two-point conversion after a touchdown: 2 points. A Field goal is worth: 3 points. A Safety awards: 2 points. (This occurs when the offense is backed up in their own endzone, and the ball carrier gets tackled in their own endzone, the opposing team is awarded 2 points and they get the ball punted to them as well). There is also the possibility of scoring touchdowns when the offense does not have the ball. A defensive player can intercept the ball return it, or return a fumbled football as well. A return specialist can return a kickoff or punted ball for a touchdown as well.",
    },
    {
        "title": "Field Layout",
        "content": "A football field is 100 yards long (120 when you include the two 10-yard end zones). Yard lines and hash marks divide the field for precise positioning.",
    },
     {
        "title": "The (Technological) Future of American Football - Trending in the Right Direction",
        "content": "As time progresses, so does the sport of American football. The game has gotten faster and players are adpating to it as well. A lot of the credit has to be given to fact that technology has "
        "been implemented to the game; mostly at the collegiate level and professsional level. There are now cameras available everywhere on the field; there are even cameras hovering over the field and cameras serving as pylons in the endzone as well."
        "Cameras are just tip of the iceberg, since every year, they integrate more and more technology within the game. At the professional level, quarterbacks have mics in their helmets that help them communicate with their coaches while the QB is on the field. It is because"
        "of technology like that the game has become faster. Now with social media being a big thing, people from all across the globe can find out about games and athletes. With technology growing more and more every single day, who knows when the stopping point for the sport of American football will be. One thing is for certain though; the concepts and rules of the game will always stay true to"
        "their roots.",
    },
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
    <title>FFF (Fun Fundamentals of Football) - Home</title>
    <style>
        body {
            font-family: Varsity, sans-serif;
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
    <h1>Welcome to the Amazing World of American Football!</h1>
    <p>This wonderful web application will allow users to learn about the sport of American football. Whether you are new to the sport, or already familiar with the game, but want to hone your skills; this is the right place for you!
    With FFF (or Fun Fundamentals of Football) users can learn the basics of American football, at one own's pace — including how scoring works, the rules of the game, the different positions, and even the formations of the different aspects of the game!.</p>
    <a href="{{ url_for('index') }}" class="button">Start Learning</a>
    <img src="https://www.printablee.com/postpic/2021/05/printable-football-field-diagram_300678.png" alt="Football Field Diagram">
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

