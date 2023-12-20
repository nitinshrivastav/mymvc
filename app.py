from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/testing',methods=['POST'])
def dhjdhj():
    try:
        a=int(request.args.get('data1'))
        b=int(request.args.get('data2'))
        return jsonify({'answer':a+b}) 
    except:
        return jsonify({'Error':'Invalid Data'})
