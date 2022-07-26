from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User, Emp, EmpPj, Dt, Pj
from forms import AddSnackForm, NewEmployeeForm

# from forms import AddSnackForm
# from forms import UserForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def homepage():
    """Show homepage links."""

    return render_template("index.html")


@app.route("/phones")
def phone_list():
    """Get list of users & dept phones.

    This version will be a 'n+1 query' --- it will query once for all
    users, and then for each department.

    There's a way to tell SQLAlchemy to load all the data in a single query,
    but don't worry about this for now.
    """

    emps = Emp.query.all()
    return render_template("phones.html", emps=emps)


@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""

    form = AddSnackForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        flash(f"Added {name} at {price}")
        return redirect("/add")

    else:
        return render_template(
            "snack_add_form.html", form=form)


@app.route('/employees/new', methods=['GET', 'POST'])
def new_emp():

    form = NewEmployeeForm()
    depts = db.session.query(Dt.dept_code, Dt.dept_name)
    form.dept_code.choices = depts

    if form.validate_on_submit():
        name = form.name.data
        state = form.state.data
        dept_code = form.dept_code.data
        dept_name = form.dept_code.data

        new_emp = Emp(name=name, state=state,
                      dept_code=dept_code, dept_name=dept_name)

        db.session.add(new_emp)
        db.session.commit()
        return redirect('/phones')
    else:
        return render_template('add_emp_form.html', form=form)

    # @app.route("/users/<int:uid>/edit", methods=["GET", "POST"])
    # def edit_user(uid):
    #     """Show user edit form and handle edit."""
    #     user = User.query.get_or_404(uid)
    #     form = UserForm(obj=user)
    #     if form.validate_on_submit():
    #         user.name = form.name.data
    #         user.email = form.email.data
    #         db.session.commit()
    #         flash(f"User {uid} updated!")
    #         return redirect(f"/users/{uid}/edit")
    #     else:
    #         return render_template("user_form.html", form=form)
