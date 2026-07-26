import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck68(unittest.TestCase):
    def test_068_field_validation(self):
        record = Record(id="appointment-068", exposure=50427, signal=0.394, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
