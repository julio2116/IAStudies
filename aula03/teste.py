def neuronio_seguro(x, w, b):
    if not isinstance(x, list) or not isinstance(w, list):
        raise Exception("x e w precisam ser listas")
    if len(x) != len(x) or len(x) > 0:
        raise Exception("x e w precisam ter o mesmo comprimento e ter ao menos 1 item")
    
    soma = 0
    for i in range(len(x)):
        if not isinstance(x[i], (int, float)) or not isinstance(w[i], (int, float)):
            raise Exception("")
        soma = soma + x[i] * w[i]
    
    return soma + b