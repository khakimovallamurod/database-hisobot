import sqlite3

conn = sqlite3.connect("hisobot_database.db")  

def table_montly():
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ishchilar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,                                        -- Фуқароларнинг исми ва шарифи
        lavozim TEXT NOT NULL,                                 -- Лавозими
        jshshir TEXT NOT NULL UNIQUE,                          -- ЖШ ШИР
        ish_orni_sana TEXT,                                    -- Иш ўрни ташкил қилинган сана
        jismoniy_shaxs_turi INTEGER,                           -- Жисмоний шахс тури (1 - резидент, 2 - норезидент)
        hodim_holati INTEGER,                                  -- Ҳодимнинг ҳолати (1 - ишлаб келмоқда, 2 - шартнома бекор)
        shartnoma_turi INTEGER,                                -- Шартнома тури (1 - асосий, 2 - ўриндош, 3 - фуқаролик-ҳуқуқий, 4 - қурилиш)
        ish_vaqti REAL,                                        -- Иш вақти (ставкада 0.25, 0.5, 1 ва ҳ.к)
        ish_orni_turi INTEGER,                                 -- Иш ўрни (1 - доимий, 2 - вакант, 3 - янги, 4 - мавсумий)
        jami_daromad REAL,                                     -- Жами ҳисобланган меҳнатга ҳақ тўлаш тарзидаги даромадлар
        hisob_daromad REAL,                                    -- Ҳисобот даврида меҳнатга ҳақ тўлаш тарзидаги даромадлар
        daromad_soligi REAL,                                   -- Жисмоний шахслардан олинадиган даромад солиғи
        jami_soliq_summasi REAL,                               -- Жами ҳисобланган солиқ суммаси
        hisob_soliq_summasi REAL,                              -- Ҳисобот даврида ҳисобланган солиқ суммаси
        oxshashlik_darajasi REAL                               -- Ўхшашлик даражаси (%)
    )
    """)
    conn.commit()
    

table_montly()
