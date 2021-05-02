from CCTV import db

class Detected(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(200), nullable=False)
    detected_time = db.Column(db.DateTime(), nullable=False)