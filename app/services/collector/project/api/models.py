from project import db

class Temperature(db.Model):
    __tablename__ = 'temperatures'
    id = db.Column(db.Integer, primary_key=True)
    UTCDateTime = db.Column(db.DateTime)
    value = db.Column(db.Float)
    
    def __repr__(self):
       return "<Temperature(date='%s', value='%s')>" % (
                            self.dt, self.value)
