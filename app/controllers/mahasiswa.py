from flask import render_template, redirect, url_for,request
from app.forms.mahasiswa import MahasiswaSave
from app.models.models import Mahasiswa




class MahasiswaController():

    def home(self):
        return render_template('index.html', title='Home')
    
    def mahasiswaSave(self):
        form = MahasiswaSave()
        if form.validate_on_submit():
            mahasiswa = Mahasiswa(nim=form.nim.data, nama=form.nama.data)
            mahasiswa.save()
            return redirect(url_for('mahasiswaall'))
        return render_template('mahasiswa.html', form=form, title='Tambah Mahasiswa')
    
    def mahasiswaShow(self):
        mahasiswaAll = Mahasiswa().getAll()
        return render_template('show.html', mahasiswaAll=mahasiswaAll, title='Data Mahasiswa')
    
    def mahasiswaUpdate(self, data): 
        mahasiswa = Mahasiswa().query.filter_by(id=data).first()     
        form = MahasiswaSave( )
        if request.method =='POST':
            mahasiswa.nim = form.nim.data
            mahasiswa.nama = form.nama.data
            mahasiswa.update()
            return redirect(url_for('mahasiswaall'))
        elif request.method ==  'GET':
            form.nim.data = mahasiswa.nim
            form.nama.data = mahasiswa.nama

        return render_template('update.html',form =form, title='Update Mahasiswa')

    def mahasiswaDelete(self, data):
        mahasiswa = Mahasiswa().query.filter_by(id=data).first()
        mahasiswa.delete()
        return redirect(url_for('mahasiswaall'))
