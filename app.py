from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from test_model import Human



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def inex():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/exercise_request/<a>')
def exercise_request(a):
    return f'{a}'

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')


@app.route('/excersize')
def excersize():
    return render_template('exercise.html')

@app.route('/exercise')
def exercise():
    return render_template('answer.html', name=request.args.get("my_name"))


@app.route('/try_rest', methods=['POST'])
def try_test():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    
    
    for i in response_json['response_json']['friends']:
        print(i)

    
    return jsonify(response_json)


@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    search_weight = request.args.get("search_weight")
    persons = db.session.query(Human).filter(Human.weight > search_weight)
    return render_template('./person_result.html', persons=persons, search_weight=search_weight)


@app.route('/try_html')
def try_html():
    return render_template('./try_html.html')

@app.route('/show_data',methods=["GET","POST"])
def show_data():
    print(request.form["submit"])
    return render_template('./try_html.html')