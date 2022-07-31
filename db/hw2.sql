--drop table albums cascade;
--drop table bands cascade;
--drop table styles cascade;
--drop table styles_band cascade;
--drop table tracks cascade;
--drop table album_band cascade;


create table if not exists styles (
  id serial primary key,
  name varchar(100) not null
);

insert into styles(id, name)
values(1, 'rock'),
(2, 'punk-rock'),
(3, 'ska')

--update styles set name = 'rock' where name = 'pop'

create table if not exists bands (
 id serial primary key,
 name varchar(100) not null
);


insert into bands(id, name)
values(1, 'naiv'),
(2, 'goodtimes')

select * from bands


create table if not exists albums (
 id serial primary key,
 name varchar(100) not null,
 year date not null
);


insert into albums(id, name, year)
values(1, 'nate kushayte', '2019.01.01')


create table if not exists tracks (
 id serial primary key,
 name varchar(100) not null,
 duration numeric not null,
 album_id integer references albums(id)
);

insert into tracks (id, name, duration, album_id)
values(1, 'pora smiritsya', 184, 1)


--create many-to-many conection for band and style
create table if not exists styles_band (
 style_id integer references styles(id),
 band_id integer references bands(id),
 constraint pk primary key (style_id, band_id)
);

insert into styles_band(style_id, band_id)
values(1, 1),
(2, 1),
(1, 2),
(2, 2),
(3, 2)

--create many-to-many conection for album and band
create table if not exists album_band (
 album_id integer references albums(id),
 band_id integer references bands(id),
 constraint ab primary key (album_id, band_id)
);

insert into album_band(album_id, band_id)
values(1, 1),
(1, 2)


create table if not exists collections (
 id serial primary key,
 name varchar(100) not null
);

insert into collections(id, name)
values(1, 'super hits')

--create many-to-many conection for collecions and tracks
create table if not exists collection_track (
 collection_id integer references collections(id),
 track_id integer references tracks(id),
 constraint ct primary key (collection_id, track_id)
);

insert into collection_track(collection_id, track_id)
values(1, 1)


