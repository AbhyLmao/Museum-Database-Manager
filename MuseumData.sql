DROP DATABASE IF EXISTS ARTMUSEUM;
CREATE DATABASE ARTMUSEUM; 
USE ARTMUSEUM;

DROP TABLE IF EXISTS USERS;
CREATE TABLE USERS(
	UserID 		varchar(30)	not null,
	PassID 		varchar(30)	not null,
	Utype  		varchar(30)	not null,
	primary key (UserID)
);

INSERT INTO USERS (UserID, PassID, Utype)
VALUES
('a','a','admin'),
('Admin','password','admin');



DROP TABLE IF EXISTS EXHIBITION;
CREATE TABLE EXHIBITION(
	EName				varchar(30)	not null,
	Start_date			date,
	End_date 			date,
	primary key (Ename)
);


INSERT INTO EXHIBITION (Ename, Start_date, End_date)
VALUES
('Turdors','2022-04-25','2024-04-25'),
('Cubism','2020-04-25','2022-01-30'),
('Hear Me','2021-06-1','2023-06-1'),
('NA',NULL,NULL);


DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS(
	Cname				varchar(30)	not null,
	Ctype				varchar(30),
	Cdescription		varchar(30),
    Caddress			varchar(30),
    Cphone 				varchar(15),
    Contact_person		varchar(30),
	primary key (Cname)
);



INSERT INTO COLLECTIONS (Cname, Ctype, Cdescription, Caddress, Cphone, Contact_person)
VALUES
('Masterpieces','Art','best art','louvre','3140205050','Kim Pham'),
('Aqusitions','Art','new aquires','louvre','3140205050','Kim Pham'),
('NA','NA','NA','NA','NA','NA');


DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST(
	Aname				varchar(30)	not null,
	Date_born			integer,
	Date_died 			integer,
	Country_of_origin 	varchar(30),
    Cdescription		varchar(30),
    Epoch 				varchar(30),
    Main_style			varchar(30),
	primary key (Aname)
);

INSERT INTO ARTIST (Aname,Date_born,Date_died,Country_of_origin,Cdescription,Epoch,Main_style)
VALUES
('Hans Eworth','1520','1574','Belgium','Flemish painter','mid-16th century','allegorical images'),
('Guillim Scrots','1537','1553','Netherlands','painter of the Tudor court','mid-15th century','Mannerist style'),
('Donatello','1386','1466','Italy','sculptor of the Renaissance','Italian Renaissance','Renaissance style'),
('Benedetto da Rovezzano','1474','1552','Italy','Italian sculptor','Italian Renaissance','Renaissance style'),
('Paul Comolera','1813','1890','France','French sculptor','19th Century','Realistic animal sculpture'),
('Affabel Partridge','1506','1587','London','London goldsmith','16th Century','old royal jewellery'),
('Michelangelo','1475','1564','Italy','Italian Artist','Italian Renaissance','Renaissance style'),
('Alexandros of Antioch','1','100','Greek','Greek Artist','Hellenistic','Hellenistic style'),
('Leonardo da Vinci','1452','1519','Italy','Italian Artist','Italian Renaissance','Renaissance style'),
('Lysippus','1','100','Greek','Greek Artist','Hellenistic','Hellenistic style'),
('Van Loo','1705','1765','France','French painter','Orientalism','allegorical images'),
('Jean-Valentin','1794','1860','France','French smith','silversmith','Cups and goblets');

DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT(
	ID_no				varchar(10)	not null,
	Artist				varchar(30),
    Artyear				Integer,
    Title				varchar(30),
	Cdescription		varchar(30),
	origin 				varchar(30),
    Epoch 				varchar(30),
    Collection			varchar(30),
    Exibition 			varchar(30),
	primary key (ID_no),
	foreign key (Artist) references ARTIST(Aname) ON DELETE CASCADE,
	foreign key (Collection) references COLLECTIONS(Cname) ON DELETE CASCADE,
	foreign key (Exibition) references EXHIBITION(Ename) ON DELETE CASCADE
);

INSERT INTO ART_OBJECT (ID_no, Artist, Artyear, Title, Cdescription, origin, Epoch, Collection, Exibition)
VALUES
('A001', 'Hans Eworth', '1520', 'Mary I', 'portrait of mary 1', 'Flemish', 'victorian era', 'NA', 'Turdors'),
('A002', 'Guillim Scrots', '1537', 'Edward VI', 'portrait of edward ', 'Flemish', 'victorian era', 'NA', 'Turdors'),
('A003', 'Donatello', '1405', 'John The Evangelist', 'Statue of St.John', 'Italian', 'Italian Renaissance', 'NA', 'Cubism'),
('A004', 'Benedetto da Rovezzano', '1524', 'Angel Bearing Candlestick', 'Angel With candlestick', 'Italian', 'Old Testament', 'NA', 'Cubism'),
('A005', 'Paul Comolera', '1873', 'Peacock', 'Peacock sculpture', 'French', 'victorian era', 'NA', 'Cubism'),
('A006', 'Donatello', '1505', 'Unknown Saint', 'Random saint sculpture', 'Italian', 'Old Testament', 'NA', 'Hear Me'),
('A007', 'Affabel Partridge', '1551', 'Cup and cover', 'Cup with cover', 'London', 'English', 'NA', 'Hear Me'),
('A008', 'Affabel Partridge', '1562', 'Ewer', 'Ewer', 'London', 'English', 'NA', 'Hear Me'),
('A009', 'Michelangelo', '1589', 'Esclave rebelle', 'Esclave rebelle', 'Italy', 'Italian', 'Masterpieces', 'NA'),
('A010', 'Alexandros of Antioch', '1', 'Venus de Milo', 'aphroditey', 'Greek', 'Hellenistic', 'Masterpieces', 'NA'),
('A011', 'Leonardo da Vinci', '1503', 'Mona Lisa', 'Mona Lisa', 'Italy', 'Italian', 'Masterpieces', 'NA'),
('A012', 'Lysippus', '1', 'Alexandre Azara', 'Alexander', 'Italy', 'Italian', 'Aqusitions', 'NA'),
('A013', 'Van Loo', '1755', 'Denis Diderot ', 'portrait of Denis', 'Flemish', 'victorian era', 'Aqusitions', 'NA'),
('A014', 'Jean-Valentin', '1843', 'Coupe Fossin ', 'Cup', 'French', 'victorian era', 'Aqusitions', 'NA');


DROP TABLE IF EXISTS ART_TYPE;
CREATE TABLE ART_TYPE(
	ID_no				varchar(10)	not null,
	Painting			varchar(30),
    Sculpture			varchar(30),
	Statue				varchar(30),
	Other 				varchar(30),
	primary key (ID_no),
	foreign key (ID_no) references ART_OBJECT(ID_no)
);

INSERT INTO ART_TYPE (ID_no, Painting, Sculpture, Statue, Other)
VALUES
('A001','yes','no','no','no'),
('A002','yes','no','no','no'),
('A003','no','no','yes','no'),
('A004','no','yes','no','no'),
('A005','no','no','yes','no'),
('A006','no','yes','no','no'),
('A007','no','no','no','yes'),
('A008','no','no','no','yes'),
('A009','no','yes','no','no'),
('A010','no','no','yes','no'),
('A011','yes','no','no','no'),
('A012','no','yes','no','no'),
('A013','yes','no','no','no'),
('A014','no','no','no','yes');

DROP TABLE IF EXISTS SCULPTURES;
CREATE TABLE SCULPTURES(
	ID_no				varchar(10)	not null,
	Material 			varchar(30),
    Height				integer,
	Weight 				integer,
	Style 				varchar(30),
	primary key (ID_no),
	foreign key (ID_no) references ART_OBJECT(ID_no)
);


INSERT INTO SCULPTURES (ID_no, Material, Height, Weight, Style)
VALUES
('A004','Bronze','103','177','sculpture'),
('A006','Terracota','18','2','Sculpture'),
('A009','Terracota','215','916','Sculpture'),
('A012','marble','40','95','Sculpture');

DROP TABLE IF EXISTS PAINTINGS;
CREATE TABLE PAINTINGS(
	ID_no				varchar(10)	not null,
	Paint_type			varchar(30),
    Drawn_on			varchar(30),
	Style 				varchar(30),
	primary key (ID_no),
	foreign key (ID_no) references ART_OBJECT(ID_no)
);

INSERT INTO PAINTINGS (ID_no, Paint_type, Drawn_on, Style)
VALUES
('A001','Portrait','1520','Victorian'),
('A002','Portrait','1537','Victorian'),
('A011','Portrait','1503','Italian'),
('A013','Portrait','1767','Victorian');

DROP TABLE IF EXISTS STATUES;
CREATE TABLE STATUES(
	ID_no				varchar(10)	not null,
	Material 			varchar(30),
    Height				integer,
	Weight 				integer,
	Style 				varchar(30),
	primary key (ID_no),
	foreign key (ID_no) references ART_OBJECT(ID_no)
);

INSERT INTO STATUES (ID_no, Material, Height, Weight, Style)
VALUES
('A003','Terracota','210','500','sculpture'),
('A005','Terracota','52','10','statue'),
('A010','Marble','204','23586','statue');


DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER(
	ID_no				varchar(10)	not null,
	Otype 				varchar(30),
	Style 				varchar(30),
	primary key (ID_no),
	foreign key (ID_no) references ART_OBJECT(ID_no)
);

INSERT INTO OTHER (ID_no, Otype, Style)
VALUES
('A007','Goblet','Glazed'),
('A008','Ewer','Silver'),
('A014','goblet','Gold');


DROP TABLE IF EXISTS PERMANANT;
CREATE TABLE PERMANANT(
	ID_no				varchar(10)	not null,
	Date_acquired 		date,
	PStatus				varchar(30),
	primary key (ID_no),
	foreign key (ID_no) references ART_OBJECT(ID_no)
);

INSERT INTO PERMANANT (ID_no, Date_acquired, PStatus)
VALUES
('A001','2015-12-30','excellent'),
('A002','2017-08-29','good'),
('A003','2014-10-03','worn'),
('A004','2012-05-12','good'),
('A005','2015-04-25','excellent'),
('A006','2003-07-16','worn'),
('A007','2005-12-07','excellent'),
('A008','2017-10-13','good');


DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED(
	ID_no				varchar(10)	not null,
	Date_Borrowed		date,
	Date_Returned 		date,
	primary key (ID_no),
	foreign key (ID_no) references ART_OBJECT(ID_no)
);

INSERT INTO BORROWED (ID_no, Date_Borrowed, Date_Returned)
VALUES
('A009', '2020-01-01','2025-01-01'),
('A010', '2020-01-01','2025-01-01'),
('A011', '2020-01-01','2025-01-01'),
('A012', '2022-05-01','2028-01-01'),
('A013', '2022-05-01','2028-01-01'),
('A014', '2022-05-01','2028-01-01');
