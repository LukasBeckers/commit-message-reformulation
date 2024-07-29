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

    prompt = f"You are a helpful assistant that reformulates commit messages to follow the GitHub semantic commit messages convention."
    response = openai.ChatCompletion.create(
        model=os.getenv("MODEL"),
        messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": f"Reformulate the following commit message to follow the GitHub semantic commit messages convention write just the reformulated commit message nothing else: {commit_message}"}
                ],
        max_tokens=60
    )

    reformulated_message = response['choices'][0]['message']['content'].strip()
    return jsonify({"reformulated_message": reformulated_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
