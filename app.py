from flask import Flask, render_template, request
import joblib

# intialise the appfile 
# if we run this directly from python then __name__ will be __main__
# if we execute thi file as module from some other file then __name__ will become name of the file.
app = Flask(__name__)
# load the model
model = joblib.load('diab_75.pkl')

@app.route('/') 
def hello():
    return render_template('form.html')
# @app.route('/home')
# def home():
#     return render_template('index.html')
# @app.route('/contacts')
# def contact():
#     return 'contact home page'
@app.route('/submit',methods = ['post'])
def form_data():
#    first_name =  request.form.get('fname')
#    second_name= request.form.get('sname')
#    ph = request.form.get('phno')
#    email = request.form.get('email')
#    dob = request.form.get('dob')
#    print(first_name,second_name,ph,email,dob)
   a =  request.form.get('a')
   b =  request.form.get('b')
   c =  request.form.get('c')
   d =  request.form.get('d')
   e =  request.form.get('e')
   f =  request.form.get('f')
   g =  request.form.get('g')
   h =  request.form.get('h')
   # insert data into database
   output = model.predict([[a,b,c,d,e,f,g,h]])
   print(output)
   if output[0] == 1:
    out = "diabetic" 
   else:
    out = "not diabetic"

   return render_template('index.html',data = f'Person is {out}')
if __name__ == '__main__':
    app.run(debug = True) # changes made will automatically reflected.
    # no need to cloe server for changes to be visible just use refresh button on web page.