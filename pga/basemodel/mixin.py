from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModelMixin(object):
    id =  db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)
    last_modified = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)
