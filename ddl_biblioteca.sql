create table biblioteca.usuarios (
dni integer,
nombre varchar(100),
telefono varchar(20),
direccion varchar(200),
fecha_alta date,
fecha_actualizacion date,
estado boolean,
PRIMARY KEY (dni)
);

create table biblioteca.libros(
IBSN varchar(20),
titulo varchar(100),
autor varchar(100),
fecha_alta date,
fecha_actualizacion date,
estado boolean,
PRIMARY KEY (IBSN)
);

create table biblioteca.prestamos(
id_prestamo integer,
dni integer,
IBSN varchar(20),
fecha_prestamo date,
fecha_devolucion date,
devuelto boolean,
FOREIGN KEY (dni) REFERENCES usuarios(dni),
FOREIGN KEY (IBSN) REFERENCES libros(IBSN)
)