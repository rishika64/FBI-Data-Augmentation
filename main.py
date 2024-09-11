import argparse  
import sys  
import urllib.request  
import json  

# fetching data from a specific page number 
def fetchdata_api(pg):
    try:
        url = f"https://api.fbi.gov/wanted/v1/list?page={pg}"
        headers = {} 
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          
        formatted_url = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(formatted_url) as response:
            raw_data = response.read()  # access data 
        
        # return data as JSON
        return json.loads(raw_data)
    
    # error handling
    except urllib.error.URLError as error:
        print(f"Error Caught: {error}")
        return None


# fetching data from local JSON file
def fetchdata_file(loc):
    try:
        with open(loc, 'r') as file:
            return json.load(file)  
    
    # error handling
    except FileNotFoundError:
        print(f"No file found")
        return None


# formatting data
def format(data):
    if data and 'items' in data:
        newoutput = []
        for item in data['items']:
            title = item.get('title', '')  # empty string for null title
            subjects = ','.join(item.get('subjects', []) or [])  # empty list for null subjects
            field_offices = ','.join(item.get('field_offices', []) or [])  # empty list for null field_offices
            
            # separate the string by thorn character (þ) 
            newoutput.append(f"{title}þ{subjects}þ{field_offices}")
        
        return '\n'.join(newoutput)  
    else:
        return "No data found"


# driver function 
def main(pg=None, loc=None):
    data = None  # initialization 

    # if page number given
    if pg is not None: 
        data = fetchdata_api(pg)

    # if file location given
    elif loc is not None: 
        data = fetchdata_file(loc)
    
    # format and return
    if data:
        finaldata = format(data)
        print(finaldata)
    else:
        print("No data")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help='file location')
    parser.add_argument("--page", type=int, required=False, help='page number')
    args = parser.parse_args()
    
    # run driver functions
    if args.page:
        main(pg=args.page)
    elif args.file:
        main(loc=args.file)
    else:
        parser.print_help(sys.stderr)
