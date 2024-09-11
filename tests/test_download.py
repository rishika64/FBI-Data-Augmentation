import pytest
import main
from unittest.mock import patch, MagicMock

# Test 1: Downloading non-empty data from a URL
@patch('urllib.request.urlopen')
def test_download(mock_urlopen):
    mockres = MagicMock()
    mockres.read.return_value = '{"items":[{"title":"Test Title","subjects":["Subject1"],"field_offices":["Office1"]}]}'.encode('utf-8')
    mock_urlopen.return_value.__enter__.return_value = mockres

    data = main.fetchdata_api(1)  # example: page number 1
    assert data is not None
    assert 'items' in data
    assert len(data['items']) > 0
