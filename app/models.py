from app import db
from sqlalchemy.dialects.postgresql import JSON, BYTEA, TIME, BOOLEAN


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


class Events(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    icon = db.Column(db.LargeBinary)
    date = db.Column(db.Date)
    description = db.Column(db.String(500))
    time = db.Column(TIME())
    location = db.Column(db.String(200))
    starred = db.Column(BOOLEAN())

    def __init__(self, name, icon, date, description, time, location, starred):
        self.name = name
        self.icon = icon
        self.date = date
        self.description = description
        self.time = time
        self.location = location
        self.starred = starred

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


class Leadership(db.Model):
    __tablename__ = "leadership"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    position = db.Column(db.String(50))
    major = db.Column(db.String(50))
    description = db.Column(db.String(500))
    year = db.Column(db.String(50))
    icon = db.Column(db.LargeBinary)
    active = db.Column(db.BOOLEAN)

    def __init__(self, name, icon, position, description, year, major, active):
        self.name = name
        self.icon = icon
        self.position = position
        self.description = description
        self.year = year
        self.major = major
        self.active = active

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
