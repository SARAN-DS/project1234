from flask import Flask,render_template,request,url_for
from textblob import TextBlob
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/success/<score>')
def success(score):
    res=''
    edu = TextBlob(score)
    x = edu.sentiment.polarity
    if x < 0:
        res='Negative'
    elif x == 0:
        res="Neutral"
    elif x > 0 and x <= 1:
        res="positive"
    return render_template('result.html', success=res)
@app.route('/submit',methods=['POST','GET'])
def submit():
    total=""
    if request.method == 'POST':
        a = request.form.get('review')
        total=a
        from werkzeug.utils import redirect
        return redirect(url_for('success', score=total))
if __name__=="__main__":
  app.run(debug=True)
