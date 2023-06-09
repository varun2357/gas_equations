-- Create the units_list table
CREATE TABLE units_list (
  unit_group VARCHAR(50) NOT NULL,
  unit_name VARCHAR(50) NOT NULL,
  unit_value INT NOT NULL,
  PRIMARY KEY (unit_group, unit_name)
);

-- Insert data into units_list table
INSERT INTO units_list (unit_group, unit_name, unit_value) VALUES
('sfu', 'slpm', 1),
('sfu', 'slph', 2),
('sfu', 'sccm', 3),
('sfu', 'sm3/hr', 4),
('sfu', 'scfm', 5),
('sfu', 'scfh', 6),
('mfu', 'nlpm', 7),
('mfu', 'nm3/hr', 8),
('mfu', 'nlph', 9),
('wu', 'kg/hr', 10),
('wu', 'gm/hr', 11),
('wu', 'ton/hr', 12),
('wu', 'lb/hr', 13),
('wu', 'ppm', 14),
('wu', 'ton/day', 15),
('wu', 'nm3/hr', 16),
('wu', 'nlph', 17),
('wu', 'nlpm', 18),
('au', 'lpm', 19),
('au', 'lph', 20),
('au', 'm3/hr', 21),
('au', 'ccm', 22),
('au', 'cfh', 23),
('au', 'cfm', 24);
