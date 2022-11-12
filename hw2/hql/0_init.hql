CREATE TABLE artists (
    mbid string,
    artist_mb string,
    artist_lastfm string,
    country_mb string,
    country_lastfm string,
    tags_mb string,   
    tags_lastfm string,
    listeners_lastfm bigint,
    scrobbles_lastfm bigint,
    ambiguous_artist boolean
) PARTITIONED BY (fake_partition boolean) 
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
tblproperties("skip.header.line.count"="1");

LOAD DATA INPATH '/hw2/artists.csv'
    OVERWRITE INTO TABLE artists
    PARTITION (fake_partition = true);
