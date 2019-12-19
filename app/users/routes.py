from flask import (
    Blueprint, render_template, redirect,
    request, url_for, flash, session, Markup)
from app.collections import get_users

users = Blueprint("users", __name__)


@users.route("/users", methods=["GET"])
def show_users():
    users = get_users()
    for u in users:
        print(u)
    return render_template('users.html', users=users)
