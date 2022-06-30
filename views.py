from flask import Flask, jsonify, make_response,render_template,request
import urllib.request, json

app = Flask(__name__)

def jsonify(status=200, indent=4, sort_keys=True, **kwargs):
    response = make_response(json.dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = status
    return response

@app.route('/',methods=('GET','POST'))
def my_form():
    return render_template('my-form.html')

@app.route('/fetch_users/', methods=('GET','POST'))
def retrieve_data():
   tech = '' #default
   if request.method == 'POST': 
      tech = request.form['text']

   with urllib.request.urlopen("https://github-trending-api.de.a9sapp.eu/") as url:
      data = json.loads(url.read().decode())
      
      result_list = []
      for each_data in data:
         if each_data.get('language') and each_data['language'].strip().lower() == tech.strip().lower():                    
                  result1 = {}
                  result1['username'] = each_data['author']
                  result1['name'] = each_data['author']
                  result1['repo'] = {'name' : each_data['name']}
                  result1['avatar'] = each_data['avatar']
                  result1['url'] = each_data['url']
                  result1['description'] = each_data['description']
                  result_list.append(result1)
      return jsonify(indent=2, sort_keys=False, result=result_list)

app.add_url_rule('/', my_form)      
app.add_url_rule('/', 'fetch_users', retrieve_data)
if __name__ == '__main__':
   app.run()