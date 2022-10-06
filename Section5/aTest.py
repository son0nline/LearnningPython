def moobar():
  print("hi")

# thằng nào chạy thì thằng đó tên là __main__
# chỉ chạy đoạn dưới khi chạy file này
# còn nếu import từ file khác thì không chạy
if __name__ == "__main__":
    moobar()

    i = 1000
    print(hash("moobar"))

    for i in range(1,11):
        print(i,end='')

    print()
    a = 1
    b = 2
    print( a, b, 3, sep=';')

    print("name: " , __name__)