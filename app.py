from flask import Flask, render_template, jsonify, request
#from database import load_jobs_from_db, load_job_from_db, add_application_to_db
from calculations import cal_sf_not_au, cal_sf_au, convert_units

app = Flask(__name__)

sfu = {
  'slpm': 1,
  'slph': 2,
  'sccm': 3,
  'sm3/hr': 4,
  'scfm': 5,
  'scfh': 6,
}
mfu ={
  'nlpm': 7,
  'nm3/hr': 8,
  'nlph': 9,
}
wu = {
  'kg/hr': 10,
  'gm/hr': 11,
  'ton/hr': 12,
  'lb/hr': 13,
  'ppm': 14,
  'ton/day': 15,
  'nm3/hr': 16,
  'nlph': 17,
  'nlpm': 18,
}
au = {
'lpm': 19,
'lph': 20,
'm3/hr': 21,
'ccm': 22,
'cfh': 23,
'cfm': 24,
}

units_list = {
    'sfu': sfu,
    'mfu': mfu,
    'wu': wu,
    'au' : au,
}

sg1 = round(float("1"), 3)
sg2 = round(float("2"), 3)
t1 = round(float("3"), 3)
t2 = round(float("4"), 3)
p1 = round(float("5"), 3)
p2 = round(float("6"), 3)
unit_class = "wu"
from_unit = "kg/hr"
to_unit = "gm/hr"
value = 7


@app.route("/")
def hello_world():
  sf1 = cal_sf_not_au(sg1,sg2,t1,t2,p1,p2)
  sf2 = cal_sf_au(sg1,sg2,t1,t2,p1,p2)
  result = convert_units(units_list, unit_class, from_unit, to_unit, value)
  return render_template('home.html', units=units_list,sf1 = sf1,sf2 = sf2,result = result)


@app.route("/api/units")
def list_units():
  return jsonify(units_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
