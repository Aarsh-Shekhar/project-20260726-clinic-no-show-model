import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck53(unittest.TestCase):
    def test_053_data_quality_guardrail(self):
        record = Record(id="appointment-053", exposure=24719, signal=0.227, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
