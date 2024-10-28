class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f'Persegi Panjang, Panjang: {self.panjang} cm, Lebar: {self.lebar} cm'

def main ():
    try:
        panjang = float(input("masukan panjang persegi: "))
        lebar = float(input("masukan lebar persegi: "))
        
        if(panjang <=0 or lebar <=0):
            raise ValueError("Nilai tidak boleh negattif atau nol")
            
        pp = PersegiPanjang(panjang, lebar)
        print(pp)
        print("keliling: ",pp.keliling())
        print("luas", pp.luas())
            
    except ValueError:
        print("Input harus berupa angka.")
            
if __name__ == "__main__":
    main()
