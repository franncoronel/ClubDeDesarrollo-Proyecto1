from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from enum import Enum 
from sqlalchemy import Enum as SqlEnum

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Datos_Personales(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    es_prestador = db.Column(db.Boolean, nullable=False, default=False)
    
class Establecimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    descripcion = db.Column(db.String(200), nullable=True)
    telefono = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    propietario_id = db.Column(db.Integer, db.ForeignKey('datos_personales.id'), nullable=False)
    
class Turno(db.Model):
    class Estados_Turno(Enum):
        DISPONIBLE = "Disponible"
        ASIGNADO = "Asignado"
        FINALIZADO = "Finalizado"
        
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    estado = db.Column(SqlEnum(Estados_Turno), nullable=False, default=Estados_Turno.DISPONIBLE)
    establecimiento_id = db.Column(db.Integer, db.ForeignKey('establecimiento.id'), nullable=False)
    
class Turno_Asignado(db.Model):
    class Estados_Turno_Usuario(Enum):
        ASIGNADO = "Asignado"
        FINALIZADO = "Finalizado"
        CANCELADO = "Cancelado"
        
    id = db.Column(db.Integer, primary_key=True)
    turno_id = db.Column(db.Integer, db.ForeignKey('turno.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    estado = db.Column(SqlEnum(Estados_Turno_Usuario), nullable=False, default=Estados_Turno_Usuario.ASIGNADO)

