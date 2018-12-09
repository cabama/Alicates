import json
import subprocess

def loadProjectsInfo():
  with open('projects.json') as json_file:
    return json.load(json_file)


def cloneRepositories (repositories):
  for repository in repositories:
    print repository
    gitRepository = repositories[repository]['repository']
    # subprocess.Popen(["echo clone", 'clone', 'ssh://' + gitRepository], cwd="../")
    subprocess.Popen(["git", 'clone', gitRepository], cwd="./pp")

if __name__ == "__main__":
  projects = loadProjectsInfo()
  print projects
  cloneRepositories(projects['repositories'])  
