from base_de_datos import bd

class ClienteModel(bd.Model):
    __tablename__="t_cliente"
    cli_id = bd.Column(bd.Integer, primary_key=True)
    cli_nomb = bd.Column(bd.String(45))
    cli_ape = bd.Column(bd.String(45))
    cli_fechanac=bd.Column(bd.DATETIME)
    usu_id= bd.Column(bd.Integer,bd.ForeignKey('t_usuario.usu_id'))

    cuentacliente = bd.relationship('CuentaModel',lazy=True)
    

    def __init__(self,nombre,apellido,fecha_nacimiento,usuario):
        self.cli_nomb=nombre
        self.cli_ape=apellido
        self.cli_fechanac=fecha_nacimiento
        self.usu_id=usuario
    
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()