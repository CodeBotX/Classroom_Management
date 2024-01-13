from django.test import TestCase
from models import *

class ScoreModelTest(TestCase):
    def test_create_score(self):
        student_id = 230001
        subject_name = "Math"
        k1_score = 90.5
        k2_score = 85.0
        k3_score = 92.5

        # Create a Score object
        score = Score.objects.create(
            student_id=student_id,
            subject=subject_name,
            K1_score=k1_score,
            K2_score=k2_score,
            K3_score=k3_score
        )

        # Check if the Score object was created successfully
        self.assertEqual(score.student_id, student_id)
        self.assertEqual(score.subject, subject_name)
        self.assertEqual(score.K1_score, k1_score)
        self.assertEqual(score.K2_score, k2_score)
        self.assertEqual(score.K3_score, k3_score)