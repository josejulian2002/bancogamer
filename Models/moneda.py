from base_de_datos import bd

class TipoMonedaModel(bd.Model):
    __tablename__="t_tipomoneda"
    tipomon_id = bd.Column(bd.Integer, primary_key=True)
    tipomon_desc = bd.Column(bd.String(45))

    def __init__(self,descripcion):
        self.tipomon_desc=descripcion