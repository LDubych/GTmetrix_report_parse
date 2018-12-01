from explicit_wait_type import ExplicitWaitType
import datetime


class GTmetrixAnalyze:

    def __init__(self, driver, site):
        self.driver = driver
        self.site = site

    def get_report(self):
        self.driver.implicitly_wait(.5)
        self.driver.get("https://gtmetrix.com")
        analyze_input = self.driver.find_element_by_name("url")
        analyze_input.send_keys(self.site)
        submit_button = self.driver.find_element_by_css_selector(".analyze-form-button button[type=\"submit\"]")
        submit_button.click()
        wait = ExplicitWaitType(self.driver)
        if wait.wait_for_url_contain("report", timeout=60, poll_frequency=1):
            report = {"report_url": self.driver.current_url,
                      "site": self.site,
                      "date_iso": datetime.datetime.now().isoformat(),
                      "date_gtmetrix": self.driver.find_element_by_css_selector(
                          ".report-details-timestamp .report-details-value").text,
                      "browser": self.driver.find_element_by_css_selector(
                          ".report-details-browser .report-details-value").text,
                      "test_server_region": self.driver.find_element_by_css_selector(
                          ".report-details-info .clear:nth-of-type(2) .report-details-value").text,
                      "performance_scores": {
                          "page_speed_score": float(self.driver.find_element_by_css_selector(
                              ".report-scores .report-score:nth-of-type(1) .report-score-percent").text[1:-2]),
                          "yslow_score": float(self.driver.find_element_by_css_selector(
                              ".report-scores .report-score:nth-of-type(2) .report-score-percent").text[1:-2])},
                      "page_details": {
                          "fully_loaded_time_in_seconds": float(self.driver.find_element_by_css_selector(
                              ".report-page-details .report-page-detail:nth-of-type(1) .report-page-detail-value").text[
                                                                :-1]),
                          "total_page_size": self.driver.find_element_by_css_selector(
                              ".report-page-detail-size .report-page-detail-value").text,
                          "requests": int(self.driver.find_element_by_css_selector(
                              ".report-page-detail-requests .report-page-detail-value").text)
                      }
                      }
        else:
            report = "Report has not been loaded"
        self.driver.close()
        self.driver.quit()
        return report

