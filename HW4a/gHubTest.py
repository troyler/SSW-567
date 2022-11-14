import unittest

# -*- coding: utf-8 -*-

import unittest
from gHub import getUserRepos, commitHistory, returnInfo
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class TestGitHubRequest(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testGetNumberRepos(self): 
        self.assertEqual(len(getUserRepos("troyler")),5)

    def testGetRepos(self):
        repositories = ['ISS-API-Learning', 'python-circleci', 'SSW-567', 'SSW-567-Triangle', 'wordleplusplus'] 
        self.assertEqual(getUserRepos("troyler"),repositories)

    def testCommitHistory(self):
        repositories = [('ISS-API-Learning',1), ('python-circleci', 30), ('SSW-567', 12), ('SSW-567-Triangle', 1), ('wordleplusplus',30)] 
        for repo in repositories:
            self.assertEqual(commitHistory("troyler", repo[0]), repo[1])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()