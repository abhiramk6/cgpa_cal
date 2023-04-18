from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    cur_gpa = float(request.form['cur_gpa'])
    cv = 3 * float(request.form['cv'])
    sc = 3 * float(request.form['sc'])
    sp = 3 * float(request.form['sp'])
    nlp = 3 * float(request.form['nlp'])
    opr = 3 * float(request.form['opr'])
    tpt = 3 * float(request.form['tpt'])
    mcp = 2 * float(request.form['mcp'])
    tp = 2 * float(request.form['tp'])
    ti = float(request.form['ti'])

    cur_overall = float(cur_gpa * 114)
    this_sem_gpa = cv + sc + sp + nlp + opr +tpt + mcp + tp + ti
    cur_overall = float(cur_overall + this_sem_gpa)
    cur_sgpa = this_sem_gpa / 23
    cur_gpa = cur_overall / 137

    cur_sgpa = round(cur_sgpa, 2)
    cur_gpa = round(cur_gpa, 2)

    return render_template('result.html', cur_gpa=cur_gpa, cur_sgpa=cur_sgpa)

if __name__ == '__main__':
    app.run(debug=True)
