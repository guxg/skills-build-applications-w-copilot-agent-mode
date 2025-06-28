from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
        db = client[settings.MONGO_DB_NAME]

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create test users
        users = [
            {"_id": "1", "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "password"},
            {"_id": "2", "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "password"},
            {"_id": "3", "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "password"},
            {"_id": "4", "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "password"},
            {"_id": "5", "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "password"},
        ]
        db.users.insert_many(users)

        # Create test teams
        team = {"_id": "blue_team", "name": "Blue Team", "members": [user["_id"] for user in users]}
        db.teams.insert_one(team)

        # Create test activities
        activities = [
            {"_id": "activity1", "user": "1", "activity_type": "Cycling", "duration": 60},
            {"_id": "activity2", "user": "2", "activity_type": "Crossfit", "duration": 120},
            {"_id": "activity3", "user": "3", "activity_type": "Running", "duration": 90},
            {"_id": "activity4", "user": "4", "activity_type": "Strength", "duration": 30},
            {"_id": "activity5", "user": "5", "activity_type": "Swimming", "duration": 75},
        ]
        db.activities.insert_many(activities)

        # Create test leaderboard
        leaderboard = [
            {"_id": "leader1", "user": "1", "score": 100},
            {"_id": "leader2", "user": "2", "score": 200},
            {"_id": "leader3", "user": "3", "score": 150},
            {"_id": "leader4", "user": "4", "score": 50},
            {"_id": "leader5", "user": "5", "score": 125},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create test workouts
        workouts = [
            {"_id": "workout1", "name": "Morning Run", "duration": 30},
            {"_id": "workout2", "name": "Evening Swim", "duration": 45},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
