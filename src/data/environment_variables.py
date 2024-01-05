import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
print(API_KEY)

password = os.getenv("pass")
print(password)

# create a function which accept 2 numbers and display the result
