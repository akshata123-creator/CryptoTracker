import os

os.system('pytest --alluredir ..\\Reports\\XML')
os.system('allure generate ..\\Reports\\XML -o ..\\Reports\\HTML -c')
