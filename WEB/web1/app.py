import json
import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, redirect
from random import choice
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import FileField, SubmitField, StringField


class LoadImageForm(FlaskForm):
    file = FileField()
    submit = SubmitField('Отправить')


class Questionnaire(FlaskForm):

    surname = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    file = FileField()
    submit = SubmitField('Отправить')




app = Flask(__name__)
load_dotenv()
app.config["SECRET_KEY"] = os.getenv("MY_SECRET_KEY")


@app.route('/distribution')
def web1():
    return render_template("web1.html", names=["Вилли", "Бони", "Клайд", "Коул", "Меган"])


@app.route("/<sex>/<int:age>")
def web2(sex, age):
    if age < 18:
        img_p = url_for('static', filename='img/child.png')

        if sex == "male":
            img_w = url_for('static', filename='img/m_ch.png')
        elif sex == "female":
            img_w = url_for('static', filename='img/f_ch.png')

    else:
        img_p = url_for('static', filename='img/adult.png')

        if sex == "male":
            img_w = url_for('static', filename='img/m_a.png')
        elif sex == "female":
            img_w = url_for('static', filename='img/f_a.png')

    return render_template("web2.html", img_p=img_p, img_w=img_w)


@app.route("/gallery")
def web3():
    return render_template("web3.html",
                           img1=url_for('static', filename='img/mars/mars1.png'),
                           img2=url_for('static', filename='img/mars/mars2.png'),
                           img3=url_for('static', filename='img/mars/mars3.png'),
                           img4=url_for('static', filename='img/mars/mars4.png'),
                           img5=url_for('static', filename='img/mars/mars5.png'))


@app.route("/my_gallery", methods=['GET', 'POST'])
def web5():
    form = LoadImageForm()
    if form.validate_on_submit():
        raw_data = form.file.data
        with open(f"./static/img/mars/mars{len(os.listdir('./static/img/')) + 1}.png", "wb") as out_file:
            out_file.write(raw_data.read())
        return redirect("my_gallery")
    return render_template("web5.html", images=list(map(lambda x: url_for('static', filename=x),
                                                        map(lambda t: "img/mars/" + t,
                                                            os.listdir("./static/img/mars")))), form=form)


@app.route("/member")
def web4():
    with open("static/json/data.json", "rt", encoding="utf8") as f:
        data = json.loads(f.read())

    name = choice(list(data.keys()))
    img = data[name][-1]
    prof = sorted(data[name][0])
    prof = ", ".join(prof)

    return render_template("web4.html", name=name, img_m=url_for('static', filename=f'img/{img}'), prof=prof)


@app.route("/selection")
def web6():
    form_info = Questionnaire()
    return render_template("web6.html", form_info=form_info)


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def web7(nickname, level, rating):
    return render_template("web7.html", nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
