import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck11(unittest.TestCase):
    def test_011_edge_case_review(self):
        record = Record(id="appointment-011", exposure=6925, signal=0.430, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
