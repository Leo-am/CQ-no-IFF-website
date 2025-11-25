from flask import Flask, render_template, request, send_file
import numpy as np
from qutip import Bloch
import io

app = Flask(__name__)

def gerar_bloch(theta, phi):
    theta = np.radians(theta)
    phi = np.radians(phi)

    x = np.cos(phi) * np.sin(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(theta)

    b = Bloch()
    b.add_vectors([x, y, z])
    b.vector_width = 4
    b.view = [120, 30]

    buffer = io.BytesIO()
    b.save(buffer, format='png')
    buffer.seek(0)
    return buffer

@app.route("/")
def index():
    return render_template("site.html")

@app.route("/bloch_image")
def bloch_image():
    theta = float(request.args.get("theta", 45))
    phi = 0
    img = gerar_bloch(theta, phi)
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)