import requests

url = "https://chart.googleapis.com/chart?cht=%s"
formula = input("Enter: ")
print(url%formula)
response = requests.get(url%formula)