import re
from sqlalchemy import func
from sqlalchemy.ext.declarative import declared_attr

# Set up SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def to_snake_case(camel_case):    
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class BaseModelMixin(object):

    @declared_attr
    def __tablename__(cls):
        """Convert CamelCase model (Class) names into something sutable for a 
        database table name.  
        """
        return to_snake_case(cls.__name__)

    id =  db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)
    last_modified = db.Column(db.DateTime, onupdate=func.now(), nullable=False)
