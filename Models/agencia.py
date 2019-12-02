from base_de_datos import bd

class AgenciaModel(bd.Model):
    __tablename__="t_agencia"
    agen_id = bd.Column(bd.Integer, primary_key=True)
    agen_nomb = bd.Column(bd.String(45))
    agen_hor = bd.Column(bd.String(45))
    agen_lat=bd.Column(bd.DECIMAL)
    agen_lng=bd.Column(bd.DECIMAL)
    usu_id= bd.Column(bd.Integer,bd.ForeignKey('t_usuario.usu_id'))

    usuario = bd.relationship('UsuarioModel',lazy=True)

    def __init__(self,nombre,horario,latitud,longitud,usuario):
        self.agen_nomb=nombre
        self.agen_hor=horario
        self.agen_lat=latitud
        self.agen_lng=longitud
        self.usu_id=usuario
    
    def retornar_json(self):
        return {
            "id":self.agen_id,
            "nombre":self.agen_nomb,
            "horario":self.agen_hor,
            "latitud":str(self.agen_lat),
            "longitud":str(self.agen_lng),
            "telefono":self.usuario.usu_fono,
            "tipo usuario":self.usuario.usu_tipo,
            "direccion":self.usuario.usu_direccion
        }
    
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()