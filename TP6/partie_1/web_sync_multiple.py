import requests
import time
import sys


def get_content(url:str) -> str:
    url_request = requests.get(url)
    if (url_request.status_code != 200):
        print(url_request.status_code)
    else:
        return url_request.content
    

def write_content(content, file):
    file = "tmp/" + file
    file_open = open(file, "w")
    file_open.write(str(content))
    file_open.close()


def main():
    try:
        file = open(sys.argv[1])
    except IOError:
        print(IOError)
    lines = file.readlines()
    for each_lines in lines:
        write_content(get_content(each_lines[:-1]), each_lines[8:-2])


if __name__ == '__main__':
    if (len(sys.argv) == 2): 
        start = time.perf_counter()
        main()
        stop = time.perf_counter()
        print("Done in {} seconds".format(stop - start))
    elif (len(sys.argv)) < 2:
        print("Missing argument")
    elif (len(sys.argv)) > 2:
        print("Too much argument")
