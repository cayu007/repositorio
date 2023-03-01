import openai_secret_manager
import openai
import json

# Cargar las credenciales de OpenAI
secrets = openai_secret_manager.get_secret("openai")

# Autenticar con OpenAI
openai.api_key = secrets["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"]

# Definir las preguntas y respuestas
preguntas_respuestas = {
    "¿Cuál es tu nombre?": "Mi nombre es Chatbot",
    "¿Cómo estás?": "Estoy bien, gracias por preguntar.",
    "¿Qué puedes hacer?": "Puedo responder preguntas simples y mantener una conversación básica.",
    "¿Cómo se hace una tortilla?": "Para hacer una tortilla, necesitas huevos, leche y una sartén. Primero, bate los huevos y la leche juntos en un tazón. Calienta la sartén a fuego medio y agrega la mezcla de huevos. Cocina la tortilla durante unos minutos, volteándola una vez, hasta que esté dorada y cocida por ambos lados. ¡Y eso es todo!",
    "¿Cuál es tu color favorito?": "No tengo un color favorito, soy un chatbot y no tengo preferencias personales.",
    "¿Qué es el amor?": "El amor es un sentimiento profundo de afecto y cuidado por otra persona o cosa.",
}

# Función para generar respuestas utilizando la API de OpenAI
def generar_respuesta(pregunta):
    prompt = (f"La siguiente es una conversación entre un usuario y un chatbot. El usuario pregunta: {pregunta}\n"
              "El chatbot responde:"
             )
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=10,
    )
    respuesta = completions.choices[0].text.strip()
    return respuesta
