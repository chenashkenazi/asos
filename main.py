from AsosCrawler import AsosCrawler

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

asos_url = "https://www.asos.com/weekday/weekday-one-shoulder-tank-in-bright-pink/prd/202828371"

if __name__ == '__main__':
    crl = AsosCrawler(asos_url, binary_location, driver_location)
    crl.check_size("L")
