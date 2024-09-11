import pytest
import main
from unittest.mock import patch, MagicMock

# Test 5: Printing the full thorn separated file
@patch('urllib.request.urlopen')
def test_thorn(mock_urlopen):
    mockres = MagicMock()
    mockres.read.return_value = '{"items":[{"title":"Test Title","subjects":["Subject1"],"field_offices":["Office1"]}]}'.encode('utf-8')    
    mock_urlopen.return_value.__enter__.return_value = mockres

    data = main.fetchdata_api(1)
    formatted_data = main.format(data)
    expected_output = "Test TitleþSubject1þOffice1"
    assert formatted_data == expected_output, f"Expected '{expected_output}', but got '{formatted_data}'"
 