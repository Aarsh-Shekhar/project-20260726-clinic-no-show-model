import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck41(unittest.TestCase):
    def test_041_edge_case_review(self):
        record = Record(id="appointment-041", exposure=88671, signal=0.474, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
