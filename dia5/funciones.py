a=",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:_#,,,,,,:::____##") #Quita los caracteres especificados al inicio de la cadena
print(a)#Python_ _Total,,,,,,::#


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"} #Conjunto de marcas de smartphones
marcas_tv = {"Sony", "Philmarcas_smartphones.ips", "Samsung", "LG"} #Conjunto de marcas de televisores
conjuntos_aislados=marcas_smartphones.isdisjoint(marcas_tv) #Verifica si los conjuntos no tienen elementos en común
print(conjuntos_aislados)#False 