
from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='Templates')


@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    return render_template("proyectos.html")

@app.route('/quienes-somos')
def quienesomos():
    return render_template("quienessomos.html")

@app.route('/staff')
def staff():
    return render_template("staff.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/noticias')
def noticias():
    return render_template("noticias.html")


if __name__ == "__main__":
    app.run(debug=True)



'''

@app.route('/hola/')
@app.route('/hola/<string:nombre>')
@app.route('/hola/<string:nombre>/<int:edad>')
def hola(nombre=None,edad=None):
    if nombre and edad:
        return "Hola, {0} tienes {1} años".format(nombre,edad)
    elif nombre:
        return "Hola, {0}".format(nombre)
    else:
        return "Hola mundo"

'''


    

