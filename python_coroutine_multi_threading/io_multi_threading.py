import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session, url = params
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com"] * 50

    executor = ThreadPoolExecutor(max_workers=2)
    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
