import requests


def main():
    r = requests.get('https://api.github.com/events')
    print("""status:{status}""".format(status=r.status_code))


main()
