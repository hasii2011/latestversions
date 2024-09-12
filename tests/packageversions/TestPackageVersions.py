
from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.UnitTestBase import UnitTestBase

from packageversions.PackageVersions import PackageVersions


class TestPackageVersions(UnitTestBase):
    """
    Auto generated by the one and only:
        Gato Malo – Humberto A. Sanchez II
        Generated: 10 September 2024
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testRunCommandFail(self):
        status: int = PackageVersions.runCommand('/bogus/bin/fail')
        self.assertNotEqual(0, status, 'This should fail')

    def testRunCommandPass(self):
        status: int = PackageVersions.runCommand('/opt/homebrew/bin/jq --version')
        self.assertEqual(0, status, 'This should fail')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPackageVersions))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
