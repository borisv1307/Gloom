def test_index_returns_status_200(flask_test_client):
    response = flask_test_client.get('/', content_type='html/text')

    assert response.status_code == 200
