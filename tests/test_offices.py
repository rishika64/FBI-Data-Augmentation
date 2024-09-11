import pytest
import main
from unittest.mock import patch, MagicMock

# Test 4: Extrating 'field_offices' field from FBI API
@patch('urllib.request.urlopen')
def test_offices(mock_urlopen):
    mockres = MagicMock()
    mockres.read.return_value = '{"items":[{"title":"Test Title","subjects":["Subject1"],"field_offices":["Office1", "Office2"]}]}'.encode('utf-8')    
    mock_urlopen.return_value.__enter__.return_value = mockres

    data = main.fetchdata_api(1)
    field_offices = ','.join(data['items'][0].get('field_offices', []))
    assert field_offices == "Office1,Office2", f"Expected 'Office1,Office2', but got '{field_offices}'"
