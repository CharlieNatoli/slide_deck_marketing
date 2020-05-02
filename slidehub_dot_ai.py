import numpy as np
import os

from authenticate import HorribleGoogleAPIService
from slide_file_utilities import HorribleSlideDeckEditor
from file_sharing import HorribleGoogleDriveHandler
import argparse

# main function. This can be where we create the command line interface

def welcome_banner():
    print( '''
  . ''`   '..' `.'-`..'  -  `.   --' - `  . '.-.-   .`'``..-''  '' .`.`. '. `-. ` -''`..-' . - - `-- -. `.` ``'- . .'.    ` .'.''-.'...   -..  ' `----.-.-`'. `   -.''
  - '' '-'-`--'- ``.~Ttzsft^-'-\zfyyt/-`.` ` --`''[yffyt+-  -`.--. . '-`` '--|fyyttv .  ..-`-` - .--- -   `.     --'-` .'  ''-.``..-  - -'` '.` csyztz+  ` .''.`  ..''
--'"y2*]uujnJjt< ``'^OBHRHW+.'-FRQHHWs  .-.  -'.  ERBgQQv`-`''``-''.- `..``.`tBggWQu`-  `` .. . ..'-`- .!fFnnJt`  '.iJj2uu?' `` ` `-  .`. -'.. `dBHHWQ). `. `'  ` ` -`
-*$HQH[$BWgWBWQDV<'.,MQggQg+. .=[c7x7= '' `.-` ` -wRBgHgv.--  `-- `  -`-  --`yRgWBQC`.` - -  . ` --.`-'`*&gRggD.- .`VWBQRRy'--`` '..-'.``-'-`  `bHggWg| ..-'.' . .-`-'
vRHRWgi_^:^,U@N@D$ -:OWgHgR> -'lSPES67-''`(ZEEhE6=9gQHHgv`.'."FA%+a9E9h#;`-- fRQQHRo`-v%PP%wT  ' zA6hSX+rDHWBW@`'   agQBQBz .T6AAAw{`..FEP9%E<  KHgBWB(_twEPa"` `..'.'
7QRHRguiviiii]i~~ - !MgBHRg>'' uWgHBQy--/%WHBgHBR|hHRHQRv` =4HRQR*OHQHWBg4=` sgQWBHC-``kQWgR&)' }HBRHgy "NRHRQ&. -` 4WRBBWy'-aRgRWBf  ~bRQHWQ?'.dWggQQ(PWBRgggXr . ' -
>$ggRRBgBBWQWRHMf~. ,OgHWRg<`-`jHWHggz 'PggRRQ}~_`%gRRWgi-~MBgHHQr_~^$QQHHO' fBHgBHu``-:URQQWU:"DHBRBk.`*NBBBg&rMN&&WRRQHHy `IWWRBgt`'_qBggWg\'-qWQHWg\^:*&RgHH@'-` .'
..;4&@@&&NNDgHgHWD"-:ORRWgB> . nRBHBgf`'AQHRBQi '.hgBQgRi`~OgRBHQr5GqDggHW&' tgHBgg2'--`=OQWQN*qQBWWm!.`"@WQRQ&>59S6DWHQHRs'.aRggBRy`'^dBHRQW\`'8BHgRW).`+&HBgg& -`' .
_ivvv{)^^~:~MgWWBg/.~OgRRgH<---CBgggWt` 6HRgRQi'`'PWgBgBv'^MQgHRW"l1Y1TT11}`-fWQgQHF'-``-|&HR[$BgRBN=` `;DRHgBD   ' ugggBWy` eHHHgHz  ,pWWRWH\``GWBBQB? `<&RgHQ&`-. '-
?&gWRHd?|/r^UBWgQO; ,bBQBQWf1i'JQQBgHz''kWBBgHjvv_6HgQWBv`-ERBWQg=(vivivii! '7RHQQQh1c>-'`TQFfBQQHW[ . -*NHgQRN- --.JBHQBgs.-YWQBRWXY7+qQBQRW(. 0RRQQg/*i}QgRBR9   . .
 <XQgHHBWRg*UgBO1^..`!TMRBHRRp_jHBBWQf`  cGHWRQBD;EHRWQHv'.-iAggB;OHWHQRWm<- -;XHHRBQRv``` cv&HWBBC-` --r@WQQQN  ` -nWgBBWs'.->2&BHgH8>bBBBgB/ 'GRgQQH?ERWgBHPv   `-'`
 .'|{LllcLv,i]i_.-' .-''i{c77v-;x]lL{*'` - |L7[v^`|7{[}[<`.-.-?[v,vl7}7L)`-   -'"]7}{[>.' `+MQQWg%^.'' .^vxc7ci`-'  "x][xL*- `.'<i[c|`'v7Lx}]_. i]L{cL!(L{cx| '.   - -
 .-- -`'  . ''`'' .  .' -` .  . .  '.    `.- .`-'`' `'.'`-.-. -''-. '- -'  `    - . '-.''-_AgWHR@>' `  -'`  .. '   ``'`--  '  '`.`'`  ` .- .  . .-'..-`''.` ' - -.  ''
 - ```- .'`'.-`-'`- -`'    `'-```--`.- '`'```.'.  - ' .    `.'-- .``'`.'         -`-`  '  {mpqp0\-'-.`  `- -  .-`  `` - '' `' .---  . -'-''.''-   '  ' -'``-` . ` .- .
 ...-   `- ``'' .  ' '`-   '``-.-..'-. ` .'-  `''``  ` '`'` .' -  . ``'...-. .  .`-``'`` - -'
.-`` ..`-.-'.*ftytf{ ' '`   ``-'-''` .`. -''-''  `'  '' ` --  -. -` -'' `''  ` - ` -` `.- `.-
 .  . `'' '  }QRRQHP  ` '`' .-`-- '   -''... +v}`  .`' -- .'-`-  ''"jCnjCi' ..  . TjJuuJJ2j1-
 -.'...-. ' '7BggWgh'-.-'.`  ' -. '`. '`.,IGDQWq^` '`   -- '`.'` .3vZBQBHD\-` - .~OgHBRWQQQM-
'.- .,yEP9P6zxHRggQE-''`!Y9w%ErowA%er`` (pRBBRBG<A9%! - `-''-.'--1gO"MQgBBM>- '.' ?1@BRQQ&T? 
'  :z&RgggRW5LRQRgWw-'~1MWQQQW\wRWBgB4*'xHHHHgRK"gHW> .-. ' - ``(@BBw)@RRgB0_`.` .`>NgHQQN+. 
 --vRBRHgh,:`}QRHQWA''yWBBWR$_ ~iBQQWHO_-/gRHgQm^!^^'   -'- .` _OHRBHv[BBBHge.-'.  >NHHBB@>'-
 .'iRQQQBh ' {QBRWB6` fWRQRRV '.)WRggBM~'*BBHQgb!.'.-.-  `-  '^kQWHBE' sRgQQQz -'  <@BBBgD> '
`` vBQggQw `-cgBHRQ9 .sQBBWWa--`)gBQRgO:`=HQgRQb,.  ---  ...  tQWBRN;]{1@gQQQQv''- +@RBHgD>- 
`.`(WWWgWOvv*[WHHWBh` iNQgBWPv:;fWWWHHZ  <MgBgg@1TYi'. ''`   vRHWgWTngBgRWWQgWNr  TegWgHQB#Y'
.-  =aHBQHHQn[QQBWgA-` >n@QggQ|0WgWWAi.'-`,xMWQQRQQO'. -` . <@HRQg5!L]x7[T&WBWHM>~OWHggRRBHO 
'.. --<l[}lr >Lc{cl(`--' !v{}[_?l[7?-. `- '. i7[}{cv-'.-..  ;lc{lL,`- .'. *7[c7[* ix[cc[}{{v 
--'`'` '`'-  '`-.' ` ' -`.  `-  -  .  .   - `..  '  '`.. ` .' `. .-` `  ``- '"'  .  .  - .  .
'`   .   ..  -'.    .  .--  ' .'-'  '`'`' -`  `..- '    '...  - '-.--` -.  ..  '- - .. -  . .
''')
DATABASE_FILE_NAME = 'database.txt'

DATABASE_FILE_PATH = os.path.join(os.getcwd(), DATABASE_FILE_NAME)

def get_emails():
    email_list = input('Please enter a list of contacts that you wish to delight: ')
    email_list = email_list.split(',')
    return [x.strip() for x in email_list]

def get_user_input():
    email_list = get_emails()
    message_text = input('Now, please enter what it is that your contacts must know: ')
    return email_list, message_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The best marketing tool')
    parser.add_argument('--num-shapes', type=int, help='How many shapes do you want?')

    welcome_banner()

    if not os.path.exists(DATABASE_FILE_PATH):
        with open(DATABASE_FILE_NAME, 'w') as fp:
            pass

    email_list, message_text = get_user_input()

    api_service = HorribleGoogleAPIService()

    slide_deck_editor = HorribleSlideDeckEditor(api_service)
    google_drive_handler = HorribleGoogleDriveHandler(api_service)

    deck_info = slide_deck_editor.create_slide_deck()

    print('Hacking into google...')
    import time
    time.sleep(2)
    print('Access granted!')

    requests = []
    requests.extend(slide_deck_editor.add_background(deck_info))
    for i in range(30):
        requests.extend(slide_deck_editor.add_random_shape(deck_info))
    requests.extend(slide_deck_editor.create_text_box(deck_info, message_text))
    slide_deck_editor.update_all(deck_info, requests)

    for email in email_list:
        google_drive_handler.share_file(deck_info['presentationId'], email)

    with open(DATABASE_FILE_NAME, 'a') as fp:
        fp.write(deck_info['presentationId'] + ',')
