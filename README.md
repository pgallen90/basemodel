# base_model

Columns & conventions that should be in every Postgresql SQLAlchemy model. Used as a mixin. Support Postgres only.

## Usage:

**Installation:** Use pip
```bash
    pip install pga.basemodel
```

**Quickstart:** To add id, timestamp, and last modified columns, simply add BaseModelMixin to your model classes.

```python
    class ExampleOldModel(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)
        last_modified = db.Column(db.DateTime, onupdate=func.now(), nullable=False)

        important_model_data = db.Column(db.Text)


    # The same model, but using the BaseModelMixin:
    from pga.basemodel import BaseModelMixin

    class ExampleModelWithMixin(db.Model, BaseModelMixin):
        important_model_data = db.Column(db.Text)
```
