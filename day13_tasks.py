import requests

def fetch_btc_prices(api_url="https://api.coindesk.com/v1/bpi/currentprice.json"):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        prices = data["bpi"]
        return {currency: info["rate"] for currency, info in prices.items()}
    except requests.exceptions.RequestException as e:
        return {"Error": f"API request failed: {e}"}
    except KeyError:
        return {"Error": "Invalid response format"}

def write_price_report(prices, filename="btc_price_report.txt"):
    with open(filename, "w") as f:
        f.write("Bitcoin Price Report\n")
        f.write("--------------------------\n")
        for currency, price in prices.items():
            f.write(f"{currency}: {price}\n")

if __name__ == "__main__":
    prices = fetch_btc_prices()
    write_price_report(prices)
