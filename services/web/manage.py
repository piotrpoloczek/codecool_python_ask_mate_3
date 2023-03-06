from flask.cli import FlaskGroup
from project import app, db
from project.data.sample_data import data_seed



cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    data_seed.run_sql_commands()

@cli.command("seed_db")
def seed_db():
    pass

if __name__ == '__main__':
    cli()