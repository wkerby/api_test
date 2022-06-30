#work with a simple api
#import requests package
import requests

#make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

#create a variable to which the api call will be attributed
r = requests.get(url)

#print the status code attribute of the object "r"
#a status code of 200 means that the response was successful
print("Status: " + str(r.status_code))

#because API returns info in JSON format, use the json() method to convert info into python dict
response_dict = r.json()

#print keys of resulting dict
# print(response_dict.keys())

#now print number of total python "repositories" in GitHub
print("Total repositories: ", response_dict['total_count'])

#the 'items' key of response dict returns list of dictionaries, all of which store info 
#on a specific python repository
#print keys of first repository dict in list
repository_dictionaries = response_dict['items']

#print total num python repositories returned
print("Repositories returned:", len(repository_dictionaries))

#print all keys of the dict of first key in 
repository_dict = repository_dictionaries[0]
# for key in list(repository_dict.keys()):
# 	print(key)

#return several columns of information on each repository in 
# 	print(":", repo_dict['name'])

for repo_dict in repository_dictionaries:
	print("Name:", repo_dict['name'])
	print("Owner:", repo_dict['owner']['login']) #in this case, the value of the "Owner" key is a nested dict, 
	#and we are returning the value attributed to the 'login' key of this nested dict
	print("Stars:", repo_dict['stargazers_count'])
	print("Repository:", repo_dict['html_url'])
	print("Created:", repo_dict['created_at'])
	print("Updated:", repo_dict['updated_at'])
	print("Description:", repo_dict['description'])











