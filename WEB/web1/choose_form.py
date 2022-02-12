from flask_wtf import FlaskForm
from wtforms import MultipleFileField, SubmitField


class ChooseFile(FlaskForm):

    file_field = MultipleFileField("Выберите файл")
    submit = SubmitField("Отправить")
