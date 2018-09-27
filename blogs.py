# __*__ coding:utf-8 __*__
from flask import Flask,url_for,redirect,request,render_template
import time

app = Flask(__name__)

users = []

def save(fname,txt):
    eth = file(fname,'w')
    eth.write('\t%s'%txt)
    eth.close()


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', says=users)
    else:
        resign = request.form.get('resigntxt')
        print resign
        if resign == '1':

            return redirect('/txt/')
        else:
            print '标志出错！！！'

@app.route('/txt/', methods=['GET','POST'])
def edit():
    if request.method == 'GET':
        return render_template('edit.html')
    else:
        txt = request.form.get('ideatxt')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        users.append({"txt": txt,
                      "date": date})
        print users
        save('suggest.txt', users)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)