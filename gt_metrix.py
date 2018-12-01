from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import datetime
import json
from GTmetrixAnalyze import GTmetrixAnalyze


def gt_metrix_analyze(site):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = GTmetrixAnalyze(webdriver.Chrome(chrome_options=chrome_options), site)
    return driver.get_report()


def save_text_in_file(text, file_name):
    with open("{0}".format(file_name), "w") as file:
        file.write(text)


def save_json_in_file(dict, file_name):
    save_text_in_file(json.dumps(dict), file_name)


site = "https://learn.letskodeit.com"
report = gt_metrix_analyze(site)
print(report)
report_html = requests.get(report["report_url"]).text
save_text_in_file(report_html, "{0}_{1}.html".format(site.replace("https://", ""), datetime.datetime.now().isoformat()))
save_json_in_file(report, "{0}_{1}.json".format(site.replace("https://", ""), datetime.datetime.now().isoformat()))
