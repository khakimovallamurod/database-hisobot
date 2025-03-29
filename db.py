import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("hisobot_database.db")  
        self.cursor = self.conn.cursor()
    def table_monthly(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ishchilar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,                                        -- Фуқароларнинг исми ва шарифи
                lavozim TEXT NOT NULL,                                 -- Лавозими
                jshshir TEXT NOT NULL UNIQUE,                          -- ЖШ ШИР
                ish_orni_sana TEXT,                                    -- Иш ўрни ташкил қилинган сана
                jismoniy_shaxs_turi TEXT,                           -- Жисмоний шахс тури (1 - резидент, 2 - норезидент)
                hodim_holati TEXT,                                  -- Ҳодимнинг ҳолати (1 - ишлаб келмоқда, 2 - шартнома бекор)
                shartnoma_turi TEXT,                                -- Шартнома тури (1 - асосий, 2 - ўриндош, 3 - фуқаролик-ҳуқуқий, 4 - қурилиш)
                ish_vaqti REAL,                                        -- Иш вақти (ставкада 0.25, 0.5, 1 ва ҳ.к)
                ish_orni_turi TEXT,                                 -- Иш ўрни (1 - доимий, 2 - вакант, 3 - янги, 4 - мавсумий)
                jami_daromad REAL,                                     -- Жами ҳисобланган меҳнатга ҳақ тўлаш тарзидаги даромадлар
                hisob_daromad REAL,                                    -- Ҳисобот даврида меҳнатга ҳақ тўлаш тарзидаги даромадлар
                daromad_soligi REAL,                                   -- Жисмоний шахслардан олинадиган даромад солиғи
                hisob_soliq_summasi REAL,                              -- Ҳисобот даврида ҳисобланган солиқ суммаси
                oxshashlik_darajasi REAL                               -- Ўхшашлик даражаси (%)
            )
            """)
        self.conn.commit()
        return True
    
    def table_bank_hisoboti(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_hisoboti (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                buy_date TEXT,              -- To'lov amalga oshirilgan sana
                hisob_raqami REAL,            
                inn_raqami REAL,            
                full_name TEXT,            
                hujjat_raqami TEXT,            -- Hujjat yoki to'lov raqami
                operatsiya_turi TEXT,          -- Operatsiya turi (kirim yoki chiqim)
                mfo TEXT,                      -- Moliya muassasasining MFO kodi
                oborot_debet REAL,             -- Debet bo'yicha aylanma summa (chiqim)
                oborot_kredit REAL,            -- Kredit bo'yicha aylanma summa (kirim)
                puy_description TEXT            -- To'lov mazmuni yoki izohi
            );
        """)
        self.conn.commit()

    def table_chek_lists(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS checklar_royxati (
                stir_jshshr TEXT,                     -- СТИР/ ЖИШШР
                fm_raqami TEXT,                        -- ФМ рақами
                chek_sanasi TEXT,                      -- Чек санаси
                chek_raqami TEXT,                      -- Чек рақами
                mahsulot_nomi TEXT,                    -- Маҳсулот номи
                miqdori REAL,                          -- Миқдори
                narxi REAL,                            -- Нархи
                chegirma_summasi REAL,                  -- Чегирма суммаси
                diskont_summasi REAL,                   -- Дисконт суммаси
                qqs_summasi REAL,                       -- ҚҚС суммаси
                jami_nakd_pul REAL,                     -- Жами нақд пул
                jami_bank_karta REAL,                   -- Жами банк карта
                jami_qqs REAL,                          -- Жами ҚҚС
                mahsulot_kodi TEXT,                     -- Маҳсулот коди
                olchov_birligi_kodi TEXT,                -- Ўлчов бирлиги коди
                shtrix_kod TEXT,                        -- Штрих код
                vositachi_stir_jshshr TEXT,              -- Воситачи СТИРи (ЖИШШРи)
                markirovka_kodi TEXT,                    -- Маркировка коди
                chek_turi TEXT                          -- Чек тури
            );
        """)
        self.conn.commit()

    def table_xarajat_docs(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS xarajat_documents (
                id INTEGER PRIMARY KEY,
                doc_id TEXT, 
                vid_dokument TEXT,
                tip_dokument TEXT,
                status TEXT,
                nomer_dokument TEXT,
                data_dokument DATE,
                dogovor_nomer TEXT,
                dogovor_data DATE,
                data_otpravki DATE,
                prodavec_inn_pinfl TEXT,
                prodavec_naimenovanie TEXT,
                prodavec_kod_filiala TEXT,
                prodavec_nazvanie_filiala TEXT,
                pokupatel_inn_pinfl TEXT,
                pokupatel_naimenovanie TEXT,
                pokupatel_kod_filiala TEXT,
                pokupatel_nazvanie_filiala TEXT,
                primechanie TEXT,
                primechanie_tovaru TEXT,
                identifikacionny_kod TEXT,
                edinitca_izmereniya TEXT,
                markirovka TEXT,
                kolichestvo REAL,
                tsena DECIMAL(10, 2),
                stavka_akciz DECIMAL(5, 2),
                summa_akciz DECIMAL(10, 2),
                stoimost_postavki DECIMAL(10, 2),
                nds_stavka DECIMAL(5, 2),
                nds_summa DECIMAL(10, 2),
                stoimost_postavki_nds DECIMAL(10, 2),
                proiskhozhdenie_tovara TEXT
            );
        """)
        self.conn.commit()
        self.conn.close()
    
    def table_ulgurji_zakas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ulgurji_document (
                id INTEGER PRIMARY KEY,
                doc_id TEXT,
                vid_dokument TEXT,
                tip_dokument TEXT,
                status TEXT,
                nomer_dokument TEXT,
                data_dokument DATE,
                dogovor_nomer TEXT,
                dogovor_data DATE,
                data_otpravki DATE,
                prodavec_inn_pinfl TEXT,
                prodavec_naimenovanie TEXT,
                prodavec_kod_filiala TEXT,
                prodavec_nazvanie_filiala TEXT,
                pokupatel_inn_pinfl TEXT,
                pokupatel_naimenovanie TEXT,
                pokupatel_kod_filiala TEXT,
                pokupatel_nazvanie_filiala TEXT,
                primechanie TEXT,
                primechanie_tovaru TEXT,
                identifikacionny_kod TEXT,
                edinitca_izmereniya TEXT,
                markirovka TEXT,
                kolichestvo REAL,
                tsena DECIMAL(10, 2),
                stavka_akciz DECIMAL(5, 2),
                summa_akciz DECIMAL(10, 2),
                stoimost_postavki DECIMAL(10, 2),
                nds_stavka DECIMAL(5, 2),
                nds_summa DECIMAL(10, 2),
                stoimost_postavki_nds DECIMAL(10, 2),
                proiskhozhdenie_tovara TEXT
            );
        """)
        self.conn.commit()
        self.conn.close()
        
    def insert_data(self, table, data):
        try:
            columns = ', '.join(data[0])
            placeholders = ', '.join(['?'] * len(data[0]))

            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.cursor.executemany(query, data[1:])
            self.conn.commit()
            return True
        except:
            return False

    def delete_table(self, table):
        try:
            query = self.cursor.execute(f"DROP TABLE IF EXISTS {table}")
            self.conn.commit()
            return True
        except :
            return False
    def table_data_all(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        data = self.cursor.fetchall()
        return data
    def check_data_one(self, table, data):
        query = ""
        for key in data:
            query += f'{key} = "{data[key]}" and '
        query = query.strip('and ')
        self.cursor.execute(f"select * from {table} WHERE {query}")
        data = self.cursor.fetchall()

        return data
    
# obj = Database()
# obj.delete_table('bank_hisoboti')
# obj.table_xarajat_docs()
