from flask_restful import Resource, reqparse
# from Models.cliente import ClienteModel
# from Models.agencia import AgenciaModel
from Models.cuenta import CuentaModel

class CuentaClienteController(Resource):
    def get(self,id):
        clientecuenta=CuentaModel.query.filter_by(cliente_id=id).filter_by(cue_tipo="1").all()
        if clientecuenta:
            print(clientecuenta)
            cuentas=[]
            for cuenta in clientecuenta:
                cuentas.append(cuenta.retornar_jsoncliente())
            return cuentas
        else:
            return {'message':'No encontrado'},404

class CuentaExisteClienteController(Resource):
    def get(self,cuenro):
        clientecuenta=CuentaModel.query.filter_by(cue_nro=cuenro).filter_by(cue_tipo="1").first()
        if clientecuenta:
            return clientecuenta.retornar_jsoncliente(),200
        else:
            return 404,404

class CuentaIdController(Resource):
    def get(self,id):
        clientecuenta=CuentaModel.query.filter_by(cue_id=id).filter_by(cue_tipo="1").first()
        if clientecuenta:
            return clientecuenta.retornar_jsoncliente(),200
        else:
            return 404,404
            
class CuentaAgenciaControlller(Resource):
    def get(self,id):
        agenciacuenta=CuentaModel.query.filter_by(agencia_id=id).filter_by(cue_tipo="0").all()
        if agenciacuenta:
            cuentas=[]
            for cuenta in agenciacuenta:
                cuentas.append(cuenta.retornar_jsonagencia())
            return cuentas
        else:
            return {'message':'No encontrado'},404    