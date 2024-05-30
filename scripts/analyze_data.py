import requests
import matplotlib.pyplot as plt
import numpy as np

def fetch_data(category, meta):
    url = f"http://0.0.0.0:8000/search/?category={category}&meta={meta}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['val']  # API 응답에서 'val' 키의 데이터를 추출
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

def analyze_and_plot(data1, data2, meta1, meta2):
    
    # 값을 추출하고 시간 데이터를 생성 (예시: 연속된 시간)
    values1 = [float(item) for item in data1]
    values2 = [float(item) for item in data2]

    plt.figure(figsize=(10, 5))
    plt.plot(values1, marker='o', linestyle='-', label=f'{meta1} Performance')
    plt.plot(values2, marker='x', linestyle='-', label=f'{meta2} Performance')

    plt.title('Performance Comparison Over Time')
    plt.xlabel('Time')
    plt.ylabel('Performance Value')
    plt.legend()
    plt.grid(True)

    mean_value1 = np.mean(values1)
    mean_value2 = np.mean(values2)
    plt.axhline(y=mean_value1, color='r', linestyle='--', label=f'{meta1} Mean')
    plt.axhline(y=mean_value2, color='b', linestyle='--', label=f'{meta2} Mean')

    plt.legend()
    plt.show()

if __name__ == "__main__":
    category = 'deploy'
    meta1 = 'docker'
    meta2 = 'nondocker'
    data1 = fetch_data(category, meta1)
    data2 = fetch_data(category, meta2)
    if data1 and data2:
        analyze_and_plot(data1, data2, meta1, meta2)
    else:
        print("No data available for the specified category and meta.")