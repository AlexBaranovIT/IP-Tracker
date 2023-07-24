import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[Internet provider]': response.get('isp'),
            '[Organisation]': response.get('ord'),
            '[Country]': response.get('country'),
            '[Region]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP Code]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")} {response.get("city")}.html')
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP Tracker'))
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
