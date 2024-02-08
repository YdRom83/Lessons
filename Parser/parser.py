from bs4 import BeautifulSoup
import requests


def weather_check(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&gs_lp=Egxnd3Mtd2l6LXNlcnAiE9C_0L7Qs9C-0LTQsCDQu9C-0L0qAggAMhUQABiABBgUGIcCGLEDGIMBGEYYgAIyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIKEAAYgAQYFBiHAjIhEAAYgAQYFBiHAhixAxiDARhGGIACGJcFGIwFGN0E2AEBSNw0UPYCWK8fcAF4AZABAJgB3Q2gAdgPqgEFMy44LTG4AQPIAQD4AQHCAgoQABhHGNYEGLADwgINEAAYgAQYigUYQxiwA8ICCxAAGIAEGLEDGIMBwgIIEAAYgAQYsQPCAhAQABiABBgUGIcCGLEDGIMB4gMEGAAgQYgGAZAGCroGBggBEAEYEw&sclient=gws-wiz-serp',
        headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    time = soup.select('#wob_dts')[0].getText().strip()
    precipitation = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    print(f'День недели и время: {time}')
    print(f'Информация об осадках: {precipitation}')
    print(f'Температура воздуха: {weather} C')


city_input = input('Enter city: ')

weather_check(f'{city_input} погода')
