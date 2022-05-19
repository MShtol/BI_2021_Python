## Alternative GitHub API
Flie `github_api.py` contains alternative GitHub API with four functions.

### Functions
1. `get_user_info(username)` - returns a dictionary wuth name, organization, location, number of subscribers and number of repositories of iser (username)
2. `get_user_repositories(username)` - returns a list of dicts with the user's repo info (repo name, progLanguage)
3. `list_repository_contents(username, repository, repository_path)` - returns list wih content of repo (not recursive). repository_path - optional
4. `download_file(username, repository, remote_file_path, local_file_path)` - downloads file from a repo. Paths should start with "/"


### Requierements
You can find them in requierements.txt and install with `pip install -r requirements.txt` in your terminal

