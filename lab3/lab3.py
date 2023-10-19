import pandas as pd


def get_expected_income(table):
    result = []

    for row in table:
        income = (2400 - 1500) * row[3] - row[4] * 1500
        result.append(income)

    return result


def get_result(table, exp_income):
    result = 0

    for index, row in enumerate(table):
        result += row[0] * exp_income[index]

    return result


def main():
    df_A = pd.read_excel("SATPR3.xlsx", sheet_name="task8",
                         skiprows=3, nrows=3, usecols="D:I", header=None,)
    df_B = pd.read_excel("SATPR3.xlsx", sheet_name="task8",
                         skiprows=7, nrows=3, usecols="D:I", header=None,)
    df_C = pd.read_excel("SATPR3.xlsx", sheet_name="task8",
                         skiprows=11, nrows=3, usecols="D:I", header=None,)
    

    A = df_A.to_numpy()
    B = df_B.to_numpy()
    C = df_C.to_numpy()

    exp_income_A = get_expected_income(A)
    exp_income_B = get_expected_income(B)
    exp_income_C = get_expected_income(C)
    
    print(exp_income_A)
    print(exp_income_B)
    print(exp_income_C)

    result_A = get_result(A, exp_income_A)
    result_B = get_result(B, exp_income_B)
    result_C = get_result(C, exp_income_C)

    print(result_A)
    print(result_B)
    print(result_C)
   

main()