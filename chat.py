import requests, getpass, os, time, json
url_daftar = "http://aplitzz.ga/online-chat/api/daftar.php"
url_login = "http://aplitzz.ga/online-chat/api/login.php"
url_daftar_pengguna = "http://aplitzz.ga/online-chat/api/daftar-pengguna.php"
url_chat = "http://aplitzz.ga/online-chat/api/chat.php"
url_insert_chat = "http://aplitzz.ga/online-chat/api/insert-chat.php"

def header(tulisan):
  header = """   _____    _     _
  /  _  \\  / \\   |_|  Online Chat
  | | | | / _ \\  | |  """ + tulisan + """
  | |_| |/ ___ \\ | |
  \\_____/_/   \\_\\|_|  Github : https://github.com/OA-i"""
  return header
  
def menu():
  os.system("clear")
  print(header("Menu"))
  print("\n  " + 40 * "=")
  print("\n  (1) Login\n  (2) Daftar\n  (3) Pengaturan")
  pilih()
  
def pilih():
  cara_login = input("\n  Pilih : ")
  
  if cara_login == "1":
    login()
  elif cara_login == "2":
    daftar()
  elif cara_login == "3":
    pengaturan()
  else:
    print("\n  Pilihan tidak tersedia")
    time.sleep(2)
    os.system("clear")
    menu()

def daftar():
  os.system("clear")
  print(header("Daftar"))
  print("\n  " + 40 * "=")
  username = input("\n  Masukkan username : ")
  password = getpass.getpass("  Masukkan password : ")
  password2 = getpass.getpass("  Masukkan password konfirmasi : ")
  
  if password == password2:
    data_daftar = {"username" : username, "password" : password}
    try:
      req = requests.post(url_daftar, data = data_daftar)
      print(req.text)
    except:
      print("  Kesalahan")
    time.sleep(2)
    menu()
  elif username == "" or password == "" or password2 == "":
    print("  Username atau password tidak boleh kosong")
    time.sleep(2)
    os.system("clear")
    daftar()
  else:
    print("  Password konfirmasi tidak sesuai")
    time.sleep(2)
    os.system("clear")
    daftar()
  
def login():
  os.system("clear")
  print(header("Login"))
  print("\n  " + 40 * "=")
  username = input("\n  Masukkan username : ")
  password = getpass.getpass("  Masukkan password : ")
  
  if username == "" or password == "":
    print("  Username atau password kosong")
    time.sleep(2)
    os.system("clear")
    login()
  else:
    data_login = {"username" : username, "password" : password}
    try:
      req = requests.post(url_login, data = data_login)
    except:
      print("  Kesalahan")
    
    if req.text == "  Gagal Login":
      time.sleep(1.5)
      os.system("clear")
      login()
    else:
      while True:
        os.system("clear")
        print(header("Chat"))
        print("\n  " + 40 * "=")
        try:
          req = requests.post(url_login, data = data_login)
        except:
          print("  Kesalahan")
        print("\n" + req.text)
        pesan = input("  Masukkan Pesan : ")
        if pesan == "/kembali":
          menu()
        else:
          data_insert_chat = {"username" : username, "pesan" : pesan}
          try:
            req = requests.post(url_insert_chat, data = data_insert_chat)
          except:
            print("  Kesalahan")
      
def pengaturan():
  os.system("clear")
  print(header("Pengaturan"))
  print("\n  " + 40 * "=")
  print("\n  (1) Daftar pengguna")
  pilih = input("\n  Pilih : ")
  
  if pilih == "1":
    try:
      req = requests.get(url_daftar_pengguna)
    except:
      print("  Kesalahan")
    print("\n" + req.text)
    input("  Kembali : ")
    menu()
  else:
   print("  Pilihan tidak tersedia")
   time.sleep(1.5)
   os.system("clear")
   pengaturan()
  
if __name__ == "__main__":
  menu()
