#search engine project
#scrapes the internet for websites with
#keywords and stores the website to a file
#began 2022-06-07
#UselessTechSupport, Zakila_Txikia, ShotGhost
from googlesearch import search


#get keyword to search from google QUERY
kw = input("Enter Keyword to search for. ") 

results = input("How many results would you like? ")
num_results = int(results)
query = kw

with open('output.txt', 'w') as f:
	for s in search(query, num_results):
		print(s)
		f.write("%s\n" % str(s))
