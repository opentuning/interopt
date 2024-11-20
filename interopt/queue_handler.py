import asyncio
import logging

class QueueHandler:
    def __init__(self, grpc_urls: list[str]):
        self.grpc_urls = grpc_urls
        self.queue = asyncio.Queue()
        self.server_availability = {url: True for url in self.grpc_urls}
        logging.info(f"Available servers: {self.server_availability}")
        self.available_server_event = asyncio.Event()
        self.available_server_event.set()
        self.lock = asyncio.Lock()

    async def get_available_server_url(self):
        logging.info("Waiting for available server")
        while True:
            async with self.lock:
                for url, is_available in self.server_availability.items():
                    if is_available:
                        self.server_availability[url] = False  # Mark the server as busy
                        if not any(self.server_availability.values()): # Check if all servers are now busy
                            self.available_server_event.clear()  # Clear the event to wait again
                        logging.info(f"Using server {url}")
                        return url # If no available servers found, wait for one to become available
            await self.available_server_event.wait()

    async def mark_server_as_available(self, url):
        async with self.lock:
            self.server_availability[url] = True
            self.available_server_event.set()  # Signal that at least one server is available
