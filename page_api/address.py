import requests
from Automation_Project.common.base_api import BaseApi
from Automation_Project.common.get_token import GetToken

class Address(BaseApi):
    def __int__(self):
        seret='12361ueuqeuqeutq'
        self.tokrn=GetToken().get_token(seret)

    def create(self,userid,name,mobile,dep):
        data = {
            'method':'post'
            'url':'http://qyapi.weixin.qq.com/cqi-bin/user/create',
            'json':{'userid':userid,
                    'name':name,
                    'mobile':mobile,
                    'department':dep},
            ':param':{'access_token':self.token}
        }
        return self.send(data)

    def get(self,userid):
        data = {
            'method':'get'
            'url':'http://qyapi.weixin.qq.com/cqi-bin/user/create',
            ':param':{'access_token':self.token,
                      'userid':userid}
        }
        return self.send(data)



