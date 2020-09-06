from flask import Flask, Response, request, render_template
import requests
import hashlib
import redis
import html

import data

app = Flask(__name__)

cache = redis.StrictRedis(host='redis', port=6379, db=0)
salt = "UNIQUE_SALT"
default_name="test"


@app.route('/', methods=['GET', 'POST'])
def index():
    # 1) Fetch the input each one has (metadata and data)
    # 2) for each input use the metadata to choose how to display each data
    # 3) add to the template all the input with way of displaying it

    d = data.get_apple_stock_price()
    d2 = data.get_amazon_stock_price()

    items = []
    items.append(d)
    items.append(d2)

    return render_template("index.html", len=len(items), items=items)
#
#     name = default_name
#     if request.method == 'POST':
#         #name = request.form['name']
#         name = html.escape(request.form['name'], quote=True)
#
#     salted_name = salt + name
#     name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
#
#     header = '<html><head><title>Identidock</title></head><body>'
#     body = '''
#         <form method="POST">
#         Hello <input type="text" name="name" value="{0}">
#         <input type="submit" value="submit">
#         </form>
#         <p>You look like a :
#         <img src="/monster/{1}"/>
#     '''.format(name, name_hash)
#     footer ='</body></html>'
#
#     return header+body+footer
#
#
# @app.route('/monster/<name>')
# def get_identicon(name):
#
#     name = html.escape(name, quote=True)
#     image = cache.get(name)
#     if image is None:
#
#         #print("Cache miss")
#         #print ("Cache miss", flush=True)
#
#         r = requests.get('http://dnmonster:8080/monster/'+name+'?size=80')
#         image = r.content
#         cache.set(name, image)
#
#     return Response(image, mimetype='image/png')
#

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


