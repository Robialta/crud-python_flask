from app import app
from app.controllers.mahasiswa import MahasiswaController

@app.route('/')
@app.route('/index')
def index():
    return MahasiswaController().home()

@app.route('/mahasiswa', methods=['GET', 'POST'])
def mahasiswa():
    return MahasiswaController().mahasiswaSave()

@app.route('/mahasiswa/all')
def mahasiswaall():
    return MahasiswaController().mahasiswaShow()

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    return MahasiswaController().mahasiswaUpdate(id)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    return MahasiswaController().mahasiswaDelete(id)
    