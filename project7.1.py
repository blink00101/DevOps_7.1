import requests

def get_public_ip(api_key, ip_type='ipv4'):
    endpoint = f'http://api.ipstack.com/check?access_key={api_key}&output=json&security=1'
    
    try:
        response = requests.get(endpoint)
        response.raise_for_status()

        return response.json().get(ip_type)

    except requests.RequestException as e:
        print(f"Error retrieving public {ip_type} address: {e}")
        return None
def main():
    api_key = '5c1eb839f8ca698ef12c5ee39293fd5c'

    public_ipv4 = get_public_ip(api_key, ip_type='ipv4')
    if public_ipv4:
        print(f"Public IPv4 Address: {public_ipv4}")

    public_ipv6 = get_public_ip(api_key, ip_type='ipv6')
    if public_ipv6:
        print(f"Public IPv6 Address: {public_ipv6}")

if __name__ == "__main__":
    main()
