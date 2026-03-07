from flask import Flask
import random 
facts_list = [
    "The Earth is the only planet in our solar system that has liquid water on its surface.",
    "The Great Wall of China is the longest wall in the world, stretching over 13,000 miles.",
    "The human brain is the most complex organ in the body, containing over 100 billion neurons.",
    "The Amazon rainforest is home to over 10% of the world's known species.",
    "The speed of light is approximately 299,792,458 meters per second.",
    "The tallest mountain in the world is Mount Everest, standing at 29,029 feet.",
    "The Great Barrier Reef is the largest coral reef system in the world, stretching over 1,400 miles.",
]
chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=`~!@#$%^&*()_+"
app = Flask(__name__)
@app.route('/')
def say_hello():
    return '<h1>Hello World</h1><a href="facts">Click here for a random fact</a><br><a href="secret">Click here to go to the secret page</a>'

@app.route('/facts')
def say_facts():
    return  f'<h1>{random.choice(facts_list)}</h1><a href="/">Click here to go back to the homepage!</a>'
@app.route('/secret')
def secret():
    return f'<h2>This is a secret page!</h2><a href="/">Click here to go back to the homepage!</a><h3>Random Password</h3><h2>Your Password is:</h2><h1>{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}</h1> '
if __name__ == '__main__': 
    app.run(debug=True)   

    
