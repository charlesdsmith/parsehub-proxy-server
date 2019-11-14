from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Property(db.Model):

    """Model for user accounts."""

    __tablename__ = 'properties'
    unique_id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    property_id = db.Column(db.String(30),
                    index=True,
                    unique=False,
                    nullable=False)
    type = db.Column(db.String(80),
                      index=True,
                      unique=False,
                      nullable=False)
    dynamicDisplayPrice = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)
    basePrice = db.Column(db.Integer,
                    index=False,
                    unique=False,
                    nullable=True)
    datetimeOfPrice = db.Column(db.String(50),
                      index=False,
                      unique=False,
                      nullable=False)

