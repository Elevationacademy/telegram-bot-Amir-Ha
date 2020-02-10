from flask import Flask, Response, request
import requests

app = Flask(__name__)
def isPrime(num):
    if num == 0 or num == 1:
        return "Not prime"
    if num % 2 == 0:
        return "Come on dude, you know even numbers are not prime!"

    for i in range(2, num):
        if num%i == 0:
            return "Not Prime"
    return "Prime"


def isFactorial(number):
    factorial = 1
    for i in range(1, int(number) + 1):
        factorial *= i
    return factorial


def isPalindrome(number):
    reversedNum = 0
    tempNumber = int(number)
    while tempNumber > 0:
        reversedNum = int(reversedNum * 10)
        reversedNum = int(reversedNum + (tempNumber%10))
        tempNumber = int(tempNumber / 10)
    return reversedNum == number


@app.route('/message', methods=["POST"])
def handle_message():
    returnMessage = ""
    chat_id = request.get_json()['message']['chat']['id']
    if request.get_json()['message']['text'].startswith("/"):
        if len(request.get_json()['message']['text'].split(" ")) == 1: # == "/check" or request.get_json()['message']['text'] == "/check ":
            returnMessage = "No number provided"
        elif request.get_json()['message']['text'].startswith("/check"):
            number = request.get_json()['message']['text'].split(" ")[1]
            returnMessage = isPrime(int(number))
        elif request.get_json()['message']['text'].startswith("/factorial"):
            number = request.get_json()['message']['text'].split(" ")[1]
            returnMessage = isFactorial(number)
        elif request.get_json()['message']['text'].startswith("/palindrome"):
            number = request.get_json()['message']['text'].split(" ")[1]
            returnMessage = isPalindrome(int(number))
    else: returnMessage = "[Write /check number to check if Prime\n/factorial number to calc factorial]"

    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                       .format(TOKEN, chat_id, returnMessage))
    return Response("Done")


if __name__ == "__main__":
    TOKEN = '983035300:AAHcux1Rp4ZtT543UdkgB85enEcSkp5MT3s'
    TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://28c38dd0.ngrok.io/message'.format(
        TOKEN)

    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=4000)