import pytest
import main
from unittest.mock import patch, MagicMock


# Test 2: Extrating 'title' field from FBI API
@patch('urllib.request.urlopen')
def test_title(mock_urlopen):
    mockres = MagicMock()
    mockres.read.return_value = '{"items":[{"title":"Test Title","subjects":["Subject1"],"field_offices":["Office1"]}]}'.encode('utf-8')    
    mock_urlopen.return_value.__enter__.return_value = mockres

    data = main.fetchdata_api(1)
    title = data['items'][0].get('title', '')
    assert title == "Test Title"
    