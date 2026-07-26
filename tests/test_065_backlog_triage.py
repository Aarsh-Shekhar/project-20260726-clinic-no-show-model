import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck65(unittest.TestCase):
    def test_065_backlog_triage(self):
        record = Record(id="appointment-065", exposure=40032, signal=0.554, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
