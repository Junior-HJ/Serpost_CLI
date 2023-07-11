import requests

class SerpostRequests:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number

    def get_tracking_information():
        import requests

    cookies = {
        'cookiesession1': '678A3EC253B65C6A44C0A8A323498AD0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'es-US,es;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'https://webservice.serpost.com.pe',
        'Referer': 'https://webservice.serpost.com.pe/prj_online/Web_Busqueda.aspx',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'Anio': '2023',
        'Tracking': 'UN041613995MU',
    }

    response = requests.post(
        'https://webservice.serpost.com.pe/prj_online/Web_Busqueda.aspx/Consultar_Tracking',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
