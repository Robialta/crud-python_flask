from app import db

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nim = db.Column(db.String(11), nullable=False)
    nama = db.Column(db.String(100), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def getAll(self):
        return Mahasiswa.query.all()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<nama: {}>'.format(self.nama)
    