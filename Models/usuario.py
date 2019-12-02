from base_de_datos import bd
import bcrypt

class UsuarioModel(bd.Model):
    __tablename__="t_usuario"
    usu_id = bd.Column(bd.Integer, primary_key=True)
    usu_hash = bd.Column(bd.Text)
    usu_salt = bd.Column(bd.Text)
    usu_mail = bd.Column(bd.Text)
    usu_tipo = bd.Column(bd.Integer)
    usu_fono = bd.Column(bd.String(10))
    usu_direccion=bd.Column(bd.String(50))

    cliente = bd.relationship('ClienteModel',lazy=True)

    def __init__(self,password,email,tipo_usuario,telefono,direccion):
        password_convertida= bytes(password,'utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_convertida,salt)
        salt = salt.decode('utf-8')
        hashed = hashed.decode('utf-8')
        self.usu_salt=salt
        self.usu_hash=hashed
        self.usu_mail=email
        self.usu_tipo=tipo_usuario
        self.usu_fono=telefono
        self.usu_direccion=direccion

    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()


