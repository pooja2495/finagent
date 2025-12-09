"""
Simple Playwright demo runner that opens the dummy bank pay page,
fills fields, and pauses for manual confirmation (simulates Conscious Pause).
Run after backend is up.
"""
from playwright.sync_api import sync_playwright
import time

def pause_prompt(action, details):
    print("PAUSE EVENT ->", action, details)
    decision = input("Type 'approve' to continue, anything else to abort: ").strip().lower()
    return decision == 'approve'

def pay_bill_flow(base_url, biller, amount):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"{base_url}/dummy_bank/pay.html")
        page.select_option('#biller', label=biller)
        page.fill('#amount', str(amount))
        # conscious pause
        ok = pause_prompt('pay', {'biller':biller, 'amount':amount})
        if not ok:
            print("Action aborted by user.")
            browser.close()
            return
        page.click('#payBtn')
        # wait a little for UI changes
        time.sleep(2)
        print("Done. Close browser when ready.")
        browser.close()

if __name__ == '__main__':
    pay_bill_flow('http://localhost:8000', 'Adani Power', 750)
