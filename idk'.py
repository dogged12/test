from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)


@app.route('/', methods=['GET', 'POST'])
def guess_number():
    if request.method == 'POST':
        # Get the user's guess from the form
        guess = int(request.form['guess'])

        # Check if the guess is correct
        if guess == secret_number:
            message = "Congratulations! You guessed the correct number."
            return render_template('result.html', message=message)
        elif guess < secret_number:
            message = "Too low. Try again!"
        else:
            message = "Too high. Try again!"

        return render_template('index.html', message=message)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
