from flask_restful import Resource, reqparse
from Models.agencia import AgenciaModel
from Models.usuario import UsuarioModel

class AgenciaController(Resource):
    def get(self):
        agencias=AgenciaModel.query.all()
        agenciasarreglo=[]
        print(agencias)
        for agencia in agencias:
            print(agencia)
            agenciasarreglo.append(agencia.retornar_json())
        return agenciasarreglo

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'nombre',
            type=str,
            required=True,
            help='Falta nombre'
        )
        parser.add_argument(
            'horario',
            type=str,
            required=True,
            help='Falta horario'
        )
        parser.add_argument(
            'latitud',
            type=float,
            required=True,
            help='Falta latitud'
        )
        parser.add_argument(
            'longitud',
            type=float,
            required=True,
            help='Falta longitud'
        )
        parser.add_argument(
            'password',
            type=str,
            required=True,
            help='Falta password'
        )
        parser.add_argument(
            'email',
            type=str,
            required=True,
            help='Falta email'
        )
        parser.add_argument(
            'tipo_usuario',
            type=int,
            required=True,
            help='Falta tipo'
        )
        parser.add_argument(
            'telefono',
            type=str,
            required=True,
            help='Falta Telefono'
        )
        parser.add_argument(
            'direccion',
            type=str,
            required=True,
            help='Falta direccion'
        )
        data=parser.parse_args()
        try:
            usuario=UsuarioModel(data['password'],data['email'],data['tipo_usuario'],data   ['telefono'],data['direccion'])
            usuario.guardar_en_la_bd()
            agencia=AgenciaModel(data['nombre'],data['horario'],data['latitud'],data['longitud'], usuario.usu_id)
            agencia.guardar_en_la_bd()
            usuagencia={
                "id":agencia.agen_id,
                "nombre":data['nombre'],
                "horario":data['horario'],
                "latitud":data['latitud'],
                "longitud":data['longitud'],
                "telefono":data['telefono'],
                "tipo ususario":data['tipo_usuario'],
                "direccion":data['direccion']
            }
            return usuagencia
        except:
            return "No se guardo"