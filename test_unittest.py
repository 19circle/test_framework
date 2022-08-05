import unittest
class Test_Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('就开始一次哦')
    @classmethod
    def tearDownClass(cls) -> None:
        print('就结束一次哦')
    def setUp(self) -> None:
        print('每一次开始啦')
    def tearDown(self) -> None:
        print('每一次结束啦')
    def test_01(self):
        print(1)
        self.assertEqual(1,1,'判断1==2')

    def test_02(self):
        print(2)
        self.assertTrue(1==1,'verify')

    def test_03(self):
        print(3)

    def test_04(self):
        print(4)
if __name__=='__main__':
    suie = unittest.TestLoader().loadTestsFromTestCase(Test_Demo)
    suite = unittest.TestSuite([suie])
    # suite = unittest.TestSuite()
    # suite.addTest(Test_Demo("test_01"))
    # suite.addTest(Test_Demo('test_02'))
    unittest.TextTestRunner().run(suite)
