# task 1 ********************************

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World!"

# @app.route('/welcome')
# def welcome():
#     return "Welcome!"


# @app.route('/welcome/home')
# def welcome_home():
#     return "Welcome home!"

# @app.route('/welcome/back')
# def welcome_back():
#     return "Welcome back!"

# @app.route('/sum')
# def sum():
#     t=5+5
#     return str(t)

# task 2 ********************************


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome!"

# #let's make up a parameter called name. Its value is going to be WHATEVER someone requests, but we will respond with the string "The name is" along with the value in the URL.
# @app.route('/name/<person>')
# def say_name(person):
#     return f"The name is {person}"

# # since all URL parameters are strings, we can convert them right away to another data type in our route definition
# @app.route('/name/<int:num>')
# def favorite_number(num):
#     return f"Your favorite number is {num}, which is half of {num * 2}"

# # since all URL parameters are strings, we can convert them right away to another data type in our route definition
# @app.route('/add/<int:num_>/<int:num__>')
# def add(num_,num__):
#     return f"Sum {num_+num__}."

# task 3 ********************************

# from flask import Flask
# app = Flask(__name__)

# @app.route('/math/add/<int:num_>/<int:num__>')
# def add(num_,num__):
#     return f"Sum {num_+num__}."

# task 4 ********************************

# from flask import Flask, render_template # we are now importing just more than Flask!

# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     names_of_instructors = ["Elie", "Tim", "Matt"]
#     random_name = "Tom"
#     return render_template('index.html', names=names_of_instructors, name=random_name)

# @app.route('/second')
# def second():
#     return "WELCOME TO THE SECOND PAGE!"

# @app.route('/title')
# def title():
#     return render_template('title.html')

# task 5 ********************************

# from flask import Flask, render_template, request # we are now importing just more than Flask!

# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     names_of_instructors = ["Elie", "Tim", "Matt"]
#     random_name = "Tom"
#     return render_template('index.html', names=names_of_instructors, name=random_name)

# @app.route('/second')
# def second():
#     return "WELCOME TO THE SECOND PAGE!"

# @app.route('/title')
# def title():
#     return render_template('title.html')

# # we need a route to render the form
# @app.route('/show-form')
# def show_form():
#     return render_template('first-form.html')

# # we need to do something when the form is submitted
# @app.route('/data')
# def print_name():
#     first = request.args.get('first')
#     last = request.args.get('last')
#     return f"You put {first} {last}"

# task 6 ********************************

# from types import AsyncGeneratorType
# from flask import Flask, render_template, request # we are now importing just more than Flask!

# app = Flask(__name__)

# @app.route('/person/<name>/<int:age>')
# def person(name,age):
#     return  render_template('person.html',name_=name, age_=age)

# @app.route('/math/<operation>/<int:num_>/<int:num__>')
# def operation(operation,num_,num__):
#     temp=0
    
#     if(operation=='add'):
#         temp=num_+num__
#     elif(operation=='sub'):
#         temp=num_-num__
#     elif(operation=='mul'):
#         temp=num_*num__ 
#     elif(operation=='div'):
#         temp=num_/num__
         
#     return f"{operation} equal {temp}." 

# task 7 ********************************

# from types import AsyncGeneratorType
# from flask import Flask, render_template, request # we are now importing just more than Flask!

# app = Flask(__name__)

# @app.route('/person/<name>/<int:age>')
# def person(name,age):
#     return  render_template('person.html',name_=name, age_=age)

# @app.route('/calculate')
# def show_form():
#     return render_template('calc.html')

# @app.route('/math')
# def operation(operation,num_,num__):
#     temp=0
    
#     if(operation=='add'):
#         temp=num_+num__
#     elif(operation=='sub'):
#         temp=num_-num__
#     elif(operation=='mul'):
#         temp=num_*num__ 
#     elif(operation=='div'):
#         temp=num_/num__
         
#     return f"{operation} equal {temp}." 


# @app.route('/data')
# def operation_pvt():
#     first = request.args.get('num_1')
#     last = request.args.get('num_2')
#     operation_1 = request.args.get('calcultion')
    
#     return  operation(operation_1,int(first),int(last))

# task 8 ********************************

# failed code? i don't understand how its to do
# import urllib.request
# from bs4 import BeautifulSoup
# from types import AsyncGeneratorType
# from flask import Flask, render_template, request # we are now importing just more than Flask!

# app = Flask(__name__)

# @app.route('/')
# def news():
#     return render_template('screping.html')

# def find_headline_by_keyword(hlines, kwds):
#     return [headline for headline in hlines if kwds.lower() in headline.lower()]


# @app.route('/results')
# def data_results():
#     key_words = request.args.get('keyword')
    
#     url = 'https://news.google.com'
#     data = urllib.request.urlopen(url).read()
#     print(data)
#     soup = BeautifulSoup(data, "html.parser")
#     titles = soup.select(".titletext")
#     headlines = [title.text for title in titles]

#     return  find_headline_by_keyword(headlines, key_words)

# task 9 ********************************

from  flask  import  Flask , render_template , redirect , url_for , request 
from  flask_modus  import  Modus 
from  toy  import  Toy
 
app = Flask(__name__) 
modus = Modus(app) # ...

duplo = Toy(name='duplo')
lego = Toy(name='lego')
knex = Toy(name='knex')

toys = [duplo,lego,knex]

@app.route('/toys', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # gather the value of an input with a name attribute of "name"
        toys.append(Toy(request.form['name']))
        print(url_for('index'))
        # respond with a redirect to the route which has a function called "index" (in this case that is '/toys')
        return redirect(url_for('index'))
    # if the method is GET, just return index.html 
    # тут якби ця функція додає і одночасно бере виводить тоді іграшки, бо переспрямування повертає нас на цю ж функцію
    return render_template('index_crud.html', toys=toys)

@app.route('/toys/new')
def new():
    return render_template('new.html')

# @app.route('/toys/<int:id>', methods=["GET", "PATCH"])
# def show(id):
#     # Refactored using a generator so that we do not need to do [0]!
#     found_toy = next(toy for toy in  toys if toy.id == id)

#     # if we are updating a toy...
#     if request.method == b"PATCH":
#         found_toy.name = request.form['name']
#         return redirect(url_for('index'))
#     # if we are showing information about a toy
#     return render_template('show.html', toy=found_toy)


# @app.route('/toys/<int:id>/edit')
# def edit(id):
#     # Refactored using a list comprehension!
#     found_toy = [toy for toy in  toys if toy.id == id][0]
#     # Refactor the code above to use a generator so that we do not need to do [0]!
#     return render_template('edit.html', toy=found_toy)

# почалися на цьому завданні проблеми з бібліотеками необхідно створити нове віртуальне середовище бо наінсталював досить багато лишнього