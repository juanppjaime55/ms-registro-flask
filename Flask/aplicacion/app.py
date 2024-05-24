from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # Permitir tanto GET como POST
def home():
    
    if request.method == 'POST':

        name = request.form['nombre']
        edad = request.form['edad']
        nacionalidad = request.form['nacionalidad']
        documento = request.form['documento']
        
        # Define la URL de la aplicación Django
        django_url = 'http://34.122.68.2:8080/crearSolicitud'

        # Datos que se enviarán a Django
        data = {
            'nombre': name,
            'edad': edad,
            'documento': documento,
            'nacionalidad': nacionalidad
        }

        response = requests.post(django_url, data=data)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
