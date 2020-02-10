from pymongo import MongoClient
# normalizar la frase de tildes
from unicodedata import normalize

class Conexion:
    def __init__(self,db,collection):
        # incializar nuestra conexión a la base de datos
        MONGO_URL_ATLAS = 'mongodb+srv://Jorge:jorge@cluster0-7gqqa.mongodb.net/test?retryWrites=true&w=majority'
        self.client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
        self.db = self.client['{0}'.format(db)]
        self.collection = self.db['{0}'.format(collection)]

    def introducir_dni(self,nombre,dni):
        resultados = self.collection.find({'nombre':'{0}'.format(nombre)})
        if resultados.count() > 0:
            return False
        else:
            longitud = len(palabra)
            self.collection.insert_one({'nombre':'{0}'.format(nombre), 'dni':'{0}'.format(dni)})
            return True

    def leer_historial(self, dni):
        busqueda = list(self.collection.find({'dni':'{0}'.format(dni)}, {'_id':0,'dni':1}))
        return busqueda

    def borrar(self,dni):
        self.collection.delete_one({'dni':'{0}'.format(dni)})
        return True