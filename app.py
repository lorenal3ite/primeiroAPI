from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}'


@app.route('/soma/<int:num1>+<int:num2>')
def soma(num1, num2):
    return (f'Soma: {num1} + {num2} = {num1 + num2}')


@app.route('/multiplicacao/<int:num1>*<int:num2>')
def multiplicacao(num1, num2):
    return (f'Soma: {num1} * {num2} = {num1 * num2}')

@app.route('/divisao/<int:num1>/<int:num2>')
def divisao(num1, num2):
    return (f'Soma: {num1} / {num2} = {num1 / num2}')

@app.route('/subtracao/<int:num1>-<int:num2>')
def subtracao(num1, num2):
    return (f'Soma: {num1} - {num2} = {num1 - num2}')

@app.route("parImpar:{n1}")
def parImpar(n1):
    if n1 % 2 == 0:
        return True
    else:
        return False
@app.route('/impar:{n1}')
def impar(n1):
    if n1 % 2 == 0:
        return True
    else:
        return False

if __name__=='__main__':
  app.run(debug=True)







