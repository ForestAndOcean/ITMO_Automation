from pages.demo_site import DemoSite

def test_demo_site(browser):
    demo_site_page = DemoSite(browser)
    # 1.1. перейти на страницу 'https://demoqa.com/'
    demo_site_page.visit()
    # 1.2. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
    assert demo_site_page.exist_text_in_footer()

    # 2.1. перейти на страницу 'https://demoqa.com/'
    demo_site_page.visit()
    # 2.2. через кнопку перейти на страницу 'https://demoqa.com/elements'
    demo_site_page.click_elements_button()
    # 2.3. проверить что текст по центру == 'Please select an item from left to start practice.'
    assert demo_site_page.exist_text_in_mid()