from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# {"data":["a","b","1"]}
@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ABCD123</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@100..900&display=swap');

        .hidden {
            display: none;
        }

        body {
            padding: 0;
            margin: 0;
            font-family: "Lexend", sans-serif;
            background-color: #f0f4f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            padding: 2rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 600px;
        }

        h1 {
            margin-bottom: 1.5rem;
            color: #0172bd;
        }

        textarea {
            width: 100%;
            border-radius: 5px;
            box-shadow: 0px 0px 5px -2px black;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid #ccc;
            font-size: 1rem;
        }

        button {
            width: 100%;
            border-radius: 5px;
            box-shadow: 0px 0px 5px -2px black;
            border: none;
            padding: 0.75rem;
            background-color: #0172bd;
            color: white;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #025a9a;
        }

        .response {
            margin-top: 2rem;
        }

        .response h2 {
            color: #0172bd;
        }

        .checkboxes {
            margin-top: 1rem;
        }

        .checkboxes label {
            display: block;
            margin-bottom: 0.5rem;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Assignment</h1>
        <form id="jsonForm">
            <textarea id="jsonInput" rows="6" cols="50" placeholder="Enter JSON data here..."></textarea><br>
            <button type="button" onclick="submitJson()">Submit</button>
        </form>
        <div id="response" class="response">
            <h2>Response</h2>
            <pre id="responseData"></pre>
            <div class="checkboxes">
                <label><input type="checkbox" id="showNumbers" onclick="toggleSection()"> Numbers</label>
                <label><input type="checkbox" id="showAlphabets" onclick="toggleSection()"> Alphabets</label>
                <label><input type="checkbox" id="showHighestAlphabet" onclick="toggleSection()"> Highest Alphabet</label>
                <label><input type="checkbox" id="showHighestNumber" onclick="toggleSection()"> Highest Number</label>
            </div>
            <div id="numbersSection" class="hidden"></div>
            <div id="alphabetsSection" class="hidden"></div>
            <div id="highestAlphabetSection" class="hidden"></div>
            <div id="highestNumberSection" class="hidden"></div>
        </div>
    </div>
    <script>
        function submitJson() {
            const jsonInput = document.getElementById('jsonInput').value;
            const url = '/bfhl';

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonInput
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('responseData').textContent = JSON.stringify(data, null, 2);
                    document.getElementById('numbersSection').textContent = `Numbers: ${data.numbers.join(', ')}`;
                    document.getElementById('alphabetsSection').textContent = `Alphabets: ${data.alphabets.join(', ')}`;
                    document.getElementById('highestAlphabetSection').textContent = `Highest Alphabet: ${data.highest_alphabet.join(', ')}`;
                    document.getElementById('highestNumberSection').textContent = `Highest Number: ${data.highest_number.join(', ')}`;
                })
                .catch(error => console.error('Error:', error));
        }

        function toggleSection() {
            document.getElementById('numbersSection').classList.toggle('hidden', !document.getElementById('showNumbers').checked);
            document.getElementById('alphabetsSection').classList.toggle('hidden', !document.getElementById('showAlphabets').checked);
            document.getElementById('highestAlphabetSection').classList.toggle('hidden', !document.getElementById('showHighestAlphabet').checked);
            document.getElementById('highestNumberSection').classList.toggle('hidden', !document.getElementById('showHighestNumber').checked);
        }
    </script>
</body>

</html>
'''

@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    data = request.json.get('data', [])
    numbers = [int(x) for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []
    highest_number = [str(max(numbers))] if numbers else []

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet,
        "highest_number": highest_number
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run()
