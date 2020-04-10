import time

from prometheus_client import start_http_server

from metrics import Metrics

if __name__ == "__main__":
    start_http_server(80)

    while True:
        # record metric every second
        time.sleep(1)
        Metrics.record("sample", {"created_at": time.time(), "error": None})