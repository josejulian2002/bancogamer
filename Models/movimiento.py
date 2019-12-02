from base_de_datos import bd

class MovimientoModel(bd.Model):
    __tablename__="t_movimiento"
    mov_id = bd.Column(bd.Integer, primary_key=True)
    mov_tipo = bd.Column(bd.String(45))
    mov_monto = bd.Column(bd.DECIMAL)
    mov_fecha=bd.Column(bd.DATETIME)
    nro_cue_destino=bd.Column(bd.String(45))
    cue_id= bd.Column(bd.Integer,bd.ForeignKey('t_cuenta.cue_id'))

    cuentacliente = bd.relationship('CuentaModel',lazy=True)

    def __init__(self,tipo,monto,fecha,destinatario,cuenta):
        self.mov_tipo=tipo
        self.mov_monto=monto
        self.mov_fecha=fecha
        self.nro_cue_destino=destinatario
        self.cue_id=cuenta

    def retornar_json(self):
        return {
            'tipo':self.mov_tipo,
            'monto':str(self.mov_monto),
            'fecha':str(self.mov_fecha),
            'cuenta_destino':self.nro_cue_destino,
            'cuenta':self.cue_id 
        }

    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()