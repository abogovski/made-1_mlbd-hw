/* Result:
+---------------------------------------+----------------+-------------------+
|                 mbid                  | artist_lastfm  | scrobbles_lastfm  |
+---------------------------------------+----------------+-------------------+
| b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d  | The Beatles    | 517126254         |
+---------------------------------------+----------------+-------------------+ */

SELECT mbid, artist_lastfm, scrobbles_lastfm
FROM artists
ORDER BY scrobbles_lastfm DESC
LIMIT 1;
