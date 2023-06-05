import math

def cal_sf_not_au(sg1,sg2,t1,t2,p1,p2):
    sg = round(sg2/sg1, 3)
    t = round(t2/t1, 3)
    p = round(p1/p2, 3)
    sf = round(math.sqrt(sg*t*p), 3)
    return sf

def cal_sf_au(sg1,sg2,t1,t2,p1,p2):
    sg = round(sg2/sg1, 3)
    t = round(t1/t2, 3)
    p = round(p2/p1, 3)
    sf = round(math.sqrt(sg*t*p), 3)
    return sf

def convert_units(units_list,unit_class, from_unit, to_unit, value):
    if unit_class in units_list:
        unit_dict = units_list[unit_class]
        if from_unit in unit_dict and to_unit in unit_dict:
            conversion_factor = unit_dict[to_unit] / unit_dict[from_unit]
            converted_value = value * conversion_factor
            return converted_value