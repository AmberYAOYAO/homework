from blueprint.user import user

@user.route("/")
def index():
    return "user's index hello world"