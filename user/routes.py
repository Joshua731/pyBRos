from flask import render_template

from user import user_blueprint
from user.forms import UserForm
from main import db

from model import User


@user_blueprint.route("/", methods=["GET"])
def list_users():
    return render_template(
        template_name_or_list="user/list.html",
        users=User.query.all())


@user_blueprint.route("/new", methods=["GET", "POST"])
def new_user():
    form = UserForm()

    if form.validate_on_submit():
        user = User(id=int(form.id.data), name=str(form.name.data))
        db.session.add(user)
        db.session.commit()
        return "Usuario inserido com sucesso", 200

    return render_template("user/new.html", form=form)
