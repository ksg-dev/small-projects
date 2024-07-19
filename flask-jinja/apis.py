import requests

name = input("Enter Name: ")

params = {
    "name": name
}
# request for gender guess
response_gen = requests.get(url="https://api.genderize.io?", params=params)
response_gen.raise_for_status()
gender = response_gen.json()["gender"]

# request for age guess
response_age = requests.get(url="https://api.agify.io?", params=params)
response_age.raise_for_status()
age = response_age.json()["age"]