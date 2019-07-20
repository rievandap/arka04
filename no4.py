minArka=50000
discArka=0.5     #50%
maxArka=50000
minDemy=25000
discDemy=0.6     #60%
maxDemy=30000
awal=1.5
ongkir1=5000
ongkir2=3000
ppn=0.05     #5%

def arkaFood(harga,kode,jarak,pajak):
    x=int(jarak-awal)
    if kode == "False":     #tidak pakai kode promo
        if harga < minDemy:     #tanpa kode promo
            if jarak <= awal:
                if pajak == "True":     #cek pajaknya yaaaa
                    pajak = ppn
                    total=harga+ongkir1
                    bayar=total+(harga*ppn)
                    print("Total Harga:",bayar)
                if pajak == "False":
                    total=harga+ongkir1
                    bayar=total
                    print("Total Harga:",bayar)
            else:
                if pajak == "True":     #cek pajaknya yaaaa
                    pajak = ppn
                    total=harga+ongkir1+ongkir2+(x*ongkir2)
                    bayar=total+(harga*ppn)
                    print("Total Harga:",bayar)
                if pajak == "False":
                    total=harga+ongkir1+(x*ongkir2)
                    bayar=total
                    print("Total Harga:",bayar)
        
    if kode == "DITRAKTIRDEMY":     #pakai kode promo DITRAKTIRDEMY
        if harga >= minDemy:     #kode promo DITRAKTIRDEMY
            if (harga*discDemy) > maxDemy:
                if jarak <= awal:
                    if pajak == "True":
                        pajak = ppn    
                        total=harga+ongkir1-maxDemy
                        bayar=total+(harga*ppn)
                        print("Total Harga:",bayar)
                    if pajak == "False":
                        total=harga+ongkir1-maxDemy
                        bayar=total
                        print("Total Harga:",bayar)
                else:
                    if pajak == "True":     #cek pajaknya yaaaa
                        pajak=ppn
                        total=harga+ongkir1+ongkir2+(x*ongkir2)-maxDemy
                        bayar=total+(harga*ppn)
                        print("Total Harga:",bayar)
                    if pajak == "False":
                        total=harga+ongkir1+(x*ongkir2)-maxDemy
                        bayar=total
                        print("Total Harga:",bayar)
            else:
                if jarak <= awal:
                    if pajak == "True":     #cek pajaknya yaaaa
                        pajak=ppn
                        total=harga+ongkir1-(harga*discDemy)
                        bayar=total+(harga*ppn)
                        print("Total Harga:",bayar)
                    if pajak == "False":
                        total=harga+ongkir1-(harga*discDemy)
                        bayar=total
                        print("Total Harga:",bayar)
                else:
                    if pajak == "True":     #cek pajaknya yaaaa
                        pajak = ppn
                        total=harga+ongkir1+ongkir2+(x*ongkir2)-(harga*discDemy)
                        bayar=total+(harga*ppn)
                        print("Total Harga:",bayar)
                    if pajak == "False":
                        total=harga+ongkir1+ongkir2+(x*ongkir2)-(harga*discDemy)
                        bayar=total
                        print("Total Harga:",bayar)
    
    if kode == "ARKAFOOD5":     #pakai kode promo ARKAFOOD5
        if harga >= minArka:     #kode promo ARKAFOOD5
            if (harga*discArka) > maxArka:
                if jarak <= awal:
                    if pajak == "True":     #cek pajaknya yaaaa
                        pajak=ppn
                        total=harga+ongkir1-maxArka
                        bayar=total+(harga*ppn)
                        print("Total Harga:",bayar)
                    if pajak == "False":
                        total=harga+ongkir1-maxArka
                        bayar=total
                        print("Total Harga:",bayar)
                else:
                    if pajak == "True":     #cek pajaknya yaaaa
                        pajak=ppn
                        total=harga+ongkir1+(x*ongkir2)-maxArka
                        bayar=total+(harga*ppn)
                        print("Total Harga:",bayar)
                    if pajak == "False":
                        total=harga+ongkir1+(x*ongkir2)-maxArka
                        bayar=total
                        print("Total Harga:",bayar)
            else:
                if jarak <= awal:
                    if pajak == "True":     #cek pajaknya yaaaa
                        pajak=ppn
                        total=harga+ongkir1-(harga*discArka)
                        bayar=total+(harga*ppn)
                        print("Total Harga:",bayar)
                    if pajak == "False":
                        total=harga+ongkir1-(harga*discArka)
                        bayar=total
                        print("Total Harga:",bayar)
                else:
                    if pajak == "True":     #cek pajaknya yaaaa
                        pajak=ppn
                        total=harga+ongkir1+ongkir2+(x*ongkir2)-(harga*discArka)
                        bayar=total+(harga*ppn)
                        print("Total Harga:",bayar)
                    if pajak == "False":
                        total=harga+ongkir1+ongkir2+(x*ongkir2)-(harga*discArka)
                        bayar=total
                        print("Total Harga:",bayar)
        
arkaFood(50000,"ARKAFOOD5",3,"True")