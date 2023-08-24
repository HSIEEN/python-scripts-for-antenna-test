# Data : 2023/8/22 17:37
# Author: Shawn Shi
# Right Reserved By COROS
import sys

from FormatingData_Fast import formatting_data
import tkinter as tk
import os
from tkinter import filedialog
import glob
import shutil
import pandas as pd
import xlwings as xw
import time


def copy_data(files, target_file):
    # delete sheet without data
    file_str = ''
    for file in files:
        file_str += file[-7:-5]
    if ('BT' not in file_str) and ('CP' in file_str) and ('LP' not in file_str):
        sys.exit("      数据不完整，请补充数据！")
    if ('BT' not in file_str) and ('L1' in file_str) and ('C1' not in file_str):
        sys.exit("      数据不完整，请补充数据！")
    if ('BT' not in file_str) and ('L5' in file_str) and ('C5' not in file_str):
        sys.exit("      数据不完整，请补充数据！")
    if not (('BT' in file_str) or ('CP' in file_str) or ('C1' in file_str) or ('C5' in file_str)):
        sys.exit("      数据不完整，请补充数据！")

    for file in files:
        # copy bluetooth data
        if 'BT.xlsx' == file[-7:]:
            columns = pd.Index(list(str(i) for i in range(0, 30)))
            # frequency.to_excel(target_file, 'BT-FS',columns=[""])
            df = pd.read_excel(file, header=3, usecols='B:AE')
            BT_efficiency = df.loc[list(i for i in range(0, 31))]
            BT_efficiency.columns = columns
            BT_efficiency.loc[:, '24'] = -BT_efficiency.loc[:, '24']
            BT_gain_2400 = df.loc[list(i for i in range(579, 592))]
            BT_gain_2400.columns = columns
            BT_gain_2440 = df.loc[list(i for i in range(783, 796))]
            BT_gain_2440.columns = columns
            BT_gain_2480 = df.loc[list(i for i in range(987, 1000))]
            BT_gain_2480.columns = columns
            # BT_efficiency.to_excel(target_file, 'BT-FS')
            with pd.ExcelWriter(target_file, mode='a', if_sheet_exists='overlay', engine="openpyxl") as writer:
                BT_efficiency.to_excel(writer, sheet_name='BT-FS', columns=list(str(i) for i in range(0, 30)),
                                       index=False, header=False, startrow=2, startcol=0)
                BT_gain_2400.to_excel(writer, sheet_name='BT-FS', columns=list(str(i) for i in range(1, 13)),
                                      index=False, header=False, startrow=38, startcol=1)
                BT_gain_2440.to_excel(writer, sheet_name='BT-FS', columns=list(str(i) for i in range(1, 13)),
                                      index=False, header=False, startrow=56, startcol=1)
                BT_gain_2480.to_excel(writer, sheet_name='BT-FS', columns=list(str(i) for i in range(1, 13)),
                                      index=False, header=False, startrow=74, startcol=1)
        elif 'LP.xlsx' == file[-7:]:
            columns = pd.Index(list(str(i) for i in range(0, 29)))
            df = pd.read_excel(file, header=3, usecols='B:AD')
            GPS_l1_effi = df.loc[list(i for i in range(50, 71))]
            GPS_l1_effi.columns = columns
            GPS_l1_effi.loc[:, '24'] = -GPS_l1_effi.loc[:, '24']
            GPS_l5_effi = df.loc[list(i for i in range(10, 31))]
            GPS_l5_effi.columns = columns
            GPS_l5_effi.loc[:, '24'] = -GPS_l5_effi.loc[:, '24']
            with pd.ExcelWriter(target_file, mode='a', if_sheet_exists='overlay', engine="openpyxl") as writer:
                GPS_l1_effi.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(0, 29)),
                                     index=False, header=False, startrow=2, startcol=0)
                GPS_l5_effi.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(0, 29)),
                                     index=False, header=False, startrow=2, startcol=0)
        elif 'CP.xlsx' == file[-7:]:
            columns = pd.Index(list(str(i) for i in range(0, 26)))
            df = pd.read_excel(file, header=3, usecols='B:AA')
            GPS_gain_1160r = df.loc[list(i for i in range(891, 905))]
            GPS_gain_1160r.columns = columns
            GPS_gain_1160l = df.loc[list(i for i in range(908, 922))]
            GPS_gain_1160l.columns = columns
            GPS_gain_1180r = df.loc[list(i for i in range(993, 107))]
            GPS_gain_1180r.columns = columns
            GPS_gain_1180l = df.loc[list(i for i in range(1010, 1024))]
            GPS_gain_1180l.columns = columns
            GPS_gain_1190r = df.loc[list(i for i in range(1044, 1058))]
            GPS_gain_1190r.columns = columns
            GPS_gain_1190l = df.loc[list(i for i in range(1061, 1075))]
            GPS_gain_1190l.columns = columns
            GPS_gain_1560r = df.loc[list(i for i in range(2931, 2945))]
            GPS_gain_1560r.columns = columns
            GPS_gain_1560l = df.loc[list(i for i in range(2948, 2962))]
            GPS_gain_1560l.columns = columns
            GPS_gain_1580r = df.loc[list(i for i in range(3033, 3047))]
            GPS_gain_1580r.columns = columns
            GPS_gain_1580l = df.loc[list(i for i in range(3050, 3064))]
            GPS_gain_1580l.columns = columns
            GPS_gain_1610r = df.loc[list(i for i in range(3186, 3200))]
            GPS_gain_1610r.columns = columns
            GPS_gain_1610l = df.loc[list(i for i in range(3203, 3217))]
            GPS_gain_1610l.columns = columns
            with pd.ExcelWriter(target_file, mode='a', if_sheet_exists='overlay', engine="openpyxl") as writer:
                # load l5 data to excel
                GPS_gain_1160r.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=28, startcol=1)
                GPS_gain_1160l.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=45, startcol=1)
                GPS_gain_1180r.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=78, startcol=1)
                GPS_gain_1180l.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=95, startcol=1)
                GPS_gain_1190r.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=128, startcol=1)
                GPS_gain_1190l.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=145, startcol=1)
                # load l1 data to excel
                GPS_gain_1560r.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=28, startcol=1)
                GPS_gain_1560l.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=45, startcol=1)
                GPS_gain_1580r.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=78, startcol=1)
                GPS_gain_1580l.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=95, startcol=1)
                GPS_gain_1610r.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=128, startcol=1)
                GPS_gain_1610l.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=145, startcol=1)
        elif 'L5.xlsx' == file[-7:]:
            columns = pd.Index(list(str(i) for i in range(0, 29)))
            df = pd.read_excel(file, header=3, usecols='B:AD')
            GPS_l5_effi = df.loc[list(i for i in range(0, 21))]
            GPS_l5_effi.columns = columns
            GPS_l5_effi.loc[:, '24'] = -GPS_l5_effi.loc[:, '24']
            with pd.ExcelWriter(target_file, mode='a', if_sheet_exists='overlay', engine="openpyxl") as writer:
                GPS_l5_effi.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(0, 29)),
                                     index=False, header=False, startrow=2, startcol=0)
        elif 'C5.xlsx' == file[-7:]:
            columns = pd.Index(list(str(i) for i in range(0, 26)))
            df = pd.read_excel(file, header=3, usecols='B:AA')
            GPS_gain_1160r = df.loc[list(i for i in range(331, 345))]
            GPS_gain_1160r.columns = columns
            GPS_gain_1160l = df.loc[list(i for i in range(348, 362))]
            GPS_gain_1160l.columns = columns
            GPS_gain_1180r = df.loc[list(i for i in range(433, 447))]
            GPS_gain_1180r.columns = columns
            GPS_gain_1180l = df.loc[list(i for i in range(450, 464))]
            GPS_gain_1180l.columns = columns
            GPS_gain_1190r = df.loc[list(i for i in range(484, 498))]
            GPS_gain_1190r.columns = columns
            GPS_gain_1190l = df.loc[list(i for i in range(501, 515))]
            GPS_gain_1190l.columns = columns
            with pd.ExcelWriter(target_file, mode='a', if_sheet_exists='overlay', engine="openpyxl") as writer:
                # load l5 data to excel
                GPS_gain_1160r.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=28, startcol=1)
                GPS_gain_1160l.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=45, startcol=1)
                GPS_gain_1180r.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=78, startcol=1)
                GPS_gain_1180l.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=95, startcol=1)
                GPS_gain_1190r.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=128, startcol=1)
                GPS_gain_1190l.to_excel(writer, sheet_name='L5-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=145, startcol=1)
        elif 'L1.xlsx' == file[-7:]:
            columns = pd.Index(list(str(i) for i in range(0, 29)))
            df = pd.read_excel(file, header=3, usecols='B:AD')
            GPS_l1_effi = df.loc[list(i for i in range(0, 21))]
            GPS_l1_effi.columns = columns
            GPS_l1_effi.loc[:, '24'] = -GPS_l1_effi.loc[:, '24']
            with pd.ExcelWriter(target_file, mode='a', if_sheet_exists='overlay', engine="openpyxl") as writer:
                GPS_l1_effi.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(0, 29)),
                                     index=False, header=False, startrow=2, startcol=0)
        elif 'C1.xlsx' == file[-7:]:
            columns = pd.Index(list(str(i) for i in range(0, 26)))
            df = pd.read_excel(file, header=3, usecols='B:AA')
            GPS_gain_1560r = df.loc[list(i for i in range(331, 345))]
            GPS_gain_1560r.columns = columns
            GPS_gain_1560l = df.loc[list(i for i in range(348, 362))]
            GPS_gain_1560l.columns = columns
            GPS_gain_1580r = df.loc[list(i for i in range(433, 447))]
            GPS_gain_1580r.columns = columns
            GPS_gain_1580l = df.loc[list(i for i in range(450, 464))]
            GPS_gain_1580l.columns = columns
            GPS_gain_1610r = df.loc[list(i for i in range(586, 600))]
            GPS_gain_1610r.columns = columns
            GPS_gain_1610l = df.loc[list(i for i in range(603, 617))]
            GPS_gain_1610l.columns = columns
            with pd.ExcelWriter(target_file, mode='a', if_sheet_exists='overlay', engine="openpyxl") as writer:
                # load l1 data to excel
                GPS_gain_1560r.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=28, startcol=1)
                GPS_gain_1560l.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=45, startcol=1)
                GPS_gain_1580r.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=78, startcol=1)
                GPS_gain_1580l.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=95, startcol=1)
                GPS_gain_1610r.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=128, startcol=1)
                GPS_gain_1610l.to_excel(writer, sheet_name='L1-FS', columns=list(str(i) for i in range(1, 13)),
                                        index=False, header=False, startrow=145, startcol=1)

    # delete sheet without data
    wb = xw.Book(target_file)
    if 'BT' not in file_str:
        for sheet in wb.sheets:
            if 'BT' in sheet.name:
                sheet.delete()
    if ('C1' not in file_str) and ('C5' not in file_str) and ('CP' not in file_str):
        for sheet in wb.sheets:
            if 'L1' in sheet.name or 'L5' in sheet.name:
                sheet.delete()
    if ('C1' in file_str) and ('C5' not in file_str):
        for sheet in wb.sheets:
            if 'L5' in sheet.name:
                sheet.delete()
    if ('C1' not in file_str) and ('C5' in file_str):
        for sheet in wb.sheets:
            if 'L1' in sheet.name:
                sheet.delete()
    # rename sheets
    for sheet in wb.sheets:
        if '-' in sheet.name:
            sheet.name = sheet.name.split('-')[0] + '-' + target_file.split('/')[-1].split('.')[0]
    # return wb
    wb.save()
    return wb
    # wb.close()
    # wb.app.kill()


def merge_files(files, target_file):
    # target file
    wb = xw.Book(target_file)
    for file in files:
        file_name = file.split('\\')[1].split('.')[0]
        # source file
        wbs = xw.Book(file)
        for ssheet in wbs.sheets:
            # if wbs contains only one data set
            if 'L1-' in ssheet.name:
                ssheet.copy(after=wb.sheets['L1-FS'], name=ssheet.name)
            elif 'L5-' in ssheet.name:
                ssheet.copy(after=wb.sheets['L5-FS'], name=ssheet.name)
            elif 'BT-' in ssheet.name:
                ssheet.copy(after=wb.sheets['BT-FS'], name=ssheet.name)
        wbs.close()
    for tsheet in wb.sheets:
        if 'FS' in tsheet.name:
            tsheet.delete()
    wb.save()
    return wb


if __name__ == '__main__':
    print("****************使用指南************************")
    print("     1. 所有测试请选择标准模板")
    print("     2. 蓝牙测试数据请导出为BT.xlsx文件")
    print("     3. 双频GPS线极化测试数据请导出为LP.xlsx")
    print("     4. 双频GPS圆极化极化测试数据请导出为CP.xlsx")
    print("     5. L1线极化测试数据请导出为L1.xlsx")
    print("     6. L1圆极化测试数据请导出为C1.xlsx")
    print("     7. L5线极化测试数据请导出为L5.xlsx")
    print("     8. L5圆极化测试数据请导出为C5.xlsx")
    print("****************************************************")
    print("!!!=================请选择一个功能=================!!!!")
    print("     1. 读取测试数据并将格式化数据写入xlsx文件")
    print("     2. 合并格式化数据到一个xlsx文件")
    print("     3. 数据评分")
    print('=========================================')
    selection = input("请输入你的选择：")
    root = tk.Tk()
    root.withdraw()
    if selection == '1':
        print("============1. 读取测试数据并将格式化数据写入xlsx文件============")
        print('************请选择一个源文件目录(内有包含GPS或者BT数据的xlsx文件)***************')
        source_file_path = filedialog.askdirectory(title='打开测试数据目录')

        print(f"源文件目录为 {source_file_path}")
        excel_name = input("========请输入xlsx名称========\n")
        while excel_name == '':
            print('名称为空，请再次输入xlsx名称')
            excel_name = input("========请输入xlsx名称========\n")
        start_time = time.perf_counter()
        print('     数据归档进行中...')
        target_file = f'{source_file_path}/{excel_name}.xlsx'
        # os.popen(f'//nas.local/DATA/Wireless/AntennaTest/Templates/Antenna passive test templates V7.0.xlsx'
        # f' {source_file_path}/{sheet_name}.xlsx')
        shutil.copyfile('//nas.local/DATA/Wireless/AntennaTest/Templates/Antenna passive test templates V7.2.xlsx',
                        target_file)
        files = glob.glob(source_file_path + r"/*.xlsx")
        files.remove(f'{source_file_path}\\{excel_name}.xlsx')
        wb = copy_data(files, target_file)
        print('     数据归档完成')
        print('     数据评分中...')
        formatting_data(target_file, wb)
        print('     数据评分完成')
        print('总计用时: %s 秒' % (round((time.perf_counter() - start_time), 2)))
    elif selection == '2':
        print("============2. 合并格式化数据并写入xlsx文件=============")
        print('************请选择一个源文件目录***************')
        source_file_path = filedialog.askdirectory(title='打开源文件目录')
        print(f"源文件目录为 {source_file_path}")
        # path = r"\\nas.local\DATA\Wireless\Library\Components\for test"
        excel_name = input("========请输入汇总后的文件名称========\n")
        while excel_name == '':
            print('名称为空，请再次输入xlsx名称')
            excel_name = input("========请输入xlsx名称========\n")
        start_time = time.perf_counter()
        print('     文件合并中...')
        target_file = f'{source_file_path}/{excel_name}.xlsx'
        # os.popen(f'//nas.local/DATA/Wireless/AntennaTest/Templates/Antenna passive test templates V7.0.xlsx'
        # f' {source_file_path}/{sheet_name}.xlsx')
        shutil.copyfile('//nas.local/DATA/Wireless/AntennaTest/Templates/Antenna passive test templates V7.2.xlsx',
                        target_file)
        # dest_path = r"\\nas.local\DATA\Wireless\Library\Components\for test\Shunt\\"
        files = glob.glob(source_file_path + r"/*.xlsx")
        files.remove(f'{source_file_path}\\{excel_name}.xlsx')
        wb = merge_files(files, target_file)
        print('     文件合并完成')
        print('     数据评分中...')
        formatting_data(target_file, wb)
        print('     数据评分完成')
        print('总计用时: %s 秒' % (round((time.perf_counter() - start_time), 2)))
    elif selection == '3':
        print("============3. 数据评分=============")
        print('************请选择一个文件***************')
        source_file = filedialog.askopenfilename(title='选定一个源文件')
        print(f"源文件为 {source_file}")
        # path = r"\\nas.local\DATA\Wireless\Library\Components\for test"
        start_time = time.perf_counter()
        wb = xw.Book(source_file)
        print('     数据评分中...')
        formatting_data(source_file, wb)
        print('     数据评分完成')
        print('总计用时: %s 秒' % (round((time.perf_counter() - start_time), 2)))