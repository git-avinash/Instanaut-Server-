import colorama
import termcolor2
import socket

colorama.init()


def server_info():
    print(termcolor2.colored("""
#######################################################################################
##                                                                                   ##
##  #### ##    ##  ######  ########    ###    ##    ##    ###    ##     ## ########  ##
##   ##  ###   ## ##    ##    ##      ## ##   ###   ##   ## ##   ##     ##    ##     ##
##   ##  ####  ## ##          ##     ##   ##  ####  ##  ##   ##  ##     ##    ##     ##
##   ##  ## ## ##  ######     ##    ##     ## ## ## ## ##     ## ##     ##    ##     ##
##   ##  ##  ####       ##    ##    ######### ##  #### ######### ##     ##    ##     ##
##   ##  ##   ### ##    ##    ##    ##     ## ##   ### ##     ## ##     ##    ##     ##
##  #### ##    ##  ######     ##    ##     ## ##    ## ##     ##  #######     ##     ##    
##                                                                                   ##
#######################################################################################
""", "yellow"))

    print(termcolor2.colored("""
################################################################################
##                                                                            ##
##   + DEV CONTACTS IF HELP NEEDED                                            ##                             
##    - INSTAGRAM => https://www.instagram.com/_avi.exe/                      ##                                                                                          
##    - GITHUB => https://github.com/git-avinash                              ##                                                                                  
##                                                                            ##                                      
##  + CONTRIBUTE TO INSTANAUT                                                 ##                                                               
##    - SERVER *PYTHON* => https://github.com/git-avinash/Instanaut-Server-   ##                                                                                                             
##    - GUI *DART* => https://github.com/git-avinash/Instanaut-GUI-           ##          
##                                                                            ##               
##  + OPENSOURCE LICENCE                                                      ##                                    
##    Copyright 2020 Avinash S Sah                                            ##                                               
##    SPDX-License-Identifier: Apache-2.0                                     ##                                                      
##                                                                            ##               
################################################################################
""", "blue"))

    print(termcolor2.colored(f"""
- [SERVER VERSION] 1.0.0+2                                         
- [RECOMMENDED APP VERSION] 1.0.0+1 ANDROID & WINDOWS                                        
- [IP] {socket.gethostbyname(socket.gethostname())}     
- [PORT] 5050
""", "green"))

    print(termcolor2.colored("""                       
    SERVER LOGS BELOW    
    *****************                                             
""", "red"))
