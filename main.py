from grabber import *
from getpass import getpass

def main():
    driver = driverSetup()
    link = getpass("Enter the link to the proquest book: ")
    grab(driver, link)

if __name__ == '__main__':
    main()
