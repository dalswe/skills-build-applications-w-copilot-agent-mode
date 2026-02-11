from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='cap@marvel.com', name='Captain America', team='Marvel'),
            User(email='thor@marvel.com', name='Thor', team='Marvel'),
            User(email='hulk@marvel.com', name='Hulk', team='Marvel'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
            User(email='flash@dc.com', name='Flash', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', type='Running', duration=30, date=date(2026, 2, 10)),
            Activity(user='Captain America', type='Cycling', duration=45, date=date(2026, 2, 9)),
            Activity(user='Thor', type='Swimming', duration=60, date=date(2026, 2, 8)),
            Activity(user='Hulk', type='Weightlifting', duration=50, date=date(2026, 2, 7)),
            Activity(user='Superman', type='Running', duration=40, date=date(2026, 2, 10)),
            Activity(user='Batman', type='Cycling', duration=35, date=date(2026, 2, 9)),
            Activity(user='Wonder Woman', type='Swimming', duration=55, date=date(2026, 2, 8)),
            Activity(user='Flash', type='Running', duration=25, date=date(2026, 2, 7)),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=185)
        Leaderboard.objects.create(team='DC', points=155)

        # Workouts
        workouts = [
            Workout(name='Push Ups', description='Do 20 push ups', difficulty='Easy'),
            Workout(name='Pull Ups', description='Do 10 pull ups', difficulty='Medium'),
            Workout(name='Squats', description='Do 30 squats', difficulty='Easy'),
            Workout(name='Plank', description='Hold plank for 1 minute', difficulty='Medium'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
