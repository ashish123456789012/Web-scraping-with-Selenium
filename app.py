import threading
from flask import Flask, jsonify, send_from_directory
from selenium_script import get_trending_topics
import logging

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/run_script')
def run_script():
    result = {}

    def selenium_task():
        nonlocal result
        result = get_trending_topics()
        app.logger.info(f"Fetched trending topics: {result}")

    thread = threading.Thread(target=selenium_task)
    thread.start()
    thread.join()

    return jsonify(result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
