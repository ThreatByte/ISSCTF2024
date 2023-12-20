using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;


/*
 * TODO:
 * Change key
 * Use input instead of commandline arg
 */


class MainReturnValTest
{
    static String Authenticate(string id)
    {
        String val = String.Empty; 
        Aes algo = Aes.Create();
        algo.KeySize = 128;
        algo.Key = new byte[] { 0x23, 0xB6, 0x49, 0xEA, 0x0B, 0x06, 0xAD, 0xBF, 0x61, 0x0f, 0x5D, 0xF3, 0xF0, 0x3D, 0xAF, 0xC3, 0xE2, 0x7A, 0xA4, 0xB7, 0x02, 0x9d, 0xC8, 0x43, 0x93, 0xE9, 0x42, 0xE7, 0xE0, 0xCB, 0xDB, 0x3A };
        algo.IV = new byte[] { 0xC4, 0x90, 0xFD, 0xC4, 0x93, 0xED, 0x36, 0xA4, 0x8A, 0xCD, 0xA2, 0xB1, 0xAB, 0x80, 0x18, 0x6A };

        //Begin Authentication
        try
        {
            byte[] cipherText = ConvertToBytes(id);

            algo.DecryptCbc(cipherText, algo.IV, System.Security.Cryptography.PaddingMode.PKCS7);
            val = "authenticated";
            return val;
        }
        catch (System.Security.Cryptography.CryptographicException e)
        {
            Console.WriteLine(e.Message);
        }
        Console.WriteLine(val);
        return val;
    }


    static byte[] ConvertToBytes(String payload)
    {
        byte[] bytes = payload.Select(c => (byte)c).ToArray();

        return bytes;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Welcome to the Flag Storage Facility. Please enter your 32-character, encrypted, authentication string to access the flag:");
        String result = Authenticate(args[0]);

        if (!String.IsNullOrEmpty(result)){
            Console.WriteLine("Welcome to the Flag Storage Facility!");
            Console.WriteLine("FLAG");
        }
    }
}
