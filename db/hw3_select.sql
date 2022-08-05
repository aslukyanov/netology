--название и год выхода альбомов, вышедших в 2018 году
SELECT name, year
FROM albums
WHERE year >= '2018.01.01' and year < '2019.01.01';


--название и продолжительность самого длительного трека
select name, duration
from tracks
where duration = (select max(duration) from tracks);


--название треков, продолжительность которых не менее 3,5 минуты
select name, duration 
from tracks
where duration >= 210;


--названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT name, year
FROM collections
WHERE year >= '2018.01.01' and year < '2021.01.01';


--исполнители, чье имя состоит из 1 слова;
select name
from bands
where name not like '% %'


--название треков, которые содержат слово "мой"/"my".

select name
from tracks
where ' ' || name || ' ' ILIKE '% my %'









