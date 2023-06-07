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

# sg1 = round(float("1"), 3)
# sg2 = round(float("2"), 3)
# t1 = round(float("3"), 3)
# t2 = round(float("4"), 3)
# p1 = round(float("5"), 3)
# p2 = round(float("6"), 3)
# unit_class = "wu"
# from_unit = "kg/hr"
# to_unit = "gm/hr"
# value = 7


@app.route("/")
def hello_world():
  # sf1 = cal_sf_not_au(sg1,sg2,t1,t2,p1,p2)
  # sf2 = cal_sf_au(sg1,sg2,t1,t2,p1,p2)
  # result = convert_units(units_list, unit_class, from_unit, to_unit, value)
  # return render_template('home.html', units=units_list,sf1 = sf1,sf2 = sf2,result = result)
  return render_template('home2.html',categories=units_list.keys())

@app.route('/conversion', methods=['GET', 'POST'])
def conversion():
    if request.method == 'POST':
        selected_category = request.form.get('category')
        if selected_category:
            selected_units = units_list[selected_category]
            input1 = request.form.get('input1')
            input2 = request.form.get('input2')
            input3 = request.form.get('input3')

            # Check if all inputs are present
            if input1 and input2 and input3:
                value1 = selected_units.get(input1)
                value2 = selected_units.get(input2)

                if value1 is not None and value2 is not None:
                    sum_values = convert_units(units_list,selected_category,input1,input2,float(input3))
                    #sum_values = value1 + value2 + float(input3)
                    return render_template('conversion.html', categories=units_list.keys(), units=selected_units, sum_values=sum_values)
                else:
                    error_message = "Invalid units selected."
                    return render_template('conversion.html', categories=units_list.keys(), units=selected_units, error_message=error_message)
            else:
                error_message = "Please fill in all input fields."
                return render_template('conversion.html', categories=units_list.keys(), units=selected_units, error_message=error_message)
        else:
            error_message = "Please select a category."
            return render_template('conversion.html', categories=units_list.keys(), units={}, error_message=error_message)
    else:
        return render_template('conversion.html', categories=units_list.keys(), units={}, sum_values=None)





@app.route('/size', methods=['GET', 'POST'])
def size():
    if request.method == 'POST':
        selected_category = request.form.get('category')
        selected_units = units_list[selected_category]

        return render_template('size.html', units=selected_units)
    else:
        return render_template('size.html', units={})

@app.route("/input")
def input():
    return render_template("input.html",units_list=units_list )
  
@app.route("/api/units")
def list_units():
  return jsonify(units_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
