from faker import Faker
import json
import random

fake = Faker()

def create_data(n):
    data = []
    for _ in range(n):
        record = {
            "pageViews": random.randint(1, 1000),
            "uniqueVisitors": random.randint(1, 500),
            "sessions": random.randint(1, 700),
            "bounceRate": round(random.uniform(0.1, 1.0), 2),
            "avgSessionDuration": str(random.randint(1, 30)) + ":" + str(random.randint(0, 59)).zfill(2),
            "pagesPerSession": random.randint(1, 10),
            "trafficSource": random.choice(["direct", "searchEngine", "socialMedia", "referrals", "paidAdvertising"]),
            "conversionRate": round(random.uniform(0.01, 0.1), 2),
            "topPages": ["/"+fake.word() for _ in range(3)],
            "exitPages": ["/"+fake.word() for _ in range(3)],
            "behaviorFlow": ["/"+fake.word() for _ in range(3)],
            "demographics": {
                "age": random.choice(["18-24", "25-34", "35-44", "45-54", "55+"]),
                "gender": random.choice(["male", "female"]),
                "location": fake.country(),
                "language": fake.language_name(),
            }
        }
        data.append(record)
    return data

def main():
    n = 100000  # 1 Lakh
    data = create_data(n)
    with open('website_data.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
