print("""

kullanıcı kaydı

""")

sıstem_kullanıcı_adı = input("kayıt kullanıcı adı: ")
sistem_parola = input("kayıt parolası: ")
giriş_hakkı = 3

print("""

kullanıcı girişi

""")



while True:
    kullanıcı_adı = input("kullanıcı adı:")
    parola = input("parola: ")
    if (kullanıcı_adı == sıstem_kullanıcı_adı and sistem_parola != parola):
        print("parola hatalı...,tekrar deneyin")
        giriş_hakkı -= 1
        print("giriş hakkı = ",giriş_hakkı)
    elif (kullanıcı_adı != sıstem_kullanıcı_adı and sistem_parola == parola):
        print("kullanıcı adı hatalı...,tekrar deneyin")
        giriş_hakkı -= 1
        print("giriş hakkı = ",giriş_hakkı)
    elif (kullanıcı_adı != sıstem_kullanıcı_adı and sistem_parola != parola):
        print("kullanıcı adı ve parola hatalı...,tekrar deneyin")
        giriş_hakkı -= 1
        print("giriş hakkı = ",giriş_hakkı)
    else:
        print("giriş başarılı")
        break
    if (giriş_hakkı == 0):
        print("giriş hakkı bitti")
        break
