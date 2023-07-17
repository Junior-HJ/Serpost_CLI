import httpx

class SerpostRequests:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
    
    async def _make_request(self, url):
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'Anio': '2023',
            'Tracking': self.tracking_number,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                cookies=cookies,
                headers=headers,
                json=json_data,
            )
        
        return response

    async def get_tracking_information(self):
        return await self._make_request('https://webservice.serpost.com.pe/prj_online/Web_Busqueda.aspx/Consultar_Tracking')

    async def tracking_details(self):
        return await self._make_request('https://webservice.serpost.com.pe/prj_online/Web_Busqueda.aspx/Consultar_Tracking_Detalle_IPS')
