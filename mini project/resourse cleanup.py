try:
  f=open("sample.txt", "W")
  f.write("hello python")
except Exception:
  print("error while writing file")
finally:
 f.close()
  print("file closed successfully")