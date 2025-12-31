import rsa
public_key,privet_key= rsa.newkeys(512)
print("publif_key",public_key)
print("privet_key",privet_key)

messege="pryank"

encrypted= rsa.encrypt(messege.encode(),public_key)
decrypted=rsa.decrypt(encrypted,privet_key).decode()
print("encrypted=",encrypted)
print("decrypted=",decrypted)