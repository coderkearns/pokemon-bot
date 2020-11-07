# This is a module to allow you to serve your discord bot on repl.it
# https://repl.it/talk/learn/Hosting-discordpy-bots-with-replit/11008
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "The bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
