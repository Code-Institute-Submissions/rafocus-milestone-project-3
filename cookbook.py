from flask import Flask, render_template
app = Flask(__name__)

recipes = [
    {
        'name': 'recipe 1',
        'description': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sapiente, rem?',
        'method': ['step1', 'step 2', 'step 3'],
        'picture': 'https://dummyimage.com/300' 
    },
    {
        'name': 'recipe 2',
        'description': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sapiente, rem?',
        'method': ['step1', 'step 2', 'step 3'],
        'picture': 'https://dummyimage.com/300' 
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', recipes=recipes)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)