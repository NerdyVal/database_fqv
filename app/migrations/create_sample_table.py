from app.migrations.migration import Migration
from settings import SAMPLES_TABLE_NAME


class CreateSampleTable:
    @staticmethod
    def run():
        """
        Создание таблицы samples
        """

        Migration.run(f'''
        CREATE TABLE {SAMPLES_TABLE_NAME} (
            id serial PRIMARY KEY,
            name text UNIQUE
        )
        ''')
