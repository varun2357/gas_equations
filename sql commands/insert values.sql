INSERT INTO units_list (unit_group, table_name) VALUES
  ('sfu', 'sfu'),
  ('mfu', 'mfu'),
  ('wu', 'wu'),
  ('au', 'au');

INSERT INTO sfu (unit_name, unit_value, unit_group) VALUES
  ('slpm', 1, 'sfu'),
  ('slph', 2, 'sfu'),
  ('sccm', 3, 'sfu'),
  ('sm3/hr', 4, 'sfu'),
  ('scfm', 5, 'sfu'),
  ('scfh', 6, 'sfu');

INSERT INTO mfu (unit_name, unit_value, unit_group) VALUES
  ('nlpm', 7, 'mfu'),
  ('nm3/hr', 8, 'mfu'),
  ('nlph', 9, 'mfu');

INSERT INTO wu (unit_name, unit_value, unit_group) VALUES
  ('kg/hr', 10, 'wu'),
  ('gm/hr', 11, 'wu'),
  ('ton/hr', 12, 'wu'),
  ('lb/hr', 13, 'wu'),
  ('ppm', 14, 'wu'),
  ('ton/day', 15, 'wu'),
  ('nm3/hr', 16, 'wu'),
  ('nlph', 17, 'wu'),
  ('nlpm', 18, 'wu');
  
INSERT INTO au (unit_name, unit_value, unit_group) VALUES
  ('lpm', 19, 'au'),
  ('lph', 20, 'au'),
  ('m3/hr', 21, 'au'),
  ('ccm', 22, 'au'),
  ('cfh', 23, 'au'),
  ('cfm', 24, 'au');