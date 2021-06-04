from exts import db

class Venue(db.Model):
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    genres = db.Column(db.String(120),nullable=False)  # this should be an db.ARRAY(), but we only recive a string from the front end
    facebook_link = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    website_link = db.Column(db.String(500), nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(1000), nullable=True)

    # shows = db.relationship('Show',backref="venues")

    # shows = db.relationship('Show',backref=db.backref("venues"), cascade="all, delete-orphan")

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean, nullable=False,default=False)
    seeking_description =db.Column(db.String(1000), nullable=True)

    # shows = db.relationship('Show',backref="artists")
    # shows = db.relationship('Show',backref=db.backref("artists", cascade="all, delete-orphan"))
    

class Show(db.Model):
      __tablename__ ='Show'
      id = db.Column('id' , db.Integer,primary_key=True)
      start_time = db.Column(db.DateTime,nullable=False)

      artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id',ondelete='CASCADE'))
      venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id',ondelete='CASCADE'))

      artist = db.relationship('Artist',backref=db.backref("shows", cascade="all, delete-orphan"))
      venue = db.relationship('Venue',backref=db.backref("shows", cascade="all, delete-orphan"))