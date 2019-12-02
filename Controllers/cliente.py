from flask_restful import Resource, reqparse
from Models.usuario import UsuarioModel
from Models.cliente import ClienteModel

class ClienteController(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument(
            'nombre',
            type=str,
            required=True,
            help='Falta nombre'
        )
        parser.add_argument(
            'apellido',
            type=str,
            required=True,
            help='Falta apellido'
        )
        parser.add_argument(
            'fecha_nac',
            type=str,
            required=True,
            help='Falta fecha nac'
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
            cliente=ClienteModel(data['nombre'],data['apellido'],data['fecha_nac'], usuario.usu_id)
            cliente.guardar_en_la_bd()
            usucliente={
                "id":cliente.cli_id,
                "nombre":data['nombre'],
                "apellido":data['apellido'],
                "fecha de nacimiento":data['fecha_nac'],
                "telefono":data['telefono'],
                "tipo ususario":data['tipo_usuario'],
                "direccion":data['direccion']
            }
            return usucliente
        except:
            return "No se guardo"
    
    def get(self,email):
        usuario=UsuarioModel.query.filter_by(usu_mail=email).first()
        for cliente in usuario.cliente:
            objusuario={
                "id":usuario.usu_id,
                "nombre":cliente.cli_nomb,
                "apellido":cliente.cli_ape,
                "email":usuario.usu_mail,
                "telefono":usuario.usu_fono,
                "direccion":usuario.usu_direccion
            }
        print(usuario)
        return objusuario
    

    
