
have_money=False

def send():
    print("send money")
    global have_money
    have_money =True
    print(f"have_money={have_money}")
def show():
    if have_money==True:
        print("happy")
    else:
        print("sad")

print(have_money)


if __name__ == '__main__':
    send()
    show()
