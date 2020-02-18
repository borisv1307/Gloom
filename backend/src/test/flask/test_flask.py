import json


def test_index_returns_status_200(flask_test_client):
    response = flask_test_client.get('/', content_type='html/text')

    assert response.status_code == 200


def test_start_returns_status_200(flask_test_client):
    response = flask_test_client.get('/start', content_type='html/text')

    assert response.status_code == 200


def test_start_returns_json_string(flask_test_client):
    for _ in range(30):
        response = flask_test_client.get('/start', content_type='html/text')
        assert response
        dungeon_json = json.loads(response.data)
        assert '0' in dungeon_json

        room_json = dungeon_json['0']
        assert 'name' in room_json
        assert 'tiles' in room_json


def test_experimental_start_returns_json_string(experimental_flask_test_client):
    test_start_returns_json_string(experimental_flask_test_client)
