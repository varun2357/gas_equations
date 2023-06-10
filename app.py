from flask import Flask, render_template, jsonify, request
from database import load_dictionary, store_conversion, load_conversion_history, store_size, load_size_history
from calculations import cal_sf_not_au, cal_sf_au, convert_units

app = Flask(__name__)

sg1 = 0
t1 = 0
p1 = 0
sg2 = 0.0
t2 = 0.0
p2 = 0.0
sg1_offset = False
t1_offset = False
p1_offset = False
result = None

units_list = load_dictionary()


@app.route("/")
def hello_world():
    return render_template('home.html', categories=units_list.keys())


@app.route('/conversion', methods=['GET', 'POST'])
def conversion():
    selected_category = None  # Default value for selected_category
    history = load_conversion_history()  # Retrieve the updated history
    if request.method == 'POST':
        category_from_home = request.form.get('category_from_home')
        selected_category = category_from_home or request.form.get('category')

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
                    sum_values = convert_units(units_list, selected_category, input1, input2, float(input3))
                    store_conversion(input1, input2, input3, sum_values, selected_category)  # Store the conversion in the history
                    
                    return render_template('conversion.html', categories=units_list.keys(), units=selected_units, selected_category=selected_category, selected_input1=input1, selected_input2=input2, input3=input3, sum_values=sum_values, history=history)
                else:
                    error_message = "Invalid units selected."
                    return render_template('conversion.html', categories=units_list.keys(), units=selected_units, selected_category=selected_category, selected_input1=input1, selected_input2=input2, input3=input3, error_message=error_message, history=history)
            else:
                error_message = "Please fill in all input fields."
                return render_template('conversion.html', categories=units_list.keys(), units=selected_units, selected_category=selected_category, selected_input1=input1, selected_input2=input2, input3=input3, error_message=error_message, history=history)
        else:
            error_message = "Please select a category."
            return render_template('conversion.html', categories=units_list.keys(), units={}, selected_category=selected_category, selected_input1=None, selected_input2=None, input3=None, error_message=error_message, history=history)
    else:
        return render_template('conversion.html', categories=units_list.keys(), units={}, selected_category=selected_category, selected_input1=None, selected_input2=None, input3=None, sum_values=None, history=history)


@app.route('/size', methods=['GET', 'POST'])
def size():
    if request.method == 'POST':
        sg1 = float(request.form.get('sg1', 0) or 0)
        sg2 = float(request.form.get('sg2', 0) or 0)
        sg2_offset = float(request.form.get('sg2_offset', 0) or 0)
        sg1_offset = bool(request.form.get('sg1_offset', False))
        t1 = float(request.form.get('t1', 0) or 0)
        t2 = float(request.form.get('t2', 0) or 0)
        t2_offset = float(request.form.get('t2_offset', 0) or 0)
        t1_offset = bool(request.form.get('t1_offset', False))
        p1 = float(request.form.get('p1', 0) or 0)
        p2 = float(request.form.get('p2', 0) or 0)
        p2_offset = float(request.form.get('p2_offset', 0) or 0)
        p1_offset = bool(request.form.get('p1_offset', False))
        category = request.form.get('category')
        
        if 'initialize' in request.form:  # Check if 'initialize' button is clicked
            initial_sg1 = 1
            initial_t1 = 2
            initial_p1 = 3
            initial_sg1_offset = True
            initial_t1_offset = True
            initial_p1_offset = True
        else:
            initial_sg1 = sg1
            initial_t1 = t1
            initial_p1 = p1
            initial_sg1_offset = sg1_offset
            initial_t1_offset = t1_offset
            initial_p1_offset = p1_offset

        if sg1_offset:
            sg2 = sg2 + sg1
        else:
            sg2 = sg2 + sg2_offset

        if t1_offset:
            t2 = t2 + t1
        else:
            t2 = t2 + t2_offset

        if p1_offset:
            p2 = p2 + p1
        else:
            p2 = p2 + p2_offset

        if sg2 <= 0:
            result = "Invalid sg1"
        elif t2 <= 0:
            result = "Invalid t1"
        elif p2 <= 0:
            result = "Invalid p1"
        elif sg2 <= 0:
            result = "Invalid sg2"
        elif t2 <= 0:
            result = "Invalid t2"
        elif p2 <= 0:
            result = "Invalid p2"
        else:
            if category == 'au':
                result = cal_sf_au(sg1,sg2,t1,t2,p1,p2)
                store_size(sg1, sg2, t1, t2, p1, p2, result, category)
            else:
                result = cal_sf_not_au(sg1,sg2,t1,t2,p1,p2)
                store_size(sg1, sg2, t1, t2, p1, p2, result, category)
        history = load_size_history()
        return render_template('size.html', result=result, units_list=units_list,
                               initial_sg1=initial_sg1, initial_t1=initial_t1, initial_p1=initial_p1,
                               initial_sg1_offset=initial_sg1_offset, initial_t1_offset=initial_t1_offset,
                               initial_p1_offset=initial_p1_offset,selected_category=category,size_history=history)

    return render_template('size.html', units_list=units_list, size_history=history)
@app.route("/api/units")
def list_units():
  return jsonify(units_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=False)
