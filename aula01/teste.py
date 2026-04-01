def somatorio_intervalo_seguro(A, inicio, fim):
    if(not isinstance(A, list)):
        raise Exception("First argurment needs to be a list")
    if(not isinstance(inicio, int) or not isinstance(fim, int)):
        raise Exception("The 'inicio' and 'fim' variables must numbers")
    if(len(A) - 1 < fim or inicio < 0 or inicio > fim):
        raise Exception("The range for sum is out of bounds of the given list or the arguments do not match a valid logic")

    total = 0
    for i in range(inicio, fim + 1, 1):
        if(not isinstance(A[i], (int, float, complex))):
            raise Exception("Each value in the list must be a number")
        total = total + A[i]
    
    return total

total = somatorio_intervalo_seguro([5,1,3,9], 0, 2)
print(total)