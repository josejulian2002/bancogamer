from base_de_datos import bd

class CuentaModel(bd.Model):
    __tablename__="t_cuenta"
    cue_id = bd.Column(bd.Integer, primary_key=True)
    cue_nro = bd.Column(bd.String(20))
    cue_tipo = bd.Column(bd.String(45))
    cue_saldo = bd.Column(bd.DECIMAL)
    cue_estado = bd.Column(bd.Boolean)
    tipomoneda_id= bd.Column(bd.Integer,bd.ForeignKey('t_tipomoneda.tipomon_id'))
    cliente_id=bd.Column(bd.Integer,bd.ForeignKey('t_cliente.cli_id'))
    agencia_id=bd.Column(bd.Integer,bd.ForeignKey('t_agencia.agen_id'))

    cliente = bd.relationship('ClienteModel',lazy=True)
    movimiento=bd.relationship('MovimientoModel',lazy=True)

    def __init__(self,nro,tipo,saldo,estado,moneda,cliente,agencia):
        self.cue_nro=nro
        self.cue_tipo=tipo
        self.cue_saldo=saldo
        self.cue_estado=estado
        self.tipomoneda_id=moneda
        self.cliente_id=cliente
        self.agencia_id=agencia

    def retornar_jsoncliente(self):
        return {
            "nro de cuenta":self.cue_nro,
            "tipo":self.cue_tipo,
            "saldo":str(self.cue_saldo),
            "estado":self.cue_estado,
            "moneda":self.tipomoneda_id,
            "id cliente":self.cliente_id,
        }

    def retornar_jsonagencia(self):
        return {
            "nro de cuenta":self.cue_nro,
            "tipo":self.cue_tipo,
            "saldo":str(self.cue_saldo),
            "estado":self.cue_estado,
            "moneda":self.tipomoneda_id,
            "id agencia":self.agencia_id
        }

    def actualizar_estado(self,nuevo_saldo):
        self.cue_saldo=nuevo_saldo
        bd.session.commit()