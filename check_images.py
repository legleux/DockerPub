import urllib.request
import json
import subprocess
# import logging
import argparse
from loggy import logger
# rootLogger = logging.getLogger()
# logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
# rootLogger.setLevel(logging.DEBUG)
# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(logFormatter)
# rootLogger.addHandler(consoleHandler)

git_command = "git rev-parse --abbrev-ref HEAD"
OWNER="XRPLF"
REPO="rippled"
NAME=f"{OWNER}/{REPO}"
headers = {}
branches={}

def get_branch():
    owner, branch = subprocess.check_output(git_command.split()).decode().split('/')
    print(owner)
    print(branch)
    logger.debug(f'got {branch}')
    repo = f"{owner}/{branch}"

def check_if_image_published(owner, repo, branch='develop', sha=None):
    repo = f"{owner}/{repo}"
    url=f"https://api.github.com/repos/{repo}/commits/heads/{branch}"
    request = urllib.request.Request(url, headers=headers)
    raw_response = urllib.request.urlopen(request)
    response = json.loads(raw_response.read())
    data = {branch: response['sha']}
    image = f"ghcr.io/{repo}:{branch}"
    docker_command = f"docker image pull {image}"
    try:
        subprocess.check_call(docker_command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logger.debug(f"already created {image}")
    except subprocess.CalledProcessError:
        logger.debug(f"Need to push {sha} for {branch}")
        to_build.append({"branch":branch, "sha":sha})

# for branch in "master release develop".split():
#     url=f"https://api.github.com/repos/{NAME}/commits/heads/{branch}"
#     request = urllib.request.Request(url, headers=headers)
#     raw_response = urllib.request.urlopen(request)
#     response = json.loads(raw_response.read())
#     branches.update({branch: response['sha']})

# to_build = []
# for branch, sha in branches.items():
#     image = f"ghcr.io/{NAME}:{sha}"
#     docker_command = f"docker image pull {image}"
#     try:
#         subprocess.check_call(docker_command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#         # print(f"already created {image}")
#     except subprocess.CalledProcessError:
#         # print(f"Need to push {sha} for {branch}")
#         to_build.append({"branch":branch, "sha":sha})


# print(json.dumps(to_build,separators=(',', ': ')))
def parse_args():
    parser = argparse.ArgumentParser(description='Check if images are published at a repo')
    parser.add_argument('-r','--repo', help='Git Hub repo to check', required=True)
    parser.add_argument('-b','--branch', help='Branch or git ref', required=False)
    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':
    args = parse_args()
    owner, repo  = args.get("repo").split('/')

    check_if_image_published(owner, repo)
