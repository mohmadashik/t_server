from chalice import Chalice

app = Chalice(app_name='t_server')


@app.route('/')
def index():
    return {'hello': 'world'}


# In-memory user data for demo purposes
users = {
    "ramu@mail.com": "ramu@123"
}

@app.route('/login', methods=['POST'])
def login():
    # data = request.json
    print('entry into login')
    request = app.current_request
    data = request.json_body
    # Extract email and password from request data
    email = data.get('email')
    password = data.get('password')
    print(f'email : {email}, password : {password}')
    # Validate input fields
    if not email or not password:
        print('email and password are required')
        return {'error': 'Email and password are required'}, 400
    
    # Check credentials (demo purpose, no DB here)
    if email in users and users[email] == password:
        print('login successfull')
        return {'message': 'Login successful', 'user': email}, 200
    else:
        print('invalid email or password')
        return {'error': 'Invalid email or password'}, 401

if __name__ == '__main__':
    app.run(debug=True)



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
