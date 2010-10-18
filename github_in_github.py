#!/usr/bin/env python

from github2.client import Github
import secrets
import settings
import jinja2
from jinja2 import Environment, FileSystemLoader
import os


github = Github(username = secrets.username, api_token = secrets.api_token)

def get_all_repos():
    "Will get all repo for logged in user"
    repos = github.repos.list(settings.for_username)
    key_f =  lambda rep: getattr(rep, "watchers")
    repos.sort(key = key_f, reverse = True)
    return repos
    
def get_index_page():
    "Creates the index from all repos"
    repos = get_all_repos()
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.txt")
    repo_count = len(repos)
    watcher_count = sum([el.watchers for el in repos])
    fork_count = sum([el.forks for el in repos])
    vars = {"username": settings.for_username,
     "watcher_count": watcher_count,
     "fork_count": fork_count,
     "repo_count": repo_count,
     "repos": repos}
    return template.render(vars)
    
def get_repo_page(repo):
    "Creates the index from all repos"
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("repo.txt")
    vars = {"repo": repo}
    return template.render(vars)

    
def reset_build_directory():
    "Resets the directory where the sphinxdocs will be built."
    
    try:
        os.system("rm -rf %s" % settings.build_dir)
    except:
        pass
    os.system("cp -r %s %s"%(settings.build_dir_template, settings.build_dir))
    
def write_index_page():
    "write the index page in the build directory"
    index_page = get_index_page()
    index_page_name = os.path.join(settings.build_dir, "index.rst")
    index_file = open(index_page_name, "w")
    index_file.write(index_page)
    index_file.close()
    
def write_repo_pages():
    repos = get_all_repos()
    for repo in repos:
        repo_page = get_repo_page(repo)
        repo_page_name = os.path.join(settings.build_dir, "%s.rst" % repo.name)
        repo_file =  open(repo_page_name, "w")
        repo_file.write(repo_page)
        repo_file.close()
        
def build_html():
    "Creates the html"
    os.chdir(settings.build_dir)
    os.system("make html")
    
def put_on_github():
    "Puts the generated html on github"
    os.system("git clone %s %s" % (settings.clone_url, settings.clone_dir))
    os.system("cp -R _build/html/* %s" % settings.clone_dir)
    os.chdir(settings.clone_dir)
    os.system("git add .")
    os.system('git commit -m "Here be Dragons"')
    os.system('git push origin master')

    
    
if __name__ == "__main__":
    #create_index()
    reset_build_directory()
    write_index_page()
    write_repo_pages()
    build_html()
    put_on_github()