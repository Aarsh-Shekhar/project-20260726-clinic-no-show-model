import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="appointment-002", exposure=54542, signal=0.794, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
