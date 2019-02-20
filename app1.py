from flask import Flask, render_template, request, url_for,redirect
app = Flask(__name__)

@app.route('/')
def Add():
   return render_template('result.html')

@app.route('/form_1',methods=["GET","POST"])
def form_1():

   if request.method=="POST":

      a=request.form.get('nm1',type=int)
      b = request.form.get('nm2', type=int)

      result= a+b
      resp(make_response(render_template(form_1.html)))
      resp.set_cookie('id',result)

      return resp

if __name__ == '__main__':
   app.run(debug = True)