import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck50(unittest.TestCase):
    def test_050_threshold_calibration(self):
        record = Record(id="appointment-050", exposure=53105, signal=0.368, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
