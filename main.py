#importacion de librerias
from flask import Flask,render_template
#creacion de objeto de tipo flask
app = Flask(__name__)
#creacion de ruta raiz a pagina principal
@app.route("/")
#creacion de funcion para llamar a index
def index():

    return render_template('index.html')


#Configuracion de archivo principal de ejecucion
if __name__ == '__main__':
    #configuracion del puerto de escucha del servidor web
   app.run(port=80,debug = True)
