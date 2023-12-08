import requests
import sys

def get_content(url:str) -> str:
    url_request = requests.get(url)
    if (url_request.status_code != 200):
        print(url_request.status_code)
    else:
        return url_request.content
    

def write_content(content, file):
    file = "/tmp/" + file
    file_open = open(file, "w")
    file_open.write(str(content))
    file_open.close()




if __name__ == '__main__':
    if (len(sys.argv) == 2): 
        write_content(get_content(sys.argv[1]), "test.txt")
    elif (len(sys.argv)) < 2:
        print("Missing argument")
    elif (len(sys.argv)) > 2:
        print("Too much argument")
