import time 

def compte_to_ten():
    for i in range(11):
        print(i)
        time.sleep(0.5)
   
    


if __name__ == '__main__':
    start = time.perf_counter()
    compte_to_ten()
    compte_to_ten()
    stop = time.perf_counter()
    print("Done in {} seconds".format(stop - start))