from flask import Flask, request
from agent import agent_executor

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
  print('Received new webhook: ', request.json)
  try:
    # TODO: Listen specifically to the chatbot mention events and run on that
    response = agent_executor.invoke({"input": request.json})
    return response
  except Exception as e:
    print(e)
    return '', 200

if __name__ == '__main__':
  app.run(port=2000, debug=True)