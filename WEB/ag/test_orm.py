from models.db_session import create_session, global_init
from models.employer import Employer

global_init("sqlite:///db/ag.db")
session = create_session()

cl = Employer(name="Pupa", phone="66373732829", email="pupa@mail.com")
session.add(cl)
session.commit()
