from flask import Flask, abort, render_template, request, redirect, session, url_for, g
import sqlite3
import matplotlib
import matplotlib.pyplot as plt
import os

matplotlib.use("Agg")
app = Flask(__name__)
DB = "reservations.sqlite"


def get_db():
    if "posts" not in g:
        g.db = sqlite3.connect(DB, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def statistics():
    db = get_db()
    rooms = db.execute("SELECT name, score FROM rooms").fetchall()
    plt.bar([room["name"] for room in rooms], [room["score"] for room in rooms])
    if not os.path.exists("static"):
        os.mkdir("static")
    plt.savefig("static/barplot.png")
    plt.close()


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/rooms", methods=["GET", "POST"])
def rooms():
    db = get_db()
    if request.method == "POST":
        name = request.form.get("name")
        db.execute("INSERT INTO rooms (name) VALUES (?)", (name,))
        db.commit()
        return redirect(url_for("rooms"))
    if request.method == "GET":
        rooms = db.execute("SELECT * FROM rooms").fetchall()
        statistics()
        return render_template("rooms.html", rooms=rooms)


@app.route("/reserve/<room_name>", methods=["GET", "POST"])
def reserve(room_name):
    db = get_db()
    if request.method == "POST":
        day = request.form.get("day")
        event_name = request.form.get("event_name")
        start_time = int(request.form.get("start_time"))
        end_time = int(request.form.get("end_time"))
        if end_time <= start_time:
            abort(400, "Előbb van vége a meetingnek, mint ahogy elkezdődött? 🤨")
        reserved_dates = db.execute(
            "SELECT start_time, end_time FROM reservations WHERE room_name = (?) AND day=(?)",
            (room_name, day),
        ).fetchall()
        for date in reserved_dates:  # Összes foglalt időpont
            for hour in range(start_time, end_time):
                if hour in range(date["start_time"], date["end_time"]) or hour in range(
                    date["start_time"], date["end_time"]
                ):
                    abort(400, "Foglalt időpont")
        db.execute(
            "INSERT INTO reservations (room_name, day, event_name, start_time, end_time) VALUES (?,?,?,?,?)",
            (room_name, day, event_name, start_time, end_time),
        )
        reservation_hours = end_time - start_time
        db.execute(
            "UPDATE rooms SET score=score+(?) WHERE name=(?)",
            (reservation_hours, room_name),
        )
        db.commit()
        return redirect(url_for("reserve", room_name=room_name))

    if request.method == "GET":
        reservations = [["" for _ in range(24)] for _ in range(5)]
        room_reservations = db.execute(
            "SELECT * FROM reservations WHERE room_name=?", (room_name,)
        ).fetchall()

        for reservation in room_reservations:
            day = reservation["day"]
            start_time = reservation["start_time"]
            end_time = reservation["end_time"]
            event_name = reservation["event_name"]
            for hour in range(start_time, end_time):
                reservations[day][hour] = event_name

        room = db.execute("SELECT * FROM rooms WHERE name=?", (room_name,)).fetchone()
        return render_template("room.html", room=room, reservations=reservations)


@app.post("/rooms/clear")
def clear():
    db = get_db()
    db.execute("DELETE FROM reservations")
    db.execute("UPDATE rooms SET score=0")
    db.commit()
    return redirect(url_for("rooms"))


if __name__ == "__main__":
    app.teardown_appcontext(close_db)
    app.run(port=8000, debug=True, host="0.0.0.0")
