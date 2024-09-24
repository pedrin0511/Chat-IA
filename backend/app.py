from flask import Flask, request, jsonify
from flask_cors import CORS  # Adicione esta linha
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Ativando o cors

# Configurando a API do Gemini
Api_gemini = os.getenv('API_KEY')
genai.configure(api_key=Api_gemini)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.get_json()
    user_input = data.get('question')

    # Gerando resposta da IA
    response = model.generate_content(
        user_input,
         generation_config=genai.types.GenerationConfig(
          candidate_count=1,
          max_output_tokens=10,
          temperature=1.0,   
         ),
         )
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
