import urllib.request
import json
import subprocess

REPO="legleux/rippled"
headers = {}
branches={}
for branch in "master release develop".split():
    url=f"https://api.github.com/repos/{REPO}/commits/heads/{branch}"
    request = urllib.request.Request(url, headers=headers)
    raw_response = urllib.request.urlopen(request)
    response = json.loads(raw_response.read())
    branches.update({branch: response['sha']})

to_build = []
for branch, sha in branches.items():
    image = f"ghcr.io/legleux/rippled:{sha}"
    docker_command = f"docker image pull {image}"
    try:
        subprocess.check_call(docker_command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # print(f"already created {image}")
    except subprocess.CalledProcessError:
        # print(f"Need to push {sha} for {branch}")
        to_build.append({"branch":branch, "sha":sha})

print(json.dumps(to_build,separators=(',', ': ')))
