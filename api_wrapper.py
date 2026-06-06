from flask import Flask, jsonify, request
from prompt_generator import DarkFantasyPortraitGenerator

app = Flask(__name__)
generator = DarkFantasyPortraitGenerator()

@app.route('/api/generate-prompt', methods=['GET'])
def generate_prompt():
    prompt = generator.generate_prompt()
    return jsonify({
        "success": True,
        "prompt": prompt,
        "skill": "dark-fantasy-portrait-prompt",
        "version": "1.0.0"
    })

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({
        "success": True,
        "message": "Dark Fantasy Portrait Prompt API is working!"
    })

if __name__ == '__main__':
    print("Starting Dark Fantasy Portrait Prompt API...")
    app.run(port=5000, debug=True)
