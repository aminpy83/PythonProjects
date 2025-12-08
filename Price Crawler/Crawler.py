import requests, re, random, time, csv, os, persiantools.jdatetime as day

url = 'https://www.tgju.org/'
reg_statement = r'em>.*> ([^a-z]*)<.*\n.*\n.*price\">([^a-z]*)<'
regex = re.compile(reg_statement)

today = day.JalaliDate.today().isoformat()
delay = random.uniform(1, 4)

prices = {}
file_existence = os.path.exists('prices.csv')

try:
    time.sleep(delay)
    req = requests.get(url, timeout=5)
    res = regex.findall(req.text)
    # print(res)
    prices['date'] = today
    for i, j in res:
        # print(i,j)
        prices[i] = j
    # print(prices)

    with open('prices.csv', 'a+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        reader = csv.DictReader(file)

        if not file_existence:
            writer.writerow(prices.keys())
        file.seek(0)
        for row in reader:
            if prices['date'] == row['date']:
                print("Today's prices already exist.")
                exit()
        writer.writerow(prices.values())
    prices = {}

except Exception as e:
    print('sth wrong!!!!!', e)
