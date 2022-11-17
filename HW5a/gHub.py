import requests
import json

GIT_ID = "troyler"

def get_user_repos(GIT_ID):
    repositories = []
    repos = requests.get("https://api.github.com/users/{}/repos".format(GIT_ID))
    for repo in repos.json():
        print(repo)
        repositories.append(repo["name"])
    return repositories


def commit_history(gitID, repo):
    com = requests.get("https://api.github.com/repos/{}/{}/commits".format(gitID,repo))
    commits = (len(com.json()))
    return commits


def return_info(GIT_ID):
    repositories = get_user_repos(GIT_ID)
    git_id_info = []

    for repo in repositories:
        repoDict = {}
        repoDict["name"] = repo
        repoDict["commits"] = commit_history(GIT_ID,repo)
        git_id_info.append(repoDict)
        print("Repo: ", repoDict["name"], " Number of Commits:", repoDict["commits"])
    return git_id_info


return_info(GIT_ID)
