create table if not exists executor (
    id serial primary key,
    name varchar(40) not null
);


create table if not exists genre (
    id serial primary key,
    name varchar(40) not null unique
);

create table if not exists executor_genre (
    executor_id integer references executor(id),
    genre_id integer references genre(id),
    constraint pk_executor_genre primary key (executor_id, genre_id)
);

create table if not exists album (
    id serial primary key,
    name varchar(40) not null,
    year integer
);

creat table if not exists album_executor (
    executor_id integer references executor(id),
    album_id integer references album(id),
    constraint pk_album_executor primary key (executor_id, album_id)
);

create table if not exists track (
    id integer primary key references album(id),
    name varchar(40) not null,
    lenght integer
);

create table if not exists collection (
    id serial primary key,
    name varchar(40) not null,
    year integer    
);

create table if not exists track_collection (
    track_id integer references track(id),
    collection_id integer references collection(id),
	constraint pk_track_collection primary key (collection_id, track_id)
);