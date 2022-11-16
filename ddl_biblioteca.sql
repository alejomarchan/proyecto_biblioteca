-- Volcando estructura para tabla biblioteca.libros
DROP TABLE IF EXISTS `libros`;
CREATE TABLE IF NOT EXISTS `libros` (
  `isbn` varchar(17) NOT NULL,
  `titulo` varchar(50) DEFAULT NULL,
  `autor` varchar(50) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla biblioteca.libros: ~3 rows (aproximadamente)
DELETE FROM `libros`;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
commit;
INSERT INTO `libros` (`isbn`, `titulo`, `autor`, `estado`, `activo`) VALUES
	('978-0060439514', 'The Calculus 7', 'Louis Leithold', 1, 1),
	('978-0486406879', 'Introduction to Logic', 'Patrick Suppes ', 1, 1),
	('978-1119573319', 'The Python Book', 'Rob Mastrodomenico', 1, 1),
	('978-1803242620', 'SQL Server Query Tuning and Optimization', 'Benjamin Nevarez', 1, 0);
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
commit;

-- Volcando estructura para tabla biblioteca.usuarios
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `dni` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `fecha_alta` date DEFAULT NULL,
  `fecha_actualizacion` date DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`dni`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla biblioteca.usuarios: ~0 rows (aproximadamente)
DELETE FROM `usuarios`;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
commit;
INSERT INTO `usuarios` (`dni`, `nombre`, `telefono`, `direccion`, `fecha_alta`, `fecha_actualizacion`, `estado`) VALUES
	(95783601, 'Alejandro', '1123473222', 'Charcas 3939', '2022-11-09', NULL, 1);
commit;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;


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