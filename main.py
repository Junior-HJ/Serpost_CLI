from app.parsers.argument_parser import ArgumentParser
from app.controllers.serpost_controller import SerpostController
import asyncio

if __name__ == '__main__':
    async def main():
        argumentParser = ArgumentParser()
        args = argumentParser.parse_args()
        
        serpostController = SerpostController(args.t)
        await serpostController.get_tracking_information()

asyncio.run(main())
