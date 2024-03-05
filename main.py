import modulos.gestoralumos as st
import os
import modulos.AddNotas as An
if __name__ == '__main__':
    alumnos = {}
    AdStuden = True
    while AdStuden:
        st.AddStudent(alumnos)
        AdStuden = bool(input('Quieres registrar a otro estudiantes? presione S(Si) o ENTER(No) : '))
    Addnotas = True
    while Addnotas:
        An.AddGradesAlumons(alumnos)
        Addnotas = bool(input('Desea registrar las notas de otro estudiante?  presione S(Si) o ENTER(No) :'))
    
    
    #st.SearchStudent(alumnos)
    st.ListData(alumnos)
    #st.DeleteStudent(alumnos)
    
    
   
    
    