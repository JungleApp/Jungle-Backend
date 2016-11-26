# JUNGLE
# App-Backend
# Last Revision: 11/26/16

# ip: 138.197.4.56

from flask import Flask, request, session, g, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Jungle</h1>
    <br/>
    <h4>Wow. What an exciting application!</h4>
    '''

if __name__ == '__main__':
    app.run(debug=True)