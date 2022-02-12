import json
import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for
from random import choice
from choose_form import ChooseFile

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
                           img1=url_for('static', filename='img/mars1.png'),
                           img2=url_for('static', filename='img/mars2.png'),
                           img3=url_for('static', filename='img/mars3.png'),
                           img4=url_for('static', filename='img/mars4.png'),
                           img5=url_for('static', filename='img/mars5.png'))


@app.route("/my_gallery")
def web5():
    form = ChooseFile()
    if form.file_field.data:
        print(form.file_field.data)
    return render_template("web5.html", form=form,
                           img1=url_for('static', filename='img/mars1.png'),
                           img2=url_for('static', filename='img/mars2.png'),
                           img3=url_for('static', filename='img/mars3.png'),
                           img4=url_for('static', filename='img/mars4.png'),
                           img5=url_for('static', filename='img/mars5.png'))


@app.route("/member")
def web4():
    with open("static/json/data.json", "rt", encoding="utf8") as f:
        data = json.loads(f.read())

    name = choice(list(data.keys()))
    img = data[name][-1]
    prof = sorted(data[name][0])
    prof = ", ".join(prof)

    return render_template("web4.html", name=name, img_m=url_for('static', filename=f'img/{img}'), prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
