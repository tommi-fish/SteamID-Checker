import requests


def run_id_checker(api_key, txt_file):
    count = 0
    unclaimed_count = 0
    with open(txt_file) as f:
        for line in f:
            line = line.strip()
            response = requests.get(f"http://api.steampowered.com/ISteamUser"
                                    f"/ResolveVanityURL/v0001/?key={api_key}"
                                    f"&vanityurl={line}")
            json_response = response.json()
            try:
                if json_response['response']['steamid']:
                    count += 1
                    pass
            except KeyError:
                count += 1
                unclaimed_count += 1
                print(f"[LINE {count}]: {line} was unclaimed, adding to "
                      f"unclaimed.txt... ")
                with open("unclaimed.txt", "a") as f:
                    f.write("\n")
                    f.write(line)
        print(f"Finished with {unclaimed_count} unclaimed IDs found.")

run_id_checker("XXXXXXXXXXXXX","ids.txt")