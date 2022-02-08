import pytest
from chees_solver.main.views import index
from chees_solver.main.figure import pawl,tower

from django.test import Client
client = Client()
k=client.get(r'C:\Users\admin\PycharmProjects\t_for_company\chees_solver\main\views.py')
print(k)
@pytest.fixture()
def prepareddata():
    Data=pawl('a2')
    yield Data


def test_data(prepareddata:pawl):
    assert prepareddata.list_available_moves()==['a3', 'a4']

def test_pavi(prepareddata:pawl):
    assert prepareddata.validate_move('a3') == 'This move is available'

def test_data_error(prepareddata:pawl):
   with pytest.raises(AssertionError):
            assert prepareddata.list_available_moves()==6
def test_pavi_error(prepareddata:pawl):
   with pytest.raises(AssertionError):
            assert prepareddata.validate_move('a3')==6


@pytest.mark.performs
@pytest.mark.parametrize('data , expected',[('a5',['a6'])])
def test_x(data,expected):
    assert pawl(data).list_available_moves()==expected
#



# class Testopp:
#     def test_data(self):
#         data= Loopse([x for x in range(10)])
#         assert data.loos()==[0,5]
#
#
#     def test_data_error(self):
#         data2 = Loopse([10, 4, 'str'])
#         with pytest.raises(TypeError):
#             assert data2.loos()==[0,5,10]


# @pytest.fixture()
# def prepareddata():
#     Data=NumberChenge(0)
#     yield Data
#     Data=NumberChenge(0)
#
#
# def test_data(prepareddata:NumberChenge):
#     assert prepareddata.cheng_n()==6
#
#
# def test_data_error(prepareddata:NumberChenge):
#     prepareddata.__init__('f')
#     with pytest.raises(TypeError):
#             assert prepareddata.cheng_n()==6
# @pytest.fixture()
# def preper():
#     testclass = Test1(data=['a', 'b', 'c', 'd', 'f'])
#     yield testclass
#     testclass = Test1(data=['a', 'b', 'c', 'd', 'f'])
#
#
# def test_index(preper):
#     assert preper.index() ==[0,1,2,3,4]
#
# def test_indexrange(preper):
#     assert preper.indexrange()==[2,3,4]
#
# def test_index_error(preper):
#     with pytest.raises(AssertionError):
#         assert preper.index()==[2,3,4,5]
#
#
# import pytest
# from uuuu import *
#
# @pytest.mark.skipif(5==5,reason="test skipif")
# def test_answer():
#     assert x1(5) == 5
# @pytest.mark.skip(reason="dont need")
# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
#
# @pytest.mark.performs
# def test_case_1():
#     assert True
# @pytest.mark.markz
# def test_case_2():
#     assert True
#
# # for run category pytest -m markz(or performs) -v
#
#
#
#
#
# @pytest.mark.parametrize('x,expected',[(6,7),
#                                        (8,9),
#                                        (12,13),
#
#
#                                        ])
# def test_x(x,expected):
#     assert x1(x)==expected
#
#
# @pytest.mark.parametrize('x,expected',[(6,0),
#                                        (8,0),
#                                        (12,5),])
# def test_zero_d(x,expected):
#     with pytest.raises(ZeroDivisionError):
#         assert zero_d(x) ==expected
#
#
# def test_join_db():
#     db=MYDB()
#     conn=db.conect("server")
#     cur=conn.Cursor()
#     id=cur.execute('select id from database where name=jon')
#     assert id==123
#
# def test_join_dtb():
#     db=MYDB()
#     conn=db.conect("server")
#     cur=conn.Cursor()
#     id=cur.execute('select id from database where name=jon')
#     assert id==954
#
#
#
#
# def pytest_run_for():
#     return pytest.main(['-s', 'test_data.py'])
#
#
# if __name__ == "__main__":
#     pytest_run_for()