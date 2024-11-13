from conector import ConectorMongoDB

conector=ConectorMongoDB()
cliente=conector.conectarse()

libreriaBD=cliente["libreria"]
librosColeccion=libreriaBD["libros"]

miquery = { "precio": 19.99 } 

libros = librosColeccion.find(miquery) #-> Busca los que tienen precio igual a 19.99

miquery = { "precio":  { "$gt": 19 } }
 
libros = librosColeccion.find(miquery) #-> > Busca los que tienen el precio mayor que 19 

miquery = { "titulo":  { "$regex": "^D" } }

libros = librosColeccion.find(miquery) #-> Busca a toso los que tengan un título que empieza por D

libros= librosColeccion.find({"paginas" : {"$eq": 1072 }})
for l in libros:
    print(l)
print("\n") 

libros= librosColeccion.find({ "$and" : [{ "titulo" : {"$regex": "1" }},{ "precio" : { "$gte":5} }]})
for l in libros:
    print(l)                                                       
print("\n")   

libros= librosColeccion.find({ "$and" : [{ "paginas" : {"$lte": 600 }},{ "precio" : { "$lte":30} }]}).sort("titulo",-1)           
for l in libros:
    print(l)                                

miquery = { "titulo": "Cien Años de Soledad" }

resultado = librosColeccion.delete_one(miquery)

miquery = { "precio": 14.5 }
nuevosValores = { "$set": { "precio": 10.99 } }
resultado = librosColeccion.update_one(miquery, nuevosValores)
