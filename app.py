from flask import Flask, request, jsonify, render_template
from nlp_analyzer import analyze_conversation  # Replace with your actual module and function

app = Flask(__name__)

@app.route('/')
def home():
    # Render the index.html template
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    screen_time = data.get('screenTime', '0')
    activity = data.get('activity', '')

    # Call your analysis function to process the input data
    try:
        result = analyze_conversation(screen_time, activity)
        response = {'analysis': result}
    except Exception as e:
        response = {'error': str(e)}

    # Return the analysis as JSON to be displayed on the frontend
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
