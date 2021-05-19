import toml 

from flask import Flask


app = Flask('__name__')
app.config.from_file('config.toml', toml.load)

# Deprecated version:
# app.config.from_json('config.json')


# Uncomment the following lines to see the loaded values
# print(app.config['DEBUG'])
# print(app.config['SECRET_KEY'])


@app.get('/first')
def my_get_endpoint():
    return 'This was a GET request.'

# Example not using the syntatic sugar
# @app.route('/first', methods=['GET'])
# def my_get_endpoint():
#     return 'This was a GET request.'


@app.post('/second')
def my_post_endpoint():
    return 'This was a POST request.'


# Example not using the syntatic sugar
# @app.route('/second', methods=['POST'])
# def my_post_endpoint():
#     return 'This was a POST request.'


@app.put('/third')
def my_put_endpoint():
    return 'This was a PUT request.'


# Example not using the syntatic sugar
# @app.route('/third', methods=['PUT'])
# def my_put_endpoint():
#     return 'This was a PUT request.'
