import time

import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.close_add()
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINKS_TEXT
        assert expected_links == actual_links, 'Validating Nav Links text'
        for index in range(12):
            homepage_nav.get_nav_links()[index].click()
