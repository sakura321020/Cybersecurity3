from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# ข้อมูลที่ได้รับ
encryption_key = b"wgwjccooybsuqnkoirclzztqhvnpbxef"
iv = b"bdpvsyhxmhztoptp"
ciphertext_base64 = "AZVyFBh3VYKW6FrwAcNIgiD4rZCtsHMo1lW03SZJQRZbTuuYT3sF0CLGgzCAzCBZnowfN/eDVffZ5kVF1pM7ZHwfBlXG6dyr5fPGi12JThKb8dqXQDDzhBD6frZJ385KFC2LnM715UZVJLUk/WdINVJY5pkcdk0n4o5+6uwtS+zQ1gtDdmM1glseGaCq+Q0XVdFvEj8gn61mzbBtY44SxU/zOF30G6CCG4tMg5dNtZAlYSvMfdkTmVuriPo4/IXU+xtjiLEdIuqadFlLA4nWEWgErnFBpVko8rpkmK23IjmwdtxE4oYR9YBwRUiRjZkfI/EF0oGHYzXD69TDMZ7B34tIoxvyeJ56kZOA3XsaNQ8tU+c9bEt1F+SC0rcyoRQF2wb3VhFUEiLyT3QBimWN8nu0bjEQxCEB/Prd1ztHhx4+E9PzSanpUb3p2Gp3pQ6apjS8cL2umwuaJ0zE3PJ4bKfHFVR7Ap6Fi9QOijmbjMcOwq4FasVf79MEhcXnf9S9gL91CgaVAVA09I/TTW8vpOGfvAQu8m8UVn9AjKO8wWh+oWceZab9YRgJeKmkNH0Hkoiipo/MNvnPx/2qRVZsnAvXWFVsU+TQCETJ11ja7+sYIN9IDfuCcElOPh5+VsVBOEgjyO9JJcXqr3zdlwcDaZY6ODdoE5jiDn8Mvn6M4A3x7917G6B6X3xL4zq2J+tzIjkmxvWEIitAonfPXRnjBUOmReCRMz4ez39cOE4HivUHcdNOFaIspk2EcWGuuS3YsWiaitC6mIYuyAzJmaFueDz/vcTzmkk5LOKbrEtsx0hEp58YsJuKleknwubkg4rR"

# แปลง ciphertext จาก base64 เป็น bytes
ciphertext = base64.b64decode(ciphertext_base64)

# สร้าง cipher object ด้วย key และ iv ที่ให้มา
cipher = AES.new(encryption_key, AES.MODE_CBC, iv)

# ถอดรหัสและลบ padding
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

# แปลง plaintext เป็น string
plaintext_str = plaintext.decode('utf-8')

print("ข้อความที่ถอดรหัสได้:", plaintext_str)
