from flask import Flask,render_template,request
import datetime
app = Flask(__name__)

#路由解析，通过用户访问的路径，匹配相应函数，/即代表原始服务器路径，
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#读入字符串变量：可以将访问路径中的字符串作为变量读入，例如下面的name，可以在路径中取多个值，都作为函数的入参
@app.route('/user/<name>')
def welcome(name):
    return '你好，%s'%name
#读入整型变量：且此时，根据参数类型不同，会返回不同的函数；float类似int，改一下就行
@app.route('/user/<int:id>')
def welcome2(id):
    return '你好，%d号用户'%id

#返回网页相关：
@app.route('/')
def index():
    #用render模块，直接调用templates路径下的html文件
    return render_template("index.html")
#向页面传递变量：
@app.route('/index2')
def index2():
    time = datetime.date.today()
    name = ["张三","李四","王五"]
    task = {'任务':"打扫",'时间':"3h"}
    #入参中可以有变量:
    #普通变量:将time变量赋给html中的var，在html中，使用{{var}}来调用
    #列表变量：需要用到jinjia的控制语句，参考index中的用法，用{}控制变量和流程，外部可以添加html代码
    #字典变量：同样参照index.html
    return render_template("index.html",var = time,list = name,task = task)

#提交表单
@app.route('/test/register')
def register():
    return render_template('/test/register.html')
#表单反馈，如果表单中请求为post，则需要下面的方法也支持post访问
@app.route('/result',methods=['get','post'])
def result():
    #通过request，获取表单信息
    if request.method == 'POST':
        #result.form获取了用户传来的表单信息，类型为字典
        #键即为html中的name属性，值为html中的value属性（用户输入的）
        result = request.form
        return render_template('/test/result.html',result = result)
    else:
        return render_template('/test/register.html')

if __name__ == '__main__':
    #run有一些参数，可以设置debug、端口等
    #pycharm中，要在编辑设置中开启debug，此处参数不生效
    app.run(debug=True)
