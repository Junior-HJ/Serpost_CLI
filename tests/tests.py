import asyncio

from app.parsers.serpost_parser import SerpostParser

serpostController = SerpostParser('######')

async def main():
    await serpostController.parse_tracking_information()

asyncio.run(main())
