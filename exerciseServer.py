from flask import Flask, Response, request
import requests
import methods

app = Flask(__name__)


@app.route('/message', methods=["POST"])
def handle_message():
    returnMessage = ""
    chat_id = request.get_json()['message']['chat']['id']
    messageText = request.get_json()['message']['text']
    if messageText.startswith("/"):
        if len(messageText.split(" ")) == 1:
            returnMessage = "No number provided"
        else:
            requestSplit = messageText.split(" ")
            returnMessage = methodsDictionary[requestSplit[0]](int(requestSplit[1]))
    else:
        returnMessage = "[Choose:\n/check number to check if Prime\n" \
                        "/factorial number to calc factorial\n" \
                        "/palindrome number to check if palindrom\n" \
                        "/sqrt number to check if has integer square root]"

    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                       .format(TOKEN, chat_id, returnMessage))
    return Response("Done")


if __name__ == "__main__":
    TOKEN = '983035300:AAHcux1Rp4ZtT543UdkgB85enEcSkp5MT3s'
    TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://4f88bc5b.ngrok.io/message'.format(
        TOKEN)

    methodsDictionary = {
        '/check' : methods.isPrime,
        '/factorial' : methods.isFactorial,
        '/palindrome' : methods.isPalindrome,
        '/sqrt' : methods.hasSqrtRoot
    }
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=4000)