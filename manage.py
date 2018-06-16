from flask_script import Manager, Server
from run import app
from models import Todo

manager = Manager(app)
manager.add_command('runserver', Server())
@manager.shell
def make_shell_context():
	return dict(app=app, Todo=Todo)
if __name__ == '__main__':
	manager.run()