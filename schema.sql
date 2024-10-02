-- flask_blog/schema.sql
DROP TABLE IF EXISTS tickets;

CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    serial_id CHAR(10) NOT NULL,
    alias VARCHAR(20) TEXT NOT NULL,
    radio_id 
);

-- 652CTT01xx serial_id must be 10 digits
-- alias will not be over 20 chars long