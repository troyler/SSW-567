import requests
import json

gitID = "troyler"

def getUserRepos(gitID):
    repositories = []
    repos = requests.get("https://api.github.com/users/{}/repos".format(gitID))
    for repo in repos.json():
        print(repo)
        repositories.append(repo["name"])
    return repositories


def commitHistory(gitID, repo):
    com = requests.get("https://api.github.com/repos/{}/{}/commits".format(gitID,repo))
    commits = (len(com.json()))
    return commits


def returnInfo(gitID):
    repositories = getUserRepos(gitID)
    gitIdInfo = []

    for repo in repositories:
        repoDict = {}
        repoDict["name"] = repo
        repoDict["commits"] = commitHistory(gitID,repo)
        gitIdInfo.append(repoDict)
        print("Repo: ", repoDict["name"], " Number of Commits:", repoDict["commits"])
    return gitIdInfo


returnInfo(gitID)
