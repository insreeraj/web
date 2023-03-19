from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/')
def index():
    return "hello world"
@app.route('/member')
def memeber():
    return "our Team has 5 members"

@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        return "the person has passed with a score of " + str(score)
    else:
        return "error!!!"
@app.route('/fail/<int:score>')
def fail(score):
    if score < 50:
        return "the person has failed with a score of " + str(score)
    else:
        return "error!!!"
@app.route('/results/<int:score>')
def results(score):
    results =""
    if score >= 50:
        results ="success"
    else:
        results ="fail"

    return redirect(url_for(results,score=score))

if __name__ == "__main__":
    app.run(debug= True)
