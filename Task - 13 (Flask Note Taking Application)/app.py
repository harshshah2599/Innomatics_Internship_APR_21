from flask import Flask, session, redirect, url_for, escape, request,render_template,flash

app = Flask(__name__)
notes = []


@app.route('/', methods=["GET", "POST"])
def add_note():
    n = request.form.get("note")
    notes.append(n)
    return render_template('home.html', notes=notes)


if __name__ == '__main__':
    app.run(debug=True)