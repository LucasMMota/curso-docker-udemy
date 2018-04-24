create database email_sender;

\c email_sender

create table emails (
  id serial not null,
  data TIMESTAMP not NULL DEFAULT CURRENT_TIMESTAMP ,
  assunto VARCHAR(100) not null,
  menssagem VARCHAR(250) not NULL
);