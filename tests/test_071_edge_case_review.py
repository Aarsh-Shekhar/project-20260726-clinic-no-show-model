import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck71(unittest.TestCase):
    def test_071_edge_case_review(self):
        record = Record(id="appointment-071", exposure=3689, signal=0.681, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
