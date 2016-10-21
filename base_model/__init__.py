import re
from sqlalchemy import func
from sqlalchemy.ext.declarative import declared_attr

from flaskapp.extensions import db


class BaseModelMixin(object):
    id =  db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)
    last_modified = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)
