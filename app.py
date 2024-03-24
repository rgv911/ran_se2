from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
       
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
       
        return redirect(url_for('hello', name=name))
   
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    with app.app_context():
         db.create_all()  # יוצר את הטבלה בבסיס הנתונים, כאשר היישום נפתח
    app.run(debug=True)