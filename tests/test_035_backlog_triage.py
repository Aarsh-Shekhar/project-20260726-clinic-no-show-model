import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck35(unittest.TestCase):
    def test_035_backlog_triage(self):
        record = Record(id="appointment-035", exposure=9982, signal=0.748, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
