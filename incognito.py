from incognito_src import *
ab = anonBrowser(proxies=[], user_agents=[('User-Agents','superSecretBrowser')])
url = input("What website do you want to fetch? ")
filename = input("Give the file a name: ")
for attempt in range(1,5):
    ab.anonymize()
    print('Fetching [*] Page')
    page =  ab.open(url)
    source_code = page.read()
    with open(f"/logs/{filename}.txt", "wb") as f:
        f.write(source_code)
    response = ab.open(url)
    for cookie in ab.cookie_jar:
        print(cookie)

