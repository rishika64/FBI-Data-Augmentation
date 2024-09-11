# cis6930fa24 -- Assignment0 

Name: Rishika Sharma
UFID: 32772571

# Assignment Description 

This assignment focuses on extracting and formatting data from the FBI Wanted API into a JSON format, using a thorn character (`þ`) as field separator. The task requires creating a Python package that retrieves information (title, subjects, and field offices) based on a given page number from the API, or alternatively, reading from a local JSON file. The program should handle command-line arguments for either the API or file input and print the output to standard out. It also includes creating test cases for key functionalities such as data downloading, title extraction, subjects extraction, and formatting. 

# How to install
pipenv install -e 

## How to run
pipenv run python main.py --page # (insert any integer from 1 to 1008 instead of #)
pipenv run python main.py --file # (insert any string file location instead of #)

## How to test
pipenv run python -m pytest -v

## Functions

#### main.py
**1. `fetchdata_api(pg)`**
- This function reads data from a specific page number given and fetches data using FBI API. The returned data is in the form of JSON file and includes fields `title`, `subjects`, and `field_offices`.
- `pg` (int) parameter is the page number from which the data is supposed to be fetched. If this integer number goes beyond the limit or page number it will show `No data found`
- A header is constructed so that the request is not rejected, often non-header requests are blocked assuming they are automated bots. So we recreate a browser request instead for all OS types such as Windows, MacOS and Linux.
- Requests data using `urllib.request.urlopen()` which ensures the connection is securely opened and closed.
- The raw data is returned as a JSON object using `json.loads()`.

**2. `fetchdata_file(loc)`**
- This function reads data from a local JSON file and fetches data using FBI API. The returned data is in the form of JSON file and converted into a Python object (list) using `json.load()`.
- `loc` (str) parameter is the file location where the JSON file is located. If the file is inaccessible, it will show `No file found` and print error message.

 **3. `format(data)`**
- This function takes the data fetched and returns a string with thorn-separated (`þ`) values. 
- `data` (dict) is a dictionary that contains the data fetched from the API or file. It contains a key called `items` that contains a list of these dictionaries. Each list represents a given word (such as `title`, `subjects`, and `field_offices`).
- The function iterates through each item in the `items` list, and fetches the following details:
  - `title`: title of the criminal (empty string if not available).
  - `subjects`: list of subjects associated with the criminal (attached by commas).
  - `field_offices`: list of field offices associated with the criminal (attached by commas).
- The extracted fields are then concatenated using the thorn character (`þ`).

**4. `main(pg=None, loc=None)`**
- This is the main driver function that connects the accessed data and formatted data according to the input parameters provided by the user. 
- If the provided item is integer `pg` parameter is triggered, and `fetchdata_api()` function is called.
- If the provided item is string `loc` parameter is triggered, and `fetchdata_file()` function is called.
- Prints the formatted data on console.
- This function assumes it’s running on command-line interface, and prints formatted data directly on the console.

**5. Command-Line Interface**
The script accepts two command-line arguments:
- `--file`: Specifies location of the local JSON file.
- `--page`: Specifies page number of the data to be fetched from FBI API.
- The script parses the arguments using `argparse.ArgumentParser` for either `--page` or `--file` argument.
- If neither argument is present, it displays help message.

#### test.py
**1. `test_download(mock_urlopen)`**
- This test checks if the `fetchdata_api()` function is correctly downloading non-empty data from the FBI API.
- The test mocks the `urllib.request.urlopen()` function, which uses `fetchdata_api()` to make an API request.
- The mocked `urlopen()` is then used to return this mock response when called.
- Assertions are added to make sure:
  - The returned data is not `None`.
  - The data contains the `items` key.
  - The `items` list is non-empty.
- We are assuming that the `items` key will always be present in the API's response.

**2. `test_title(mock_urlopen)`**
- This test checks if the `fetchdata_api()` function is correctly extracting the `title` field from the API response.
- The test mocks `urllib.request.urlopen()` function which returns a sample JSON response with the `title`.
- The test sample calls page number 1 (`fetchdata_api(1)`) to fetch data from mock API.
- It then extracts the `title` from the first item in the `items` list.

**3. `test_subjects(mock_urlopen)`**
- This test checks if the `fetchdata_api()` function is correctly extracting and formatting the `subjects` field from the API response.
- The test mocks `urllib.request.urlopen()` function which returns a sample JSON response with  multiple `subjects`.
- The mocked response is a JSON object that contains two subjects: `Subject1` and `Subject2`.
- The test sample calls page number 1 (`fetchdata_api(1)`) to fetch the mock data.
- It then extracts and concatenates the `subjects` list with commas.

**4. `test_offices(mock_urlopen)`**
- This test checks if the `fetchdata_api()` function is correctly extracting and formatting the `field_offices` field from the API response.
- The test mocks `urllib.request.urlopen()` function which returns a sample JSON response with multiple `field_offices`.
- The mocked response is a JSON object that contains two field offices: `Office1` and `Office2`.
- The test sample calls page number 1 (`fetchdata_api(1)`) to fetch the mock data.
- It then extracts and joins the `field_offices` list with commas.

**5. `test_thorn(mock_urlopen)`**
- This test checks if the `format()` function is correctly formatting the data into a thorn-separated string.
- The test mocks `urllib.request.urlopen()` function which returns a sample JSON response with `title`, `subjects`, and `field_offices` fields.
- The mocked response includes the `title`, a single subject (`Subject1`), and a single field office (`Office1`).
- The test sample calls page number 1 (`fetchdata_api(1)`) to fetch the mock data.
- It then passes the fetched data through `format()`.
- Assertion is added to make sure the formatted string matches the expected result: "Test TitleþSubject1þOffice1".
- The `format()` function correctly handles and processes the data returned by the API.

**6. `test_local(mock_file)`**
- This test checks if the `fetchdata_file()` function is correctly reading and parsing the data from a local JSON file.
- The test uses `mock_open` to simulate opening and reading a file.
- The file contains a sample JSON string with fields: `title`, `subjects`, and `field_offices`.
- The test calls `fetchdata_file()` with the mocked file.
- Assertions are added to make sure:
  - The data is not `None`.
  - The data contains the `items` key.
  - The `title` field in the first item matches the expected value.
- we are assuming the `items` key is always present in the JSON structure.

