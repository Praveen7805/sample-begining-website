from flask import Flask , render_template , jsonify

app=Flask(__name__)

JOBS=[
  {
  'id':1,
  'title':'Data Analyst',
  'Location': 'TamilNadu , India',
  'Salary':'10,000,00'
  },
  {
  'id':2,
  'title':'Data Scientist',
  'Location': 'Kerala , India',
  'Salary':'20,000,00'
  },
 {
  'id':3,
  'title':'Frontend developer',
  'Location': 'Telangana , India',
  'Salary':'30,000,00'
 },
 {
  'id':4,
  'title':'Backend developer',
  'Location': 'Hyderabad , India',
  'Salary':'40,000,00'
 }
  ]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name="NOVA INDUSTRIES")
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)