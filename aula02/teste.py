def produto_escalar_seguro(A, B):
    if(not isinstance(A, list) or not isinstance(B, list)):
        raise Exception("A and B need to be lists")
    if(len(A) != len(B)):
        raise Exception("Both lists need to be equals on length")
    
    soma = 0
    for i in range(0, len(A)):
        if(not isinstance(A[i], (int, float)) or not isinstance(B[i], (int, float))):
            raise Exception("Only numbers allowed as values of each list")
        soma = soma + (A[i] * B[i])

    return soma


def produto_escalar_seguro_normalizado(A, B):
    if(not isinstance(A, list) or not isinstance(B, list)):
        raise Exception("A and B need to be lists")
    if(len(A) != len(B)):
        raise Exception("Both lists need to be equals on length")
    
    soma = 0

    for i in range(0, len(A)):
        if(not isinstance(A[i], (int, float)) or not isinstance(B[i], (int, float))):
            raise Exception("Only numbers allowed as values of each list")
        soma = soma + (A[i] * B[i])

    return soma / len(A)
list = produto_escalar_seguro_normalizado([1, 2, 3], [3, 2, 1])
print(list)