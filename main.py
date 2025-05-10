import argparse
from func import load_config_from_file, get_ip_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="IP address to check")
    parser.add_argument("-k", "--keyfile", default="key.txt", help="Path to API key file")
    args = parser.parse_args()

    config = load_config_from_file(args.keyfile)
    api_key = config.get("api_key")

    if args.ip:
        ip_to_check = args.ip
    else:
        ip_to_check = input("Enter an IP address: ")

    get_ip_data(ip_to_check, api_key)

if __name__ == "__main__":
    main()
