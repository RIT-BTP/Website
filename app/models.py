from app import db
from sqlalchemy.dialects.postgresql import JSON


class tmpUsers(db.Model):
    __tablename__ = "tmpUsers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<id {}, name {}>".format(self.id, self.name)

    @classmethod
    def get(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def insert(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
