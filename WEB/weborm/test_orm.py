from models.db_session import create_session, global_init
from models.user import User

global_init("sqlite:///db/blogs.db")
session = create_session()
