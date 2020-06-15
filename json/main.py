import json

if __name__ == "__main__":
    test_data = {
        'task_id': '123456789',
        'occur_time': '20190830193260000',
        'device_code': '232322323232544535231#2034958222222222203849023',
        'image': str(encoding="utf-8")}
    print(json.dumps(test_data))
