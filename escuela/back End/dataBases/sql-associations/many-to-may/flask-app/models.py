from enum import unique

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


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

    # This is the magic line!
    # Sets up a dept attribute on each instance of Employee.
    # SQLA will populate it with data from the departments table automatically!
    dept_code = db.Column(db.Text,
                          db.ForeignKey('departments.dept_code'))  # we create a relationship primary\foreign between both tables dept_code (s) , from  __tablename__= departments  , not the Dt model , __the tablename__

    # we can only call dept in Emp, employees can be accesed from Dt
    dept = db.relationship('Dt', backref='employees')

    # direct navigation: emp -> employeeproject & back
    # assignments = db.relationship('EmpPj', backref='employee')/

#secondary refers to a __tablename__ in this case EmpPj __tablename__='employee_projects'
    # direct navigation: emp -> project & back
    projects = db.relationship(
        "Pj", secondary="employees_projects", backref="employee")

    def __repr__(self):
        """Show info about pet."""

        s = self
        return f"< id={s.id} name={s.name} state= {s.state} >"


class Dt(db.Model):

    '''Department . A department has many employees '''

    __tablename__ = "departments"

    dept_code = db.Column(db.Text,
                          primary_key=True)  # we set a primary key

    dept_name = db.Column(db.Text,
                          nullable=False,
                          unique=True)
    phone = db.Column(db.Text)

    # employees = db.relationship('Employee')

    def __repr__(self):
        """Show info about pet."""

        s = self
        return f"< dept_code={s.dept_code} dept_name={s.dept_name} phone= {s.phone} >"


class Pj(db.Model):

    __tablename__ = 'projects'

    proj_code = db.Column(db.Text,
                          primary_key=True)

    proj_name = db.Column(db.Text,
                          nullable=True  # meaning is required
                          , unique=True)

    # dept_proj = db.relationship('EmpPj', backref='projects')

    # assignments = db.relationship('EmpPj', backref='project')


class EmpPj(db.Model):

    __tablename = 'employees_projects'
    #we can have a primary key that consist in two columns in db table example emp_id and proj_code, this two pk go together , and need a employee.id and projects.proj_code

    emp_id = db.Column(db.Integer,
                       db.ForeignKey('employees.id'), primary_key=True)  # this constraint is enforced
    proj_code = db.Column(db.Text,
                          db.ForeignKey('projects.proj_code'), primary_key=True)
    role = db.Column(db.Text)
