from flask import Flask, request, render_template, jsonify
import cohere

app = Flask(__name__)

co = cohere.Client(api_key="UkJsf5LTHL1g0Gk1re82j50ieqdLfxWQUI2pEz4D")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_knowledge', methods=['POST'])
def get_knowledge():
    try:
        user_input = request.form['user_input']
        response = ""
        stream = co.chat_stream(message=user_input)

        for event in stream:
            if event.event_type == "text-generation":
                response += event.text

        return jsonify({'knowledge': response}), 200
    except KeyError:
        return jsonify({'error': 'Invalid request format. Please provide user_input in the request.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.after_request
def add_cache_control_headers(response):
    response.headers['Cache-Control'] = 'private, max-age=86400'
    return response

# Add the x-content-type-options header
@app.after_request
def add_content_type_options_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

if __name__ == '__main__':
    app.run(debug=True)