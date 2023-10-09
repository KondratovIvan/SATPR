import numpy 
import pandas 
import seaborn 
import matplotlib.pyplot 

#сргеом
def geomean(arr):  
    return numpy.exp(numpy.log(arr).mean())


#Wi
def priority_makrs_avg(matrix):
    result = []

    for array in matrix:
        result.append(geomean(array))

    return result


#Wнорм
def priority_vector(arr):
    result = []

    sum = numpy.sum(arr)

    for w in arr:
        result.append(w/sum)

    return result
def get_from_excel(path,sheet_name,skiprows,usecols,nrows):
    df = pandas.read_excel(path, sheet_name=sheet_name,header=None, skiprows=skiprows, usecols=usecols, nrows=nrows)
    matrix = df.to_numpy()
    return matrix


def main():
    first_matrix = get_from_excel(path='D:\SATPR\lab2\SATPR2.xlsx', sheet_name='1',skiprows=3, usecols='B:D', nrows=3)
    second_matrix = get_from_excel(path='D:\SATPR\lab2\SATPR2.xlsx', sheet_name='1',skiprows=10, usecols='B:D', nrows=3)


    first_k1_matrix = get_from_excel(path='D:\SATPR\lab2\SATPR2.xlsx', sheet_name='2', skiprows=2, usecols='B:E', nrows=4)
    first_k2_matrix = get_from_excel(path='D:\SATPR\lab2\SATPR2.xlsx', sheet_name='2', skiprows=10, usecols='B:E', nrows=4)
    first_k3_matrix = get_from_excel(path='D:\SATPR\lab2\SATPR2.xlsx', sheet_name='2', skiprows=18, usecols='B:E', nrows=4)
 

    second_k1_matrix = get_from_excel(path='D:\SATPR\lab2\SATPR2.xlsx', sheet_name='3', skiprows=2, usecols='B:E', nrows=4)
    second_k2_matrix = get_from_excel(path='D:\SATPR\lab2\SATPR2.xlsx', sheet_name='3', skiprows=10, usecols='B:E', nrows=4)
    second_k3_matrix = get_from_excel(path='D:\SATPR\lab2\SATPR2.xlsx', sheet_name='3', skiprows=18, usecols='B:E', nrows=4)

   

    first_vector = priority_vector(priority_makrs_avg(first_matrix))
    second_vector = priority_vector(priority_makrs_avg(second_matrix))

    first_step_result = []

    for i in range(len(first_vector)):
        first_step_result.append(geomean([first_vector[i], second_vector[i]]))

    

    first_k1_vector = priority_vector(priority_makrs_avg(first_k1_matrix))
    first_k2_vector = priority_vector(priority_makrs_avg(first_k2_matrix))
    first_k3_vector = priority_vector(priority_makrs_avg(first_k3_matrix))

    second_k1_vector = priority_vector(priority_makrs_avg(second_k1_matrix))
    second_k2_vector = priority_vector(priority_makrs_avg(second_k2_matrix))
    second_k3_vector = priority_vector(priority_makrs_avg(second_k3_matrix))

    k1_result = []
    k2_result = []
    k3_result = []

    for i in range(len(first_k1_vector)):
        k1_result.append(numpy.max([first_k1_vector[i],second_k1_vector[i]]))
        k2_result.append(numpy.max([first_k2_vector[i],second_k2_vector[i]]))
        k3_result.append(numpy.max([first_k3_vector[i],second_k3_vector[i]]))

           

    final_result = []

    for i in range(len(k1_result)):
        final_result.append(geomean([k1_result[i],k2_result[i], k3_result[i]]))

    data = pandas.DataFrame([final_result], columns = ['A','B','C','D'])

    print(data)

    matplotlib.pyplot.figure()
    diagram = seaborn.barplot(data=data)
    diagram.bar_label(diagram.containers[0], fontsize=12);
    matplotlib.pyplot.show()

if __name__ == '__main__':
    main()