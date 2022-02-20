from flask import Blueprint
from models.db_session import create_session
from models.employer import Employer
import json

router = Blueprint("employee_api", __name__, template_folder="/app/template", url_prefix="/employee")


@router.route("/", methods=["GET"])
def get_employees():

     with create_session() as session:
        emp = session.query(Employer).all()
        emp = list(map(lambda x: x.__dict__(), emp))
        return json.dumps(emp)


