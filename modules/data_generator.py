from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pdfkit


def generate_html(driver, path_to_data):
    html = driver.execute_script("return document.body.innerHTML;")
    print(html)
    soup = bs(html, 'html.parser')

    Html_file = open(path_to_data + "/search.html", "w")
    Html_file.write(str(soup))
    Html_file.close()

    html_path = path_to_data + "/search.html"
    return html_path


def generate_pdf(html_path, path_to_data):
    pdfkit.from_file(html_path, path_to_data + '/website.pdf') 


def generate_data(driver, path_to_data):
    html_path = generate_html(driver, path_to_data)
    # generate_pdf(html_path, path_to_data)

# def scroll_to_page_floor(driver):
#     scrolls = 20
#     time.sleep(30)
#     while True:
#         scrolls -= 1
#         driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
#         time.sleep(1)
#         if scrolls < 0:
#             break