with open("urls.txt", "+a") as file:
    contents = file.read().split()

print(contents)
sites = list()
for site in contents:
    site = site.replace("s", "")
    site = site.replace("/", "//")
    sites.append(site)

print(sites)
