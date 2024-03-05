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