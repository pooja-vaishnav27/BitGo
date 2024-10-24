from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class BlockExplorerAutomation:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()  

    def visit_page(self):
        self.driver.get(self.url)  

    def validate_transaction_header(self):
        try:
            header = self.driver.find_element(By.CSS_SELECTOR, '.transactions-header')  
            assert "25 of 2875 Transactions" in header.text
            print("Transaction header validated successfully.")
        except AssertionError:
            print("Transaction header validation failed.")
        except NoSuchElementException:
            print("Transaction header element not found.")

    def parse_transactions(self):
        transactions = self.driver.find_elements(By.CSS_SELECTOR, '.transaction-box')  
        for transaction in transactions:
            inputs = len(transaction.find_elements(By.CSS_SELECTOR, '.vin'))  
            outputs = len(transaction.find_elements(By.CSS_SELECTOR, '.vout'))  
            if inputs == 1 and outputs == 2:
                transaction_hash = transaction.find_element(By.CSS_SELECTOR, '.txn a').text  
                print(f'Transaction Hash: {transaction_hash}')

    def close_browser(self):
        self.driver.quit()

    def run(self):
        self.visit_page()
        self.validate_transaction_header()
        self.parse_transactions()
        self.close_browser()

if __name__ == "__main__":
    url = "https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf6420347336450917732"
    automation = BlockExplorerAutomation(url)
    automation.run()
