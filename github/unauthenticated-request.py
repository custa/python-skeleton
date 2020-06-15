import requests

url = 'https://api.github.com/users/octocat'

try:
    r = requests.get(url)
    if 200 != r.status_code:
        print("{}".format(r.content))
except Exception as e:
    print("{}".format(e))
