import pandas as pd

def get_general_income(table):
    result = []

    for row in table:
        income = (row[2]+row[3])*row[1]+row[1]
        result.append(income)

    return result


def get_result(table, exp_income):
    result = 0

    for index, row in enumerate(table):
        result += row[0] * exp_income[index]

    return result

def main():
    df_A=pd.read_excel("SATPR3.xlsx", sheet_name="task5", skiprows=3, nrows=3, usecols="F:I", header=None,)
    df_B = pd.read_excel("SATPR3.xlsx", sheet_name="task5", skiprows=7, nrows=3, usecols="F:I", header=None,)

    A = df_A.to_numpy()
    B = df_B.to_numpy()

    exp_income_A = get_general_income(A)
    exp_income_B = get_general_income(B)

    print(exp_income_A)
    print(exp_income_B)

    result_A = get_result(A, exp_income_A)
    result_B = get_result(B, exp_income_B)
  
    print(result_A)
    print(result_B)

main()