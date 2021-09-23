import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login, TV
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

     #To run action as specific user uncomment code bellow.
     #NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
     #just before test_2_selenium_z_log_out action

    @print_timing("selenium_app_specific_user_login")
    def measure():
        def app_specific_user_login(username='chiranjeevdas27', password='27TH*april'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username='chiranjeevdas27', password='27TH*april')
    measure()

    #@print_timing("selenium_app_custom_action")
    #def measure():
        #@print_timing("selenium_app_custom_action:view_issue")
        #def sub_measure():
        #    page.go_to_url(f"http://jira-loadb-g63c4pti2rg8-150787780.us-west-2.elb.amazonaws.com/browse/KAN-41?jql=summary%20~%20%27AppIssue*%27")
        #    page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/{issue_key}")
        #    page.go_to_url(f"http://jira-loadb-g63c4pti2rg8-150787780.us-west-2.elb.amazonaws.com/browse/KAN-41")
        #    page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
        #    page.get_element((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT")).  # Wait for you app-specific UI element by ID selector
        #    page.wait_until_visible((By.XPATH, "//button[text()='Create session']"))
        #    page.clickable((By.CLASS_NAME, "aui-button-primary"))
        #    page.wait_until_visible((By.ID, "issue-comment-add-submit"))
        #    page.clickable((By.ID, "issue-comment-add-submit"))
        #    page.wait_until_visible(TV.session_creation())
        #    page.session_creation()
    #measure()

    @print_timing("TeamViewer_specific_function")
    def measure():
        teamviewer_session = TV(webdriver)
        teamviewer_session.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/{issue_key}")
        teamviewer_session.session_creation()
    measure()
