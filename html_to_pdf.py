import os.path
from utilities.utils import Utils
from testData import constants
from bs4 import BeautifulSoup
import os


class Test_html_to_pdf:

    def test_add_logo(self):
        html_file = os.path.abspath(constants.htmlreport_path)
        with open(html_file) as file:
            soup = BeautifulSoup(file, "html.parser")
            h1_element = soup.find("h1")
            image_url = os.path.abspath(constants.logo_path)
            image_element = soup.new_tag("img", src=image_url)
            image_element["style"] = "width:150px;height:90px;"
            image_element["align"] = "right"
            text = constants.report_title
            h1_element.clear()
            h1_element.append(text)
            h1_element.append(image_element)
            updated_html_content = soup.prettify()
            with open(html_file, "w") as file1:
                file1.write(updated_html_content)

    def test_html_to_pdf(self):
        Utils.convert_html_to_pdf(constants.htmlreport_path, constants.pdf_report_path)

    def Atest_encrypt(self):
        Utils.password_encrypt('xxxxx', 'yyyyy', 'zzzzzz', 'wwwww')

    def Atest_decrypt(self):
        password = Utils.password_decrypt(b'UGhhcm1hdGVrQDEyMw==')
        print("password = ", password)
