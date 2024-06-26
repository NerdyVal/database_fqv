from app.migrations.migration import Migration
from settings import RANKS_TABLE_NAME, TAXONOMY_TABLE_NAME


class CreateRanksTable:
    @staticmethod
    def run():
        """
        Создание таблицы ranks
        """

        Migration.run(f'''
        CREATE TABLE {RANKS_TABLE_NAME} (
        id serial PRIMARY KEY,
        taxonomy_id integer REFERENCES {TAXONOMY_TABLE_NAME}(id) ON DELETE CASCADE ON UPDATE CASCADE,
        _Kingdom text,
        _Phylum text,
        _Class text,
        _Order text,
        _Family text,
        _Genus text,
        UNIQUE (_Kingdom, _Phylum, _Class, _Order, _Family, _Genus)
        )
        ''')
