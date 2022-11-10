CREATE DATABASE jogoteca;

USE jogoteca;

CREATE TABLE jogos(
id int(60) AUTO_INCREMENT,
nome varchar(30) NOT NULL,
categoria varchar(50) NOT NULL,
console varchar(50) NOT NULL,
PRIMARY KEY (id)
);

DROP TABLE jogos;

INSERT INTO jogos (nome, categoria, console) VALUES('Fifa23','Futebol','Play Station 5');

select * from jogos;