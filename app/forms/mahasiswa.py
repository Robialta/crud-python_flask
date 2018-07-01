from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class MahasiswaSave(FlaskForm):
    message_null = 'data tidak boleh kosong'
    nim = StringField('NIM', validators=[DataRequired(message=message_null)])
    nama = StringField('Nama', validators=[DataRequired(message=message_null)])
    simpan = SubmitField('Simpan')