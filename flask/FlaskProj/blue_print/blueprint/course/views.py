from blueprint.course import course

@course.route("/")
def index():
    return "user's index hello world"