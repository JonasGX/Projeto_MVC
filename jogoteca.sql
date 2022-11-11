CREATE DATABASE jogoteca;

USE jogoteca;

CREATE TABLE jogos(
id int(60) AUTO_INCREMENT,
nome varchar(30) NOT NULL,
categoria varchar(50) NOT NULL,
console varchar(50) NOT NULL,
PRIMARY KEY (id)
);
CREATE TABLE usuarios(
cpf varchar(11) NOT NULL,
nome_usuario varchar(30) NOT NULL,
senha varchar(8) NOT NULL,
PRIMARY KEY (cpf)
);

INSERT INTO usuarios(cpf, nome_usuario, senha) VALUES(51731214839, 'jonas','Jonas@#');

select * from usuarios;
select * from jogos;
select * from jogos where categoria = 'Tiro';

