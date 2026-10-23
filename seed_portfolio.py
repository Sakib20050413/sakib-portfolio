import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from core.management.commands.seed_portfolio import run_canonical_seed

if __name__ == '__main__':
    run_canonical_seed()
    print("Database seeded successfully with all 8 skill categories and 8 verified projects!")
