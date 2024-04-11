from flask import Flask, render_template, request, redirect, make_response # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Создаем куки с данными пользователя
        response = make_response(render_template('welcome.html', name=name))
        response.set_cookie('user_data', f'{name}:{email}')
        return response

@app.route('/logout')
def logout():
    # Удаляем куки с данными пользователя
    response = make_response(redirect('/'))
    response.set_cookie('user_data', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
