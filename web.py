from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>歡迎進入黃彥璋的網頁</h1>"     
    link += "<a href=/mis>課程</a><hr>" 
    link += "<a href=/today>今天日期</a><hr>" 
    link += "<a href=/about>關於彥璋</a><hr>"
    link += "<a href=/welcome?u=彥璋&dep=靜宜資管>GET傳</a><hr> "
    link += "<a href=/account>POST傳值(帳號密碼)</a><hr> "
    link += "<a href=/math>簡易計算機</a><hr> " 
    return link                               

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1><a href=/>回到網站首頁</a>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    now = year + "年" + month + "月" + day + "日"
    return render_template("today.html", datetime = now)

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/welcome",methods=["GET"])
def welcome():
    x = request.values.get("u")
    y = request.values.get("dep")
    return render_template("welcome.html",name = x ,dep = y ) 

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")
        
@app.route("/math", methods=["GET", "POST"])
def math():
    if request.method == "POST":
        # 接收表單傳來的資料
        x = int(request.form["x"])
        opt = request.form["opt"]
        y = int(request.form["y"])
        
        # 你的計算邏輯
        if opt == "/" and y == 0:
            result = "除數不能等於0"
        else:
            match opt:
                case "+": result = x + y
                case "-": result = x - y
                case "*": result = x * y
                case "/": result = x / y
        
        # 將結果傳回給同一個頁面顯示
        return render_template("math.html", x=x, opt=opt, y=y, result=result)
    else:
        # 如果是 GET 請求，就只顯示空白表單
        return render_template("math.html")

if __name__ == "__main__":
    app.run()