import pandas as pd
import csv
import db

def get_worker_data(file_path):
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    need_datas = []
    columns = ["full_name", "lavozim", "jshshir", "ish_orni_sana", "jismoniy_shaxs_turi", "hodim_holati", 
               "shartnoma_turi", "ish_vaqti", "ish_orni_turi", "jami_daromad", "hisob_daromad", 
               "daromad_soligi", "hisob_soliq_summasi", "oxshashlik_darajasi"]

    for list_name in sheet_names:
        # Excel faylidan to'g'ridan-to'g'ri DataFrame yaratish
        excel_data_df = pd.read_excel(file_path, sheet_name=list_name)

        # Faqat kerakli ustunlarni olish (14 ta asosiy ustun + oxshashlik darajasi)
        need_data = []

        for idx, row in excel_data_df.iterrows():
            # Ma'lumotni to'g'ri formatda olish
            if idx > 13:
                scilcing_data = list(row.iloc[2:14]) + [row.iloc[-2]] 
                if '' not in scilcing_data and None not in scilcing_data:
                    check_data = {
                        columns[0]: scilcing_data[0],
                        columns[1]: scilcing_data[1],
                        columns[2]: scilcing_data[2],
                        columns[3]: scilcing_data[3],
                        columns[7]: float(scilcing_data[7]),
                        columns[-1]: scilcing_data[-1],
                    }
                    obj_db = db.Database()
                    is_get_data = obj_db.check_data_one('ishchilar', data=check_data)
                    if not is_get_data:
                        need_data.append(scilcing_data)
        
        if need_data:
            need_datas.append(need_data)

    if need_datas:
        need_datas[0].insert(0, columns)
    return need_datas[0] if need_datas else []


def get_bank_hisoboti_data(file_path):
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    need_datas = []
    columns = ['buy_date', 'hisob_raqami', 'inn_raqami', 'full_name', 'hujjat_raqami', 'operatsiya_turi', 'mfo', 'oborot_debet', 'oborot_kredit', "puy_description"]
    for list_name in sheet_names:
        excel_data_df = pd.read_excel(file_path, sheet_name=list_name)
        need_data = []
        
        for idx, row in excel_data_df.iterrows():
            if idx > 4:
                split_data = str(row[1]).replace('"', '').split('/')
                hisob_raqam, inn_raqam, full_name = split_data[0], split_data[1], '/'.join(split_data[2:])
                check_data = {
                    columns[0]: str(row[0]),
                    columns[1]: hisob_raqam,
                    columns[2]: inn_raqam,
                    columns[3]: full_name,
                    columns[4]: str(row[2]),
                    columns[5]: str(row[3]),
                    columns[6]: str(row[4]),
                    columns[-2]: str(row[-2])
                }
                obj_db = db.Database()
                is_get_data = obj_db.check_data_one('bank_hisoboti', data=check_data)
                if is_get_data == []:
                    change_row = [row[0], hisob_raqam, inn_raqam, full_name, row[2], row[3], row[4], row[5], row[6], row[7]]
                    need_data.append(change_row)

        if need_data:
            need_datas.append(need_data)
    if need_datas:
        need_datas[0].insert(0, columns)
    return need_datas[0] if need_datas else []

def get_chek_lists(file_path):
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    need_datas = []
    columns = [
        "vid_dokument", "tip_dokument", "status", "nomer_dokument", "data_dokument",
        "dogovor_nomer", "dogovor_data", "data_otpravki", "prodavec_inn_pinfl",
        "prodavec_naimenovanie", "prodavec_kod_filiala", "prodavec_nazvanie_filiala",
        "pokupatel_inn_pinfl", "pokupatel_naimenovanie", "pokupatel_kod_filiala",
        "pokupatel_nazvanie_filiala", "primechanie", "primechanie_tovaru", "identifikacionny_kod",
        "edinitca_izmereniya", "markirovka", "kolichestvo", "tsena", "stavka_akciz",
        "summa_akciz", "stoimost_postavki", "nds_stavka", "nds_summa",
        "stoimost_postavki_nds", "proiskhozhdenie_tovara"
    ]
    for list_name in sheet_names:
        excel_data_df = pd.read_excel(file_path, sheet_name=list_name)
        need_data = []
        
        for idx, row in excel_data_df.iterrows():
            if idx > 2:
                check_data = {
                    columns[0]: str(row[0]),
                    columns[1]: str(row[1]),
                    columns[2]: str(row[2]),
                    columns[3]: str(row[3]),
                    columns[13]: str(row[13]),
                }
                obj_db = db.Database()
                is_get_data = obj_db.check_data_one('checklar_royxati', data=check_data)
                if is_get_data == []:
                    need_data.append(row.tolist())

        if need_data:
            need_datas.append(need_data)
    if need_datas:
        need_datas[0].insert(0, columns)
    return need_datas[0] if need_datas else []

def get_xarajat_doc_datas(file_path):
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    need_datas = []
    columns = [
        "doc_id", "vid_dokument", "tip_dokument", "status", "nomer_dokument", "data_dokument",
        "dogovor_nomer", "dogovor_data", "data_otpravki", "prodavec_inn_pinfl",
        "prodavec_naimenovanie", "prodavec_kod_filiala", "prodavec_nazvanie_filiala",
        "pokupatel_inn_pinfl", "pokupatel_naimenovanie", "pokupatel_kod_filiala",
        "pokupatel_nazvanie_filiala", "primechanie", "primechanie_tovaru", "identifikacionny_kod",
        "edinitca_izmereniya", "markirovka", "kolichestvo", "tsena", "stavka_akciz",
        "summa_akciz", "stoimost_postavki", "nds_stavka", "nds_summa",
        "stoimost_postavki_nds", "proiskhozhdenie_tovara"
    ]
    for list_name in sheet_names:
        excel_data_df = pd.read_excel(file_path, sheet_name=list_name)
        need_data = []
        
        for idx, row in excel_data_df.iterrows():
            change_row = row[2:]
            if idx > 2 and change_row[0] != "":
                check_data = {
                    columns[0]: str(change_row[0]),
                    columns[5]: str(change_row[5]),
                    columns[7]: str(change_row[7]),
                    columns[9]: str(change_row[9]),
                    columns[13]: str(change_row[13]),
                }
                obj_db = db.Database()
                is_get_data = obj_db.check_data_one('xarajat_documents', data=check_data)
                if is_get_data == []:
                    need_data.append(row.tolist())

        if need_data:
            need_datas.append(need_data)
    if need_datas:
        need_datas[0].insert(0, columns)
    return need_datas[0] if need_datas else []

def get_ulgurji_doc_datas(file_path):
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    need_datas = []
    columns = [
        "doc_id", "vid_dokument", "tip_dokument", "status", "nomer_dokument", "data_dokument",
        "dogovor_nomer", "dogovor_data", "data_otpravki", "prodavec_inn_pinfl", 
        "prodavec_naimenovanie", "prodavec_kod_filiala", "prodavec_nazvanie_filiala", 
        "pokupatel_inn_pinfl", "pokupatel_naimenovanie", "pokupatel_kod_filiala", 
        "pokupatel_nazvanie_filiala", "primechanie", "primechanie_tovaru", 
        "identifikacionny_kod", "edinitca_izmereniya", "markirovka", "kolichestvo", 
        "tsena", "stavka_akciz", "summa_akciz", "stoimost_postavki", 
        "nds_stavka", "nds_summa", "stoimost_postavki_nds", "proiskhozhdenie_tovara"
    ]
    for list_name in sheet_names:
        excel_data_df = pd.read_excel(file_path, sheet_name=list_name)
        need_data = []
        
        # DataFramedagi satrlarni aylanib chiqish
        for idx, row in excel_data_df.iterrows():
            change_row = row[2:]
            if idx > 2 and change_row[0] != "":
                check_data = {
                    columns[0]: change_row[0],
                    columns[5]: change_row[5],
                    columns[7]: change_row[7],
                    columns[9]: change_row[9],
                    columns[13]: change_row[13],
                }
                obj_db = db.Database()
                is_get_data = obj_db.check_data_one('ulgurji_document', data=check_data)
                if is_get_data == []:
                    need_data.append(row.tolist())
        if need_data:
            need_datas.append(need_data)
    if need_datas:
        need_datas[0].insert(0, columns)
    return need_datas[0] if need_datas else []
