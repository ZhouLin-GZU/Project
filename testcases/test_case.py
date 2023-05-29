import pytest

# @pytest.fixture(scope='class',autouse=True)
# def before
#     print('-----------------------')

class Test_py_01:
    @classmethod
    def setUpCalss(self):
        print('执行开始')
    @classmethod
    def tearDownClass(self):
        print('执行结束')

    @pytest.mark.parametrize('a',[3,6])
    def test_01(self,a):
        print('test001')
        assert 1

    @pytest.mark.run(order = 1)
    # @pytest.mark.last
    # @pytest.mark.skip
    def test_02(self):
        print('test002')
        assert 1

    # @pytest.mark.repeat(2)
    def test_03(self):
        print('test003')
        assert 1


if __name__=='__main__':
    pytest.main(['-s','-v','--html=F:\file2\Automation_Project\report/test_Test.html','test_tt.py::Test_py'])
