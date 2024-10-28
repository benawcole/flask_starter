# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
POST /album
"""
def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post("/album", data={'title':'Revolver', 'release_year':1966, 'artist_id':4})
    assert response.status_code == 200

"""
GET /album
"""
def test_get_album(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get("/album")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == """Album(1, Doolittle, 1989, 1)
Album(2, Surfer Rosa, 1988, 1)
Album(3, Waterloo, 1974, 2)
Album(4, Super Trouper, 1980, 2)
Album(5, Bossanova, 1990, 1)
Album(6, Lover, 2019, 3)
Album(7, Folklore, 2020, 3)
Album(8, I Put a Spell on You, 1965, 4)
Album(9, Baltimore, 1978, 4)
Album(10, Here Comes the Sun, 1971, 4)
Album(11, Fodder on My Wings, 1982, 4)
Album(12, Ring Ring, 1973, 2)"""



