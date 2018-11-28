# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.phonon import Phonon
from view.home import Ui_Form
import websocket
import requests
import json
def run_async(func):
    from threading import Thread
    from functools import wraps
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target = func, args = args, kwargs = kwargs)
        func_hl.setDaemon(True)
        func_hl.start()
        return func_hl
    return async_func
class HomeView(QWidget,Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
class Home():
    play_indx = 0
    to_play = []
    WS = None
    SRV = "http://192.168.42.228:8000/"

    def __init__(self):
        Home.server = requests.session()
        self.output = Phonon.AudioOutput(Phonon.MusicCategory)
        self.m_media = Phonon.MediaObject()
        Phonon.createPath(self.m_media, self.output)
        QObject.connect(self.m_media, SIGNAL('finished()'), self.enqueueNextSource)
        self.home = HomeView()
        self.home.showNormal()
        self.home.setWindowTitle(u'customers caller app')
        self.home.label.setText(u"غير متصل")
        self.WS_OPEN()

    @run_async
    def WS_OPEN(self):
        self.WS = websocket.WebSocketApp("ws://192.168.42.228:8000/sounds/",
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error)
        while True:
            self.WS.run_forever()
    def on_open(self):
        self.home.label.setText(u"متصل")
        print(555)

    def on_error(self,err):
        self.home.label.setText(u'مشكلة بالاتصال')


    def on_message(self,data):
        data = json.loads(data).get("message")
        print data
        msg = data.get('num')
        term = data.get('terminal')
        self.home.label.setText(u'عميل رقم {} شباك رقم {} '.format(msg,term))
        if msg:
            self.call_cust(msg,term)
            self.play_s()
    def play_s(self):
        self.m_media.setCurrentSource(Phonon.MediaSource(self.to_play[self.play_indx]))
        self.m_media.play()

    def enqueueNextSource(self):
        self.play_indx += 1
        if self.play_indx < len(self.to_play):
            self.play_s()

    def call_cust(self,num,term):
        try:
                self.to_play.append('sounds/Tone1.wav')
                self.to_play.append('sounds/customer11.wav')
                self.call_num(num)
                self.to_play.append('sounds/counter.wav')
                self.to_play.append('sounds/%s.wav' % (term))
                self.play_s()
        except Exception as ex:
            print(ex)
    def call_num(self,num,plus=False):
        direct = list(range(1,21))
        direct.extend([30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900])
        if plus:
            self.to_play.append('sounds/plus.wav')
        if num in direct:
            self.to_play.append('sounds/%s.wav'%(str(num)))
        elif num < 100:#52
            num1 = str(num)[1]
            plus = 'plus'
            num2 = str(num)[0]+"0"
            self.to_play.append('sounds/%s.wav' % (num1))
            self.to_play.append('sounds/%s.wav' % (plus))
            self.to_play.append('sounds/%s.wav' % (num2))
        elif num < 1000:#999
            num1 = str(num)[0] + "00"
            num2 = str(num)[1:]
            self.to_play.append('sounds/%s.wav' % (num1))
            self.call_num(int(num2),True)
