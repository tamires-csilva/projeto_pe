print("Este ChatBot foi desenvolvido para definir se o preço de um imóvel está caro com base nos imóveis do CEP 98011")
print("Por favor, utilize apenas números para responder as perguntas")
print("--------------------------------------------------------------------------------------------------------------")

sqft_living = float(input("Quanto é o Sqft Living? "))

if sqft_living > 1965:
    if sqft_living > 2520:
        sqft_lot = float(input("Quanto é o Sqft Lot? "))
        if sqft_lot > 31317.5:
            print("O imóvel é CARO")
        else:
            view = float(input("Qual é o View? "))
            if view <= 1:
                print("O imóvel é BARATO")
            else:
                if sqft_living > 2560:
                    bathrooms = float(input("Há quantos Bathrooms? "))
                    if bathrooms > 2.875:
                        print("O imóvel é BARATO")
                    else:
                        print("O imóvel é CARO")
                else:
                    print("O imóvel é BARATO")
    else:
        grade = float(input("Qual é a Grade? "))
        if grade > 8.5:
            sqft_basement = float(input("Quanto é o Sqft Basement? "))

            if sqft_basement > 295:
                if sqft_basement > 955:
                    print("O imóvel é CARO")
                else:
                    print("O imóvel é BARATO")
            else:
                print("O imóvel é CARO")
        else:
            if sqft_living > 2465:
                print("O imóvel é CARO")
            else:
                sqft_lot = float(input("Quanto é o Sqft Lot? "))
                if sqft_lot > 8001:
                    if sqft_living > 2400:
                        bathrooms = float(input("Há quantos Bathrooms? "))
                        if bathrooms > 2.125:
                            print("O imóvel é CARO")
                        else:
                            print("O imóvel é BARATO")
                    else:
                        if sqft_living > 1975:
                            if sqft_lot > 21593:
                                if sqft_living > 2195:
                                    print("O imóvel é CARO")
                                else:
                                    print("O imóvel é BARATO")
                            else:
                                print("O imóvel é BARATO")
                        else:
                            bathrooms = float(input("Há quantos Bathrooms? "))
                            if bathrooms > 2:
                                print("O imóvel é BARATO")
                            else:
                                print("O imóvel é CARO")
                else:
                    if sqft_living > 2105:
                        if sqft_lot > 7551:
                            print("O imóvel é CARO")
                        else:
                            if sqft_living > 2210:
                                print("O imóvel é CARO")
                            else:
                                sqft_above = float(input("Quanto é o Sqft Above?"))
                                if sqft_above > 2150:
                                    bedrooms = float(input("Há quantos Bedrooms? "))
                                    if bedrooms > 3.5:
                                        print("O imóvel é CARO")
                                    else:
                                        if grade > 7.5:
                                            print("O imóvel é BARATO")
                                        else:
                                            print("O imóvel é CARO")
                                else:
                                    print("O imóvel é BARATO")
                    else:
                        print("O imóvel é CARO")
# AQUI
else:
    sqft_lot = float(input("Quanto é o Sqft Lot? "))
    if sqft_lot > 11000.0:
        sqft_living = float(input("Quanto é o Sqft Living? "))
        if sqft_living <= 1260.0:
            print("O imóvel é CARO")
        else:
            sqft_lot = float(input("Quanto é o Sqft Lot? "))
            if sqft_lot <= 17125.5:
                print("O imóvel é BARATO")
            else:
                sqft_living = float(input("Quanto é o Sqft Living? "))
                if sqft_living <= 1555.0:
                    print("O imóvel é CARO")-
                else:
                    print("O imóvel é BARATO")-
    else:
        sqft_living = float(input("Quanto é o Sqft Living? "))
        if sqft_living <= 1915.0:
            sqft_lot = float(input("Quanto é o Sqft Lot? "))
            if sqft_lot <= 4936.0:
                bathrooms = float(input("Há quantos Bathrooms? "))
                if bathrooms <= 2.375:
                    print("O imóvel é BARATO")
                else:
                    print("O imóvel é CARO")
            else:
                sqft_above = float(input("Quanto é o Sqft Above?"))
                if sqft_above <= 1020.0:
                    sqft_living = float(input("Quanto é o Sqft Living? "))
                    if sqft_living <= 1285.0:
                        print("O imóvel é CARO")
                    else:
                        print("O imóvel é BARATO")
                else:
                    sqft_above = float(input("Quanto é o Sqft Above?"))
                    if sqft_above <= 1750.0:
                        print("O imóvel é CARO")
                    else:
                        sqft_above = float(input("Quanto é o Sqft Above?"))
                        if sqft_above <= 1810.0:
                            print("O imóvel é BARATO")
                        else:
                            print("O imóvel é CARO")
        else:
            sqft_living = float(input("Quanto é o Sqft Living? "))
            if sqft_living > 1940.0:
                print("O imóvel é CARO")
            else:
                sqft_above = float(input("Quanto é o Sqft Above?"))
                if sqft_above <= 1680.0:
                    print("O imóvel é BARATO")
                else:
                    sqft_lot = float(input("Quanto é o Sqft Lot? "))
                    if sqft_lot <= 7006.5:
                        print("O imóvel é BARATO")
                    else:
                        print("O imóvel é CARO")
