from unittest import mock
import gHub
import unittest
import requests
import json

class Testing_gHub_API(unittest.TestCase):


    @mock.patch('gHub.getUserRepos')
    def mock_getUserRepos(self,mock_get):
        mock_get.return_value = 10
        result = gHub.getUserRepos('rickhempinski')
        self.assertEqual(result, 10)

    
    @mock.patch('gHub.getUserRepos')
    def mock_getUserRepos_troyler(self,mock_GUR):
        mock_GUR.return_value = 6
        result = gHub.getUserRepos('troyler')
        self.assertEqual(result, 6)

    @mock.patch('gHub.requests')
    def testUserRepos(self, mock_req):
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        f = open('HW4a/rk_repo.json')
        mock_response.json.return_value = json.load(f)
        f.close()

