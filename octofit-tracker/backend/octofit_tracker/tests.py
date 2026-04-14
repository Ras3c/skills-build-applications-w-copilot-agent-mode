from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, calories=300)
        self.workout = Workout.objects.create(user=self.user, name='Test Workout', description='Test Desc')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_user_str(self):
        self.assertEqual(self.user.username, 'testuser')
    def test_activity_str(self):
        self.assertIn('run', str(self.activity))
    def test_workout_str(self):
        self.assertIn('Test Workout', str(self.workout))
    def test_leaderboard_str(self):
        self.assertIn('Test Team', str(self.leaderboard))
