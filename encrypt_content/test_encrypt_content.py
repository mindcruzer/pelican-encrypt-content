import unittest
import base64

from Crypto.Cipher import AES

from encrypt_content import (
    hash_md5, 
    encrypt_text_aes
)


class TestEncryptContent(unittest.TestCase):

    def test_hash_md5(self):
        """
        Verify that md5 hashes are being computed correctly.
        """
        md5_bytes = hash_md5('test')
        self.assertEqual(md5_bytes.encode('hex'), '098f6bcd4621d373cade4e832627b4f6')

    def test_encrypt_text_aes(self):
        """
        Verify that the ciphertext is actually decryptable.

        Note that just because this passes doesn't mean everything is necessarily 
        working, as in production the actual decryption is done in JavaScript.
        """
        text = 'some text to encrypt'
        password = 'agoodpassword'
        
        iv_b64, ciphertext_b64, padding_char = encrypt_text_aes(text, password)
        
        cipher = AES.new(hash_md5(password), AES.MODE_CBC, base64.b64decode(iv_b64))
        plaintext = cipher.decrypt(base64.b64decode(ciphertext_b64))

        self.assertEqual(plaintext.decode('utf-8').rstrip(padding_char), text)
        

if __name__ == "__main__":
    unittest.main()
