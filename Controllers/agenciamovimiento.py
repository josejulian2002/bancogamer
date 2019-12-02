from flask_restful import Resource, reqparse
from Models.agenciamovimiento import AgenciaMovimientoModel

class MovimientoAgenciaController(Resource):
    def get(self,id_agen):
        agencias=AgenciaMovimientoModel.query.filter_by(agen_id=id_agen).all()
        agenciasall=[]
        for agencias in agencias:
            agenciasall.append({"movimiento":agencias.movimiento_id,"confirmacion":agencias.agenmov_confirmacion})
        return agenciasall
