from flask import Flask,jsonify,request,render_template
app=Flask(__name__)

store=[
{
'name':'My Store',
'items':[
{
'name':'My item',
'price':15.99
}
]
}
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store',methods=['POST'])
def create_store():
    request_data=request.get_jsonify()
    new_store=[
    {
    "name":request_data['name'],
    "items":[]
    }
    ]
    store.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    for i in store:
        if i['name']==name:
            return jsonify(i)
    return jsonify({'message':'Error, No such store found!!!'})


@app.route('/stores',methods=['GET'])
def get_stores():
    return jsonify({'stores':store})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item(name):
    request_data=request.get_json()
    for i in store:
        if i['name']==name:
            new_item={
            'name':request_data['name'],
            'price':request_data['price']
            }
            i['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'Message':'No such store found'})

@app.route('/store/<string:name>/item',methods=['GET'])
def get_item_in_store(name):
    for i in store:
        if i['name']==name:
            return jsonify({'items':i['items']})
    return jsonify({'Message':'No such store found'})

app.run(port=5000)
