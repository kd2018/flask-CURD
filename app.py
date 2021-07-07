from re import A
from flask import Flask,render_template,request,redirect
from datetime import datetime
from typing import DefaultDict

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

# create model for the datafields

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    descri=db.Column(db.String(5000),nullable=False)
    

    def __repr__(self)->str: #when the data model exicute then how to print
        return f"{self.sno}-{self.descri}"


# route 1
@app.route('/' ,methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
       title=request.form['title']
       decription=request.form['decription']
       todo=Todo(title=title,descri=decription)
        # todo=Todo(title="first Todo second ",descri="start in django test ")
       db.session.add(todo)
       db.session.commit()
    allTodo=Todo.query.all()
    return  render_template('index.html',allTodo=allTodo)
    #this is the use of the return of templeteing



@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo.query.filter_by(sno=sno).first()
         # todo=Todo(title="first Todo second ",descri="start in django test ")
        todo.title=title
        todo.desc=desc
        todo=Todo(title=title,descri=desc)
        db.session.add(todo)
        db.session.commit()
    todo=Todo.query.filter_by(sno=sno).first()
    return  render_template('update.html',todo=todo)

# route 2
@app.route('/test')

def test():
    
    return 'this is production page'

# route 2
@app.route('/show')

def show():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)