import random
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

pokeneas = [
    {"id": 1, "nombre": "Pokenea1", "altura": 1.5, "habilidad": "Fuerza", "imagen": "https://storage.googleapis.com/pokeneas-danniela/poke1.png", "frase": "¿Por que tan debil, mano? La fuerza esta en el amor."},
    {"id": 2, "nombre": "Pokenea2", "altura": 1.3, "habilidad": "Velocidad", "imagen": "https://storage.googleapis.com/pokeneas-danniela/poke2.jpeg", "frase": "3 steps ahead, always 3 steps ahead."},
    {"id": 3, "nombre": "Pokenea3", "altura": 1.5, "habilidad": "Fuego", "imagen": "https://storage.googleapis.com/pokeneas-danniela/poke3.jpeg", "frase": "Que tu fuego queme a los demas de amor."},
    {"id": 4, "nombre": "Pokenea4", "altura": 1.3, "habilidad": "Agua", "imagen": "https://storage.googleapis.com/pokeneas-danniela/poke5.jpeg", "frase": "La calma precede a la tormenta."},
    {"id": 5, "nombre": "Pokenea5", "altura": 1.3, "habilidad": "Tierra", "imagen": "https://storage.googleapis.com/pokeneas-danniela/poke6.jpeg", "frase": "Se tan firme como una montaña y nadie te podra mover."},
    {"id": 6, "nombre": "Pokenea6", "altura": 1.3, "habilidad": "Aire", "imagen": "https://storage.googleapis.com/pokeneas-danniela/poke7.jpeg", "frase": "Que tus buenas acciones sean llevadas con el viento, no las muestres.."},
    {"id": 7, "nombre": "Pokenea7", "altura": 1.3, "habilidad": "Hielo", "imagen": "https://storage.googleapis.com/pokeneas-danniela/poke8.jpeg", "frase": "La sobriedad es la cuspide del ser humano."},
]

@app.route('/pokejson', methods=['GET'])
def poke_json():
    poke = random.choice(pokeneas)
    return jsonify({
        "id": poke["id"],
        "nombre": poke["nombre"],
        "altura": poke["altura"],
        "habilidad": poke["habilidad"],
        "container_id": "https://storage.cloud.google.com/pokeneas-danniela/poke2.webp"
    })

@app.route('/pokeimage', methods=['GET'])
def poke_image():
    poke = random.choice(pokeneas)
    return render_template_string("""
        <img src="{{ poke['imagen'] }}" alt="Pokenea">
        <p>{{ poke['frase'] }}</p>
        <p>Container ID: {{ container_id }}</p>
    """, poke=poke, container_id="https://storage.cloud.google.com/pokeneas-danniela/poke1.webp")

if __name__ == '__main__':
    print("Flask está corriendo...")
    app.run(debug=True)
