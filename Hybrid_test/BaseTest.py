from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:

    @staticmethod
    def generate_email_with_time_stamp():
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "test" + time_stamp + "@test.co"

