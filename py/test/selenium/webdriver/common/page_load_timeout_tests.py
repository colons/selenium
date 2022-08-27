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

from typing import Iterator

import pytest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from test.selenium.webdriver.common.webserver import Pages


@pytest.fixture(autouse=True)
def reset_timeouts(driver: WebDriver) -> Iterator[None]:
    yield
    driver.set_page_load_timeout(300)


def test_should_timeout_on_page_load_taking_too_long(driver: WebDriver, pages: Pages) -> None:
    driver.set_page_load_timeout(0.01)
    with pytest.raises(TimeoutException):
        pages.load("simpleTest.html")


@pytest.mark.xfail_safari
def test_click_should_timeout(driver: WebDriver, pages: Pages) -> None:
    pages.load("simpleTest.html")
    driver.set_page_load_timeout(0.01)
    with pytest.raises(TimeoutException):
        driver.find_element(By.ID, "multilinelink").click()
