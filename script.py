import requests
import numpy as np

def main():
    response = requests.get('https://api.github.com')
    print(f'Status code: {response.status_code}')
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f'Numpy array: {arr}')

if __name__ == "__main__":
    main()
