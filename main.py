from AsosCrawler import AsosCrawler

# Windows
# driver_location = "/usr/bin/chromedriver"
# binary_location = "/usr/bin/google-chrome"

# mac
driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

asos_url = "https://www.asos.com/asos-edition/asos-edition-satin-midi-dress-with-tie-back-in-sage-green/prd/201489618?colourWayId=201489619&cid=8799"

if __name__ == '__main__':
    try:
        crl = AsosCrawler(asos_url, binary_location, driver_location)
        crl.check_size("L")
    except Exception as ex:
        print(f"Error!: {str(ex)}")
