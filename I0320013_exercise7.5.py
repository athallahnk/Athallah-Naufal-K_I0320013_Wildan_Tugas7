def panggil (func):
    return func
def helloworld():
    return "HELLO WORLD"
def main():
    daftarnama = ["Adi, cahyo, budi, dedi"]
    print("keadaan awal")
    print(daftarnama)

    print("\nmanggunakan sorted():")
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower())

    print("\nkeadaan akhir:")
    print(daftarnama)
if __name__ == '__main__':
    main()
