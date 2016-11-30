from django.test import TestCase
from django.utils import timezone
from .models import Course
from .models import Step
class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
        title = "Python Regular Expression",
        description = "Learn To write Python Regular Expressions "
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class StepModelTests(TestCase):
    def test_step_creation(self):
        course = Course.objects.create(
        title = "Python Regular Expression",
        description = "Learn To write Python Regular Expressions "
        )
        step = Step.objects.create(
        title = "Python Regular Expression Step",
        description = "Learn To write Python Regular Expressions Step",
        course = course
        )
        now = timezone.now()
        self.assertEqual(step.title, "Python Regular Expression Step")

# Create your tests here.
