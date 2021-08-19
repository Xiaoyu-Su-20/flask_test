from flask import Blueprint

user = Blueprint("user", __name__)

@user.route("/task")
def task():
    return "task"

# @user.route("/login", methods=["GET", "POST"])
# def login():
#     # if a user is already logged in, redirect her
#     if current_user.is_authenticated:
#         return redirect(url_for("main.home"))
#     form = LoginForm()
#     if form.validate_on_submit():

#         username = (
#             "APISYNC"  # Username for MDHQ #TODO Change to environment variable
#         )
#         subdomain = (
#             "rcode"  # Subdomain for MDHQ # TODO Change to environment variable
#         )
#         key = "sk_56470fc3M53e5fL58Pr7"  # secret key for MDHQ # TODO Change to environment variable

#         URL = "https://{0}:{1}@{2}.md-hq.com/api/v1/patients/portal/validate_credentials".format(
#             username, key, subdomain
#         )  # The URL to access MDHQ API endpoints

#         response = requests.post(
#             URL, json={"username": form.id.data, "password": form.password.data},
#         )

#         # if response not successful, abort
#         if response.status_code not in [200]:
#             abort(500)

#         data = response.json()
#         if data["result"]:
#             id = data["patient_details"]["id"]
#             user = User.query.filter_by(id=id).first()
#             if not user:
#                 abort(500)

#             login_user(user, remember=form.remember.data)

#             # if you click on locked page without authentication,
#             # redirects to the page after login
#             next_page = request.args.get("next")
#             return (
#                 redirect(next_page) if next_page else redirect(url_for("main.home"))
#             )
#         else:
#             flash("Incorrect Username Password Combination", "danger")
#     return render_template("main/login.html", title="Login", form=form)

# @user.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for("user.login"))