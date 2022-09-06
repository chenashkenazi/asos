from AsosCrawler import AsosCrawler

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

asos_url = "https://www.asos.com/adidas-originals/adidas-originals-forum-low-trainers-in-white-and-iridesent/prd/24108913"

if __name__ == '__main__':
    crl = AsosCrawler(asos_url, binary_location, driver_location)
    crl.check_size("40")
