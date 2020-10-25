from main import app
from flask import json

def test_success():
    response = app.test_client().get(
        '/calendars',
        content_type = 'application/json',
    )

    data = json.loads(response.get_data(as_text=False))

    assert response.status_code == 200
    assert response.content_type == 'application/json'

    assert data['data']['id'] == None
    assert data['data']['type'] == 'calendars'

    attributes = data['data']['attributes']
    assert len(attributes) == 5

    assert attributes[0]['mod1']
    assert attributes[0]['mod1']['frontend']
    assert attributes[0]['mod1']['frontend'] == {'zoom_link': ''}
    assert attributes[0]['mod1']['backend']
    assert attributes[0]['mod1']['backend'] == {'zoom_link': ''}

    mod2 = attributes[1]['mod2']
    assert mod2
    assert mod2['frontend']
    assert mod2['frontend'] == {'zoom_link': ''}
    assert mod2['backend']
    assert mod2['backend'] == {'zoom_link': ''}

    mod3 = attributes[2]['mod3']
    assert mod3
    assert mod3['frontend']
    assert mod3['frontend'] == {'zoom_link': ''}
    assert mod3['backend']
    assert mod3['backend'] == {'zoom_link': ''}

    assert attributes[3]['mod4']
    assert attributes[3]['mod4']['frontend']
    assert attributes[3]['mod4']['frontend'] == {'zoom_link': ''}
    assert attributes[3]['mod4']['backend']
    assert attributes[3]['mod4']['backend'] == {'zoom_link': ''}

    assert attributes[4]['community']  == {'zoom_link': ''}
