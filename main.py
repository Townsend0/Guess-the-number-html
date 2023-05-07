from flask import Flask
from random import randint

random_no = randint(0, 9)
app = Flask(__name__)

@app.route('/')
def home():
    return '''<h1>Guess a number between 0 and 9</h1><br>
    <img src="https://media2.giphy.com/media/JdFEeta1hLNnO/giphy.gif?cid=ecf05e47y6
    sfqqlov286fki2e2f35dw73if696rlnpaz8sgf&ep=v1_gifs_search&rid=giphy.gif&ct=g">'''
    
@app.route('/<int:guess>')
def check_guess(guess):
    if guess < random_no:
        return '''<h1>Higher</h1><br><img src="https://media4.giphy.com/media/SDi3kPcN4mILsLKgQc/giphy.gif?
        cid=ecf05e47b6iivl6x9gsg4t93zqyejfbgv8linsfkmon5qdhf&ep=v1_gifs_search&rid=giphy.gif&ct=g">'''
    elif guess > random_no:
        return '''<h1>Lower</h1><br><img src="https://media4.giphy.com/media/2A1HVPlfT4SvvMABqq/giphy.gif?cid
        =ecf05e47kvdesbj7g3h4t6q6oy0sm1ycxmzk5fqma3rjhkfq&ep=v1_gifs_search&rid=giphy.gif&ct=g">'''
    elif guess == random_no:
        return '''<h1>Congrats you got it right</h1><br><img src="https://media4.giphy.com/media/psmj7c3DbrJKkbRYFj/giphy.gif?
        cid=ecf05e47zpbqbmmz1cz6e4l8zm3kxm13pi8o2rxp4ouka3ig&ep=v1_gifs_search&rid=giphy.gif&ct=g">'''

if __name__ == '__main__':
    app.run(debug = True)