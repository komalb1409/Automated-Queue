# Import QRCode from pyqrcode 
import qrcode
import datetime
from PIL import Image

class MyClass:
    count=0
def main():
        print("                    ----------------------------------------------")
        print("                              Welcome To Syndicate Bank")
        print("                    ----------------------------------------------")                 
        choice=input("                    Press 1 then Enter to cotinue ")
        print("              Follow the instructions to get your unique token")
        if choice == "1":
                fun()


def fun():
        print("please Enter your details ")
        cname=input("Enter your Name ")
        mno=input("Enter your Mobile Number ")
        ano=input("Enter your Account Number ")
        
        MyClass.count = MyClass.count+1
        
        qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
        )
# Generate QR code
        stg="Your token Number is "+str(MyClass.count)+"\n"+str(cname)+"\n"+str(mno)+"\n"+str(ano)
        qr.add_data(stg)
        img = qr.make_image()

# Create and save the png file naming "image.jpg"
        img.save("image.jpg", scale = 8)
        img=Image.open('image.jpg')
        img.show()

        print("Token issued successfully!!!")
        print("Name-"+cname)
        print("Mobile No.-"+mno)
        print("Account Number-"+ano)
        currentDT = datetime.datetime.now()
        print ("Time:"+str(currentDT))
        main()

# next=input("Press 2 and Enter for next token")
# if next == "2":
main()
