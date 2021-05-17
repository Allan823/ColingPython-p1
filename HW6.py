import requests
from github import Github
from pprint import pprint


class GitHubUser:

    def int(self):
        pass

    def init(self, username):
        self.username = username
        self.token = "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"
        self.i = requests.get(f"https://api.github.com/users/{self.username}",
                              headers={"Authorization": f'token {self.token}'})

    def print(self):
        r = self.i.json()
        print("Username: http://github.com/{username}"
              "\nName: {name},"
              "\nNumber of followers:"
              " {followers}".format(username=r["html_url"], name=r["name"], followers=r["followers"]))

    def repos(self):
        g = Github()
        user = g.get_user(self.username)
        for repo in user.get_repos():
            print("Repository: {repo},"
                  "\n Description:"
                  " {desc}".format(repo=repo.name,
                                   desc=repo.description))

    def language(self):
        array = []
        g = Github()
        user = g.get_user(self.username)
        for repo in user.get_repos():
            self.i = requests.get(f"https://api.github.com/repos/{repo.full_name}/languages",
                                  headers={"Authorization": f'token {self.token}'})
            r = self.i.json()
            for i in r:
                if i not in array:
                    array.append(i)
        print("LANGUAGES USED:")
        for x in array:
            print(x)

    def top_user(self):
        url = "https://api.github.com/search/users?q=a&sort=followers&order=desc"
        q = requests.get(url, headers={"Authorization": f'token {self.token}'}).json()
        user = q["items"][0]

        print("URL is:" + str(user["html_url"]))
        print("Name:" + str(user['login']))
        g = Github();
        user_ac = g.get_user(user['login'])
        print("Number of followers:"+str(user_ac.followers))

    def top_lang(self):
        url = "http://api.github.com/search/languages?q=stars:%3E1&sort=stars"
        q = requests.get(url, headers={"Authorization": f'token {self.token}'}).json()
        pprint(q)

user = input("Введите юзернейм пользователя: ")
User = GitHubUser(user)
if (User.i.ok):
    User.print()
    User.repos()
    User.language()
    print("\n\nTop user with followers:")
    User.top_user()
    User.top_lang()
else:
    print(User.i.text)
