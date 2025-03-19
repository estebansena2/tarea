-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-07-2024 a las 23:40:55
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `animalsearch2`
--
CREATE DATABASE IF NOT EXISTS `animalsearch2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `animalsearch2`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `adopciones`
--

DROP TABLE IF EXISTS `adopciones`;
CREATE TABLE IF NOT EXISTS `adopciones` (
  `idAdopcion` int(11) NOT NULL AUTO_INCREMENT,
  `adjuntoContrato` blob NOT NULL,
  PRIMARY KEY (`idAdopcion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

DROP TABLE IF EXISTS `carrito`;
CREATE TABLE IF NOT EXISTS `carrito` (
  `idCarrito` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idCarrito`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citaempleado`
--

DROP TABLE IF EXISTS `citaempleado`;
CREATE TABLE IF NOT EXISTS `citaempleado` (
  `idCitaEmpleado` int(11) NOT NULL AUTO_INCREMENT,
  `idEmpleadoAsociado` int(11) NOT NULL,
  `idCita` int(11) NOT NULL,
  PRIMARY KEY (`idCitaEmpleado`),
  KEY `fk10` (`idEmpleadoAsociado`),
  KEY `fk11` (`idCita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

DROP TABLE IF EXISTS `citas`;
CREATE TABLE IF NOT EXISTS `citas` (
  `idCita` int(11) NOT NULL AUTO_INCREMENT,
  `calendario` date NOT NULL,
  `idServicio` int(11) NOT NULL,
  PRIMARY KEY (`idCita`),
  UNIQUE KEY `calendario` (`calendario`),
  KEY `fk07` (`idServicio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `cedulaCliente` int(10) UNSIGNED NOT NULL,
  `nombreCliente` varchar(255) NOT NULL,
  `contactoCliente` int(10) UNSIGNED NOT NULL,
  `ciudad` varchar(255) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  PRIMARY KEY (`idCliente`),
  UNIQUE KEY `cedulaCliente` (`cedulaCliente`),
  UNIQUE KEY `contactoCliente` (`contactoCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleadoasociado`
--

DROP TABLE IF EXISTS `empleadoasociado`;
CREATE TABLE IF NOT EXISTS `empleadoasociado` (
  `idEmpleadoAsociado` int(11) NOT NULL AUTO_INCREMENT,
  `nombreEmpleado` varchar(255) NOT NULL,
  `contactoEmpleado` int(10) UNSIGNED NOT NULL,
  `direccionEmpleado` varchar(255) NOT NULL,
  `ciudad` varchar(255) NOT NULL,
  PRIMARY KEY (`idEmpleadoAsociado`),
  UNIQUE KEY `contactoEmpleado` (`contactoEmpleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidadempleado`
--

DROP TABLE IF EXISTS `especialidadempleado`;
CREATE TABLE IF NOT EXISTS `especialidadempleado` (
  `idEspecialidadEmpleado` int(11) NOT NULL AUTO_INCREMENT,
  `idEmpleadoAsociado` int(11) NOT NULL,
  `idEspecialidad` int(11) NOT NULL,
  PRIMARY KEY (`idEspecialidadEmpleado`),
  KEY `fk12` (`idEmpleadoAsociado`),
  KEY `fk13` (`idEspecialidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidades`
--

DROP TABLE IF EXISTS `especialidades`;
CREATE TABLE IF NOT EXISTS `especialidades` (
  `idEspecialidad` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) NOT NULL,
  PRIMARY KEY (`idEspecialidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturas`
--

DROP TABLE IF EXISTS `facturas`;
CREATE TABLE IF NOT EXISTS `facturas` (
  `idFactura` int(11) NOT NULL AUTO_INCREMENT,
  `total` int(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`idFactura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascotas`
--

DROP TABLE IF EXISTS `mascotas`;
CREATE TABLE IF NOT EXISTS `mascotas` (
  `idMascota` int(11) NOT NULL AUTO_INCREMENT,
  `nombreMascota` varchar(255) NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `peso` int(10) UNSIGNED NOT NULL,
  `raza` varchar(255) NOT NULL,
  `genero` varchar(255) NOT NULL,
  `idCliente` int(11) NOT NULL,
  PRIMARY KEY (`idMascota`),
  KEY `fk01` (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

DROP TABLE IF EXISTS `pagos`;
CREATE TABLE IF NOT EXISTS `pagos` (
  `idPago` int(11) NOT NULL AUTO_INCREMENT,
  `medioPago` varchar(55) NOT NULL,
  `totalPago` int(10) UNSIGNED NOT NULL,
  `idFactura` int(11) NOT NULL,
  PRIMARY KEY (`idPago`),
  KEY `fk03` (`idFactura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
CREATE TABLE IF NOT EXISTS `pedidos` (
  `idPedido` int(11) NOT NULL AUTO_INCREMENT,
  `fechaPedido` date NOT NULL,
  `hora` time NOT NULL,
  PRIMARY KEY (`idPedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidosservicios`
--

DROP TABLE IF EXISTS `pedidosservicios`;
CREATE TABLE IF NOT EXISTS `pedidosservicios` (
  `idpedidoServicio` int(11) NOT NULL AUTO_INCREMENT,
  `idPedido` int(11) NOT NULL,
  `idServicio` int(11) NOT NULL,
  PRIMARY KEY (`idpedidoServicio`),
  KEY `fk08` (`idServicio`),
  KEY `fk09` (`idPedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

DROP TABLE IF EXISTS `productos`;
CREATE TABLE IF NOT EXISTS `productos` (
  `idProducto` int(11) NOT NULL AUTO_INCREMENT,
  `nombreProducto` varchar(255) NOT NULL,
  `Cantidad` int(10) UNSIGNED NOT NULL,
  `idFactura` int(11) NOT NULL,
  PRIMARY KEY (`idProducto`),
  UNIQUE KEY `nombreProducto` (`nombreProducto`),
  KEY `fk02` (`idFactura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

DROP TABLE IF EXISTS `servicios`;
CREATE TABLE IF NOT EXISTS `servicios` (
  `idServicio` int(11) NOT NULL AUTO_INCREMENT,
  `veterineria` varchar(255) NOT NULL,
  `peluqueria` varchar(255) NOT NULL,
  `esterilizacion` varchar(255) NOT NULL,
  `idFactura` int(11) NOT NULL,
  PRIMARY KEY (`idServicio`),
  KEY `fk04` (`idFactura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `serviciosproductos`
--

DROP TABLE IF EXISTS `serviciosproductos`;
CREATE TABLE IF NOT EXISTS `serviciosproductos` (
  `idServicioProducto` int(11) NOT NULL AUTO_INCREMENT,
  `idServicio` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  PRIMARY KEY (`idServicioProducto`),
  KEY `fk05` (`idServicio`),
  KEY `fk06` (`idProducto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citaempleado`
--
ALTER TABLE `citaempleado`
  ADD CONSTRAINT `fk10` FOREIGN KEY (`idEmpleadoAsociado`) REFERENCES `empleadoasociado` (`idEmpleadoAsociado`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk11` FOREIGN KEY (`idCita`) REFERENCES `citas` (`idCita`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `citas`
--
ALTER TABLE `citas`
  ADD CONSTRAINT `fk07` FOREIGN KEY (`idServicio`) REFERENCES `servicios` (`idServicio`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `especialidadempleado`
--
ALTER TABLE `especialidadempleado`
  ADD CONSTRAINT `fk12` FOREIGN KEY (`idEmpleadoAsociado`) REFERENCES `empleadoasociado` (`idEmpleadoAsociado`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk13` FOREIGN KEY (`idEspecialidad`) REFERENCES `especialidades` (`idEspecialidad`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `mascotas`
--
ALTER TABLE `mascotas`
  ADD CONSTRAINT `fk01` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD CONSTRAINT `fk03` FOREIGN KEY (`idFactura`) REFERENCES `facturas` (`idFactura`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `pedidosservicios`
--
ALTER TABLE `pedidosservicios`
  ADD CONSTRAINT `fk08` FOREIGN KEY (`idServicio`) REFERENCES `servicios` (`idServicio`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk09` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`idPedido`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `fk02` FOREIGN KEY (`idFactura`) REFERENCES `facturas` (`idFactura`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD CONSTRAINT `fk04` FOREIGN KEY (`idFactura`) REFERENCES `facturas` (`idFactura`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `serviciosproductos`
--
ALTER TABLE `serviciosproductos`
  ADD CONSTRAINT `fk05` FOREIGN KEY (`idServicio`) REFERENCES `servicios` (`idServicio`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk06` FOREIGN KEY (`idProducto`) REFERENCES `productos` (`idProducto`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
