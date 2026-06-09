
def enem(nota1,nota2,nota3,nota4,nota5):
    nota1= int (input ("coloque sua primeira nota aqui: "))
    nota2= int (input ("coloque sua segunda nota aqui: "))
    nota3= int (input ("coloque sua terceira nota aqui: "))
    nota4= int (input ("coloque sua quarta nota aqui: "))
    nota5= int (input ("coloque sua quinta nota aqui: "))
    media_enem=(nota1+nota2+nota3+nota4+nota5)/5
    return media_enem
resultado_enem=enem("nota1","nota2","nota3","nota4","nota5")
print(f"o resultado da media do enem é:{resultado_enem}")







