kamus={
    "pir":"buah berrwarna kuning","semangka":"buah berwarna hijau",
    "nanas":"buah berwarna kuning","anggur":"buah berwarna hijau",
    "kelapa":" buah berwarna coklat","ubi":"buah berwarna ungu"}
kata=input("masukan buah yg ingin di cari  :").lower()
if kata in kamus:
    print(f"arti dari {kata} adalah {kamus[kata]}")
else:
    print(f"maaf,arti dari{kata}tidak di temukan dlam kamus.")
