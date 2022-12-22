
import sqlite3

class SQLitePipeline(object):
    def open_spider(self, spider):
        self.connection = sqlite3.connect('motos.db')
        self.cursor = self.connection.cursor()
        #Criar Tabela
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS motos( 
                modelo TEXT NOT NULL,
                preco TEXT,
                link TEXT     
            )
        ''')

        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT OR IGNORE INTO 
            motos(modelo, preco, link) VALUES(?,?,?)
        ''', (
            item.get('modelo'),
            item.get('preco'),
            item.get('link')
        ))
        
        self.connection.commit()
        return item
        