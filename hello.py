from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def welcome_msg():
    return "<h1>Hi there! Here you can find some Leetcode problems solutions in a form of Python Flask microservice</p>"


@app.route("/find_squares")
def find_squares():
    
    num = int(request.args.get("num"))

    if num % 2 == 0:
        raise ObjectNotFound("Bad param. Num difference cannot be even.")

    current = 1
    next = 2

    current2 = current ** 2
    next2 = next ** 2
    diff = next2 - current2

    #return "Diff is {0}".format(diff)

    while diff != num:
        current+=1
        next+=1
        current2 = current ** 2
        next2 = next ** 2
        diff = next2 - current2

    return "For the given difference {0} first square is {1} and second square is {2}".format(num, next2, current2)
