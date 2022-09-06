print("**DEPÓSITO - DELIVERY DE BEBIDAS**")

print("\n")

print("Qual tipo de bebida que você vai querer?")

print("\n")

print("1 - CERVEJAS")
print("2 - BEBIDAS QUENTES")
print("3 - REFRIGERANTE")
print("4 - SUCOS")

print("\n")

n = 0
while n == 0:
  drink = int(input("DIGITE O NÚMERO DE SUA BEBIDA: "))
  if(drink == 1):
    print("********CERVEJAS********")
    print('\n')
    print("1 - HEINEKEN 600 ML")
    print("2 - HEINEKEN LONG NECK - 355 ML")
    print("3 - BUDWEISER 600 ML")
    print("4 - BUDWEISER LONG NECK - 355 ML")
    print("5 - AMSTEL 600 ML")
    print("6 - AMSTEL LATA 355 ML")
    print("7 - HEISENBAHN LONG NECK 355 ML")
    print("\n")
    n = 0
    while n == 0:
      cerva = int(input("DIGITE O NÚMERO DE SUA CERVEJA: "))
      if(cerva == 1):
        print("HEINEKEN 600 ML - PREÇO: R$ 11,29")
        qtd1 = int(input("QUANTIDADE: "))
        tot1 = 11.29*qtd1
        print(tot1, 'reais')
        break
      elif(cerva == 2):
        print("2 - HEINEKEN LONG NECK - 355 ML - PREÇO: R$ 5,87")
        qtd2 = int(input("QUANTIDADE: "))
        tot2 = 5.87*qtd2
        print(tot2, 'reais')
        break
      elif(cerva == 3):
        print("BUDWEISER 600 ML - PREÇO: R$ 9,90")
        qt3 = int(input("QUANTIDADE: "))
        tot3 = 9.9*qt3
        print(tot3, 'reais')
        break
      elif(cerva == 4):
        print("BUDWEISER LONG NECK - 355 ML - R$ 4,19")
        qtd4 = int(input("QUANTIDADE: "))
        tot4 = 4.19*qtd4
        print(tot4, 'reais')
        break
      elif(cerva == 5):
        print("AMSTEL 600 ML - R$ 8,90")
        qtd5 = int(input("QUANTIDADE: "))
        tot5 = 8.9*qtd5
        print(tot5, 'reais')
        break
      elif(cerva == 6):
        print("AMSTEL LATA 355 ML - R$ 3,55")
        qtd6 = int(input("QUANTIDADE: "))
        tot6 = 3.55*qtd6
        print(tot6, 'reais')
        break
      elif(cerva == 7):
        print("HEISENBAHN LONG NECK 355 ML - R$ 3,99")
        qtd7 = int(input("QUANTIDADE: "))
        tot7 = 3.99*qtd7
        print(tot7, 'reais')
        break
      else:
        print("Opa!! Opção inválida!")
  elif(drink == 2):
    print("********BEBIDAS QUENTES********")
    print('\n')
    print("1 - CACHAÇA YPIOCA PRATA")
    print("2 - CACHAÇA PIRASSUNUNGA 51")
    print("3 - CACHAÇA VELHO BARREIRO")
    print("\n")
    print("4 - WHISKY OLD PARR 12 ANOS")
    print("5 - WHISKY BLACK WHITE")
    print("6 - WHISKY BALLANTINES")
    print("\n")
    print("7 - VODKA SMIRNOFF 1L")
    print("8 - VODKA ORLOFF 1L")
    print("\n")
    print("9 - TEQUILA JOSÉ CUERVO 1L")
    print("10 - CAMPARI 1L")
    print("\n")
    n = 0
    while n == 0:
      quente = int(input("DIGITE O NÚMERO DE SUA BEBIDA QUENTE: "))
      if(quente == 1):
        print("CACHAÇA YPIOCA PRATA - R$ 29,90")
        qtde1 = int(input("QUANTIDADE: "))
        total1 = qtde1*29.9
        print(total1, "reais")
        break
      elif(quente == 2):
        print("CACHAÇA PIRASSUNUNGA 51 - R$ 15,90")
        qtde2 = int(input("QUANTIDADE: "))
        total2 = qtde2*15.9
        print(total2, 'reais')
        break
      elif(quente == 3):
        print("CACHAÇA VELHO BARREIRO - R$ 16,90")
        qtde3 = int(input("QUANTIDADE: "))
        total3 = qtde3*16.9
        print(total3, 'reais')
        break
      elif(quente == 4):
        print("WHISKY OLD PARR 12 ANOS - R$ 119,90")
        qtde4 = int(input("QUANTIDADE: "))
        total4 = qtde4*119.9
        print(total4, 'reais')
        break
      elif(quente == 5):
        print("WHISKY BLACK WHITE - R$ 69,90")
        qtde5 = int(input("QUANTIDADE: "))
        total5 = qtde5*69.9
        print(total5, 'reais')
        break
      elif(quente == 6):
        print("WHISKY BALLANTINES - R$ 89,90")
        qtde6 = int(input("QUANTIDADE: "))
        total6 = qtde6*89.9
        print(total6, 'reais')
        break
      elif(quente == 7):
        print('VODKA SMIRNOFF 1L - R$ 39,90')
        qtde7 = int(input("QUANTIDADE: "))
        total7 = qtde7*39.9
        print(total7, 'reais')
        break
      elif(quente == 8):
        print("VODKA ORLOFF 1L - R$ 29,90")
        qtde8 = int(input("QUANTIDADE: "))
        total8 = qtde8*29.9
        print(total8, 'reais')
        break
      elif(quente == 9):
        print("TEQUILA JOSÉ CUERVO 1L - R$ 99,90")
        qtde9 = int(input("QUANTIDADE: "))
        total9 = qtde9*99.9
        print(total9, 'reais')
        break
      elif(quente == 10):
        print("CAMPARI 1L - R$ 19,90")
        qtde10 = int(input("QUANTIDADE: "))
        total10 = qtde10*19.9
        print(total10, "reais")
        break
      else:
        print("Opção inválida!")
  elif(drink == 3):
    print('********REFRIGERANTES********')

    # completar a parte de refrigerante e suco
      
