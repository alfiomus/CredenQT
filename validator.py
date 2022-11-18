import sys

from prueba import *

class Miformulario(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_ACEPUSER, QtCore.SIGNAL('clicked()'), self.mensaje_usuario)
        QtCore.QObject.connect(self.ui.pushButton_ACEPPASS, QtCore.SIGNAL('clicked()'), self.mensaje_password)

    def mensaje_usuario(self):

        long=len(self.ui.lineEdit_USUARIO.text())
        y=self.ui.lineEdit_USUARIO.text().isalnum()
        
        if y==False:
            self.ui.label_MSJUSER.setText("El nombre de usuario puede contener solo letras y números")
            self.ui.lineEdit_USUARIO.clear() #Borra el campo donde se escribe la contraseña
        if long < 6: 
            self.ui.label_MSJUSER.setText("El nombre de usuario debe contener al menos 6 caracteres")
            self.ui.lineEdit_USUARIO.clear() #Borra el campo donde se escribe la contraseña
        if long > 12: 
            self.ui.label_MSJUSER.setText("El nombre de usuario no puede contener más de 12 caracteres")
            self.ui.lineEdit_USUARIO.clear() #Borra el campo donde se escribe la contraseña
        if long >5 and long <13 and y ==True:
            self.ui.label_MSJUSER.setText("Usuario creado correctamente")
            

    def mensaje_password(self):
            
        user=False  #variable de inicialización para identificar espacios
        validar=False #variable de inicialización para identificar número de caracteres
        long=len(self.ui.lineEdit_PASSWORD.text()) #Calcula la longitud de la contraseña
        y=self.ui.lineEdit_PASSWORD.text().isalnum()#True si es alfanumérica, False si no lo es.(Nos interesa que sea False)
        mayuscula=False #variable iniciliazción para contar las letras mayúsculas
        minuscula=False #variable iniciliazción para contar las letras minúsculas
        numeros=False #variable iniciliazción para contar los números
        correcto=True

        for carac in self.ui.lineEdit_PASSWORD.text(): #ciclo for que recorre caracter por caracter en la contraseña

            if carac.isspace()==True: #Saber si el caracter es un espacio
                user=True #si encuentra un espacio se cambia el valor a True

            if carac.isupper()== True: #saber si hay mayuscula
                    mayuscula=True #Si encuentra al menos una Mayuscula cambia a True
                
            if carac.islower()== True: #saber si hay minúsculas
                    minuscula=True #Si encuentra al menos una minúscula cambia a True
                
            if carac.isdigit()== True: #saber si hay números
                    numeros=True #Si encuentra al menos un número cambia a True

        if user==True: #este valor indica que encontró un espacio
            self.ui.label_MSJPASS.setText("La contraseña no puede contener espacios")
            self.ui.lineEdit_PASSWORD.clear() #Borra el campo donde se escribe la contraseña
            
        else:
            validar=True #se escoge con el fin de garantizar que no hay espacios
            #y pasar al número mínimo de caracteres que contiene la contraseña
            
                       
        if long <8 and validar==True: #Se garantiza que la contraseña posea mínimo 8 caracteres sin espacios.
            self.ui.label_MSJPASS.setText("Mínimo 8 caracteres")
            self.ui.lineEdit_PASSWORD.clear() #Borra el campo donde se escribe la contraseña
            validar=False


        if mayuscula==True and minuscula==True and numeros==True and y==False and validar==True:  
            self.ui.label_MSJPASS.setText("La contraseña es correcta")
        else:
            correcto=False #Quiere decir que no cumple al menos uno de los requisitos

        if correcto==False and validar==True: #No cumpla al menos un requisito, no contiene espacios y es mayor o igual a 8 caracteres.
            self.ui.lineEdit_PASSWORD.clear()
            self.ui.label_MSJPASS.setText("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

if __name__== "__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = Miformulario()
    myapp.show()
    sys.exit(app.exec_())