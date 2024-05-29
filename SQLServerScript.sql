-- se crea la base de datos
CREATE DATABASE IF NOT EXISTS TransitoBA;	
-- se usa la misma
USE TransitoBA;
-- se crea la tabla para trabajar
CREATE TABLE IF NOT EXISTS homicidios (
    N_VICTIMAS INT,
    TIPO_DE_CALLE VARCHAR(9),
    Direccion_Normalizada VARCHAR(255),
    COMUNA INT,
    pos_x FLOAT,
    pos_y FLOAT,
    VICTIMA VARCHAR(11),
    ACUSADO VARCHAR(11),
    fecha_hora DATETIME
);