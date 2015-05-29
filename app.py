#!/usr/bin/env python

import os
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'squashthefatties'
app.debug = True  # TODO: change this when we deploy
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect', namespace='/server')
def on_connect():
    emit('response', {'data': 'Connection successful'})


@socketio.on('disconnect', namespace='/server')
def on_disconnect():
    emit('response', {'data': 'Disconnection successful'})

@socketio.on('client_connect', namespace='/server')
def on_client_connect(data):
    print 'client conncted:', data


if __name__ == "__main__":
    socketio.run(app, 
                 host=os.environ.get('OPENSHIFT_PYTHON_IP','127.0.0.1'), 
                 port=int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080)))