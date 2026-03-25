
CREATE TABLE donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    medicine TEXT,
    quantity INTEGER
);

CREATE TABLE requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    medicine TEXT,
    quantity INTEGER
);