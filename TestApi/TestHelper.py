import requests
import os
import json

class TestHelper:
    session = None
    limHost = None
    salusSyncPost = None
    limBaseUrl = None
    additionalHeaders = {}

    def setupMasterKey(self, masterKey):
        self.additionalHeaders['MASTER-KEY'] = masterKey

    def printPrettyJsonResponse(self, jsonData):
        jsonPrettyString = self.returnPrettyJsonString(jsonData)
        print("Response: \n")
        print(jsonPrettyString)
        print("\n")

    def returnPrettyJsonString(self, jsonData):
        jsonPrettyString = json.dumps(jsonData, indent=4, sort_keys=True)
        return jsonPrettyString

    def headRequest(self, subUrl):
        response = requests.head(self.ehlpBaseUrl + '/' + subUrl)
        return response

    def handleJsonResponse(self, response):
        if isinstance(response, requests.Response):
            responseJson = response.json()
            if response.status_code == 200:
                print ("Request (" + response.request.method + ") successful for "+response.url)
                self.printPrettyJsonResponse(responseJson)
                return response.status_code, responseJson
            else:
                print ("Request (" + response.request.method + ") failed with status code " + str(response.status_code) + " for "+response.url)
                self.printPrettyJsonResponse(responseJson)
                return response.status_code, responseJson
        else:
            raise(Exception("Response must be of type requests response"))


    def makeHeadRequestAndPrintResult(self, subUrl):
        headResponse = self.headRequest(subUrl)
        jsonHeadResponse = self.handleJsonResponse(headResponse)
        return jsonHeadResponse

    def makeOptionRequestAndPrintResult(self, subUrl):
        optionResponse = self.optionRequest(subUrl)
        jsonOptionResponse = self.handleJsonResponse(optionResponse)
        return jsonOptionResponse

    def makeDeleteRequestAndPrintResult(self, subUrl):
        deleteResponse = self.deleteRequest(subUrl)
        jsonDeleteResposne = self.handleJsonResponse(deleteResponse)
        return jsonDeleteResposne

    def make_get_request_and_print_result(self, subUrl):
        getResposne = self.getRequest(subUrl)
        jsonGetResponse = self.handleJsonResponse(getResposne)
        return jsonGetResponse

    def makePutRequestAndPrintResult(self, subUrl, data):
        putResponse = self.putRequest(subUrl, data)
        jsonPutResponse = self.handleJsonResponse(putResponse)
        return jsonPutResponse

    def make_post_request_and_print_result(self, subUrl, data):
        postResponse = self.postRequest(subUrl, data)
        jsonPostResponse = self.handleJsonResponse(postResponse)
        return jsonPostResponse

    def optionRequest(self, subUrl):
        response = None
        if subUrl is not None and subUrl.strip() != '':
            if len(self.additionalHeaders) > 0:
                response = self.session.options(self.limBaseUrl + '/' + subUrl, headers=self.additionalHeaders)
            else:
                response = self.session.options(self.limBaseUrl + '/' + subUrl)
        return response

    def deleteRequest(self, subUrl):
        response = None
        if subUrl is not None and subUrl.strip() != '':
            if len(self.additionalHeaders) > 0:
                response = self.session.delete(self.limBaseUrl + '/' + subUrl, headers=self.additionalHeaders)
            else:
                response = self.session.delete(self.limBaseUrl + '/' + subUrl)
        return response

    def putRequest(self, subUrl, data):
        response = None
        if subUrl is not None and subUrl.strip() != '':
            if len(self.additionalHeaders) > 0:
                response = self.session.put(self.limBaseUrl + '/' + subUrl, json=data, headers=self.additionalHeaders)
            else:
                response = self.session.put(self.limBaseUrl + '/' + subUrl, json=data)
        return response

    def getRequest(self, subUrl):
        response = None
        if subUrl is not None and subUrl.strip() != '':
            if len(self.additionalHeaders) > 0:
                response = self.session.get(self.limBaseUrl + '/' + subUrl, headers=self.additionalHeaders)
            else:
                response = self.session.get(self.limBaseUrl + '/' + subUrl)
        return response

    def postRequest(self, subUrl, data):
        response = None
        if subUrl is not None and subUrl.strip() != '':
            if len(self.additionalHeaders) > 0:
                response = self.session.post(self.limBaseUrl + '/' + subUrl, json=data, headers=self.additionalHeaders)
            else:
                response = self.session.post(self.limBaseUrl + '/' + subUrl, json=data)
        return response

    def __init__(self):
        self.limHost = os.environ.get("lim_host")
        self.limPort = os.environ.get("lim_port")
        if self.limHost is not None and self.limPort is not None:
            self.limBaseUrl = "http://" + self.limHost + ":" + self.limPort
        else:
            self.limBaseUrl = "http://localhost:5000"
        self.session = requests.Session()
