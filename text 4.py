import os
from dotenv import load_dotenv
load_dotenv()
wp_user = os.getenv('wp_user')
wp_password = os.getenv('wp_password')
print(wp_user)