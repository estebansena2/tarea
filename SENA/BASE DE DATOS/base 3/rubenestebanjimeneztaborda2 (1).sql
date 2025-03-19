-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-05-2024 a las 22:31:45
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
-- Base de datos: `rubenestebanjimeneztaborda2`
--
CREATE DATABASE IF NOT EXISTS `rubenestebanjimeneztaborda2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `rubenestebanjimeneztaborda2`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alquiler`
--

DROP TABLE IF EXISTS `alquiler`;
CREATE TABLE IF NOT EXISTS `alquiler` (
  `idAlquiler` int(11) NOT NULL AUTO_INCREMENT,
  `fechaAlquiler` date NOT NULL,
  `fechaDevolucion` date NOT NULL,
  `idCliente` int(11) NOT NULL,
  PRIMARY KEY (`idAlquiler`),
  KEY `fk01` (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) NOT NULL,
  `Apellido` varchar(255) DEFAULT NULL,
  `Email` varchar(255) NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `Direccion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallealquiler`
--

DROP TABLE IF EXISTS `detallealquiler`;
CREATE TABLE IF NOT EXISTS `detallealquiler` (
  `idDetalleAlquiler` int(11) NOT NULL AUTO_INCREMENT,
  `idAlquiler` int(11) NOT NULL,
  `idPelicula` int(11) NOT NULL,
  PRIMARY KEY (`idDetalleAlquiler`),
  KEY `fk02` (`idAlquiler`),
  KEY `fk03` (`idPelicula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peliculas`
--

DROP TABLE IF EXISTS `peliculas`;
CREATE TABLE IF NOT EXISTS `peliculas` (
  `idPelicula` int(11) NOT NULL AUTO_INCREMENT,
  `Titulo` varchar(255) NOT NULL,
  `Director` varchar(255) NOT NULL,
  `Genero` varchar(255) NOT NULL,
  `Anio` int(11) NOT NULL,
  `Duracion` int(11) NOT NULL,
  PRIMARY KEY (`idPelicula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alquiler`
--
ALTER TABLE `alquiler`
  ADD CONSTRAINT `fk01` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `detallealquiler`
--
ALTER TABLE `detallealquiler`
  ADD CONSTRAINT `fk02` FOREIGN KEY (`idAlquiler`) REFERENCES `alquiler` (`idAlquiler`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk03` FOREIGN KEY (`idPelicula`) REFERENCES `peliculas` (`idPelicula`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
