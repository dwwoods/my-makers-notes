# Workshop 2

Date: *4 Nov 24*

This workshop focuses on applying Test-Driven Development (TDD) to web routes. We will be writing integration tests that simulate HTTP requests to our application and assert that the server provides the correct response (e.g., status code, body content). This test-first approach will guide the creation and implementation of our web routes.

We will use the makers starter project - which I've updated to a initialized project here:

[text](https://github.com/dwwoods/Mod4Workshop2)

##  Integration Testing: Database Seeding and Client Requests

A typical integration test for a web application follows a clear pattern:

1. **Arrange (Set the Scene):** First, prepare the database to a known state. This is often done by running a seed script (`db_connection.seed(...)`) to ensure your test starts with predictable data.
2. **Act (Make the Request):** Use the test client (`web_client`) to simulate an HTTP request to your application. This involves specifying the route (e.g., `/albums`) and any data to be sent (e.g., for a `POST` request).
3. **Assert (Check the Result):** Finally, check the response from the server to ensure it's what you expect (e.g., status code is 200, correct content is in the response body).

Here is a brief example of a test for creating a new album:

```python
# test_app.py
def test_post_create_album(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql") # 1. Arrange
    response = web_client.post('/albums', data={'title': 'New Album', 'release_year': '2024'}) # 2. Act
    assert response.status_code == 200 # 3. Assert
```
