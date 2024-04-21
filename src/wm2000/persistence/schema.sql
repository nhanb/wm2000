-- TODO: Some migration system.
-- Maybe adapt Pytaku's [1] to use sqlite3 instead of apsw.
-- [1]: https://github.com/nhanb/pytaku/tree/16dd25ce047c9be493870afa7b5232fdc3e9d68d/src/pytaku/database

pragma user_version = 1;
pragma foreign_keys = on;
pragma busy_timeout = 4000;

-- All time values must be in UTC, in this format: 'YYYY-MM-DD HH:MM:SSZ'.
-- I like it because it's human-friendly and leaves no room for interpretation.
--
-- Sqlite's date/time functions default to UTC, but datetime() doesn't include
-- the Z, so to get the current time in our desired format, use this instead:
-- strftime('%Y-%m-%d %H:%M:%SZ')

-- global options & site-wide metadata
create table site (
    id integer primary key check (id = 0), -- ensures single row
    title text not null default 'My Site',
    tagline text not null default 'Let''s start this thing off right.',
    export_to text not null default ''
) strict;
insert into site(id) values(0);

create table post (
    id integer primary key,
    slug text unique not null,
    title text unique not null,
    content text not null default '',
    created_at datetime not null default (strftime('%Y-%m-%d %H:%M:%SZ')),
    updated_at datetime default null,
    is_draft boolean not null default true,
    show_in_feed boolean not null default true
);
