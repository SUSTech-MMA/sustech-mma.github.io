import requests

url = "https://chart.googleapis.com/chart?cht=tx&chl=%s"
formula = input("Enter: ")
# print(url%formula)
# https://chart.googleapis.com/chart?cht=tx&chl=$$\sum_{i=1}^n$$
response = requests.get(url%formula)
ignore   = [i for i in "\\/:*?<>|\'\""]
for ig in ignore:
	formula = formula.replace(ig, "")
with open("%s.jpg"%formula, mode="wb") as f:
	f.write(response.content)
