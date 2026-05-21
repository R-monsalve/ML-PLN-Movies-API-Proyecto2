from flask import Flask
from flask_restx import Api, Resource, reqparse
from movie_model import predecir_generos

app = Flask(__name__)
api = Api(app, title='API Géneros de Películas', doc='/')

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Título de la película')
parser.add_argument('plot', type=str, required=True, help='Sinopsis de la película')

@api.route('/predict/')
class Predict(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        resultado = predecir_generos(args['title'], args['plot'])
        return resultado

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)