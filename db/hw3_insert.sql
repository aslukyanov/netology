

--adding new bands

insert into bands(id, name)
values(3, 'manowar'),
(4, 'scorpions'),
(5, 'king and jester'),
(6, 'sector gaza'),
(7, 'area'),
(8, 'knyazz'),
(9, 'godsmack'),
(10, 'brigadniy podryad')


--new styles, 3 already exist - 

insert into styles(id, name) values(1, 'rock') ON CONFLICT (id) DO nothing

insert into styles(id, name) values(2, 'punk-rock') ON CONFLICT (id) DO nothing

insert into styles(id, name) values(3, 'ska') ON CONFLICT (id) DO nothing

insert into styles(id, name) values(4, 'metall')  ON CONFLICT (id) DO nothing

insert into styles(id, name) values(5, 'pop') ON CONFLICT (id) DO nothing


--adding new albums
insert into albums(id, name, year) values(1, 'nate kushayte', '2019.01.01') ON CONFLICT (id) DO nothing

insert into albums(id, name, year)
values(2, 'the best', '2018.01.01'),
(3, 'battle hymns', '2011.01.01'),
(4, 'unbreakeble', '2004.01.01'),
(5, 'todd', '2012.01.01'),
(6, 'sector gaza', '1997.01.01'),
(7, 'maniya velichia', '1985.01.01'),
(8, 'home album', '2020.01.01'),
(9, 'lova hate sex pain', '2010.01.01'),
(10, 'somnambula', '2013.01.01')


--adding new tracks
insert into tracks (id, name, duration, album_id)
values(2, 'slam', 256, 1),
(3, 'morning', 165, 2),
(4, 'superstar', 230, 2),
(5, 'death tone', 307, 3),
(6, 'metal daze', 277, 3),
(7, 'new generation', 351, 4),
(8, 'deep and dark', 221, 4),
(9, 'kind people', 316, 5),
(10, 'holliday of blood', 179, 5),
(11, 'sector gaza', 221, 6),
(12, 'auto-mat', 196, 6),
(13, 'it is the rock', 354, 7),
(14, 'torero', 328, 7),
(15, 'pivo-pivo-pivo', 129, 8),
(16, 'bezborodich', 168, 8),
(17, 'love hate sex pain', 315, 9),
(18, 'touche', 218, 9),
(19, 'friend', 144, 10),
(20, 'somnambula', 179, 10),
(21, 'my test song', 201, 10),
(22, 'song my test', 202, 10),
(23, 'tes song my', 203, 10),
(24, 'asdmyasd', 204, 10)


--adding collections
insert into collections(id, name, year)
values(2, 'super hits 2', '2014.01.01'),
(3, 'best', '2015.01.01'),
(4, 'collections1', '2016.01.01'),
(5, 'collections2', '2017.01.01'),
(6, 'collections3', '2018.01.01'),
(7, 'new best', '2019.01.01'),
(8, 'new best2', '2020.01.01'),
(9, 'new best 3', '2021.01.01')


--adding styles_band
insert into styles_band(style_id, band_id)
values(2, 3),
(3, 3),
(4, 4),
(5, 4),
(1, 5),
(2, 5),
(3, 6),
(4, 6),
(5, 7),
(1, 8),
(2, 8),
(3, 9),
(4, 9),
(5, 10),
(1, 10),
(2, 10),
(3, 10)


--adding album_band

insert into album_band(album_id, band_id)
values(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9),
(10,10)



insert into collection_track(collection_id, track_id)
values(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9)





















