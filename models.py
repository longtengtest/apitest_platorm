from app import db


class Env(db.Model):
    __tablename__ = 'env'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    base_url = db.Column(db.String(200))
    request = db.Column(db.Text)
    variables = db.Column(db.Text)


class Suite(db.Model):
    __tablename__ = 'suite'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    env_id = db.Column(db.Integer, db.ForeignKey('env.id'))
    testcases = db.relationship('Case', backref='suite_testcases', lazy='dynamic')
    reports = db.relationship('Report', backref='suite_reports', lazy='dynamic')


class Case(db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    suite_id = db.Column(db.Integer, db.ForeignKey('suite.id'))
    index = db.Column(db.Integer, default=0)
    skip = db.Column(db.Boolean)
    request = db.Column(db.Text)
    extract = db.Column(db.Text)
    validate = db.Column(db.Text)