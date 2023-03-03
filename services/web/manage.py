from flask.cli import FlaskGroup
from project import app, db
from project.data.init_db import create_schema
from project.data.data_inserter import main


cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    create_schema()

@cli.command("seed_db")
def seed_db():
    main()

if __name__ == '__main__':
    cli()