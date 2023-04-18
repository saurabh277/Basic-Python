import requests

response = requests.get( "https://api.github.com/users/Saurabh277/repos")
"""
print(response.text)
print(type(response.text)) #string
print(response.json())
print(type(response.json())) #list
print(response.json()[0])
"""

my_projects = response.json()
#now i want to print out window for each project - project name , url
result = {}
for project in my_projects:
    project_name  = project['name']
    project_url = project['html_url']
    result[project_name] = project_url
    print(f"Project name : {project_name}\n Project url : {project_url}\n")

#print(result)