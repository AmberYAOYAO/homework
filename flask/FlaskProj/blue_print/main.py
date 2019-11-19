from blueprint import create_app,db
from flask_script import Manager
from flask_script import Command
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command("db",MigrateCommand)

class Hello(Command):
    def run(self):
        print("hello")

class Runserver(Command):
    def run(self):
        app.run(host="127.0.0.1", port=8000, use_reloader=True)

manager.add_command("hello",Hello)
manager.add_command("runserver",Runserver)

if __name__ == '__main__':
    manager.run()

