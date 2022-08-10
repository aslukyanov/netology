

--количество исполнителей в каждом жанре;
select style_id, count(band_id) from styles_band sb
group by style_id


--количество треков, вошедших в альбомы 2019-2020 годов
select year, count(t.id) from tracks t
left join albums a on t.album_id = a.id
where year >= '2019.01.01' and year < '2021.01.01'
group by year;


--средняя продолжительность треков по каждому альбому
select a.name, avg(duration) from tracks t
left join albums a on t.album_id = a.id
group by a.name;


--все исполнители, которые не выпустили альбомы в 2020 году
select year, a.name, b.name from albums a
left join album_band ab on a.id = ab.album_id 
left join bands b on ab.band_id  = b.id
where year >= '2021.01.01' or year < '2019.12.31'


--названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
select c.name, t.name, a.name, b.name from collections c
left join collection_track ct on c.id = ct.collection_id
left join tracks t on ct.track_id = t.id 
left join albums a on t.album_id = a.id 
left join album_band ab on a.id = ab.album_id
left join bands b on ab.band_id = b.id
where b.name = 'king and jester'


--название альбомов, в которых присутствуют исполнители более 3 жанра
--select a.name, b.name, s.name from albums a
select a.name from albums a
left join album_band ab on a.id = ab.album_id
left join bands b on ab.band_id = b.id
left join styles_band sb on b.id = sb.band_id 
left join styles s on sb.style_id = s.id 
group by a.name
having count(s.id) > 3


--наименование треков, которые не входят в сборники;
select t.name from tracks t
left join collection_track ct on t.id = ct.track_id 
where collection_id IS NOT NULL



--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
select t.name, t.duration, a.name, b.name from tracks t 
left join albums a on t.album_id = a.id
left join album_band ab on a.id = ab.album_id 
left join bands b on ab.band_id = b.id 
where duration = (select min(duration) from tracks)


--название альбомов, содержащих наименьшее количество треков
--select t.album_id, count(a.name) from albums a
--left join tracks t on a.id = t.album_id
--group by a.name, t.album_id
--having count(a.name) = (select in)
--having count(a.name) = 2
--having count(a.name) = (select min(count(a.name)) from albums)



CREATE TABLE IF NOT EXISTS amount_of_tracks (album_id, amount) 
AS 
select t.album_id, count(a.name) from albums a
left join tracks t on a.id = t.album_id
group by a.name, t.album_id


select a.name, aot.amount from albums a 
left join amount_of_tracks aot on a.id = aot.album_id 
group by a.name, aot.amount
having aot.amount = (select min(amount) from amount_of_tracks limit 1)
--having aot.amount = 2





