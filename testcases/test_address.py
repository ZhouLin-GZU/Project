import pytest
class TestAddress():
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize('dict1',yaml.safe_load(open('./create.yaml',encoding='utf-8')))
    @pytest.mark.run(order=1)
    def test_create(self,dict1):
        if self.address.get(userid = dict1['userid'])['errcode'] == 0:
            self.address.delete(userid=dict1['userid'])
        assert self.address.create(userid=dict1['userid'],name=dict1['name'],
                                   mobile = dict1['mobile']),dep=dict1['department'])['errcode']==0

    @pytest.mark.parametrize('dict1',yaml.safe_load(open('./create.yaml',encoding='utf-8')))
    @pytest.mark.run(order=2)
    def test_get(self,dict1):
        assert self.address.get(userid=dict1['userid'])['userid'] == dict1['userid']

    @pytest.mark.parametrize('dict1',yaml.safe_load(open('./create.yaml',encoding='utf-8')))
    @pytest.mark.run(order=3)
    def test_update(self,dict1):
        assert self.address.update(userid=dict1['userid'],name=dict1['name'])==0

    @pytest.mark.parametrize('dict1',yaml.safe_load(open('./create.yaml',encoding='utf-8')))
    @pytest.mark.run(order=4)
    def test_get(self,dict1):
        assert self.address.get(userid=dict1['userid'])['userid'] == dict1['userid']

    @pytest.mark.parametrize('dict1',yaml.safe_load(open('./create.yaml',encoding='utf-8')))
    @pyexpat.mark.run(order=5)
    def test_delete(self,dict1):
        assert self.address.delete(userid=dict1['userid'])['errcode']==0



