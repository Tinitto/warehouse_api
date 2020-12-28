"""Test for tokyo-commodities-exchange/quotes-by-day-session microservice"""
import os
import unittest

from fastapi import FastAPI

from dotenv import load_dotenv

try:
    load_dotenv(
        os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), '.local.env'))
finally:
    pass

from test.utils.base_test_for_microservices import TestCase
from test.utils.config import RawDatabaseMockAsset
from test.utils.mock_models import QuotesByDaySession


class TestQuotesByDaySessionMicroservice(TestCase):
    """Tests for the Tokyo Commodities Exchanges quotes by day session microservice"""
    app = FastAPI()
    url_path = '/tokyo-commodities-exchange/quotes-by-day-session'
    raw_database_mock_assets = [
        RawDatabaseMockAsset(
            db_uri=os.getenv('TOKYO_COMMODITIES_HISTORICAL_DB_URI'),
            db_name='tokyo_commodities_historical',
            db_table_name='quotes_by_day_session',
            model_class=QuotesByDaySession)]
    service_name = 'tokyo_commodities_exchange'
    microservice_name = 'quotes_by_day_session'


if __name__ == '__main__':
    unittest.main()
