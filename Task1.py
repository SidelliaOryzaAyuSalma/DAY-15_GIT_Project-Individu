import pandas as pd

class MarketingDataETL:
  def__init__(self, filename) :
     self.filename = filename
     self. data = None

def extract(self):
    try:
       self.data = pd.read_csv(self.filename, sep=';')
       print("Data berhasil diestrak dari file:", self.filename)
    expect FileNotFoundError:
       print("File tidak ditemukan.")
    expect Exception as e:
       print("Terjadi kesalahan saat ektraksi data:", str(e))

def transform(self):
    if self.data is not None:
       # Implementasi transformasi sederhana pada data
       try:
          # Mengubah format tanggal
          self.data['purchase_date] = pd,to_datetime(self.data['purchase_date'], errors='coerce', format='%d%m%y')
          print("Data berhasil ditransformasi.")
       expect Exception as e:
          print("Terjadi kesalahan saat transformasi data:", str(e))
    else:
          print("Data belum diekstrak dan ditransformasi. Lakukan ektraksi dan transformasi terlebih dahulu.")

# Contoh penggunaan
if__name__ == "__main__":
  etl = MarketingDataETL("marketing_data.csv")
  etl.extract()
  etl.transform()
  etl.store("transformed_marketing_data.csv")
         
         
  
