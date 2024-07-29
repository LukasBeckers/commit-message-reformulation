from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

@app.route('/reformulate', methods=['POST'])
def reformulate_commit_message():
    data = request.json
    commit_message = data.get('commit_message')
    api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = api_key

    prompt = f"Reformulate the following commit message to follow the GitHub semantic commit messages convention: {commit_message}"
    response = openai.Completion.create(
        engine=os.getenv("MODEL"),
        prompt=prompt,
        max_tokens=60
    )

    reformulated_message = response.choices[0].text.strip()
    return jsonify({"reformulated_message": reformulated_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv("PORT"))
