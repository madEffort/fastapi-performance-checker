import time
import requests
from functools import wraps


def time_logger(category):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time

            # 메타 데이터로 함수의 이름을 사용
            meta = func.__name__
            # 데이터를 FastAPI 엔드포인트로 전송
            url = "http://localhost:8000/collect/"
            data = {
                "category": category,
                "meta": meta,
                "value": elapsed_time,
                "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
            try:
                requests.post(url, json=data)
            except requests.RequestException as e:
                print(f"Failed to send data: {str(e)}")

            return result

        return wrapper

    return decorator
