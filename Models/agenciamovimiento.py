from base_de_datos import bd

class AgenciaMovimientoModel(bd.Model):
    __tablename__="t_agencia_movimiento"
    agenmov_id = bd.Column(bd.Integer, primary_key=True)
    agenmov_confirmacion = bd.Column(bd.BOOLEAN)
    agen_id= bd.Column(bd.Integer,bd.ForeignKey('t_agencia.agen_id'))
    movimiento_id= bd.Column(bd.Integer,bd.ForeignKey('t_movimiento.mov_id'))

    def __init__(self,confirmacion,agencia,movimiento):
        self.agenmov_confirmacion=confirmacion
        self.agen_id=agencia
        self.movimiento_id=movimiento
    
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()