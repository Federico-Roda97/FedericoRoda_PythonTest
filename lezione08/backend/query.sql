drop database if exists verificaChat;
create database verificaChat;
use verificaChat;

create table User(
  username varchar(320) primary key,
  password char(60) not null
);

create table Chat(
  id int primary key auto_increment,
  message text,
  username varchar(320) references User(username)
);
