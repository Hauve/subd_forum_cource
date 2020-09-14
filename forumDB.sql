create database forumbase;
use forumbase;

CREATE TABLE users(
Id INT AUTO_INCREMENT,
Username VARCHAR(20) NOT NULL UNIQUE,
Pass VARCHAR(20) NOT NULL,
Role ENUM ("admin", "moderator", "client") DEFAULT "client",
PRIMARY KEY(Id)
);

CREATE TABLE forums(
Id INT AUTO_INCREMENT,
Title VARCHAR(100) NOT NULL UNIQUE,
PRIMARY KEY(Id)
);

CREATE TABLE sections(
Id INT AUTO_INCREMENT,
Title VARCHAR(100) NOT NULL UNIQUE,
Forum_id INT,
PRIMARY KEY(Id),
FOREIGN KEY(Forum_id) 
	REFERENCES forums(Id) 
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

CREATE TABLE topics(
Id INT AUTO_INCREMENT,
Title VARCHAR(100) NOT NULL,
Dt_last_mes DATETIME DEFAULT NOW(),
Section_id INT,
PRIMARY KEY(Id),
FOREIGN KEY(Section_id) 
	REFERENCES sections(Id) 
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

CREATE TABLE messages(
Id INT AUTO_INCREMENT,
TextContent TEXT NOT NULL,
Create_dt DATETIME DEFAULT NOW(),
Author INT,
Topic_id INT NOT NULL,
PRIMARY KEY(Id),
FOREIGN KEY(Topic_id) 
	REFERENCES topics(Id) 
		ON DELETE CASCADE
		ON UPDATE CASCADE,
FOREIGN KEY(Author) 
	REFERENCES users(Id) 
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

INSERT INTO users (Username,Pass,Role) VALUES ("admin","password","admin");
INSERT INTO users (Username,Pass,Role) VALUES ("moderator","password","moderator");

INSERT INTO users (Username,Pass,Role) VALUES ("user1","password1","client");
INSERT INTO users (Username,Pass,Role) VALUES ("user2","password2","client");

INSERT INTO forums (Title) VALUES ("Форум программистов");
INSERT INTO forums (Title) VALUES ("Компьютерный форум");
INSERT INTO forums (Title) VALUES ("Форум по электронике и бытовой технике");
INSERT INTO forums (Title) VALUES ("Форум web-программистов");
INSERT INTO forums (Title) VALUES ("Форум о софте");

INSERT INTO sections (Title, Forum_id) VALUES ("C++",1);
INSERT INTO sections (Title, Forum_id) VALUES (".NET",1);
INSERT INTO sections (Title, Forum_id) VALUES ("Python",1);
INSERT INTO sections (Title, Forum_id) VALUES ("Java",1);
INSERT INTO sections (Title, Forum_id) VALUES ("Выбор конфигурации компьютера",2);
INSERT INTO sections (Title, Forum_id) VALUES ("Компьютерное железо",2);
INSERT INTO sections (Title, Forum_id) VALUES ("Ноутбуки, нетбуки, ультрабуки",2);
INSERT INTO sections (Title, Forum_id) VALUES ("Windows",2);
INSERT INTO sections (Title, Forum_id) VALUES ("Linux",2);
INSERT INTO sections (Title, Forum_id) VALUES ("Компьютерная безопасность",2);
INSERT INTO sections (Title, Forum_id) VALUES ("Электроника и радиотехника",3);
INSERT INTO sections (Title, Forum_id) VALUES ("Ремонт бытовой техники",3);
INSERT INTO sections (Title, Forum_id) VALUES ("Бытовая электроника",3);
INSERT INTO sections (Title, Forum_id) VALUES ("PHP",4);
INSERT INTO sections (Title, Forum_id) VALUES ("HTML, CSS",4);
INSERT INTO sections (Title, Forum_id) VALUES ("JavaScript",4);
INSERT INTO sections (Title, Forum_id) VALUES ("Готовые движки (CMS и форумы)",4);
INSERT INTO sections (Title, Forum_id) VALUES ("Интернет-маркетинг, SEO",4);
INSERT INTO sections (Title, Forum_id) VALUES ("Web-серверы",4);
INSERT INTO sections (Title, Forum_id) VALUES ("Софт для Windows",5);
INSERT INTO sections (Title, Forum_id) VALUES ("Офисные программы",5);
INSERT INTO sections (Title, Forum_id) VALUES ("Компьютерные игры",5);
INSERT INTO sections (Title, Forum_id) VALUES ("САПР",5);
INSERT INTO sections (Title, Forum_id) VALUES ("Драйверы",5);

INSERT INTO topics (Title,Dt_last_mes,Section_id) VALUES ("Русские шрифты в консоли", "2020-05-02 23:15:00",1);
INSERT INTO topics (Title,Dt_last_mes,Section_id) VALUES ("Создать класс целых чисел", "2020-05-02 23:24:00",1);

INSERT INTO messages (Create_dt,Author,TextContent,Topic_id) VALUES ("2020-05-02 23:05:00",1,"всем привет. Я новичек, и у меня такой вопрос. Как написать сообщение с русскими буквами, чтоб нормально показывала? Например:
cout<<\"hello world\"; выводить сообщение нормальна? с английсками шрифтами
cout<<\"привет мир\"; выводить в каком не понятном языке, какие та закавычки.",2);
INSERT INTO messages (Create_dt,Author,TextContent,Topic_id) VALUES ("2020-05-02 23:09:00",4,"я вот так это делаю:
1. установить вручную шрифт Lucida Console в свойствах окна консоли
2. и запомнить это для всех окон с этим именем
3. записать в начале программы строку",2);

-- Строки ниже по неизвестной причине вызывают ошибку. Ранее работали. 
-- Создания сообщений для визуального наполнения форума
-- INSERT INTO messages (Create_dt,Author,TextContent,Topic_id) VALUES ("2020-05-02 23:15:00",5,"Чет никто про эту конструкцию не говорит:
-- setlocale( LC_ALL,\"Russian\" ); или
-- setlocale( LC_ALL,"" );",2);
-- INSERT INTO messages (Create_dt,Author,TextContent,Topic_id) VALUES ("2020-05-02 23:24:00",4,"Помогите решить задание

-- Создать класс целых чисел (в закрытой части классе находится значение целого типа). 
-- Определить необходимые конструкторы, методы, деструктор. Перегрузить операции: + сложение, - вычитание, * умножение, / деление,% остаток от целочисленного деления, 
-- [] проверка числа на четность, возведение в степень, - проверка, число является простым. Определить поточные операции ввода-вывода",3);
-- INSERT INTO messages (Create_dt,Author,TextContent,Topic_id) VALUES ("2020-05-02 23:25:00",5,"Что конкретно у Вас не получается?",3);
-- INSERT INTO messages (Create_dt,Author,TextContent,Topic_id) VALUES ("2020-05-02 23:26:00",4,"Я не знаю как его сделать",3);
-- INSERT INTO messages (Create_dt,Author,TextContent,Topic_id) VALUES ("2020-05-02 23:27:00",5,"В задании же сказано, как. Начните с создания класса с одним полем целого типа, потом определяйте операторы.",3);