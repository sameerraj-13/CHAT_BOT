# import openai
# from flask import Flask, request, render_template, jsonify

# app = Flask(__name__)

# # Set OpenAI API key
# openai.api_key = "API_KEY"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get("message")
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": user_input}
#         ]
#     )
#     bot_response = response.choices[0].message['content'].strip()
#     return jsonify({"response": bot_response})

# if __name__ == '__main__':
#     app.run(debug=True, port=none)  # Change the port number if needed

# msg = str(input("Enter the query:"))
# print ("Hello",msg)


msg = str(input("Enter the query:"))
print ("Hello",msg)