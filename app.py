from flask import Flask
from flask_restful import Api
from base_de_datos import bd

app = Flask(__name__)

from Models.usuario import UsuarioModel
from Models.moneda import TipoMonedaModel
from Controllers.agencia import AgenciaController
from Controllers.cliente import ClienteController
from Controllers.cuenta import CuentaClienteController,CuentaAgenciaControlller,CuentaExisteClienteController
from Controllers.movimientos import MovimientoController,MovimientoTransferirController,RetirarMovimientoController,DepositarMovimientoController
from Controllers.agenciamovimiento import MovimientoAgenciaController

from flask_cors import CORS
from flask_jwt import JWT
from seguridad import autentication, identificador

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@localhost/banca"

app.config['SECRET_KEY'] = 'clave_secreta'
app.config['JWT_AUTH_URL_RULE']='/usuario/login'
import datetime
app.config['JWT_EXPIRATION_DELTA']=datetime.timedelta(hours=1)
jsonwebtoken = JWT(app, autentication, identificador)

api = Api(app)

@app.route('/')
def inicio():
    return 'La API REST ha escuchado tus suplicas! 😀😱💩'

@app.before_first_request
def iniciar_bd():
    bd.init_app(app)
    # bd.drop_all(app=app)
    bd.create_all(app=app)

api.add_resource(ClienteController,"/agregar/cliente","/traer/usuario/<string:email>")
api.add_resource(AgenciaController,"/agregar/agencia","/traer/agencias")

api.add_resource(CuentaClienteController,"/buscar/cuentacliente/<string:id>")
api.add_resource(CuentaAgenciaControlller,"/buscar/cuentaagencia/<string:id>")
api.add_resource(CuentaExisteClienteController,"/buscar/nrocuenta/<string:cuenro>")
api.add_resource(MovimientoController,'/conseguir/movimientos/<string:id_cliente>')
api.add_resource(MovimientoTransferirController,'/transferir/monto')
api.add_resource(RetirarMovimientoController,"/retirar/monto")
api.add_resource(DepositarMovimientoController,"/depositar/monto")
api.add_resource(MovimientoAgenciaController,"/traer/movagencia/<string:id_agen>")


if __name__=="__main__":
    app.run(debug=True)