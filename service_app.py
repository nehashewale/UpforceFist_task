from extension import app
from user.api import user_blueprint
from competition.api import competition_blueprint
from entry.api import entry_blueprint


app.register_blueprint(user_blueprint)
app.register_blueprint(competition_blueprint)
app.register_blueprint(entry_blueprint)


