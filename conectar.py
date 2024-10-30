from pymongo import MongoClient

from dotenv import load_dotenv
import os
load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

cliente = MongoClient('mongodb+srv://'+usuario+':'+password+'@'+cluster+'.jowl2.mongodb.net/?retryWrites=true&w=majority&appName='+cluster)
#cliente = MongoClient('mongodb+srv://ang:639487811@cluster0.jowl2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
try:
   cliente.admin.command('ping')
   print("NOS CONECTAMOS CORRECTAMENTE")
except Exception as e:
   print(e)

baseDatos = cliente["mi_primera_base_datos"]

coleccion = baseDatos["mi_primera_coleccion"]

documento = { "nombre": "Jorge", "apellido": "Baron" }

inserccion = coleccion.insert_one(documento)