-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.11.0-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

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
INSERT INTO `libros` (`isbn`, `titulo`, `autor`, `estado`, `activo`) VALUES
	('9780060439514', 'The Calculus 7', 'Louis Leithold', 1, 1),
	('9780486406879', 'Introduction to Logic', 'Patrick Suppes ', 1, 1),
	('9781119573319', 'The Python Book', 'Rob Mastrodomenico', 1, 0),
	('9781803242620', 'SQL Server Query Tuning and Optimization', 'Benjamin Nevarez', 1, 0),
	('9789562477062', 'Comunidad de los anillos', 'Tolkien', 1, 1);
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;

-- Volcando estructura para tabla biblioteca.prestamos
DROP TABLE IF EXISTS `prestamos`;
CREATE TABLE IF NOT EXISTS `prestamos` (
  `id_prestamo` int(11) NOT NULL,
  `dni` int(11) DEFAULT NULL,
  `ISBN` varchar(20) DEFAULT NULL,
  `fecha_prestamo` date DEFAULT NULL,
  `fecha_devolucion` date DEFAULT NULL,
  `devuelto` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_prestamo`),
  KEY `dni` (`dni`),
  KEY `ISBN` (`ISBN`),
  CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`dni`) REFERENCES `usuarios` (`dni`),
  CONSTRAINT `prestamos_ibfk_2` FOREIGN KEY (`ISBN`) REFERENCES `libros` (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla biblioteca.prestamos: ~3 rows (aproximadamente)
DELETE FROM `prestamos`;
/*!40000 ALTER TABLE `prestamos` DISABLE KEYS */;
INSERT INTO `prestamos` (`id_prestamo`, `dni`, `ISBN`, `fecha_prestamo`, `fecha_devolucion`, `devuelto`) VALUES
	(1, 95783601, '9789562477062', '2022-11-27', '2022-11-27', 1),
	(2, 95783601, '9789562477062', '2022-11-27', '2022-11-27', 1),
	(3, 95783601, '9789562477062', '2022-11-30', '2022-11-30', 1),
	(4, 45567765, '9780486406879', '2022-11-30', '2022-11-30', 1);
/*!40000 ALTER TABLE `prestamos` ENABLE KEYS */;

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

-- Volcando datos para la tabla biblioteca.usuarios: ~3 rows (aproximadamente)
DELETE FROM `usuarios`;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`dni`, `nombre`, `telefono`, `direccion`, `fecha_alta`, `fecha_actualizacion`, `estado`) VALUES
	(45567765, 'Ana', '12345678', 'Tigre', '2022-11-23', '2022-11-23', 1),
	(95783601, 'Alejandro', '1123473222', 'Charcas 3939', '2022-11-09', NULL, 1),
	(95783602, 'Lautaro', '12345678', 'Charcas', '2022-11-22', '2022-11-23', 1);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
