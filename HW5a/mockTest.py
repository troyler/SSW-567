from unittest import mock
import gHub
import unittest

class Testing_gHub_API(unittest.TestCase):


    @mock.patch('gHub.getUserRepos')
    def mock_getUserRepos(self,mock_GUR):
        mock_GUR.return_value = 10
        result = gHub.getUserRepos('rickhempinski')
        self.assertEqual(result, 10)

    
    @mock.patch('gHub.getUserRepos')
    def mock_getUserRepos_troyler(self,mock_GUR):
        mock_GUR.return_value = 6
        result = gHub.getUserRepos('troyler')
        self.assertEqual(result, 6)

