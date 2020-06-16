
from flask import Flask, Response, jsonify, request

from dataGenerator import dataGenerator


class CPSAPi(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)
        self.ip="0.0.0.0"
        self.port=80
        self.data=[]

    def run(self):
        self.app.run(host=self.ip, port=self.port,threaded=True)


    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, handler)

    def help(self):
        rep = {"getData": "/getData", "getDatas": "/getDatas/<time>"}
        return rep

    def getData(self):
        return jsonify(self.data[len(self.data)-1])

    def getDatas(self,time):
        d =  []
        time=int(time)
        if time > len(self.data):
            time = 0
        for i in range(len(self.data)-time,len(self.data)-1):
            d.append(self.data[i])
        return jsonify(d)

    def start(self):
        self.genrator = dataGenerator(self)
        self.genrator.daemon = True
        self.genrator.start()
        return jsonify(True)

class CPS():
    def __init__(self):

        self.manager = CPSAPi('manager')
        self.manager.add_endpoint(endpoint='/', endpoint_name='/', handler=self.manager.help)
        self.manager.add_endpoint(endpoint='/start', endpoint_name='start', handler=self.manager.start)
        self.manager.add_endpoint(endpoint='/getData', endpoint_name='getData',
                                  handler=self.manager.getData)
        self.manager.add_endpoint(endpoint='/getDatas/<time>', endpoint_name='getDatas', handler=self.manager.getDatas)

        self.manager.run()
        self.genrator.start()


