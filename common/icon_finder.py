import requests

def get_crypto_icon(coin_name):
    try:
        coin_data = requests.get(f'https://pro-api.coinmarketcap.com/v1/cryptocurrency'
                            f'/info?CMC_PRO_API_KEY=6896edf5-71f1-4e50-8f7d-4ab174c4a547&symbol={coin_name}')
        logo = coin_data.json()['data'][coin_name]['logo']
        resized_logo = logo.replace("64x64", "200x200")
        return resized_logo
    except Exception as e:
        print(e)
        return None
