"""Sample file demonstrating SQLAlchemy joins & relationships."""

from flask_sqlalchemy import SQLAlchemy
from app import app

# This is the connection to the database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


# Model go below

class Dt(db.Model):

    '''Department . A department has many employees '''

    __tablename__ = "departments"

    dept_code = db.Column(db.Text,
                          primary_key=True)  # we set a primary key

    dept_name = db.Column(db.Text,
                          nullable=False,
                          unique=True)
    phone = db.Column(db.Text)

    def __repr__(self):
        """Show info about pet."""

        s = self
        return f"< dept_code={s.dept_code} dept_name={s.dept_name} phone= {s.phone} >"


class Emp(db.Model):

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True
                   )

    name = db.Column(db.Text,
                     nullable=False,
                     unique=True)  # must have a value (NOT NULL )

    state = db.Column(db.String(10),
                      nullable=False,
                      default='FL')

    dept_code = db.Column(db.Text,
                          db.ForeignKey('departments.dept_code'))  # we create a relationship primary\foreign between both tables dept_code (s) , from  __tablename__= departments  , not the Dt model , __the tablename__;this constraint is enforced

    dept = db.relationship('Dt', backref='employees')

    def __repr__(self):
        """Show info about pet."""

        s = self
        return f"< id={s.id} name={s.name} state= {s.state} >"


def get_directory():
    """Not efficient when having alot of info in database """

    all_emps = Emp.query.all()

    for emp in all_emps:
        if emp.dept is not None:
            print(emp.name, emp.dept.dept_name, emp.dept.phone)
        else:
            print(emp.name)


def get_directory_join():
    """MORE EFFICIENT """

    directoy = db.session.query(
        Emp.name, Dt.dept_name, Dt.phone).join(Dt).all()

    for name, dept, phone in directoy:
        print(name, dept, phone)


def get_directory_join_all():
    """MORE EFFICIENT """

    directoy = db.session.query(Emp, Dt).join(Dt).all()

    for emp, dept in directoy:
        print(emp.name, dept.dept_name, dept.phone)
