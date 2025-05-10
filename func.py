import requests
import random
import ipaddress
import json
from color import Color  # Assumes color.py exists

# Load config from a Python-formatted key.txt file
def load_config_from_file(filepath):
    context = {}
    with open(filepath, "r") as f:
        code = f.read()
        exec(code, context)
    return context

# Generate a random realistic User-Agent string
def generate_random_user_agent():
    platforms = [
        "Windows NT 10.0; Win64; x64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "X11; Linux x86_64",
        "iPhone; CPU iPhone OS 14_0 like Mac OS X",
        "Android 11; Mobile"
    ]
    browsers = [
        lambda: f"Mozilla/5.0 ({random.choice(platforms)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80, 115)}.0.{random.randint(1000, 5000)}.{random.randint(0, 200)} Safari/537.36",
        lambda: f"Mozilla/5.0 ({random.choice(platforms)}) Gecko/20100101 Firefox/{random.randint(70, 115)}.0",
        lambda: f"Mozilla/5.0 ({random.choice(platforms)}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{random.randint(13, 16)}.0 Safari/605.1.15",
        lambda: f"Mozilla/5.0 ({random.choice(platforms)}) AppleWebKit/537.36 (KHTML, like Gecko) Edg/{random.randint(80, 115)}.0.{random.randint(1000, 5000)}.{random.randint(0, 200)}"
    ]
    return random.choice(browsers)()

# Validate IP address (IPv4 or IPv6)
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Query ipdata.co API for IP info
def get_ip_data(ip, api_key):
    if not is_valid_ip(ip):
        print(f"{Color.RED}[!] Invalid IP address format{Color.RESET}")
        return

    headers = {
        'accept': '*/*',
        'user-agent': generate_random_user_agent(),
        'referer': 'https://ipdata.co/',
    }
    params = {
        'api-key': api_key,
    }

    try:
        response = requests.get(f'https://api.ipdata.co/{ip}', params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        print(f"\n{Color.BRIGHT_CYAN}[>] IP Information:{Color.RESET}")
        print(f"{Color.BRIGHT_GREEN}[>] IP:{Color.RESET} {data.get('ip')}")
        print(f"{Color.BRIGHT_GREEN}[>] Country:{Color.RESET} {data.get('country_name')} ({data.get('country_code')})")
        print(f"{Color.BRIGHT_GREEN}[>] Region:{Color.RESET} {data.get('region')}")
        print(f"{Color.BRIGHT_GREEN}[>] City:{Color.RESET} {data.get('city')}")
        print(f"{Color.BRIGHT_GREEN}[>] Continent:{Color.RESET} {data.get('continent_name')}")
        print(f"{Color.BRIGHT_GREEN}[>] Latitude:{Color.RESET} {data.get('latitude')}")
        print(f"{Color.BRIGHT_GREEN}[>] Longitude:{Color.RESET} {data.get('longitude')}")
        print(f"{Color.BRIGHT_GREEN}[>] Timezone:{Color.RESET} {data.get('time_zone', {}).get('name')} ({data.get('time_zone', {}).get('abbr')})")
        print(f"{Color.BRIGHT_GREEN}[>] Currency:{Color.RESET} {data.get('currency', {}).get('name')} ({data.get('currency', {}).get('code')})")
        print(f"{Color.BRIGHT_GREEN}[>] ASN:{Color.RESET} {data.get('asn', {}).get('asn')} - {data.get('asn', {}).get('name')}")

        print(f"\n{Color.BRIGHT_CYAN}[>] Threat Info:{Color.RESET}")
        threat = data.get('threat', {})
        print(f"{Color.YELLOW}[>] Proxy:{Color.RESET} {threat.get('is_proxy')}")
        print(f"{Color.YELLOW}[>] VPN:{Color.RESET} {threat.get('is_vpn')}")
        print(f"{Color.YELLOW}[>] TOR:{Color.RESET} {threat.get('is_tor')}")
        print(f"{Color.YELLOW}[>] Threat Score:{Color.RESET} {threat.get('scores', {}).get('threat_score')}")

    except requests.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                error_message = error_data.get("message", "No error message available")
            except json.JSONDecodeError:
                error_message = e.response.text
        else:
            error_message = str(e)
        
        print(f"{Color.RED}[!] Request failed: {error_message}{Color.RESET}")

    except json.JSONDecodeError:
        print(f"{Color.RED}[!] Failed to decode JSON response.{Color.RESET}")
