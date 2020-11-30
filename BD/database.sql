CREATE TABLE `bdregistro`.`estudiantes` 
( `id` INT NOT NULL AUTO_INCREMENT, 
  `nombre` varchar(100) NOT NULL , 
  `apellido` varchar(100) NOT NULL , 
  `genero` varchar(100) NOT NULL , 
  `direccion` varchar(100) NOT NULL , 
  `usuario` varchar(100) NOT NULL , 
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)) 
ENGINE = InnoDB;