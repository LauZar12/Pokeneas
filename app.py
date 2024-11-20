import random
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

pokeneas = [
    {"id": 1, "nombre": "Pokenea1", "altura": 1.5, "habilidad": "Fuerza", "imagen": "https://storage.googleapis.com/pokeneas-imagenes/p9.png", "frase": "Siempre adelante."},
    {"id": 2, "nombre": "Pokenea2", "altura": 1.3, "habilidad": "Velocidad", "imagen": "https://storage.googleapis.com/pokeneas-imagenes/p8.webp", "frase": "La calma precede a la tormenta."},
    {"id": 3, "nombre": "Pokenea3", "altura": 1.5, "habilidad": "Fuego", "imagen": "https://storage.googleapis.com/pokeneas-imagenes/p7.jpg", "frase": "Siempre adelante."},
    {"id": 4, "nombre": "Pokenea4", "altura": 1.3, "habilidad": "Agua", "imagen": "https://storage.googleapis.com/pokeneas-imagenes/p6.webp", "frase": "La calma precede a la tormenta."},
    {"id": 5, "nombre": "Pokenea5", "altura": 1.3, "habilidad": "Tierra", "imagen": "https://storage.googleapis.com/pokeneas-imagenes/p4.png", "frase": "La calma precede a la tormenta."},
    {"id": 6, "nombre": "Pokenea6", "altura": 1.3, "habilidad": "Aire", "imagen": "https://storage.googleapis.com/pokeneas-imagenes/p1.jpg", "frase": "La calma precede a la tormenta."},
    {"id": 7, "nombre": "Pokenea7", "altura": 1.3, "habilidad": "Hielo", "imagen": "https://storage.googleapis.com/pokeneas-imagenes/p10.jpg", "frase": "La calma precede a la tormenta."},
]

@app.route('/pokejson', methods=['GET'])
def poke_json():
    poke = random.choice(pokeneas)
    return jsonify({
        "id": poke["id"],
        "nombre": poke["nombre"],
        "altura": poke["altura"],
        "habilidad": poke["habilidad"],
        "container_id": "ID_DEL_CONTENEDOR"
    })

@app.route('/pokeimage', methods=['GET'])
def poke_image():
    poke = random.choice(pokeneas)
    return render_template_string("""
        <img src="{{ poke['imagen'] }}" alt="Pokenea">
        <p>{{ poke['frase'] }}</p>
        <p>Container ID: {{ container_id }}</p>
    """, poke=poke, container_id="ID_DEL_CONTENEDOR")

if __name__ == '__main__':
    print("Flask está corriendo...")
    app.run(debug=True)
