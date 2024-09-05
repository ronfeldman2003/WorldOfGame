from flask import Flask
from Utils import SCORES_FILE_NAME


def score_server():
    app = Flask(__name__)

    try:
        file = open(SCORES_FILE_NAME, "r")
        score_current = int(file.read())
        @app.route("/")
        def hello_world():
            return f'''
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is <div id="score">{score_current}</div></h1>
                </body>
            </html>'''
    except FileNotFoundError as e:
        ERROR = str(e)
        print(ERROR)
        @app.route("/")
        def hello_world():
            return f'''
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1><div id="score" style="color:red">{ERROR}</div></h1>
                    </body>
                </html>'''

    app.run(host="0.0.0.0", port=3000, debug=True)

##score_server()
