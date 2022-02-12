from flask import Flask, render_template, url_for, redirect
import os
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


class LoadImageForm(FlaskForm):
    file = FileField()
    submit = SubmitField('Войти')


load_dotenv()


app = Flask(__name__)


app.config["SECRET_KEY"] = os.getenv('MY_SECRET_KEY')


@app.route("/gallery", methods=['GET', 'POST'])
def web3():
    form = LoadImageForm()
    if form.validate_on_submit():
        raw_data = form.file.data
        with open(f"./static/img/mars{len(os.listdir('./static/img/')) + 1}.jpg", "wb") as out_file:
            out_file.write(raw_data.read())
        return redirect("gallery")
    return render_template("web3.html", images=list(map(lambda x: url_for('static', filename=x),
                                                        map(lambda t: "img/" + t,
                                                            os.listdir("./static/img/")))), form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
