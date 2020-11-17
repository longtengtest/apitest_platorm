from flask import request, jsonify
from app import app, db
from models import Case


@app.route('/api/case_add', methods=['POST'])
def case_add():
    obj = Case(**request.values)
    db.session.add(obj)
    db.session.commit()


def case_update():
    pass


def case_list():
    pass


def case_detail():
    pass


def case_data():
    pass


def case_debug():
    pass

