from pymongo import MongoClient

from dotenv import load_dotenv
import os
load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

cliente = MongoClient('mongodb+srv://'+usuario+':'+password+'@'+cluster+'.jowl2.mongodb.net/?retryWrites=true&w=majority&appName='+cluster)

baseDatos = cliente["mi_primera_base_datos"]
coleccion = baseDatos["mi_primera_coleccion"]
documento = { "nombre": "Ángel", "apellido": "García" }
inserccion = coleccion.insert_one(documento)