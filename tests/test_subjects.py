import pytest
import main
from unittest.mock import patch, MagicMock

# Test 3: Extrating 'subjects' field from FBI API
@patch('urllib.request.urlopen')
def test_subjects(mock_urlopen):
    mockres = MagicMock()
    mockres.read.return_value = '{"items":[{"title":"Test Title","subjects":["Subject1", "Subject2"],"field_offices":["Office1"]}]}'.encode('utf-8')    
    mock_urlopen.return_value.__enter__.return_value = mockres

    data = main.fetchdata_api(1)
    subjects = ','.join(data['items'][0].get('subjects', [])) 
    assert subjects == "Subject1,Subject2", f"Expected 'Subject1,Subject2', but got '{subjects}'"
