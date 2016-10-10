# base_model

Columns & conventions that should be in every Postgresql SQLAlchemy model. Used as a mixin. Support Postgres only.

## Usage:

**Quickstart:** To add tablename, id, timestamp, and last modified columns, simply add BaseModelMixin to your model classes.

[The example below modifies Miguel Grinberg's excellent Flask Migrate wrapper. ](http://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask)

```python
    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy
    from flask.ext.script import Manager
    from flask.ext.migrate import Migrate, MigrateCommand
    from sqlalchemy import func

    from base_model import BaseModelMixin

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    class ExampleOldModel(db.Model):
        __tablename__ = 'example_old_model'

        id = db.Column(db.Integer, primary_key = True)
        timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)
        last_modified = db.Column(db.DateTime, onupdate=func.now(), nullable=False)

        important_model_data = db.Column(db.Text)


    class ExampleModelWithMixin(db.Model, BaseModelMixin):
        important_model_data = db.Column(db.Text)

    if __name__ == '__main__':
        manager.run()
```

