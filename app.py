from flask import Flask, request, jsonify
from chatbot import generar_respuesta

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    pregunta = request.json['pregunta']
    respuesta = generar_respuesta(pregunta)
    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(debug=True)
