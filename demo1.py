#从flask模块导入Flask类
from flask import Flask

#2.创建一个flask对象
#参数1：__name__，如果从当前文件启动，那么值是__main__,如果从其他模块调用运行，那么值是模块名字__name__
#参数2：static_url_path,表示静态资源的访问地址，/static
#参数3：static_folder,表示用来存储静态资源的，默认名字是static
#参数4：template_folder,模板文件夹，默认值是templates
app = Flask(__name__)
print(__name__)
print(app.static_url_path)
print(app.static_folder)
print(app.template_folder)

#使用app，通过路由绑定一个视图函数
#注意点：视图函数一定要有返回值
@app.route("/")

def index1():
    return "Don't worry, everything gonna be ok ^_^"

#判断是否直接使用当前模块运行程序
if __name__ == "__main__":
    #运行方法参数，指定端口，打开调试模式，还有一个参数：host
    app.run(port=5002,debug=True)
