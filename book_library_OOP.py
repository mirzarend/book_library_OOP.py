class Book :
  def __init__(self,judul,penulis,tahun_terbit,pembeli):
    self.__judul = judul
    self.__penulis = penulis
    self.__tahun_terbit = tahun_terbit
    self.__jumlah_pembeli = pembeli
  def get_judul(self):
    return(self.__judul)
  def get_penulis(self):
    return(self.__penulis)
  def get_tahun_terbit(self):
    return(self.__tahun_terbit)
  def get_jumlah_pembeli(self) :
    return(self.__jumlah_pembeli)
  def set_jumlah_pembeli(self,terbaru) :
    if terbaru >= 0 :
      self.__jumlah_pembeli = terbaru
    else :
      print("Tidak boleh minus")
class Fiction_Book(Book) :
  def __init__(self,judul,penulis,tahun_terbit,jumlah_pembeli,genre):
    super().__init__(judul,penulis,tahun_terbit,jumlah_pembeli)
    self.__genre = genre
  def get_genre(self):
    return self.__genre
  def info(self) :
    print(f"Judul : {self.get_judul()}")
    print(f"Penulis : {self.get_penulis()}")
    print(f"Tahun Terbit : {self.get_tahun_terbit()}")
    print(f"Jumlah Pembeli : {self.get_jumlah_pembeli()} pcs")
    print(f"Genre : {self.get_genre()}")
class Non_Fiction_Book(Book) :
  def __init__(self,judul,penulis,tahun_terbit,jumlah_pembeli,topik) :
    super().__init__(judul,penulis,tahun_terbit,jumlah_pembeli)
    self.__topik = topik
  def get_topik(self) :
    return self.__topik
  def info(self) :
    print(f"Judul : {self.get_judul()}")
    print(f"Penulis : {self.get_penulis()}")
    print(f"Tahun Terbit : {self.get_tahun_terbit()}")
    print(f"Jumlah Pembeli : {self.get_jumlah_pembeli()} pcs")
    print(f"Topik : {self.get_topik()}")

Fbook1 = Fiction_Book("Rainbow","Andrew",2008,450,"Slice of Life")
Nfbook1 = Non_Fiction_Book("A Corruption From The Goverment","Dior J.",2015,200,"Corruption")
Nfbook1.set_jumlah_pembeli(400)
Fbook1.set_jumlah_pembeli(-10)
book_list = [Fbook1,Nfbook1]
for book in book_list :
  book.info()
