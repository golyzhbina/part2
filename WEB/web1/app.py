from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
