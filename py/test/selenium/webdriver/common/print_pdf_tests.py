# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.remote.webdriver import WebDriver
from test.selenium.webdriver.common.webserver import Pages

START_INDEX = 0
END_INDEX = 5
PDF_MAGIC_NUMBER = 'JVBER'


def test_pdf_with_2_pages(driver: WebDriver, pages: Pages) -> None:
    print_options = PrintOptions()
    print_options.page_ranges = ['1-2']

    pages.load("printPage.html")

    base64code = driver.print_page(print_options)

    assert base64code[START_INDEX: END_INDEX] == PDF_MAGIC_NUMBER


def test_pdf_with_all_pages(driver: WebDriver, pages: Pages) -> None:
    pages.load("printPage.html")
    base64code = driver.print_page()

    assert base64code[START_INDEX: END_INDEX] == PDF_MAGIC_NUMBER


def test_valid_params(driver: WebDriver, pages: Pages) -> None:
    print_options = PrintOptions()

    print_options.page_ranges = ['1-2']
    print_options.orientation = 'landscape'
    print_options.page_width = 30

    pages.load("printPage.html")
    base64code = driver.print_page(print_options)

    assert base64code[START_INDEX: END_INDEX] == PDF_MAGIC_NUMBER
