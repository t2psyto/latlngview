from flaskr import db

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Text)
    long = db.Column(db.Text)
    timestamp = db.Column(db.Integer)
    client = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} lat={lat}> long={long} timestamp={timestamp} client={client}>'.format(
                id=self.id, lat=self.lat, long=self.long, timestamp=self.timestamp, client=self.client)

def init():
    db.create_all()

