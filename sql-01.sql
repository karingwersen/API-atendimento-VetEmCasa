CREATE DATABASE vetemcasa;

\c vetemcasa;

CREATE TABLE atendimentos (pet VARCHAR(50), tutor VARCHAR(50), veterinario VARCHAR(50), id VARCHAR(32), data DATE, horario TIME, PRIMARY KEY (id));

INSERT INTO atendimentos (pet, tutor, veterinario, id, data, horario) values ('Pipoca', 'Victor', 'Karin', '1d11ddcc24e6ccef1091f5ca0064697c', '2023-05-01', '19:30:00');
