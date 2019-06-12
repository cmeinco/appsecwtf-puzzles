from flask import Flask
import time 
import random
from threading import Lock

app = Flask(__name__)
lock = Lock()

@app.route('/')
def hello_world():
   return "Hello World"

@app.route("/concurrenttest")
def concurrent_test():
    
    # check total potatoes
    # read a file
    with open("testfile.dat", "r") as infile:
        lines=infile.readlines()
    infile.close()
    
    #sleep here to fake a slow io process
    time.sleep(10)

    totalpotatoes=len(lines)
    retVal=""
    if totalpotatoes > 5:
        retVal+="Exceed the Potato Limit, currently {}.".format(totalpotatoes)
    else:
        retVal+="Read in {} Potatos.".format(totalpotatoes)
        with open("testfile.dat","a") as outfile:
            outfile.write("a potato\n")
        outfile.close()

    return retVal


@app.route("/concurrenttestfixed")
def concurrent_fixed():
    retVal=""

    with lock:

        # check total potatoes
        # read a file
        with open("testfilefixed.dat", "r") as infile:
            lines=infile.readlines()
        infile.close()
        
        #sleep here to fake a slow io process
        time.sleep(10)

        totalpotatoes=len(lines)
        if totalpotatoes > 5:
            retVal+="Exceed the Potato Limit, currently {}.".format(totalpotatoes)
        else:
            retVal+="Read in {} Potatos.\n".format(totalpotatoes)
            with open("testfilefixed.dat","a") as outfile:
                outfile.write("a potato\n")
            outfile.close()

    return retVal


if __name__ == "__main__":

    app.run(port=5000,threaded=True)

