import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for
from models.db_session import create_session, global_init
from routers import empl_router


app = Flask(__name__)
load_dotenv()
app.config["SECRET_KEY"] = os.getenv("MY_SECRET_KEY")
app.register_blueprint(empl_router)


def main():
    global_init("sqlite:///../db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()

