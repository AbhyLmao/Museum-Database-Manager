show tables;

SELECT Aname,Main_style FROM ARTIST WHERE Country_of_origin = 'Belgium';

SELECT A.Aname, O.Artyear, O.Cdescription, ID_no FROM ART_OBJECT as O, ARTIST as A ORDER BY O.Artyear Desc;

SELECT Aname, Country_of_origin FROM ARTIST WHERE Date_born IN (SELECT Artyear FROM ART_OBJECT GROUP BY Artyear );

(SELECT S.Style, S.Material, O.Artist FROM SCULPTURES as S, ART_OBJECT as O WHERE S.ID_no = O.ID_no) union(SELECT SU.Style, SU.Material, O.Artist FROM STATUES as SU, ART_OBJECT as O WHERE SU.ID_no = O.ID_no);

UPDATE STATUES SET Height = '909' WHERE ID_no ='A003';

DELETE FROM PAINTINGS WHERE ID_no ='A001';