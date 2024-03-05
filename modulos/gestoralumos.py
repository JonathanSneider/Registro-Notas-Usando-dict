import os
from tabulate import tabulate
alumno = {}
notas ={
        'parciales' : [],
        'quices' : [],
        'trabajos' : [],
    }
#añadir estudiante
def AddStudent(alumnos:dict):
    id = input('ingrese el id : ')
    nombre = input('ingrese el nombre : ')
    edad = input('ingrese la edad : ')
    email = input('ingrese el email : ')
    alumno = {
        'id':id,
        'nombre':nombre,
        'edad':edad,
        'email':email,
        'calificaciones':notas
    }
    alumnos.update({id:alumno})


#Buscar Estuante
def SearchStudent(alumnos:dict):
    id = input('ingrese el id del estudiante :')
    #Buscar dato en diccionario
    data = alumnos.get(id,False)
    if(type(data) == dict):
        print(data)
    elif((type(data) == bool) and (data == False)):
        print('El estudiante no se encuentra registrado')

#Listar un Diccionario y buscar en cada uno + crear tabla con tabulate
def ListData(alumnos:dict):
    info = []
    for key,value in alumnos.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))


#Verificar que el estudiante este registrado
def ValidateStudent(alumnos:dict,id)->bool:
    #al darle valor de bool, y al retornar '' es igual False
    return bool(alumnos.get(id,''))

def DeleteStudent(alumnos:dict):
    id = input('ingrese el id del estudiante :')
    if (ValidateStudent(alumnos,id)):
        alumnos.pop(id)
    else:
        print(f'el estudiante con id {id} no esta registrado')


#otra forma de eliminar a un estudiante
def DelByName(alumnos:dict):
    nombre = input('ingrese el nombre del estudiante :')
    for key,value in alumnos.items():
        if(nombre in value['nombre']):
            alumnos.pop(key)
            #el break se usa para salirse del ciclo y que no de error por modificarse en plena iteracion
            break

#Agregar calificaciones a estudiantes
def AddGradesAlumons(alumnos:dict):
    nombrenota = input('ingresa el nombre del estudiante del cual quieres agrega las notas : ') 
    for key,value in alumnos.items():
        if (nombrenota not in value['nombre']):
            print('El estudiante no se encuentra registrado')
            return
    
    for key,value in alumnos.items():
        try:
            CnotasParciales = int(input(f'Ingrese cuantos parciales realizo {value["nombre"]} : '))
        except ValueError:
            print('Ingrese un numero valido ')
            return
        if(nombrenota in value['nombre']):
            calificacionespar = {
                'parciales': [],
                'quices' : [],
                'trabajos' : [],
            }
            
            
            
            for i in range(CnotasParciales):
                try:
                    NtsParciales = int(input(f'Ingrese la nota numero {i+1} de los parciales para el estudiante {value["nombre"]} : '))
                    calificacionespar['parciales'].append(NtsParciales)
                except ValueError:
                    print('ingrese un numero valido')
                    return
                finally:
                    value['calificaciones'] = calificacionespar
                    alumnos[key] = value
                
            Cnotasquices = int(input(f'Ingrese cuantos quices realizo {value["nombre"]} : '))
            for i in range(Cnotasquices):
                Ntsquicess = int(input(f'Ingrese la nota numero {i+1} de los quices para el estudiante {value["nombre"]} : '))
                calificacionespar['quices'].append(Ntsquicess)
                value['calificaciones'] = calificacionespar
                alumnos[key] = value
                
            Cnotastrabajos = int(input(f'Ingrese cuantos trabajos realizo {value["nombre"]} : '))    
            for i in range(Cnotastrabajos):
                Ntstrabajos = int(input(f'Ingrese la nota numero {i+1} de los trabajos para el estudiante {value["nombre"]} : '))
                calificacionespar['trabajos'].append(Ntstrabajos)
                value['calificaciones'] = calificacionespar
                alumnos[key] = value
                
            break
        
            
            
                

                
                
    
                


        
    

