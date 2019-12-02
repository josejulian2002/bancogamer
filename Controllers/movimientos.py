from flask_restful import Resource, reqparse
from Models.cliente import ClienteModel
from Models.movimiento import MovimientoModel
from Models.agenciamovimiento import AgenciaMovimientoModel
from Models.cuenta import CuentaModel

class MovimientoController(Resource):
    def get(self,id_cliente):
        sentencia=ClienteModel.query.filter_by(cli_id=id_cliente).first()
        resultado = []
        for cuenta in sentencia.cuentacliente:
            for movimiento in cuenta.movimiento:
                resultado.append({
                    'Saldo de Cuenta': str(cuenta.cue_saldo),
                    'tipo movimiento': movimiento.mov_tipo,
                    'monto movimiento': str(movimiento.mov_monto),
                    'fecha': str(movimiento.mov_fecha)})
        return resultado

class MovimientoTransferirController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'tipo_mov',
            type=str,
            required=True,
            help='Falta tipo'
        )
        parser.add_argument(
            'monto',
            type=float,
            required=True,
            help='Falta monto'
        )
        parser.add_argument(
            'fecha',
            type=str,
            required=True,
            help='Falta fecha'
        )
        parser.add_argument(
            'destinatario',
            type=str,
            required=True,
            help='Falta destinatario'
        )
        parser.add_argument(
            'cuenta',
            type=int,
            required=True,
            help='Falta cuenta'
        )
        data=parser.parse_args()
        # Transferencia=1 
        # Retiro=2
        # Deposito=3
        movimiento=MovimientoModel(data['tipo_mov'],data['monto'],data['fecha'],data['destinatario'],data['cuenta'])
        clientecuentanro=CuentaModel.query.filter_by(cue_nro=data['destinatario']).filter_by(cue_tipo="1").first()
        clientecuentaid=CuentaModel.query.filter_by(cue_id=data['cuenta']).filter_by(cue_tipo="1").first()
        if data['tipo_mov']=="1":
            if clientecuentaid and clientecuentanro:
                if clientecuentanro!=None and clientecuentaid.cue_saldo>data['monto']:
                    try:
                        print(float(clientecuentaid.cue_saldo))
                        print(data['monto'])
                        MiCuenta=float(clientecuentaid.cue_saldo)-data['monto']
                        print(MiCuenta)
                        clientecuentaid.actualizar_estado(MiCuenta)
                        TuCuenta=float(clientecuentanro.cue_saldo)+data['monto']
                        print(TuCuenta)
                        clientecuentanro.actualizar_estado(TuCuenta)
                        movimiento.guardar_en_la_bd()
                        return movimiento.retornar_json()
                    except:
                        return {'message':'Hubo un error'},500
                else:
                    return {'message':'El nro destino no existe'}
            else:
                return {'message':'No se permite'}

class RetirarMovimientoController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'confirmacion',
            type=int,
            required=True,
            help="Falta confirmacion"
        )
        parser.add_argument(
            'agencia',
            type=int,
            required=True,
            help="Falta agencia"
        )
        parser.add_argument(
            'monto',
            type=float,
            required=True,
            help='Falta monto'
        )
        parser.add_argument(
            'fecha',
            type=str,
            required=True,
            help='Falta fecha'
        )
        parser.add_argument(
            'cuenta',
            type=int,
            required=True,
            help='Falta cuenta'
        )
        data=parser.parse_args()
        try:
            movimiento=MovimientoModel("2",data['monto'],data['fecha'],"null",data['cuenta'])
            movimiento.guardar_en_la_bd()
            movagencia=AgenciaMovimientoModel(data['confirmacion'],data['agencia'],movimiento.mov_id)
            movagencia.guardar_en_la_bd()
            return {
                "tipo_mov":"2",
                "monto":data['monto'],
                "fecha":data['fecha'],
                "cuenta":data['cuenta'],
                "confirmacion":data['confirmacion'],
                "agencia":data['agencia'],
                "mov_id":movimiento.mov_id
            }
        except:
            return {'message':"Hubo error"}             

class DepositarMovimientoController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'confirmacion',
            type=int,
            required=True,
            help="Falta confirmacion"
        )
        parser.add_argument(
            'agencia',
            type=int,
            required=True,
            help="Falta agencia"
        )
        parser.add_argument(
            'monto',
            type=float,
            required=True,
            help='Falta monto'
        )
        parser.add_argument(
            'fecha',
            type=str,
            required=True,
            help='Falta fecha'
        )
        parser.add_argument(
            'cuenta',
            type=int,
            required=True,
            help='Falta cuenta'
        )
        data=parser.parse_args()
        try:
            movimiento=MovimientoModel("3",data['monto'],data['fecha'],"null",data['cuenta'])
            movimiento.guardar_en_la_bd()
            movagencia=AgenciaMovimientoModel(data['confirmacion'],data['agencia'],movimiento.mov_id)
            movagencia.guardar_en_la_bd()
            return {
                "tipo_mov":"3",
                "monto":data['monto'],
                "fecha":data['fecha'],
                "cuenta":data['cuenta'],
                "confirmacion":data['confirmacion'],
                "agencia":data['agencia'],
                "mov_id":movimiento.mov_id
            }
        except:
            return {'message':"Hubo error"}             
        
        

            
        

            

