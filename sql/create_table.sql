CREATE TABLE IF NOT EXISTS materials(
    id INTEGER,
    brand TEXT,
    material TEXT,
    GOST TEXT,
    description TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS parts(
    id INTEGER,
    type_part TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS parameters(
    id INTEGER,
    id_part INTEGER,
    parameter TEXT,
    tag_parameter TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_part) REFERENCES parts (id)
);