#!/usr/bin/env python
# coding: utf-8
import requests
from bs4 import BeautifulSoup

def get_user_info(username):
    """
    This function accept GitHub username and parses from it Name, Organization, Location, number of public repos
    and number of followers
    @ return: user_info, dict
    """
    url = 'https://github.com/' + username
    req = requests.get(url)
    soup = BeautifulSoup(req.content)
    user_info = {'Name':None, 'Organization':None, 'Location':None, 'n_repos':None, 'n_subscribers':None}
    try:
        user_info['Name'] = soup.find('span', itemprop = 'name').text.strip()
    except:
        pass
    try:
        user_info['Organization'] = soup.find("span", class_="p-org").text
    except:
        pass
    try:
        user_info['Location'] = soup.find('span',class_="p-label").text
    except:
        pass
    try:
        user_info['n_repos'] = int(soup.find('span', class_='Counter').text)
    except:
        pass
    try:
        user_info['n_subscribers'] = int(soup.find('span', class_ = "text-bold color-fg-default").text)
    except:
        pass
    return user_info


def get_user_repositories(username):
    """
    This function accepts GitHub username and parses his repos names and languages.
    @ return: repos, list of dict
    """
    url = 'https://github.com/' + username + '?tab=repositories'
    req = requests.get(url)
    soup = BeautifulSoup(req.content)
    repo_soup = soup.find('div', id="user-repositories-list").find_all("li")
    repos = []
    for i in range(len(repo_soup)):
        repo_dict = {'User':username, "repo_name": None, 'lang':None}
        try:
            repo_dict["repo_name"] = repo_soup[i].find('a', itemprop="name codeRepository").text.strip()
        except:
            pass
        try:
            repo_dict['lang'] = repo_soup[i].find('span', itemprop="programmingLanguage").text
        except:
            pass
        repos.append(repo_dict)
    return repos


def list_repository_contents(username, repository, repository_path=None:
    """
    This function accepts GitHub username, and repo name and returns it's content list.
    @ return: repos, list of dict
    """
    if repository_path:
        url = f'https://github.com/{username}/{repository}'
    else:
        url = f'https://github.com/{username}/{repository}/tree/branch/{repository_path}'
    req = requests.get(url)
    soup = BeautifulSoup(req.content)
    rep_cont = []
    rowheads = soup.find_all('div', role='rowheader')
    for rowhead in rowheads:
        rep_cont.append(rowhead.text.strip())
    return rep_cont



def download_file(username, repository, remote_file_path, local_file_path):
    """
    This function accepts GitHub username, and repo name, remote file path (down from the level of repo name)
    and local path file. All paths should start with '/',
    Downoloads file to the local path
    """
    # repository_path - spare variable
    url = 'https://raw.githubusercontent.com/'+username+'/'+repository+remote_file_path
    req = requests.get(url)
    name = remote_file_path.split('/')[-1]
    if not req.ok:
        print("Wrong path or it's a directory")
    else:
        with open(local_file_path+name, 'wb') as f:
                f.write(req.content)
