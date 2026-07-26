import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck56(unittest.TestCase):
    def test_056_risk_explanation(self):
        record = Record(id="appointment-056", exposure=74452, signal=0.849, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
