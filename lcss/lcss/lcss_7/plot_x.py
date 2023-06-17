import xlrd, csv
import xlwt
import math

#根据x1，x2轨迹，得到h值
def combine_excel(file_1, file_2):
    wb_pri = xlrd.open_workbook(file_1)  # 打开原始文件
    wb_tar = xlrd.open_workbook(file_2)  # 打开目标文件
    wb_result = xlwt.Workbook()  # 新建一个文件，用来保存结果
    sheet_result = wb_result.add_sheet('Sheet1', cell_overwrite_ok=True)
    sheet_pri = wb_pri.sheet_by_index(0)  # 通过index获取每个sheet
    sheet_tar = wb_tar.sheet_by_index(0)  # 通过index获取每个sheet
    ncols = sheet_pri.ncols  # Excel列的数目  原Excel和目标Excel的列表的长度相同
    for i in range(0, ncols):  # 将Excel表格对应位置相加
        l_p = sheet_pri.col_values(i, start_rowx=0, end_rowx=None)
        l_t = sheet_tar.col_values(i, start_rowx=0, end_rowx=None)
        l_r = [abs(l_p[i] - l_t[i]) for i in range(0, len(l_p))]  # 两列表对应位置相减，取绝对值
        print(l_r)
        for j, key in enumerate(l_r):
            sheet_result.write(j , i, key)
    wb_result.save('D:\pythonProject\opacity_loss1u\plot_traj\data_x1x2.xlsx')


if __name__ == "__main__":
    file_1 = "D:\pythonProject\opacity_loss1u\plot_traj\data_x1.xlsx"
    file_2 = "D:\pythonProject\opacity_loss1u\plot_traj\data_x2.xlsx"
    combine_excel(file_1,file_2)
