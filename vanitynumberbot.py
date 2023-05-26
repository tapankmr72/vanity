import time
import re
import datetime
from datetime import date, timedelta, datetime
from datetime import datetime, timedelta
import streamlit as st
mite = time.time()
print(mite)
# give a title to our app
st.title('Welcome to Vanity number Valuation')
regex = "[6-9]{1}[0-9]{9}"
p = re.compile(regex)
mobile1=""

mobile1 = st.text_input('Please enter 10 digit mobile number: ', key=1)
mobile = "0000000000"
if mobile1!="":
    mobile=mobile1
i3s = 8.53248
i4s = 7.840062721
i5s = 7.19999424
i6s = 5
i7s = 3.2
i8s = 2.40000018
i9s = 1.6
i10s = 1

i2r = 9
i3r = 8
i4r = 7
i5r = 6
i6r = 5
i7r = 4
i8r = 3
i9r = 2
i10r = 1

# declare variables
for i in range(1000):
    globals()[f'p{i}'] = ""

list1 = ["9999999999",
         "8888888888",
         "7777777777",
         "6666666666"]
l1 = 0
length1 = len(list1)

list2 = ["000000000",
         "111111111",
         "222222222",
         "333333333",
         "444444444",
         "555555555",
         "666666666",
         "777777777",
         "888888888",
         "999999999"]
l2 = 0
length2 = len(list2)

list3 = ["00000000",
         "11111111",
         "22222222",
         "33333333",
         "44444444",
         "55555555",
         "66666666",
         "77777777",
         "88888888",
         "99999999"]

l3 = 0
length3 = len(list3)

list4 = ["0000000",
         "1111111",
         "2222222",
         "3333333",
         "4444444",
         "5555555",
         "6666666",
         "7777777",
         "8888888",
         "9999999"]

l4 = 0
length4 = len(list4)

list5 = ["000000",
         "111111",
         "222222",
         "333333",
         "444444",
         "555555",
         "666666",
         "777777",
         "888888",
         "999999"]
l5 = 0
length5 = len(list5)

list6 = ["00000", "11111", "22222", "33333", "44444", "55555", "66666", "77777", "88888", "99999"]
l6 = 0
length6 = len(list6)

list7 = ["0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999"]
l7 = 0
length7 = len(list7)

list8 = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
l8 = 0
length8 = len(list8)

list9 = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
l9 = 0
length9 = len(list9)

list10 = ["9876543210"]
l10 = 0
length10 = len(list10)

list11 = ["987654321",
          "876543210",
          "123456789",
          "012345678"]
l11 = 0
length11 = len(list11)

list12 = ["98765432",
          "87654321",
          "76543210",
          "01234567",
          "12345678",
          "23456789"]
l12 = 0
length12 = len(list12)

list13 = ["9876543",
          "8765432",
          "7654321",
          "6543210",
          "0123456",
          "1234567",
          "2345678",
          "3456789"]

l13 = 0
length13 = len(list13)

list14 = ["987654",
          "876543",
          "765432",
          "654321",
          "543210",
          "012345",
          "123456",
          "234567",
          "345678",
          "456789"]
l14 = 0
length14 = len(list14)

list15 = ["98765",
          "87654",
          "76543",
          "65432",
          "54321",
          "43210",
          "01234",
          "12345",
          "23456",
          "34567",
          "45678",
          "56789"]
l15 = 0
length15 = len(list15)

list16 = ["9876",
          "8765",
          "7654",
          "6543",
          "5432",
          "4321",
          "3210",
          "0123",
          "1234",
          "2345",
          "3456",
          "4567",
          "5678",
          "6789"]
l16 = 0
length16 = len(list16)

list17 = ["987",
          "876",
          "765",
          "654",
          "543",
          "432",
          "321",
          "210",
          "012",
          "123",
          "234",
          "345",
          "456",
          "567",
          "678",
          "789"]
l17 = 0
length17 = len(list17)

list18 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

l18 = 0
length18 = len(list18)

list19 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "12", "13", "14", "15", "16", "17", "18", "19",
          "20",
          "21", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "34", "35", "36", "37", "38", "39", "40",
          "41",
          "42", "43", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "56", "57", "58", "59", "60", "61",
          "62",
          "63", "64", "65", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "78", "79", "80", "81", "82",
          "83", "84", "85", "86", "87", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98"]
l19 = 0
length19 = len(list19)
g = 0
while g == 0:
    print("==========================================================")

    count = 0
    text = ""
    plus1 = ""
    minus1 = ""
    plus2 = ""
    minus2 = ""
    plus3 = ""
    minus3 = ""
    plus4 = ""
    minus4 = ""
    plus5 = ""
    minus5 = ""
    plus10 = ""
    minus10 = ""
    temp0 = ""
    temp1 = ""
    temp2 = ""
    temp3 = ""
    temp4 = ""
    temp5 = ""
    temp6 = ""
    temp7 = ""
    temp8 = ""
    temp9 = ""
    temp10 = ""
    temp11 = ""
    temp12 = ""

    while count < 100:
        ab = str(count)
        if len(ab) == 1:
            text = "0" + ab
        if len(ab) == 2:
            text = ab
            asc = text
        loc = mobile.find(text)
        if loc != -1:
            loc2 = mobile[loc + 2:10].find(text)
            text1 = int(text) + 1
            text2 = int(text) - 1
            text3 = int(text) + 2
            text4 = int(text) - 2
            text5 = int(text) + 3
            text6 = int(text) - 3
            text7 = int(text) + 4
            text8 = int(text) - 4
            text9 = int(text) + 5
            text10 = int(text) - 5
            text11 = int(text) + 6
            text12 = int(text) - 6
            text13 = int(text) + 7
            text14 = int(text) - 7
            text15 = int(text) + 8
            text16 = int(text) - 8
            text17 = int(text) + 9
            text18 = int(text) - 9
            text19 = int(text) + 10
            text20 = int(text) - 10

            text1 = str(text1)
            if len(text1) == 1:
                text1 = "0" + text1
            text2 = str(text2)
            if len(text2) == 1:
                text2 = "0" + text2
            text3 = str(text3)
            if len(text3) == 1:
                text3 = "0" + text3
            text4 = str(text4)
            if len(text4) == 1:
                text4 = "0" + text4
            text5 = str(text5)
            if len(text5) == 1:
                text5 = "0" + text5
            text6 = str(text6)
            if len(text6) == 1:
                text6 = "0" + text6
            text7 = str(text7)
            if len(text7) == 1:
                text7 = "0" + text7
            text8 = str(text8)
            if len(text8) == 1:
                text8 = "0" + text8
            text9 = str(text9)
            if len(text9) == 1:
                text9 = "0" + text9
            text10 = str(text10)
            if len(text10) == 1:
                text10 = "0" + text10
            text11 = str(text11)
            if len(text11) == 1:
                text11 = "0" + text11
            text12 = str(text12)
            if len(text12) == 1:
                text12 = "0" + text12
            text13 = str(text13)
            if len(text13) == 1:
                text13 = "0" + text13
            text14 = str(text14)
            if len(text14) == 1:
                text14 = "0" + text14
            text15 = str(text15)
            if len(text15) == 1:
                text15 = "0" + text15
            text16 = str(text16)
            if len(text16) == 1:
                text16 = "0" + text16
            text17 = str(text17)
            if len(text17) == 1:
                text17 = "0" + text17
            text18 = str(text18)
            if len(text18) == 1:
                text18 = "0" + text18
            text19 = str(text19)
            if len(text19) == 1:
                text19 = "0" + text19
            text20 = str(text20)
            if len(text20) == 1:
                text20 = "0" + text20

            loc2a = mobile[loc + 2:10].find(text1)
            loc2b = mobile[loc + 2:10].find(text2)
            loc2c = mobile[loc + 2:10].find(text3)
            loc2d = mobile[loc + 2:10].find(text4)
            loc2e = mobile[loc + 2:10].find(text5)
            loc2f = mobile[loc + 2:10].find(text6)
            loc2g = mobile[loc + 2:10].find(text7)
            loc2h = mobile[loc + 2:10].find(text8)
            loc2i = mobile[loc + 2:10].find(text9)
            loc2j = mobile[loc + 2:10].find(text10)
            loc2k = mobile[loc + 2:10].find(text11)
            loc2l = mobile[loc + 2:10].find(text12)
            loc2m = mobile[loc + 2:10].find(text13)
            loc2n = mobile[loc + 2:10].find(text14)
            loc2o = mobile[loc + 2:10].find(text15)
            loc2p = mobile[loc + 2:10].find(text16)
            loc2q = mobile[loc + 2:10].find(text17)
            loc2r = mobile[loc + 2:10].find(text18)
            loc2s = mobile[loc + 2:10].find(text19)
            loc2t = mobile[loc + 2:10].find(text20)

            if loc2a != -1 and int(text1) <= 99:

                plus1 = "4 digit - 2 digit ascending(+1) no. 2 times found "

                text1a = int(text1) + 1
                text1a = str(text1a)
                if len(text1a) == 1:
                    text1a = "0" + text1a
                loc3a = mobile[loc + 2 + loc2a + 2:10].find(text1a)
                if loc3a != -1 and int(text1a) <= 99:

                    plus1 = "6 digit - 2 digit ascending(+1) no. 3 times found "
                    temp1 = "6 digit - 2 digit ascending(+1) no. 3 times found "
                    text1b = int(text1a) + 1
                    text1b = str(text1b)
                    if len(text1b) == 1:
                        text1b = "0" + text1b
                    loc4a = mobile[loc + 2 + loc2a + 2 + loc3a + 2:10].find(text1b)

                    if loc4a != -1 and int(text1b) <= 99:
                        plus1 = "8 digit - 2 digit ascending(+1) no. 4 times found"

                        temp2 = "8 digit - 2 digit ascending(+1) no. 4 times found"
                        text1c = int(text1b) + 1
                        text1c = str(text1c)
                        if len(text1c) == 1:
                            text1c = "0" + text1c
                        loc5a = mobile[loc + 2 + loc2a + 2 + loc3a + 2 + loc4a + 2:10].find(text1c)
                        if loc5a != -1 and int(text1c) <= 99:
                            plus1 = "10 digit- 2 digit ascending(+1) no. 5 times found "

                            break
            if loc2b != -1:
                minus1 = "4 digit - 2 digit descending(-1) no. 2 times found"
                text2a = int(text2) - 1
                text2a = str(text2a)
                if len(text2a) == 1:
                    text2a = "0" + text2a
                loc3b = mobile[loc + 2 + loc2b + 2:10].find(text2a)
                if loc3b != -1:

                    minus1 = "6 digit - 2 digit descending(-1) no. 3 times found "
                    text2b = int(text2a) - 1
                    text2b = str(text2b)
                    if len(text2b) == 1:
                        text2b = "0" + text2b
                    loc4b = mobile[loc + 2 + loc2b + 2 + loc3b + 2:10].find(text2b)
                    if loc4b != -1:

                        minus1 = "8 digit - 2 digit descending(-1) no. 4 times found "

                        text2c = int(text2b) - 1
                        text2c = str(text2c)
                        if len(text2c) == 1:
                            text2c = "0" + text2c
                        loc5b = mobile[loc + 2 + loc2b + 2 + loc3b + 2 + loc4b + 2:10].find(text2c)
                        if loc5b != -1:
                            minus1 = "10 digit- 2 digit descending(-1) no. 5 times found "

                            break
            if loc2c != -1 and int(text3) <= 99:

                plus2 = "4 digit - 2 digit ascending(+2) no. 2 times  found "
                text3a = int(text3) + 2
                text3a = str(text3a)
                if len(text3a) == 1:
                    text3a = "0" + text3a
                loc3c = mobile[loc + 2 + loc2c + 2:10].find(text3a)
                if loc3c != -1 and int(text3a) <= 99:

                    plus2 = "6 digit - 2 digit ascending(+2) no. 3 times found "
                    temp3 = "6 digit - 2 digit ascending(+2) no. 3 times found "
                    text3b = int(text3a) + 2
                    text3b = str(text3b)
                    if len(text3b) == 1:
                        text3b = "0" + text3b
                    loc4c = mobile[loc + 2 + loc2c + 2 + loc3c + 2:10].find(text3b)
                    if loc4c != -1 and int(text3b) <= 99:
                        plus2 = "8 digit - 2 digit ascending(+2) no. 4 times found "
                        temp4 = "8 digit - 2 digit ascending(+2) no. 4 times found "
                        text3c = int(text3b) + 2
                        text3c = str(text3c)
                        if len(text3c) == 1:
                            text3c = "0" + text3c
                        loc5c = mobile[loc + 2 + loc2c + 2 + loc3c + 2 + loc4c + 2:10].find(text3c)
                        if loc5c != -1 and int(text3c) <= 99:
                            plus2 = "10 digit- 2 digit ascending(+2) no. 5 times found "
                            break
            if loc2d != -1:
                minus2 = "4 digit - 2 digit descending(-2) no. 2 times found "

                text4a = int(text4) - 2
                text4a = str(text4a)
                if len(text4a) == 1:
                    text4a = "0" + text4a
                loc3d = mobile[loc + 2 + loc2d + 2:10].find(text4a)
                if loc3d != -1:
                    minus2 = "6 digit - 2 digit descending(-2) no. 3 times found "
                    text4b = int(text4a) - 2
                    text4b = str(text4b)
                    if len(text4b) == 1:
                        text4b = "0" + text4b
                    loc4d = mobile[loc + 2 + loc2d + 2 + loc3d + 2:10].find(text4b)
                    if loc4d != -1:
                        minus2 = "8 digit - 2 digit descending(-2) no. 4 times found "

                        text4c = int(text4b) - 2
                        text4c = str(text4c)
                        if len(text4c) == 1:
                            text4c = "0" + text4c
                        loc5d = mobile[loc + 2 + loc2d + 2 + loc3d + 2 + loc4d + 2:10].find(text4c)
                        if loc5d != -1:
                            minus2 = "10 digit - 2 digit descending(-2) no. 5 times found "
                            break
            if loc2e != -1 and int(text5) <= 99:
                plus3 = "4 digit - 2 digit ascending(+3) no. 2 times found "
                text5a = int(text5) + 3
                text5a = str(text5a)
                if len(text5a) == 1:
                    text5a = "0" + text5a
                loc3e = mobile[loc + 2 + loc2e + 2:10].find(text5a)
                if loc3e != -1 and int(text5a) <= 99:
                    plus3 = "6 digit - 2 digit ascending(+3) no. 3 times found "
                    temp5 = "6 digit - 2 digit ascending(+3) no. 3 times found "
                    text5b = int(text5a) + 3
                    text5b = str(text5b)
                    if len(text5b) == 1:
                        text5b = "0" + text5b
                    loc4e = mobile[loc + 2 + loc2e + 2 + loc3e + 2:10].find(text5b)
                    if loc4e != -1 and int(text5b) <= 99:
                        plus3 = "8 digit - 2 digit ascending(+3) no. 4 times found "
                        temp6 = "8 digit - 2 digit ascending(+3) no. 4 times found "
                        text5c = int(text5b) + 3
                        text5c = str(text5c)
                        if len(text5c) == 1:
                            text5c = "0" + text5c
                        loc5e = mobile[loc + 2 + loc2e + 2 + loc3e + 2 + loc4e + 2:10].find(text5c)
                        if loc5e != -1 and int(text5c) <= 99:
                            plus3 = "10 digit- 2 digit ascending(+3) no. 5 times found "
                            break
            if loc2f != -1:
                minus3 = "4 digit - 2 digit descending(-3) no. 2 times found "
                text6a = int(text6) - 3
                text6a = str(text6a)
                if len(text6a) == 1:
                    text6a = "0" + text6a
                loc3f = mobile[loc + 2 + loc2f + 2:10].find(text6a)
                if loc3f != -1:
                    minus3 = "6 digit - 2 digit descending(-3) no. 3 times found "
                    text6b = int(text6a) - 3
                    text6b = str(text6b)
                    if len(text6b) == 1:
                        text6b = "0" + text6b
                    loc4f = mobile[loc + 2 + loc2f + 2 + loc3f + 2:10].find(text6b)
                    if loc4f != -1:
                        minus3 = "8 digit - 2 digit descending(-3) no. 4 times found "

                        text6c = int(text6b) - 3
                        text6c = str(text6c)
                        if len(text6c) == 1:
                            text6c = "0" + text6c
                        loc5f = mobile[loc + 2 + loc2f + 2 + loc3f + 2 + loc4f + 2:10].find(text6c)
                        if loc5f != -1:
                            minus3 = "10 digit - 2 digit descending(-3) no. 5 times found "
                            break
            if loc2g != -1 and int(text7) <= 99:
                plus4 = "4 digit - 2 digit ascending(+4) no. 2 times found "
                text7a = int(text7) + 4
                text7a = str(text7a)
                if len(text7a) == 1:
                    text7a = "0" + text7a
                loc3g = mobile[loc + 2 + loc2g + 2:10].find(text7a)
                if loc3g != -1 and int(text7a) <= 99:
                    plus4 = "6 digit - 2 digit ascending(+4) no. 3 times found "
                    temp7 = "6 digit - 2 digit ascending(+4) no. 3 times found "
                    text7b = int(text7a) + 4
                    text7b = str(text7b)
                    if len(text7b) == 1:
                        text7b = "0" + text7b
                    loc4g = mobile[loc + 2 + loc2g + 2 + loc3g + 2:10].find(text7b)
                    if loc4g != -1 and int(text7b) <= 99:
                        plus4 = "8 digit - 2 digit ascending(+4) no. 4 times found "
                        temp8 = "8 digit - 2 digit ascending(+4) no. 4 times found "
                        text7c = int(text7b) + 4
                        text7c = str(text7c)
                        if len(text7c) == 1:
                            text7c = "0" + text7c
                        loc5g = mobile[loc + 2 + loc2g + 2 + loc3g + 2 + loc4g + 2:10].find(text7c)
                        if loc5g != -1 and int(text7c) <= 99:
                            plus4 = "10 digit- 2 digit ascending(+4) no. 5 times found "
                            break
            if loc2h != -1:
                minus4 = "4 digit - 2 digit descending no. 2 times -4 found "
                text8a = int(text8) - 4
                text8a = str(text8a)
                if len(text8a) == 1:
                    text8a = "0" + text8a
                loc3h = mobile[loc + 2 + loc2h + 2:10].find(text8a)
                if loc3h != -1:
                    minus4 = "6 digit - 2 digit descending(-4) no. 3 times found "
                    text8b = int(text8a) - 4
                    text8b = str(text8b)
                    if len(text8b) == 1:
                        text8b = "0" + text8b
                    loc4h = mobile[loc + 2 + loc2h + 2 + loc3h + 2:10].find(text8b)
                    if loc4h != -1:
                        minus4 = "8 digit - 2 digit descending(-4) no. 4 times found "

                        text8c = int(text8b) - 4
                        text8c = str(text8c)
                        if len(text8c) == 1:
                            text8c = "0" + text8c
                        loc5h = mobile[loc + 2 + loc2h + 2 + loc3h + 2 + loc4h + 2:10].find(text8c)
                        if loc5h != -1:
                            minus4 = "10 digit - 2 digit descending(-4) no. 5 times found "
                            break
            if loc2i != -1 and int(text9) <= 99:
                plus5 = "4 digit - 2 digit ascending(+5) no. 2 times found"
                text9a = int(text9) + 5
                text9a = str(text9a)
                if len(text9a) == 1:
                    text9a = "0" + text9a
                loc3i = mobile[loc + 2 + loc2i + 2:10].find(text9a)
                if loc3i != -1 and int(text9a) <= 99:
                    plus5 = "6 digit - 2 digit ascending(+5) no. 3 times found "
                    temp9 = "6 digit - 2 digit ascending(+5) no. 3 times found "
                    text9b = int(text9a) + 5
                    text9b = str(text9b)
                    if len(text9b) == 1:
                        text9b = "0" + text9b
                    loc4i = mobile[loc + 2 + loc2i + 2 + loc3i + 2:10].find(text9b)
                    if loc4i != -1 and int(text9b) <= 99:
                        plus5 = "8 digit - 2 digit ascending(+5) no. 4 times found "
                        temp10 = "8 digit - 2 digit ascending(+5) no. 4 times found "
                        text9c = int(text9b) + 5
                        text9c = str(text9c)
                        if len(text9c) == 1:
                            text9c = "0" + text9c
                        loc5i = mobile[loc + 2 + loc2i + 2 + loc3i + 2 + loc4i + 2:10].find(text9c)
                        if loc5i != -1 and int(text9c) <= 99:
                            plus5 = "10 digit- 2 digit ascending(+5) no. 5 times found "
                            break
            if loc2j != -1:
                minus5 = "4 digit - 2 digit descending(-5) no. 2 times found "
                text10a = int(text10) - 5
                text10a = str(text10a)
                if len(text10a) == 1:
                    text10a = "0" + text10a
                loc3j = mobile[loc + 2 + loc2j + 2:10].find(text10a)
                if loc3j != -1:
                    minus5 = "6 digit - 2 digit descending(-5) no. 3 times found "
                    text10b = int(text10a) - 5
                    text10b = str(text10b)
                    if len(text10b) == 1:
                        text10b = "0" + text10b
                    loc4j = mobile[loc + 2 + loc2j + 2 + loc3j + 2:10].find(text10b)
                    if loc4j != -1:
                        minus5 = "8 digit - 2 digit descending(-5) no. 4 times found "

                        text10c = int(text10b) - 5
                        text10c = str(text10c)
                        if len(text10c) == 1:
                            text10c = "0" + text10c
                        loc5j = mobile[loc + 2 + loc2j + 2 + loc3j + 2 + loc4j + 2:10].find(text10c)
                        if loc5j != -1:
                            minus5 = "10 digit - 2 digit descending(-5) no. 5 times found "
                            break
            if loc2s != -1 and int(text19) <= 99:
                plus10 = "4 digit - 2 digit ascending(+10) no. 2 times found "

                text19a = int(text19) + 10
                text19a = str(text19a)
                if len(text19a) == 1:
                    text19a = "0" + text19a
                loc3s = mobile[loc + 2 + loc2s + 2:10].find(text19a)
                if loc3s != -1 and int(text19a) <= 99:
                    plus10 = "6 digit - 2 digit ascending(+10) no. 3 times found "
                    temp11 = "6 digit - 2 digit ascending(+10) no. 3 times found "
                    text19b = int(text19a) + 10
                    text19b = str(text19b)
                    if len(text19b) == 1:
                        text19b = "0" + text19b
                    loc4s = mobile[loc + 2 + loc2s + 2 + loc3s + 2:10].find(text19b)
                    if loc4s != -1 and int(text19b) <= 99:
                        plus10 = "8 digit - 2 digit ascending(+10) no. 4 times found "
                        temp12 = "8 digit - 2 digit ascending(+10) no. 4 times found "
                        text19c = int(text19b) + 10
                        text19c = str(text19c)
                        if len(text19c) == 1:
                            text19c = "0" + text19c
                        loc5s = mobile[loc + 2 + loc2s + 2 + loc3s + 2 + loc4s + 2:10].find(text19c)
                        if loc5s != -1 and int(text19c) <= 99:
                            plus10 = "10 digit- 2 digit ascending(+10) no. 5 times found "
                            break
            if loc2t != -1:
                minus10 = "4 digit - 2 digit descending(-10) no. 2 times found "

                text20a = int(text20) - 10
                text20a = str(text20a)
                if len(text20a) == 1:
                    text20a = "0" + text20a
                loc3t = mobile[loc + 2 + loc2t + 2:10].find(text20a)
                if loc3t != -1:
                    minus10 = "6 digit - 2 digit descending(-10) no. 3 times found "
                    text20b = int(text20a) - 10
                    text20b = str(text20b)
                    if len(text20b) == 1:
                        text20b = "0" + text20b
                    loc4t = mobile[loc + 2 + loc2t + 2 + loc3t + 2:10].find(text20b)
                    if loc4t != -1:
                        minus10 = "8 digit - 2 digit descending(-10) no. 4 times found "

                        text20c = int(text20b) - 10
                        text20c = str(text20c)
                        if len(text20c) == 1:
                            text20c = "0" + text20c
                        loc5t = mobile[loc + 2 + loc2t + 2 + loc3t + 2 + loc4t + 2:10].find(text20c)
                        if loc5t != -1:
                            minus10 = "10 digit - 2 digit descending(-10) no. 5 times found "
                            break

        count = count + 1
    if plus1 != "":
        t1 = int(plus1[36:37])

        t2 = (temp1[36:37])
        if t2 == "":
            t2 = int(0)
        else:
            t2 = int(temp1[36:37])
        t3 = (temp2[36:37])
        if t3 == "":
            t3 = int(0)
        else:
            t3 = int(temp2[36:37])
        if t3 > t1 and t3 > t2:
            plus1 = temp2
        if t2 > t1 and t2 > t3:
            plus1 = temp1

        t1 = 0
        t2 = 0
        t3 = 0
    if plus2 != "":
        t1 = int(plus2[36:37])
        t2 = (temp3[36:37])
        if t2 == "":
            t2 = int(0)
        else:
            t2 = int(temp3[36:37])
        t3 = (temp4[36:37])
        if t3 == "":
            t3 = int(0)
        else:
            t3 = int(temp4[36:37])
        if t3 > t1 and t3 > t2:
            plus2 = temp4
        if t2 > t1 and t2 > t3:
            plus2 = temp3

        t1 = 0
        t2 = 0
        t3 = 0

    if plus3 != "":
        t1 = int(plus3[36:37])
        t2 = (temp5[36:37])
        if t2 == "":
            t2 = int(0)
        else:
            t2 = int(temp5[36:37])
        t3 = (temp6[36:37])
        if t3 == "":
            t3 = int(0)
        else:
            t3 = int(temp6[36:37])
        if t3 > t1 and t3 > t2:
            plus3 = temp6
        if t2 > t1 and t2 > t3:
            plus3 = temp5

        t1 = 0
        t2 = 0
        t3 = 0

    if plus4 != "":
        t1 = int(plus4[36:37])
        t2 = (temp7[36:37])
        if t2 == "":
            t2 = int(0)
        else:
            t2 = int(temp7[36:37])
        t3 = (temp8[36:37])
        if t3 == "":
            t3 = int(0)
        else:
            t3 = int(temp8[36:37])
        if t3 > t1 and t3 > t2:
            plus4 = temp8
        if t2 > t1 and t2 > t3:
            plus4 = temp7

        t1 = 0
        t2 = 0
        t3 = 0

    if plus5 != "":
        t1 = int(plus5[36:37])
        t2 = (temp9[36:37])
        if t2 == "":
            t2 = int(0)
        else:
            t2 = int(temp9[36:37])
        t3 = (temp10[36:37])
        if t3 == "":
            t3 = int(0)
        else:
            t3 = int(temp10[36:37])
        if t3 > t1 and t3 > t2:
            plus5 = temp10
        if t2 > t1 and t2 > t3:
            plus5 = temp9

        t1 = 0
        t2 = 0
        t3 = 0

    if plus10 != "":
        t1 = int(plus10[37:38])
        t2 = (temp11[37:38])
        if t2 == "":
            t2 = int(0)
        else:
            t2 = int(temp11[37:38])
        t3 = (temp12[37:38])
        if t3 == "":
            t3 = int(0)
        else:
            t3 = int(temp12[37:38])
        if t3 > t1 and t3 > t2:
            plus10 = temp12
        if t2 > t1 and t2 > t3:
            plus10 = temp11

        t1 = 0
        t2 = 0
        t3 = 0


    total = int(mobile[0:1]) + int(mobile[1:2]) + int(mobile[2:3]) + int(mobile[3:4]) + int(mobile[4:5]) + int(mobile[5:6]) + int(mobile[6:7]) + int(mobile[7:8]) + int(mobile[8:9]) + int(mobile[9:10])
    total = str(total)

    if len(total) == 1:
        total = int(total)
    else:
        total = int(total[0:1]) + int(total[1:2])
        total = str(total)
        if len(total) == 1:
            total = int(total)
        else:
            total = int(total[0:1]) + int(total[1:2])

    # extracting single digits from mobile no.
    result1p0 = ""
    result1p1 = ""
    result1p2 = ""
    result1p3 = ""
    result1p4 = ""
    result1p5 = ""
    result1p6 = ""
    result1p7 = ""
    result1p8 = ""
    result1p9 = ""
    counterd1 = 0
    d1 = ""
    l18 = 0
    length18 = len(list18)

    while l18 != length18:

        a18 = (list18[l18])
        if result1p0 == "":
            result1p0 = mobile[0:1].find(str(a18))
            if result1p0 != -1:
                counterd1 = counterd1 + 1
                result1p0 = mobile[0:1]
            else:
                result1p0 = ""

        a18 = (list18[l18])
        if result1p1 == "":
            result1p1 = mobile[1:2].find(str(a18))
            if result1p1 != -1:
                counterd1 = counterd1 + 1
                result1p1 = mobile[1:2]
            else:
                result1p1 = ""

        a18 = (list18[l18])
        if result1p2 == "":
            result1p2 = mobile[2:3].find(str(a18))
            if result1p2 != -1:
                counterd1 = counterd1 + 1
                result1p2 = mobile[2:3]
            else:
                result1p2 = ""

        a18 = (list18[l18])
        if result1p3 == "":
            result1p3 = mobile[3:4].find(str(a18))
            if result1p3 != -1:
                counterd1 = counterd1 + 1
                result1p3 = mobile[3:4]
            else:
                result1p3 = ""

        a18 = (list18[l18])
        if result1p4 == "":
            result1p4 = mobile[4:5].find(str(a18))
            if result1p4 != -1:
                counterd1 = counterd1 + 1
                result1p4 = mobile[4:5]
            else:
                result1p4 = ""

        a18 = (list18[l18])
        if result1p5 == "":
            result1p5 = mobile[5:6].find(str(a18))
            if result1p5 != -1:
                counterd1 = counterd1 + 1
                result1p5 = mobile[5:6]
            else:
                result1p5 = ""

        a18 = (list18[l18])
        if result1p6 == "":
            result1p6 = mobile[6:7].find(str(a18))
            if result1p6 != -1:
                counterd1 = counterd1 + 1
                result1p6 = mobile[6:7]
            else:
                result1p6 = ""

        a18 = (list18[l18])
        if result1p7 == "":
            result1p7 = mobile[7:8].find(str(a18))
            if result1p7 != -1:
                counterd1 = counterd1 + 1
                result1p7 = mobile[7:8]
            else:
                result1p7 = ""

        a18 = (list18[l18])
        if result1p8 == "":
            result1p8 = mobile[8:9].find(str(a18))
            if result1p8 != -1:
                counterd1 = counterd1 + 1
                result1p8 = mobile[8:9]
            else:
                result1p8 = ""

        a18 = (list18[l18])
        if result1p9 == "":
            result1p9 = mobile[9:10].find(str(a18))
            if result1p9 != -1:
                counterd1 = counterd1 + 1
                result1p9 = mobile[9:10]
            else:
                result1p9 = ""

        d1 = d1 + "< " + str(a18) + "> " + str(counterd1)

        if counterd1 > 5:
            p1002 = "1 digit no. " + "(" + (str(a18) + ")" + " found " + str(counterd1) + " times")
            # print(p1002)

        counterd1 = 0
        l18 = l18 + 1

    # extracting repeat no. from mobile
    result2t0 = ""
    result2t1 = ""
    result2t2 = ""
    result2t3 = ""
    result2t4 = ""
    result2t5 = ""
    result2t6 = ""
    result2t7 = ""
    result2t8 = ""
    l9 = 0
    length9 = len(list9)

    while l9 != length9:

        a9 = (list9[l9])
        if result2t0 == "":
            result2t0 = mobile[0:2].find(str(a9))
            if result2t0 != -1:
                result2t0 = mobile[0:2]
            else:
                result2t0 = ""

        a9 = (list9[l9])
        if result2t1 == "":
            result2t1 = mobile[1:3].find(str(a9))
            if result2t1 != -1:
                result2t1 = mobile[1:3]
            else:
                result2t1 = ""

        a9 = (list9[l9])
        if result2t2 == "":
            result2t2 = mobile[2:4].find(str(a9))
            if result2t2 != -1:
                result2t2 = mobile[2:4]
            else:
                result2t2 = ""

        a9 = (list9[l9])
        if result2t3 == "":
            result2t3 = mobile[3:5].find(str(a9))
            if result2t3 != -1:
                result2t3 = mobile[3:5]
            else:
                result2t3 = ""

        a9 = (list9[l9])
        if result2t4 == "":
            result2t4 = mobile[4:6].find(str(a9))
            if result2t4 != -1:
                result2t4 = mobile[4:6]
            else:
                result2t4 = ""

        a9 = (list9[l9])
        if result2t5 == "":
            result2t5 = mobile[5:7].find(str(a9))
            if result2t5 != -1:
                result2t5 = mobile[5:7]
            else:
                result2t5 = ""

        a9 = (list9[l9])
        if result2t6 == "":
            result2t6 = mobile[6:8].find(str(a9))
            if result2t6 != -1:
                result2t6 = mobile[6:8]
            else:
                result2t6 = ""

        a9 = (list9[l9])
        if result2t7 == "":
            result2t7 = mobile[7:9].find(str(a9))
            if result2t7 != -1:
                result2t7 = mobile[7:9]
            else:
                result2t7 = ""

        a9 = (list9[l9])
        if result2t8 == "":
            result2t8 = mobile[8:10].find(str(a9))
            if result2t8 != -1:
                result2t8 = mobile[8:10]
            else:
                result2t8 = ""

        l9 = l9 + 1

    result3t0 = ""
    result3t1 = ""
    result3t2 = ""
    result3t3 = ""
    result3t4 = ""
    result3t5 = ""
    result3t6 = ""
    result3t7 = ""

    l8 = 0
    length8 = len(list8)

    while l8 != length8:

        a8 = (list8[l8])
        if result3t0 == "":
            result3t0 = mobile[0:3].find(str(a8))
            if result3t0 != -1:
                result3t0 = mobile[0:3]
            else:
                result3t0 = ""

        a8 = (list8[l8])
        if result3t1 == "":
            result3t1 = mobile[1:4].find(str(a8))
            if result3t1 != -1:
                result3t1 = mobile[1:4]
            else:
                result3t1 = ""

        a8 = (list8[l8])
        if result3t2 == "":
            result3t2 = mobile[2:5].find(str(a8))
            if result3t2 != -1:
                result3t2 = mobile[2:5]
            else:
                result3t2 = ""

        a8 = (list8[l8])
        if result3t3 == "":
            result3t3 = mobile[3:6].find(str(a8))
            if result3t3 != -1:
                result3t3 = mobile[3:6]
            else:
                result3t3 = ""

        a8 = (list8[l8])
        if result3t4 == "":
            result3t4 = mobile[4:7].find(str(a8))
            if result3t4 != -1:
                result3t4 = mobile[4:7]
            else:
                result3t4 = ""

        a8 = (list8[l8])
        if result3t5 == "":
            result3t5 = mobile[5:8].find(str(a8))
            if result3t5 != -1:
                result3t5 = mobile[5:8]
            else:
                result3t5 = ""

        a8 = (list8[l8])
        if result3t6 == "":
            result3t6 = mobile[6:9].find(str(a8))
            if result3t6 != -1:
                result3t6 = mobile[6:9]
            else:
                result3t6 = ""

        a8 = (list8[l8])
        if result3t7 == "":
            result3t7 = mobile[7:10].find(str(a8))
            if result3t7 != -1:
                result3t7 = mobile[7:10]
            else:
                result3t7 = ""

        l8 = l8 + 1

    result4t0 = ""
    result4t1 = ""
    result4t2 = ""
    result4t3 = ""
    result4t4 = ""
    result4t5 = ""
    result4t6 = ""

    l7 = 0
    length7 = len(list7)

    while l7 != length7:

        a7 = (list7[l7])
        if result4t0 == "":
            result4t0 = mobile[0:4].find(str(a7))
            if result4t0 != -1:
                result4t0 = mobile[0:4]
            else:
                result4t0 = ""

        a7 = (list7[l7])
        if result4t1 == "":
            result4t1 = mobile[1:5].find(str(a7))
            if result4t1 != -1:
                result4t1 = mobile[1:5]
            else:
                result4t1 = ""

        a7 = (list7[l7])
        if result4t2 == "":
            result4t2 = mobile[2:6].find(str(a7))
            if result4t2 != -1:
                result4t2 = mobile[2:6]
            else:
                result4t2 = ""

        a7 = (list7[l7])
        if result4t3 == "":
            result4t3 = mobile[3:7].find(str(a7))
            if result4t3 != -1:
                result4t3 = mobile[3:7]
            else:
                result4t3 = ""

        a7 = (list7[l7])
        if result4t4 == "":
            result4t4 = mobile[4:8].find(str(a7))
            if result4t4 != -1:
                result4t4 = mobile[4:8]
            else:
                result4t4 = ""

        a7 = (list7[l7])
        if result4t5 == "":
            result4t5 = mobile[5:9].find(str(a7))
            if result4t5 != -1:
                result4t5 = mobile[5:9]
            else:
                result4t5 = ""

        a7 = (list7[l7])
        if result4t6 == "":
            result4t6 = mobile[6:10].find(str(a7))
            if result4t6 != -1:
                result4t6 = mobile[6:10]
            else:
                result4t6 = ""

        l7 = l7 + 1

    result5t0 = ""
    result5t1 = ""
    result5t2 = ""
    result5t3 = ""
    result5t4 = ""
    result5t5 = ""

    l6 = 0
    length6 = len(list6)

    while l6 != length6:

        a6 = (list6[l6])
        if result5t0 == "":
            result5t0 = mobile[0:5].find(str(a6))
            if result5t0 != -1:
                result5t0 = mobile[0:5]
            else:
                result5t0 = ""

        a6 = (list6[l6])
        if result5t1 == "":
            result5t1 = mobile[1:6].find(str(a6))
            if result5t1 != -1:
                result5t1 = mobile[1:6]
            else:
                result5t1 = ""

        a6 = (list6[l6])
        if result5t2 == "":
            result5t2 = mobile[2:7].find(str(a6))
            if result5t2 != -1:
                result5t2 = mobile[2:7]
            else:
                result5t2 = ""

        a6 = (list6[l6])
        if result5t3 == "":
            result5t3 = mobile[3:8].find(str(a6))
            if result5t3 != -1:
                result5t3 = mobile[3:8]
            else:
                result5t3 = ""

        a6 = (list6[l6])
        if result5t4 == "":
            result5t4 = mobile[4:9].find(str(a6))
            if result5t4 != -1:
                result5t4 = mobile[4:9]
            else:
                result5t4 = ""

        a6 = (list6[l6])
        if result5t5 == "":
            result5t5 = mobile[5:10].find(str(a6))
            if result5t5 != -1:
                result5t5 = mobile[5:10]
            else:
                result5t5 = ""

        l6 = l6 + 1

    result6t0 = ""
    result6t1 = ""
    result6t2 = ""
    result6t3 = ""
    result6t4 = ""
    l5 = 0
    length5 = len(list5)

    while l5 != length5:

        a5 = (list5[l5])
        if result6t0 == "":
            result6t0 = mobile[0:6].find(str(a5))
            if result6t0 != -1:
                result6t0 = mobile[0:6]
            else:
                result6t0 = ""

        a5 = (list5[l5])
        if result6t1 == "":
            result6t1 = mobile[1:7].find(str(a5))
            if result6t1 != -1:
                result6t1 = mobile[1:7]
            else:
                result6t1 = ""

        a5 = (list5[l5])
        if result6t2 == "":
            result6t2 = mobile[2:8].find(str(a5))
            if result6t2 != -1:
                result6t2 = mobile[2:8]
            else:
                result6t2 = ""

        a5 = (list5[l5])
        if result6t3 == "":
            result6t3 = mobile[3:9].find(str(a5))
            if result6t3 != -1:
                result6t3 = mobile[3:9]
            else:
                result6t3 = ""

        a5 = (list5[l5])
        if result6t4 == "":
            result6t4 = mobile[4:10].find(str(a5))
            if result6t4 != -1:
                result6t4 = mobile[4:10]
            else:
                result6t4 = ""

        l5 = l5 + 1

    result7t0 = ""
    result7t1 = ""
    result7t2 = ""
    result7t3 = ""
    l4 = 0
    length4 = len(list4)

    while l4 != length4:

        a4 = (list4[l4])
        if result7t0 == "":
            result7t0 = mobile[0:7].find(str(a4))
            if result7t0 != -1:
                result7t0 = mobile[0:7]
            else:
                result7t0 = ""

        a4 = (list4[l4])
        if result7t1 == "":
            result7t1 = mobile[1:8].find(str(a4))
            if result7t1 != -1:
                result7t1 = mobile[1:8]
            else:
                result7t1 = ""

        a4 = (list4[l4])
        if result7t2 == "":
            result7t2 = mobile[2:9].find(str(a4))
            if result7t2 != -1:
                result7t2 = mobile[2:9]
            else:
                result7t2 = ""

        a4 = (list4[l4])
        if result7t3 == "":
            result7t3 = mobile[3:10].find(str(a4))
            if result7t3 != -1:
                result7t3 = mobile[3:10]
            else:
                result7t3 = ""

        l4 = l4 + 1

    result8t0 = ""
    result8t1 = ""
    result8t2 = ""
    l3 = 0
    length3 = len(list3)

    while l3 != length3:

        a3 = (list3[l3])
        if result8t0 == "":
            result8t0 = mobile[0:8].find(str(a3))
            if result8t0 != -1:
                result8t0 = mobile[0:8]
            else:
                result8t0 = ""

        a3 = (list3[l3])
        if result8t1 == "":
            result8t1 = mobile[1:9].find(str(a3))
            if result8t1 != -1:
                result8t1 = mobile[1:9]
            else:
                result8t1 = ""

        a3 = (list3[l3])
        if result8t2 == "":
            result8t2 = mobile[2:10].find(str(a3))
            if result8t2 != -1:
                result8t2 = mobile[2:10]
            else:
                result8t2 = ""

        l3 = l3 + 1

    result9t0 = ""
    result9t1 = ""
    l2 = 0
    length2 = len(list2)

    while l2 != length2:

        a2 = (list2[l2])
        if result9t0 == "":
            result9t0 = mobile[0:9].find(str(a2))
            if result9t0 != -1:
                result9t0 = mobile[0:9]
            else:
                result9t0 = ""

        a2 = (list2[l2])
        if result9t1 == "":
            result9t1 = mobile[1:10].find(str(a2))
            if result9t1 != -1:
                result9t1 = mobile[1:10]
            else:
                result9t1 = ""

        l2 = l2 + 1

    result10t0 = ""
    l1 = 0
    length1 = len(list1)

    while l1 != length1:

        a1 = (list1[l1])
        if result10t0 == "":
            result10t0 = mobile[0:10].find(str(a1))
            if result10t0 != -1:
                result10t0 = mobile[0:10]
            else:
                result10t0 = ""

        l1 = l1 + 1

    # extracting sequence from mobile

    result3s0 = ""
    result3s1 = ""
    result3s2 = ""
    result3s3 = ""
    result3s4 = ""
    result3s5 = ""
    result3s6 = ""
    result3s7 = ""

    l17 = 0
    length17 = len(list17)

    while l17 != length17:

        a17 = (list17[l17])
        if result3s0 == "":
            result3s0 = mobile[0:3].find(str(a17))
            if result3s0 != -1:
                result3s0 = mobile[0:3]
            else:
                result3s0 = ""

        a17 = (list17[l17])
        if result3s1 == "":
            result3s1 = mobile[1:4].find(str(a17))
            if result3s1 != -1:
                result3s1 = mobile[1:4]
            else:
                result3s1 = ""

        a17 = (list17[l17])
        if result3s2 == "":
            result3s2 = mobile[2:5].find(str(a17))
            if result3s2 != -1:
                result3s2 = mobile[2:5]
            else:
                result3s2 = ""

        a17 = (list17[l17])
        if result3s3 == "":
            result3s3 = mobile[3:6].find(str(a17))
            if result3s3 != -1:
                result3s3 = mobile[3:6]
            else:
                result3s3 = ""

        a17 = (list17[l17])
        if result3s4 == "":
            result3s4 = mobile[4:7].find(str(a17))
            if result3s4 != -1:
                result3s4 = mobile[4:7]
            else:
                result3s4 = ""

        a17 = (list17[l17])
        if result3s5 == "":
            result3s5 = mobile[5:8].find(str(a17))
            if result3s5 != -1:
                result3s5 = mobile[5:8]
            else:
                result3s5 = ""

        a17 = (list17[l17])
        if result3s6 == "":
            result3s6 = mobile[6:9].find(str(a17))
            if result3s6 != -1:
                result3s6 = mobile[6:9]
            else:
                result3s6 = ""

        a17 = (list17[l17])
        if result3s7 == "":
            result3s7 = mobile[7:10].find(str(a17))
            if result3s7 != -1:
                result3s7 = mobile[7:10]
            else:
                result3s7 = ""

        l17 = l17 + 1

    result4s0 = ""
    result4s1 = ""
    result4s2 = ""
    result4s3 = ""
    result4s4 = ""
    result4s5 = ""
    result4s6 = ""

    l16 = 0
    length16 = len(list16)

    while l16 != length16:

        a16 = (list16[l16])
        if result4s0 == "":
            result4s0 = mobile[0:4].find(str(a16))
            if result4s0 != -1:
                result4s0 = mobile[0:4]
            else:
                result4s0 = ""

        a16 = (list16[l16])
        if result4s1 == "":
            result4s1 = mobile[1:5].find(str(a16))
            if result4s1 != -1:
                result4s1 = mobile[1:5]
            else:
                result4s1 = ""

        a16 = (list16[l16])
        if result4s2 == "":
            result4s2 = mobile[2:6].find(str(a16))
            if result4s2 != -1:
                result4s2 = mobile[2:6]
            else:
                result4s2 = ""

        a16 = (list16[l16])
        if result4s3 == "":
            result4s3 = mobile[3:7].find(str(a16))
            if result4s3 != -1:
                result4s3 = mobile[3:7]
            else:
                result4s3 = ""

        a16 = (list16[l16])
        if result4s4 == "":
            result4s4 = mobile[4:8].find(str(a16))
            if result4s4 != -1:
                result4s4 = mobile[4:8]
            else:
                result4s4 = ""

        a16 = (list16[l16])
        if result4s5 == "":
            result4s5 = mobile[5:9].find(str(a16))
            if result4s5 != -1:
                result4s5 = mobile[5:9]
            else:
                result4s5 = ""

        a16 = (list16[l16])
        if result4s6 == "":
            result4s6 = mobile[6:10].find(str(a16))
            if result4s6 != -1:
                result4s6 = mobile[6:10]
            else:
                result4s6 = ""

        l16 = l16 + 1

    result5s0 = ""
    result5s1 = ""
    result5s2 = ""
    result5s3 = ""
    result5s4 = ""
    result5s5 = ""

    l15 = 0
    length15 = len(list15)

    while l15 != length15:

        a15 = (list15[l15])
        if result5s0 == "":
            result5s0 = mobile[0:5].find(str(a15))
            if result5s0 != -1:
                result5s0 = mobile[0:5]
            else:
                result5s0 = ""

        a15 = (list15[l15])
        if result5s1 == "":
            result5s1 = mobile[1:6].find(str(a15))
            if result5s1 != -1:
                result5s1 = mobile[1:6]
            else:
                result5s1 = ""

        a15 = (list15[l15])
        if result5s2 == "":
            result5s2 = mobile[2:7].find(str(a15))
            if result5s2 != -1:
                result5s2 = mobile[2:7]
            else:
                result5s2 = ""

        a15 = (list15[l15])
        if result5s3 == "":
            result5s3 = mobile[3:8].find(str(a15))
            if result5s3 != -1:
                result5s3 = mobile[3:8]
            else:
                result5s3 = ""

        a15 = (list15[l15])
        if result5s4 == "":
            result5s4 = mobile[4:9].find(str(a15))
            if result5s4 != -1:
                result5s4 = mobile[4:9]
            else:
                result5s4 = ""

        a15 = (list15[l15])
        if result5s5 == "":
            result5s5 = mobile[5:10].find(str(a15))
            if result5s5 != -1:
                result5s5 = mobile[5:10]
            else:
                result5s5 = ""

        l15 = l15 + 1

    result6s0 = ""
    result6s1 = ""
    result6s2 = ""
    result6s3 = ""
    result6s4 = ""
    l14 = 0
    length14 = len(list14)

    while l14 != length14:

        a14 = (list14[l14])
        if result6s0 == "":
            result6s0 = mobile[0:6].find(str(a14))
            if result6s0 != -1:
                result6s0 = mobile[0:6]
            else:
                result6s0 = ""

        a14 = (list14[l14])
        if result6s1 == "":
            result6s1 = mobile[1:7].find(str(a14))
            if result6s1 != -1:
                result6s1 = mobile[1:7]
            else:
                result6s1 = ""

        a14 = (list14[l14])
        if result6s2 == "":
            result6s2 = mobile[2:8].find(str(a14))
            if result6s2 != -1:
                result6s2 = mobile[2:8]
            else:
                result6s2 = ""

        a14 = (list14[l14])
        if result6s3 == "":
            result6s3 = mobile[3:9].find(str(a14))
            if result6s3 != -1:
                result6s3 = mobile[3:9]
            else:
                result6s3 = ""

        a14 = (list14[l14])
        if result6s4 == "":
            result6s4 = mobile[4:10].find(str(a14))
            if result6s4 != -1:
                result6s4 = mobile[4:10]
            else:
                result6s4 = ""

        l14 = l14 + 1

    result7s0 = ""
    result7s1 = ""
    result7s2 = ""
    result7s3 = ""
    l13 = 0
    length13 = len(list13)

    while l13 != length13:

        a13 = (list13[l13])
        if result7s0 == "":
            result7s0 = mobile[0:7].find(str(a13))
            if result7s0 != -1:
                result7s0 = mobile[0:7]
            else:
                result7s0 = ""

        a13 = (list13[l13])
        if result7s1 == "":
            result7s1 = mobile[1:8].find(str(a13))
            if result7s1 != -1:
                result7s1 = mobile[1:8]
            else:
                result7s1 = ""

        a13 = (list13[l13])
        if result7s2 == "":
            result7s2 = mobile[2:9].find(str(a13))
            if result7s2 != -1:
                result7s2 = mobile[2:9]
            else:
                result7s2 = ""

        a13 = (list13[l13])
        if result7s3 == "":
            result7s3 = mobile[3:10].find(str(a13))
            if result7s3 != -1:
                result7s3 = mobile[3:10]
            else:
                result7s3 = ""

        l13 = l13 + 1

    result8s0 = ""
    result8s1 = ""
    result8s2 = ""
    l12 = 0
    length12 = len(list12)

    while l12 != length12:

        a12 = (list12[l12])
        if result8s0 == "":
            result8s0 = mobile[0:8].find(str(a12))
            if result8s0 != -1:
                result8s0 = mobile[0:8]
            else:
                result8s0 = ""

        a12 = (list12[l12])
        if result8s1 == "":
            result8s1 = mobile[1:9].find(str(a12))
            if result8s1 != -1:
                result8s1 = mobile[1:9]
            else:
                result8s1 = ""

        a12 = (list12[l12])
        if result8s2 == "":
            result8s2 = mobile[2:10].find(str(a12))
            if result8s2 != -1:
                result8s2 = mobile[2:10]
            else:
                result8s2 = ""

        l12 = l12 + 1

    result9s0 = ""
    result9s1 = ""
    l11 = 0
    length11 = len(list11)

    while l11 != length11:

        a11 = (list11[l11])
        if result9s0 == "":
            result9s0 = mobile[0:9].find(str(a11))
            if result9s0 != -1:
                result9s0 = mobile[0:9]
            else:
                result9s0 = ""

        a11 = (list11[l11])
        if result9s1 == "":
            result9s1 = mobile[1:10].find(str(a11))
            if result9s1 != -1:
                result9s1 = mobile[1:10]
            else:
                result9s1 = ""

        l11 = l11 + 1

    result10s0 = ""
    l10 = 0
    length10 = len(list10)

    while l10 != length10:

        a10 = (list10[l10])
        if result10s0 == "":
            result10s0 = mobile[0:10].find(str(a10))
            if result10s0 != -1:
                result10s0 = mobile[0:10]
            else:
                result10s0 = ""

        l10 = l10 + 1

    # extracting 2 digit simple no. from mobile

    result2p0 = ""
    result2p1 = ""
    result2p2 = ""
    result2p3 = ""
    result2p4 = ""
    result2p5 = ""
    result2p6 = ""
    result2p7 = ""
    result2p8 = ""
    l19 = 0
    length19 = len(list19)

    while l19 != length19:

        a19 = (list19[l19])
        if result2p0 == "":
            result2p0 = mobile[0:2].find(str(a19))
            if result2p0 != -1:
                result2p0 = mobile[0:2]
            else:
                result2p0 = ""

        a19 = (list19[l19])
        if result2p1 == "":
            result2p1 = mobile[1:3].find(str(a19))
            if result2p1 != -1:
                result2p1 = mobile[1:3]
            else:
                result2p1 = ""

        a19 = (list19[l19])
        if result2p2 == "":
            result2p2 = mobile[2:4].find(str(a19))
            if result2p2 != -1:
                result2p2 = mobile[2:4]
            else:
                result2p2 = ""

        a19 = (list19[l19])
        if result2p3 == "":
            result2p3 = mobile[3:5].find(str(a19))
            if result2p3 != -1:
                result2p3 = mobile[3:5]
            else:
                result2p3 = ""

        a19 = (list19[l19])
        if result2p4 == "":
            result2p4 = mobile[4:6].find(str(a19))
            if result2p4 != -1:
                result2p4 = mobile[4:6]
            else:
                result2p4 = ""

        a19 = (list19[l19])
        if result2p5 == "":
            result2p5 = mobile[5:7].find(str(a19))
            if result2p5 != -1:
                result2p5 = mobile[5:7]
            else:
                result2p5 = ""

        a19 = (list19[l19])
        if result2p6 == "":
            result2p6 = mobile[6:8].find(str(a19))
            if result2p6 != -1:
                result2p6 = mobile[6:8]
            else:
                result2p6 = ""

        a19 = (list19[l19])
        if result2p7 == "":
            result2p7 = mobile[7:9].find(str(a19))
            if result2p7 != -1:
                result2p7 = mobile[7:9]
            else:
                result2p7 = ""

        a19 = (list19[l19])
        if result2p8 == "":
            result2p8 = mobile[8:10].find(str(a19))
            if result2p8 != -1:
                result2p8 = mobile[8:10]
            else:
                result2p8 = ""

        l19 = l19 + 1
    # extracting 3 digit simple no. from mobilw
    result3p0 = ""
    result3p0 = mobile[0:3]
    result3p1 = ""
    result3p1 = mobile[1:4]
    result3p2 = ""
    result3p2 = mobile[2:5]
    result3p3 = ""
    result3p3 = mobile[3:6]
    result3p4 = ""
    result3p4 = mobile[4:7]
    result3p5 = ""
    result3p5 = mobile[5:8]
    result3p6 = ""
    result3p6 = mobile[6:9]
    result3p7 = ""
    result3p7 = mobile[7:10]
    # extracting 4 digit simple no. from mobilw
    result4p0 = ""
    result4p0 = mobile[0:4]
    result4p1 = ""
    result4p1 = mobile[1:5]
    result4p2 = ""
    result4p2 = mobile[2:6]
    result4p3 = ""
    result4p3 = mobile[3:7]
    result4p4 = ""
    result4p4 = mobile[4:8]
    result4p5 = ""
    result4p5 = mobile[5:9]
    result4p6 = ""
    result4p6 = mobile[6:10]

    ptc2 = ""
    tc2 = 0
    if (result2t0 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "0"
    if (result2t1 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "1"
    if (result2t2 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "2"
    if (result2t3 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "3"
    if (result2t4 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "4"
    if (result2t5 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "5"
    if (result2t6 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "6"
    if (result2t7 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "7"
    if (result2t8 != ""):
        tc2 = tc2 + 1
        ptc2 = ptc2 + "8"
    ptc3 = ""
    tc3 = 0
    if result3t0 != "":
        tc3 = tc3 + 1
        ptc3 = ptc3 + "0"
    if result3t1 != "":
        tc3 = tc3 + 1
        ptc3 = ptc3 + "1"
    if result3t2 != "":
        tc3 = tc3 + 1
        ptc3 = ptc3 + "2"
    if result3t3 != "":
        tc3 = tc3 + 1
        ptc3 = ptc3 + "3"
    if result3t4 != "":
        tc3 = tc3 + 1
        ptc3 = ptc3 + "4"
    if result3t5 != "":
        tc3 = tc3 + 1
        ptc3 = ptc3 + "5"
    if result3t6 != "":
        tc3 = tc3 + 1
        ptc3 = ptc3 + "6"
    if result3t7 != "":
        tc3 = tc3 + 1
        ptc3 = ptc3 + "7"
    ptc4 = ""
    tc4 = 0
    if result4t0 != "":
        tc4 = tc4 + 1
        ptc4 = ptc4 + "0"
    if result4t1 != "":
        tc4 = tc4 + 1
        ptc4 = ptc4 + "1"
    if result4t2 != "":
        tc4 = tc4 + 1
        ptc4 = ptc4 + "2"
    if result4t3 != "":
        tc4 = tc4 + 1
        ptc4 = ptc4 + "3"
    if result4t4 != "":
        tc4 = tc4 + 1
        ptc4 = ptc4 + "4"
    if result4t5 != "":
        tc4 = tc4 + 1
        ptc4 = ptc4 + "5"
    if result4t6 != "":
        tc4 = tc4 + 1
        ptc4 = ptc4 + "6"
    ptc5 = ""
    tc5 = 0
    if result5t0 != "":
        tc5 = tc5 + 1
        ptc5 = ptc5 + "0"
    if result5t1 != "":
        tc5 = tc5 + 1
        ptc5 = ptc5 + "1"
    if result5t2 != "":
        tc5 = tc5 + 1
        ptc5 = ptc5 + "2"
    if result5t3 != "":
        tc5 = tc5 + 1
        ptc5 = ptc5 + "3"
    if result5t4 != "":
        tc5 = tc5 + 1
        ptc5 = ptc5 + "4"
    if result5t5 != "":
        tc5 = tc5 + 1
        ptc5 = ptc5 + "5"
    ptc6 = ""
    tc6 = 0
    if result6t0 != "":
        tc6 = tc6 + 1
        ptc6 = ptc6 + "0"
    if result6t1 != "":
        tc6 = tc6 + 1
        ptc6 = ptc6 + "1"
    if result6t2 != "":
        tc6 = tc6 + 1
        ptc6 = ptc6 + "2"
    if result6t3 != "":
        tc6 = tc6 + 1
        ptc6 = ptc6 + "3"
    if result6t4 != "":
        tc6 = tc6 + 1
        ptc6 = ptc6 + "4"

    ptc7 = ""
    tc7 = 0
    if result7t0 != "":
        tc7 = tc7 + 1
        ptc7 = ptc7 + "0"
    if result7t1 != "":
        tc7 = tc7 + 1
        ptc7 = ptc7 + "1"
    if result7t2 != "":
        tc7 = tc7 + 1
        ptc7 = ptc7 + "2"
    if result7t3 != "":
        tc7 = tc7 + 1
        ptc7 = ptc7 + "3"

    ptc8 = ""
    tc8 = 0
    if result8t0 != "":
        tc8 = tc8 + 1
        ptc8 = ptc8 + "0"
    if result8t1 != "":
        tc8 = tc8 + 1
        ptc8 = ptc8 + "1"
    if result8t2 != "":
        tc8 = tc8 + 1
        ptc8 = ptc8 + "2"
    ptc9 = ""
    tc9 = 0
    if result9t0 != "":
        tc9 = tc9 + 1
        ptc9 = ptc9 + "0"
    if result9t1 != "":
        tc9 = tc9 + 1
        ptc9 = ptc9 + "1"
    psc3 = ""
    sc3 = 0
    if result3s0 != "":
        sc3 = sc3 + 1
        psc3 = psc3 + "0"
    if result3s1 != "":
        sc3 = sc3 + 1
        psc3 = psc3 + "1"
    if result3s2 != "":
        sc3 = sc3 + 1
        psc3 = psc3 + "2"
    if result3s3 != "":
        sc3 = sc3 + 1
        psc3 = psc3 + "3"
    if result3s4 != "":
        sc3 = sc3 + 1
        psc3 = psc3 + "4"
    if result3s5 != "":
        sc3 = sc3 + 1
        psc3 = psc3 + "5"
    if result3s6 != "":
        sc3 = sc3 + 1
        psc3 = psc3 + "6"
    if result3s7 != "":
        sc3 = sc3 + 1
        psc3 = psc3 + "7"

    psc4 = ""
    sc4 = 0
    if result4s0 != "":
        sc4 = sc4 + 1
        psc4 = psc4 + "0"
    if result4s1 != "":
        sc4 = sc4 + 1
        psc4 = psc4 + "1"
    if result4s2 != "":
        sc4 = sc4 + 1
        psc4 = psc4 + "2"
    if result4s3 != "":
        sc4 = sc4 + 1
        psc4 = psc4 + "3"
    if result4s4 != "":
        sc4 = sc4 + 1
        psc4 = psc4 + "4"
    if result4s5 != "":
        sc4 = sc4 + 1
        psc4 = psc4 + "5"
    if result4s6 != "":
        sc4 = sc4 + 1
        psc4 = psc4 + "6"
    psc5 = ""
    sc5 = 0
    if result5s0 != "":
        sc5 = sc5 + 1
        psc5 = psc5 + "0"
    if result5s1 != "":
        sc5 = sc5 + 1
        psc5 = psc5 + "1"
    if result5s2 != "":
        sc5 = sc5 + 1
        psc5 = psc5 + "2"
    if result5s3 != "":
        sc5 = sc5 + 1
        psc5 = psc5 + "3"
    if result5s4 != "":
        sc5 = sc5 + 1
        psc5 = psc5 + "4"
    if result5s5 != "":
        sc5 = sc5 + 1
        psc5 = psc5 + "5"
    psc6 = ""
    sc6 = 0
    if result6s0 != "":
        sc6 = sc6 + 1
        psc6 = psc6 + "0"
    if result6s1 != "":
        sc6 = sc6 + 1
        psc6 = psc6 + "1"
    if result6s2 != "":
        sc6 = sc6 + 1
        psc6 = psc6 + "2"
    if result6s3 != "":
        sc6 = sc6 + 1
        psc6 = psc6 + "3"
    if result6s4 != "":
        sc6 = sc6 + 1
        psc6 = psc6 + "4"

    psc7 = ""
    sc7 = 0
    if result7s0 != "":
        sc7 = sc7 + 1
        psc7 = psc7 + "0"
    if result7s1 != "":
        sc7 = sc7 + 1
        psc7 = psc7 + "1"
    if result7s2 != "":
        sc7 = sc7 + 1
        psc7 = psc7 + "2"
    if result7s3 != "":
        sc7 = sc7 + 1
        psc7 = psc7 + "3"

    psc8 = ""
    sc8 = 0
    if result8s0 != "":
        sc8 = sc8 + 1
        psc8 = psc8 + "0"
    if result8s1 != "":
        sc8 = sc8 + 1
        psc8 = psc8 + "1"
    if result8s2 != "":
        sc8 = sc8 + 1
        psc8 = psc8 + "2"
    psc9 = ""
    sc9 = 0
    if result9s0 != "":
        sc9 = sc9 + 1
        psc9 = psc9 + "0"
    if result9s1 != "":
        sc9 = sc9 + 1
        psc9 = psc9 + "1"
    # extracting 2 digit count

    ppc2 = ""
    pc2 = 1
    if (result2p0 != "" and result2p0 == result2p2):
        pc2 = pc2 + 1
        ppc2 = ppc2 + "2"
    if (result2p0 != "" and result2p0 == result2p3):
        pc2 = pc2 + 1
        ppc2 = ppc2 + "3"
    if (result2p0 != "" and result2p0 == result2p4):
        pc2 = pc2 + 1
        ppc2 = ppc2 + "4"
    if (result2p0 != "" and result2p0 == result2p5):
        pc2 = pc2 + 1
        ppc2 = ppc2 + "5"
    if (result2p0 != "" and result2p0 == result2p6):
        pc2 = pc2 + 1
        ppc2 = ppc2 + "6"
    if (result2p0 != "" and result2p0 == result2p7):
        pc2 = pc2 + 1
        ppc2 = ppc2 + "7"
    if (result2p0 != "" and result2p0 == result2p8):
        pc2 = pc2 + 1
        ppc2 = ppc2 + "8"

    ppc3 = ""
    pc3 = 1
    if (result2p1 != "" and result2p1 == result2p3):
        pc3 = pc3 + 1
        ppc3 = ppc3 + "3"
    if (result2p1 != "" and result2p1 == result2p4):
        pc3 = pc3 + 1
        ppc3 = ppc3 + "4"
    if (result2p1 != "" and result2p1 == result2p5):
        pc3 = pc3 + 1
        ppc3 = ppc3 + "5"
    if (result2p1 != "" and result2p1 == result2p6):
        pc3 = pc3 + 1
        ppc3 = ppc3 + "6"
    if (result2p1 != "" and result2p1 == result2p7):
        pc3 = pc3 + 1
        ppc3 = ppc3 + "7"
    if (result2p1 != "" and result2p1 == result2p8):
        pc3 = pc3 + 1
        ppc3 = ppc3 + "8"

    ppc4 = ""
    pc4 = 1
    if (result2p2 != "" and result2p2 == result2p4):
        pc4 = pc4 + 1
        ppc4 = ppc4 + "4"
    if (result2p2 != "" and result2p2 == result2p5):
        pc4 = pc4 + 1
        ppc4 = ppc4 + "5"
    if (result2p2 != "" and result2p2 == result2p6):
        pc4 = pc4 + 1
        ppc4 = ppc4 + "6"
    if (result2p2 != "" and result2p2 == result2p7):
        pc4 = pc4 + 1
        ppc4 = ppc4 + "7"
    if (result2p2 != "" and result2p2 == result2p8):
        pc4 = pc4 + 1
        ppc4 = ppc4 + "8"

    ppc5 = ""
    pc5 = 1
    if (result2p3 != "" and result2p3 == result2p5):
        pc5 = pc5 + 1
        ppc5 = ppc5 + "5"
    if (result2p3 != "" and result2p3 == result2p6):
        pc5 = pc5 + 1
        ppc5 = ppc5 + "6"
    if (result2p3 != "" and result2p3 == result2p7):
        pc5 = pc5 + 1
        ppc5 = ppc5 + "7"
    if (result2p3 != "" and result2p3 == result2p8):
        pc5 = pc5 + 1
        ppc5 = ppc5 + "8"
    ppc6 = ""
    pc6 = 1
    if (result2p4 != "" and result2p4 == result2p6):
        pc6 = pc6 + 1
        ppc6 = ppc6 + "6"
    if (result2p4 != "" and result2p4 == result2p7):
        pc6 = pc6 + 1
        ppc6 = ppc6 + "7"
    if (result2p4 != "" and result2p4 == result2p8):
        pc6 = pc6 + 1
        ppc6 = ppc6 + "8"
    ppc7 = ""
    pc7 = 1
    if (result2p5 != "" and result2p5 == result2p7):
        pc7 = pc7 + 1
        ppc7 = ppc7 + "7"
    if (result2p5 != "" and result2p5 == result2p8):
        pc7 = pc7 + 1
        ppc7 = ppc7 + "8"
    ppc8 = ""
    pc8 = 1
    if (result2p6 != "" and result2p6 == result2p8):
        pc8 = pc8 + 1
        ppc8 = ppc8 + "8"

    # extracting 3 digit count

    ppc3p = ""
    pc3p = 1
    if (result3p0 != "" and result3p0 == result3p3):
        pc3p = pc3p + 1
        ppc3p = ppc3p + "3"
    if (result3p0 != "" and result3p0 == result3p4):
        pc3p = pc3p + 1
        ppc3p = ppc3p + "4"
    if (result3p0 != "" and result3p0 == result3p5):
        pc3p = pc3p + 1
        ppc3p = ppc3p + "5"
    if (result3p0 != "" and result3p0 == result3p6):
        pc3p = pc3p + 1
        ppc3p = ppc3p + "6"
    if (result3p0 != "" and result3p0 == result3p7):
        pc3p = pc3p + 1
        ppc3p = ppc3p + "7"
    ppc3p1 = ""
    pc3p1 = 1
    if (result3p1 != "" and result3p1 == result3p4):
        pc3p1 = pc3p1 + 1
        ppc3p1 = ppc3p1 + "4"
    if (result3p1 != "" and result3p1 == result3p5):
        pc3p1 = pc3p1 + 1
        ppc3p1 = ppc3p1 + "5"
    if (result3p1 != "" and result3p1 == result3p6):
        pc3p1 = pc3p1 + 1
        ppc3p1 = ppc3p1 + "6"
    if (result3p1 != "" and result3p1 == result3p7):
        pc3p1 = pc3p1 + 1
        ppc3p1 = ppc3p1 + "7"

    ppc3p2 = ""
    pc3p2 = 1
    if (result3p2 != "" and result3p2 == result3p5):
        pc3p2 = pc3p2 + 1
        ppc3p2 = ppc3p2 + "5"
    if (result3p2 != "" and result3p2 == result3p6):
        pc3p2 = pc3p2 + 1
        ppc3p2 = ppc3p2 + "6"
    if (result3p2 != "" and result3p2 == result3p7):
        pc3p2 = pc3p2 + 1
        ppc3p2 = ppc3p2 + "7"

    ppc3p3 = ""
    pc3p3 = 1
    if (result3p3 != "" and result3p3 == result3p6):
        pc3p3 = pc3p3 + 1
        ppc3p3 = ppc3p3 + "6"
    if (result3p3 != "" and result3p3 == result3p7):
        pc3p3 = pc3p3 + 1
        ppc3p3 = ppc3p3 + "7"

    ppc3p4 = ""
    pc3p4 = 1
    if (result3p4 != "" and result3p4 == result3p7):
        pc3p4 = pc3p4 + 1
        ppc3p4 = ppc3p4 + "7"

    # extracting 4 digit count
    ppc4p = ""
    pc4p = 1
    if (result4p0 != "" and result4p0 == result4p4):
        pc4p = pc4p + 1
        ppc4p = ppc4p + "4"
    if (result4p0 != "" and result4p0 == result4p5):
        pc4p = pc4p + 1
        ppc4p = ppc4p + "5"
    if (result4p0 != "" and result4p0 == result4p6):
        pc4p = pc4p + 1
        ppc4p = ppc4p + "6"

    ppc4p1 = ""
    pc4p1 = 1
    if (result4p1 != "" and result4p1 == result4p5):
        pc4p1 = pc4p1 + 1
        ppc4p1 = ppc4p1 + "5"
    if (result4p1 != "" and result4p1 == result4p6):
        pc4p1 = pc4p1 + 1
        ppc4p1 = ppc4p1 + "6"

    ppc4p2 = ""
    pc4p2 = 1
    if (result4p2 != "" and result4p2 == result4p6):
        pc4p2 = pc4p2 + 1
        ppc4p2 = ppc4p2 + "6"

    # extracting different same no.details
    dp0 = 0
    dp1 = 0
    dp2 = 0
    dp3 = 0
    if result2p0 != "":
        dpa = (mobile[0:2]).count(result2p0)
        dpb = (mobile[2:4]).count(result2p0)
        dpc = (mobile[4:6]).count(result2p0)
        dpd = (mobile[6:8]).count(result2p0)
        dpe = (mobile[8:10]).count(result2p0)
        dp0 = dpa + dpb + dpc + dpd + dpe
    if result2p2 != result2p0 and result2p2 != "":
        dp1a = (mobile[2:4]).count(result2p2)
        dp1b = (mobile[4:6]).count(result2p2)
        dp1c = (mobile[6:8]).count(result2p2)
        dp1d = (mobile[8:10]).count(result2p2)
        dp1 = dp1a + dp1b + dp1c + dp1d
    if result2p4 != result2p2 and result2p4 != result2p0 and result2p4 != "":
        dp2a = (mobile[4:6]).count(result2p4)
        dp2b = (mobile[6:8]).count(result2p4)
        dp2c = (mobile[8:10]).count(result2p4)
        dp2 = dp2a + dp2b + dp2c
    if result2p6 != result2p2 and result2p6 != result2p0 and result2p6 != result2p4 and result2p6 != "":
        dp3a = (mobile[6:8]).count(result2p6)
        dp3b = (mobile[8:10]).count(result2p6)
        dp3 = dp3a + dp3b
    # print(dp0,dp1,dp2,dp3)

    d1p0 = 0
    d1p1 = 0
    d1p2 = 0
    d1p3 = 0
    d1pa = 0
    d1pb = 0
    d1pc = 0
    d1pd = 0
    d1pe = 0
    d1pf = 0
    d1pg = 0
    # print(mobile[1:3],mobile[3:5])
    if result2p1 != "":
        d1pa = (mobile[1:3]).count(result2p1)
        d1pb = (mobile[3:5]).count(result2p1)
        if d1pb == 1:
            d1pb = 1
        else:
            d1pb = 0
            d1pc = (mobile[4:6]).count(result2p1)
            if d1pc == 1:
                d1pc = 1
            else:
                d1pc = 0
                d1pd = (mobile[5:7]).count(result2p1)
                if d1pd == 1:
                    d1pd = 1
                else:
                    d1pd = 0
                    d1pe = (mobile[6:8]).count(result2p1)
                    if d1pe == 1:
                        d1pe = 1
                    else:
                        d1pe = 0
                        d1pf = (mobile[7:9]).count(result2p1)
                        if d1pf == 1:
                            d1pf = 1
                        else:
                            d1pf = 0
                            d1pg = (mobile[8:10]).count(result2p1)
                            if d1pg == 1:
                                d1pg = 1
                            else:
                                d1pg = 0

    d1p0 = d1pa + d1pb + d1pc + d1pd + d1pe + d1pf + d1pg
    # print(d1p0)

    pos1 = 0
    pos2 = 0
    pos3 = 0
    pos4 = 0
    pos5 = 0
    pos6 = 0
    pos7 = 0
    pos8 = 0
    pos9 = 0
    pos10 = 0
    pos11 = 0
    pos12 = 0

    # extracting 3 digit sequence position
    if result3s0 != "":
        pos1 = 0
    if result3s1 != "":
        pos1 = 1

    if result3s2 != "":
        pos1 = 2
    if result3s3 != "":
        pos1 = 3
    if result3s4 != "":
        pos1 = 4
    if result3s5 != "":
        pos1 = 5
    if result3s6 != "":
        pos1 = 6
    if result3s7 != "":
        pos1 = 7

    # extracting 3 digit repeat no. position
    if result3t0 != "":
        pos2 = 0
    if result3t1 != "":
        pos2 = 1
    if result3t2 != "":
        pos2 = 2
    if result3t3 != "":
        pos2 = 3
    if result3t4 != "":
        pos2 = 4
    if result3t5 != "":
        pos2 = 5
    if result3t6 != "":
        pos2 = 6
    if result3t7 != "":
        pos2 = 7
    # extracting 2 digit repeat position
    if result2t0 != "":
        pos3 = 0
    if result2t1 != "":
        pos3 = 1
    if result2t2 != "":
        pos3 = 2
    if result2t3 != "":
        pos3 = 3
    if result2t4 != "":
        pos3 = 4
    if result2t5 != "":
        pos3 = 5
    if result2t6 != "":
        pos3 = 6
    if result2t7 != "":
        pos3 = 7
    if result2t8 != "":
        pos3 = 8
    # extracting 4 digit repeat no. position
    if result4t0 != "":
        pos4 = 0
    if result4t1 != "":
        pos4 = 1
    if result4t2 != "":
        pos4 = 2
    if result4t3 != "":
        pos4 = 3
    if result4t4 != "":
        pos4 = 4
    if result4t5 != "":
        pos4 = 5
    if result4t6 != "":
        pos4 = 6
    # extracting 4 digit sequence no. position
    if result4s0 != "":
        pos5 = 0
    if result4s1 != "":
        pos5 = 1
    if result4s2 != "":
        pos5 = 2
    if result4s3 != "":
        pos5 = 3
    if result4s4 != "":
        pos5 = 4
    if result4s5 != "":
        pos5 = 5
    if result4s6 != "":
        pos5 = 6
    # extracting 5 digit sequence no. position
    if result5s0 != "":
        pos6 = 0
    if result5s1 != "":
        pos6 = 1
    if result5s2 != "":
        pos6 = 2
    if result5s3 != "":
        pos6 = 3
    if result5s4 != "":
        pos6 = 4
    if result5s5 != "":
        pos6 = 5
    # extracting 5 digit repeat no. position

    if result5t0 != "":
        pos7 = 0
    if result5t1 != "":
        pos7 = 1
    if result5t2 != "":
        pos7 = 2
    if result5t3 != "":
        pos7 = 3
    if result5t4 != "":
        pos7 = 4
    if result5t5 != "":
        pos7 = 5
    # extracting 6 digit seq no. position
    if result6s0 != "":
        pos8 = 0
    if result6s1 != "":
        pos8 = 1
    if result6s2 != "":
        pos8 = 2
    if result6s3 != "":
        pos8 = 3
    if result6s4 != "":
        pos8 = 4
    # extracting 6 digit repeat no. position
    if result6t0 != "":
        pos9 = 0
    if result6t1 != "":
        pos9 = 1
    if result6t2 != "":
        pos9 = 2
    if result6t3 != "":
        pos9 = 3
    if result6t4 != "":
        pos9 = 4
    # extracting 7 digit repeat no. position
    if result7t0 != "":
        pos10 = 0
    if result7t1 != "":
        pos10 = 1
    if result7t2 != "":
        pos10 = 2
    if result7t3 != "":
        pos10 = 3
    # extracting 8 digit repeat no. position
    if result8t0 != "":
        pos11 = 0
    if result8t1 != "":
        pos11 = 1
    if result8t2 != "":
        pos11 = 2
    # extracting 7 digit seq no. position
    if result7s0 != "":
        pos12 = 0
    if result7s1 != "":
        pos12 = 1
    if result7s2 != "":
        pos12 = 2
    if result7s3 != "":
        pos12 = 3
    # print("DP0 : "+str(dp0) +","+ " DP1 : "+str(dp1)+","+ " DP2 : "+str(dp2) +","+ " DP3 : "+str(dp3)+","+ " D1P0 : "+str(d1p0))
    # print("PC2 : "+str(pc2) +","+ " PC3 : "+str(pc3)+","+ " PC4 : "+str(pc4) +","+ " PC5 : "+str(pc5) +","+ " PC6 : "+str(pc6) +","+ " PC7 : "+str(pc7) +","+ " PC8 : "+str(pc8))
    # print("PPC2 : "+str(ppc2) +","+ " PPC3 : "+str(ppc3)+","+ " PPC4 : "+str(ppc4) +","+ " PPC5 : "+str(ppc5) +","+ " PPC6 : "+str(ppc6) +","+ " PPC7 : "+str(ppc7) +","+ " PPC8 : "+str(ppc8))
    # print("TC2 : "+str(tc2) +","+ " TC3 : "+str(tc3)+","+ " TC4 : "+str(tc4) +","+ " TC5 : "+str(tc5) +","+ " TC6 : "+str(tc6) +","+ " TC7 : "+str(tc7) +","+ " TC8 : "+str(tc8))
    # print("PTC2 : "+str(ptc2) +","+ " PTC3 : "+str(ptc3)+","+ " PTC4 : "+str(ptc4) +","+ " PTC5 : "+str(ptc5) +","+ " PTC6 : "+str(ptc6) +","+ " PTC7 : "+str(ptc7) +","+ " PTC8 : "+str(ptc8))
    # print("SC3 : "+str(sc3)+","+ " SC4 : "+str(sc4) +","+ " SC5 : "+str(sc5) +","+ " SC6 : "+str(sc6) +","+ " SC7 : "+str(sc7) +","+ " SC8 : "+str(sc8))
    # print("PSC3 : "+str(psc3)+","+ " PSC4 : "+str(psc4) +","+ " PSC5 : "+str(psc5) +","+ " PSC6 : "+str(psc6) +","+ " PSC7 : "+str(psc7) +","+ " PSC8 : "+str(psc8))
    # print("pc4p : " + str(pc4p) + "," + " pc4p1 : " + str(pc4p1) + "," + " pc4p2 : " + str(pc4p2) )
    # print("ppc4p : " + str(ppc4p) + "," + " ppc4p1 : " + str(ppc4p1) + "," + " ppc4p2 : " + str(ppc4p2) )
    # print("pc3p : " + str(pc3p) + "," + " pc3p1 : " + str(pc3p1) + "," + " pc3p2 : " + str(pc3p2) + "," + " pc3p3 : " + str(pc3p3)+ "," + " pc3p4 : " + str(pc3p4) )
    # print("ppc3p : " + str(ppc3p) + "," + " ppc3p1 : " + str(ppc3p1) + "," + " ppc3p2 : " + str(ppc3p2) + "," + " ppc3p3 : " + str(ppc3p3)+ "," + " ppc3p4 : " + str(ppc3p4) )
    #
    # print("1 seq3 : "+str(pos1)+","+"2 rep3 : "+str(pos2)+","+"3 rep2 : "+str(pos3)+","+"4 rep4 : "+str(pos4)+","+"5 seq4 : "+str(pos5)+","+"6 seq5 : "+str(pos6)+","+"7 rep5 : "+str(pos7)+","+"8 seq6 : "+str(pos8)+","+"9 rep6 : "+str(pos9)+","+"10 rep7 : "+str(pos10)+","+"11 rep8 : "+str(pos11)+","+"12 seq7 : "+str(pos12))

    # print("---------------------------------------------------------------------------------------------------")
    if result10s0 != "":
        p1 = "10 digit - 10 digit sequence found p1"
        print(p1)
        p1 = "0000000001" + p1
    if result10t0 != "":
        p2 = "10 digit - 10 digit repeat no. found p2"
        print(p2)
        p2 = "0000000004" + p2
    if (result2t0 != "" and result2t0 != result2t2) and (result2t2 != "" and result2t2 != result2t4) and (
            result2t4 != "" and result2t4 != result2t6) and (
            result2t6 != "" and result2t6 != result2t8 and result2t8 != ""):
        p3 = "10 digit - 2 digit different repeat no. 5 times found p3"
        print(p3)
        p3 = "0000040000" + p3
    if (result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4) and (
            result2p6 != result2p0 and result2p6 == result2p8 and result2p8 != ""):
        p4 = "10 digit - same 2 digit no. 3 times and different 2 digit no. 2 times found p4"
        print(p4)
        p4 = "0000004000" + p4
    if (result2p0 != "" and result2p0 == result2p2) and (
            result2p4 != result2p0 and result2p4 == result2p6 and result2p4 == result2p8 and result2p8 != ""):
        p5 = "10 digit - same 2 digit no. 2 times and different 2 digit no. 3 times found p5"
        print(p5)
        p5 = "0000003999" + p5
    if result8t0 != "" and result2t8 != "":
        p6 = "10 digit - 8 digit repeat and 2 digit repeat no.found p6"
        print(p6)
        p6 = "0000000040" + p6
    if result8t2 != "" and result2t0 != "":
        p7 = "10 digit - 2 digit repeat and 8 digit repeat no.found p7"
        print(p7)
        p7 = "0000000040" + p7
    if (sc8 == 1) and (result8s1 != "" and result1p0 == result1p9):
        p8 = "10 digit - 8 digit seq no.found with same starting and ending no. p8"
        print(p8)
        p8 = "0000000024" + p8
    if result8s2 != "" and result2t0 != "":
        p9 = "10 digit - 2 digit repeat and 8 digit seq no.found p9"
        print(p9)
        p9 = "0000000024" + p9
    if result8s0 != "" and result2t8 != "":
        p10 = "10 digit - 8 digit seq and 2 digit repeat no.found p10"
        print(p10)
        p10 = "0000000030" + p10
    if result7s0 != "" and result3t7 != "":
        p11 = "10 digit - 7 digit seq and 3 digit repeat no.found p11"
        print(p11)
        p11 = "0000000040" + p11
    if result7s0 != "" and result3s7 != "":
        p12 = "10 digit - 7 digit seq and 3 digit seq no.found p12"
        print(p12)
        p12 = "0000000064" + p12
    if result3s0 != "" and result7s3 != "":
        p13 = "10 digit - 3 digit seq and 7 digit seq no.found p13"
        print(p13)
        p13 = "0000000048" + p13
    if result3s0 != "" and result7t3 != "":
        p14 = "10 digit - 3 digit seq and 7 digit repeat no.found p14"
        print(p14)
        p14 = "0000000060" + p14
    if result3t0 != "" and result7s3 != "":
        p15 = "10 digit - 3 digit repeat and 7 digit seq no.found p15"
        print(p15)
        p15 = "0000000032" + p15
    if result3t0 != "" and result7t3 != "":
        p16 = "10 digit - 3 digit repeat and 7 digit repeat no.found p16"
        print(p16)
        p16 = "0000000040" + p16
    if result7t0 != "" and result3s7 != "":
        p17 = "10 digit - 7 digit repeat and 3 digit seq no.found p17"
        print(p17)
        p17 = "0000000064" + p17
    if result7t0 != "" and result3t7 != "":
        p18 = "10 digit - 7 digit repeat and 3 digit repeat no.found p18"
        print(p18)
        p18 = "0000000040" + p18
    if result6t0 != "" and result4t6 != "":
        p19 = "10 digit - 6 digit repeat and 4 digit repeat no.found p19"
        print(p19)
        p19 = "0000000040" + p19
    if result6t0 != "" and result4s6 != "":
        p20 = "10 digit - 6 digit repeat and 4 digit seq no.found p20"
        print(p20)
        p20 = "0000000056" + p20
    if result6s0 != "" and result4t6 != "":
        p21 = "10 digit - 6 digit seq and 4 digit repeat no.found p21"
        print(p21)
        p21 = "0000000040" + p21
    if result6s0 != "" and result4s6 != "":
        p22 = "10 digit - 6 digit seq and 4 digit seq no.found p22"
        print(p22)
        p22 = "0000000056" + p22
    if result4s0 != "" and result6s4 != "":
        p23 = "10 digit - 4 digit seq and 6 digit seq no.found p23"
        print(p23)
        p23 = "0000000050" + p23
    if result4s0 != "" and result6t4 != "":
        p24 = "10 digit - 4 digit seq and 6 digit repeat no.found p24"
        print(p24)
        p24 = "0000000050" + p24
    if result4t0 != "" and result6t4 != "":
        p25 = "10 digit - 4 digit repeat and 6 digit repeat no.found p25"
        print(p25)
        p25 = "0000000040" + p25
    if result4t0 != "" and result6s4 != "":
        p26 = "10 digit - 4 digit repeat and 6 digit seq no.found p26"
        print(p26)
        p26 = "0000000040" + p26
    if result5t0 != "" and result5s5 != "":
        p27 = "10 digit - 5 digit repeat and 5 digit seq no.found p27"
        print(p27)
        p27 = "0000000048" + p27
    if result5t0 != "" and result5t5 != "":
        p28 = "10 digit - 5 digit repeat and 5 digit repeat no.found p28"
        print(p28)
        p28 = "0000000040" + p28
    if result5s0 != "" and result5t5 != "":
        p29 = "10 digit - 5 digit seq and 5 digit repeat no.found p29"
        print(p29)
        p29 = "0000000040" + p29
    if result5s0 != "" and result5s5 != "":
        p30 = "10 digit - 5 digit seq and 5 digit seq no.found p30"
        print(p30)
        p30 = "0000000048" + p30
    if result9s0 != "":
        p31 = "9 digit - 9 digit seq no. found at start p31"
        print(p31)
        p31 = "0000000020" + p31
    if result9s1 != "":
        p32 = "9 digit - 9 digit seq no. found at end p32"
        print(p32)
        p32 = "0000000016" + p32
    if result9t0 != "":
        p33 = "9 digit - 9 digit repeat no. found at start p33"
        print(p33)
        p33 = "0000000040" + p33
    if result9t1 != "":
        p34 = "9 digit - 9 digit repeat no. found at end p34"
        print(p34)
        p34 = "0000000040" + p34
    if (tc3 == 3 and tc4 < 1) and result3t0 != "" and result3t3 != "" and result3t6 != "":
        p35 = "9 digit - 3 digit repeat no. and 3 digit repeat no. and 3 digit repeat no found at start p35"
        print(p35)
        p35 = "0000004000" + p35
    if (tc3 == 3 and tc4 < 1) and result3t1 != "" and result3t4 != "" and result3t7 != "":
        p36 = "9 digit - 3 digit repeat no. and 3 digit repeat no. and 3 digit repeat no found at end p36"
        print(p36)
        p36 = "0000004000" + p36
    if sc3 == 3 and sc4 < 1 and result3s0 != "" and result3s3 != "" and result3s6 != "":
        p37 = "9 digit - 3 digit seq no. and 3 digit seq no. and 3 digit seq no found at start p37"
        print(p37)
        p37 = "0000015360" + p37
    if sc3 == 3 and sc4 < 1 and result3s1 != "" and result3s4 != "" and result3s7 != "":
        p38 = "9 digit - 3 digit seq no. and 3 digit seq no. and 3 digit seq no found at end p38"
        print(p38)
        p38 = "0000016384" + p38
    if (result2t0 != "") and (result4s2 != "") and (result4s6 != ""):
        p39 = "10 digit - 2 digit repeat no. and 4 digit seq and 4 digit seq no. found p39"
        print(p39)
        p39 = "0000000784" + p39
    if (result2t0 != "") and (result4t2 != "") and (result4s6 != ""):
        p40 = "10 digit - 2 digit repeat no. and 4 digit repeat and 4 digit seq no. found p40"
        print(p40)
        p40 = "0000000560" + p40
    if (result2t0 != "") and (result4t2 != "") and (result2t6 != "") and (result2t8 != ""):
        p41 = "10 digit - 2 digit repeat no. and 4 digit repeat and 2 digit repeat and 2 digit repeat no. found p41"
        print(p41)
        p41 = "0000004000" + p41
    if (result2t0 != "") and (result2t2 != "") and (result4s4 != "") and (result2t8 != ""):
        p42 = "10 digit - 2 digit repeat no. and 2 digit repeat and 4 digit seq and 2 digit repeat no. found p42"
        print(p42)
        p42 = "0000005600" + p42
    if (result2t0 != "") and (result2t2 != "") and (result4t4 != "") and (result2t8 != ""):
        p43 = "10 digit - 2 digit repeat no. and 2 digit repeat and 4 digit repeat and 2 digit repeat no. found p43"
        print(p43)
        p43 = "0000004000" + p43
    if (tc8 == 1 and tc9 < 1) and (result8t1 != "" or result8t2 != ""):
        p44 = "8 digit - 8 digit repeat no.found p44"
        print(p44)
        p44 = "0000001200" + p44
    if (tc8 == 1 and tc9 < 1) and (result8t1 != "" and result1p0 == result1p9):
        p45 = "10 digit - 8 digit repeat no.found with same starting and ending no. p45"
        print(p45)
        p45 = "0000000040" + p45
    if (sc8 == 1) and (result8s1 != "" or result8s2 != ""):
        p46 = "8 digit - 8 digit seq no.found p46"
        print(p46)
        p46 = "0000000780" + p46
    if ((result5t0 != "" and result4s5 != "") or (result5t1 != "" and result4s6 != "") or (
            result5t0 != "" and result4s6 != "")):
        p47 = "9 digit - 5 digit repeat and 4 digit seq no.found p47"
        print(p47)
        p47 = "0000001120" + p47
    if ((result5t0 != "" and result4t5 != "") or (result5t1 != "" and result4t6 != "") or (
            result5t0 != "" and result4t6 != "")):
        p48 = "9 digit - 5 digit repeat and 4 digit repeat no.found p48"
        print(p48)
        p48 = "0000000800" + p48
    if ((result5s0 != "" and result4t5 != "") or (result5s1 != "" and result4t6 != "") or (
            result5s0 != "" and result4t6 != "")):
        p49 = "9 digit - 5 digit seq and 4 digit repeat no.found p49"
        print(p49)
        p49 = "0000000880" + p49
    if ((result5s0 != "" and result4s5 != "") or (result5s1 != "" and result4s6 != "") or (
            result5s0 != "" and result4s6 != "")):
        p50 = "9 digit - 5 digit seq and 4 digit seq no.found p50"
        print(p50)
        p50 = "0000001232" + p50
    if ((result4s0 != "" and result5s4 != "") or (result4s1 != "" and result5s5 != "") or (
            result4s0 != "" and result5s5 != "")):
        p51 = "9 digit - 4 digit seq and 5 digit seq no.found p51"
        print(p51)
        p51 = "0000001272" + p51
    if ((result4s0 != "" and result5t4 != "") or (result4s1 != "" and result5t5 != "") or (
            result4s0 != "" and result5t5 != "")):
        p52 = "9 digit - 4 digit seq and 5 digit repeat no.found p52"
        print(p52)
        p52 = "0000001060" + p52
    if ((result4t0 != "" and result5t4 != "") or (result4t1 != "" and result5t5 != "") or (
            result4t0 != "" and result5t5 != "")):
        p53 = "9 digit - 4 digit repeat and 5 digit repeat no.found p53"
        print(p53)
        p53 = "0000000800" + p53
    if ((result4t0 != "" and result5s4 != "") or (result4t1 != "" and result5s5 != "") or (
            result4t0 != "" and result5s5 != "")):
        p54 = "9 digit - 4 digit repeat and 5 digit seq no.found p54"
        print(p54)
        p54 = "0000000960" + p54
    if ((result6t0 != "" and result3s6 != "") or (result6t1 != "" and result3s7 != "") or (
            result6t0 != "" and result3s7 != "")):
        p55 = "9 digit - 6 digit repeat and 3 digit seq no.found p55"
        print(p55)
        p55 = "0000001280" + p55
    if ((result6t0 != "" and result3t6 != "") or (result6t1 != "" and result3t7 != "") or (
            result6t0 != "" and result3t7 != "")):
        p56 = "9 digit - 6 digit repeat and 3 digit repeat no.found p56"
        print(p56)
        p56 = "0000000800" + p56
    if ((result6s0 != "" and result3s6 != "") or (result6s1 != "" and result3s7 != "") or (
            result6s0 != "" and result3s7 != "")):
        p57 = "9 digit - 6 digit seq and 3 digit seq no.found p57"
        print(p57)
        p57 = "0000001280" + p57
    if ((result6s0 != "" and result3t6 != "") or (result6s1 != "" and result3t7 != "") or (
            result6s0 != "" and result3t7 != "")):
        p58 = "9 digit - 6 digit seq and 3 digit repeat no.found p58"
        print(p58)
        p58 = "0000000800" + p58
    if ((result3t0 != "" and result6t3 != "") or (result3t0 != "" and result6t4 != "") or (
            result3t1 != "" and result6t4 != "")):
        p59 = "9 digit - 3 digit repeat and 6 digit repeat no.found p59"
        print(p59)
        p59 = "0000000800" + p59
    if ((result3s0 != "" and result6s3 != "") or (result3s0 != "" and result6s4 != "") or (
            result3s1 != "" and result6s4 != "")):
        p60 = "9 digit - 3 digit seq and 6 digit seq no.found p60"
        print(p60)
        p60 = "0000001240" + p60
    if ((result3s0 != "" and result6t3 != "") or (result3s0 != "" and result6t4 != "") or (
            result3s1 != "" and result6t4 != "")):
        p61 = "9 digit - 3 digit seq and 6 digit repeat no.found p61"
        print(p61)
        p61 = "0000001240" + p61
    if ((result7s0 != "" and result2t7 != "") or (result7s0 != "" and result2t8 != "") or (
            result7s1 != "" and result2t8 != "")):
        p62 = "9 digit - 7 digit seq and 2 digit repeat no.found p62"
        print(p62)
        p62 = "0000000720" + p62
    if ((result7t0 != "" and result2t7 != "") or (result7t0 != "" and result2t8 != "") or (
            result7t1 != "" and result2t8 != "")):
        p63 = "9 digit - 7 digit repeat and 2 digit repeat no.found p63"
        print(p63)
        p63 = "0000000800" + p63
    if ((result2t0 != "" and result7t2 != "") or (result2t0 != "" and result7t3 != "") or (
            result2t1 != "" and result7t3 != "")):
        p64 = "9 digit - 2 digit repeat and 7 digit repeat no.found p64"
        print(p64)
        p64 = "0000000800" + p64
    if ((result2t0 != "" and result7s2 != "") or (result2t0 != "" and result7s3 != "") or (
            result2t1 != "" and result7s3 != "")):
        p65 = "9 digit - 2 digit repeat and 7 digit seq no.found p65"
        print(p65)
        p65 = "0000000640" + p65
    if (result8t0 != ""):
        p66 = "8 digit - 8 digit repeat no.found at start p66"
        print(p66)
        p66 = "0000000400" + p66
    if (result8s0 != ""):
        p67 = "9 digit - 8 digit seq no.found at start p67"
        print(p67)
        p67 = "0000000300" + p67
    if (
            result2t0 != "" and result2t0 != result2t2 and result2t2 != "" and result2t2 != result2t4 and result2t4 != "" and result2t4 != result2t6 and result2t6 != ""):
        p68 = "8 digit - 2 digit repeat no. 4 times found at start p68"
        print(p68)
        p68 = "0000400000" + p68
    if result2t2 != "" and result2t2 != result2t4 and result2t4 != "" and result2t4 != result2t6 and result2t6 != "" and result2t6 != result2t8 and result2t8 != "":
        p69 = "8 digit - 2 digit repeat no. 4 times found at end p69"
        print(p69)
        p69 = "0000400000" + p69
    if (
            result1p0 == result1p9) and result2t1 != "" and result2t1 != result2t3 and result2t3 != "" and result2t3 != result2t5 and result2t5 != "" and result2t5 != result2t7 and result2t7 != "":
        p70 = "10 digit - 2 digit repeat no. 4 times found with same starting and ending no. p70"
        print(p70)
        p70 = "0000040000" + p70
    if (tc2 < 6 and tc2 > 3 and tc3 < 1) and (ptc2 != "" and pos3 >= int(ptc2[0:1]) + 6):
        p71 = "8 digit - 2 digit repeat no. 4 times found p71"
        print(p71)
        p71 = "0002000000" + p71

    if (result3s0 != "") and (result4t3 != "") and (result3s7 != ""):
        p72 = "10 digit - 3 digit seq no. and 4 digit repeat no. and 3 digit seq no. found p72"
        print(p72)
        p72 = "0000000960" + p72
    if (result3s0 != "") and (result3s3 != "") and (result4t6 != ""):
        p73 = "10 digit - 3 digit seq no. and 3 digit seq no. and 4 digit repeat no. found p73"
        print(p73)
        p73 = "0000000960" + p73
    if (result3s0 != "") and (result4s3 != "") and (result3t7 != ""):
        p74 = "10 digit - 3 digit seq no. and 4 digit seq no. and 3 digit repeat no. found p74"
        print(p74)
        p74 = "0000000840" + p74
    if (result3s0 != "") and (result4s3 != "") and (result3s7 != ""):
        p75 = "10 digit - 3 digit seq no. and 4 digit seq no. and 3 digit seq no. found p75"
        print(p75)
        p75 = "0000001344" + p75
    if (result3s0 != "") and (result3s3 != "") and (result4s6 != ""):
        p76 = "10 digit - 3 digit seq no. and 3 digit seq no. and 4 digit seq no. found p76"
        print(p76)
        p76 = "0000001344" + p76
    if (result3s0 != "") and (result2t3 != "") and (result5t5 != ""):
        p77 = "10 digit - 3 digit seq no. and 2 digit repeat no. and 5 digit repeat no. found p77"
        print(p77)
        p77 = "0000000600" + p77
    if (result3s0 != "") and (result5t3 != "") and (result2t8 != ""):
        p78 = "10 digit - 3 digit seq no. and 5 digit repeat no. and 2 digit repeat no. found p78"
        print(p78)
        p78 = "0000000600" + p78
    if (result3s0 != "") and (result5s3 != "") and (result2t8 != ""):
        p79 = "10 digit - 3 digit seq no. and 5 digit seq no. and 2 digit repeat no. found p79"
        print(p79)
        p79 = "0000000720" + p79
    if (result3s0 != "") and (result2t3 != "") and (result3s5 != "") and (result2t8 != ""):
        p80 = "10 digit - 3 digit seq no. and 2 digit repeat no. and 3 digit seq no. and 2 digit repeat no. found p80"
        print(p80)
        p80 = "0000009600" + p80
    if (result3s0 != "") and (result3s3 != "") and (result2t6 != "") and (result2t8 != ""):
        p81 = "10 digit - 3 digit seq no. and 3 digit seq no. and 2 digit repeat no. and 2 digit repeat no. found p81"
        print(p81)
        p81 = "0000009600" + p81
    if (tc2 == 1 and tc3 < 1) and ((result2t0 != "") or (result2t8 != "")):
        p82 = "2 digit - 2 digit repeat no. found at start or end p82"
        print(p82)
        p82 = "0400000000" + p82
    if (tc2 == 1 and tc3 < 1) and (
            result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "" or result2t6 != "" or result2t7 != ""):
        p83 = "2 digit - 2 digit repeat no. found p83"
        print(p83)
        p83 = "0800000000" + p83
    if ((tc2 == 2 and tc3 < 1) or (tc2 > 2 and tc3 == 1)):
        p84 = "4 digit - 2 digit repeat no. found and 2 digit repeat no. found p84"
        print(p84)
        p84 = "0160000000" + p84
    if (tc5 == 1) and (ptc5 != "" and int(ptc2[1:2]) >= int(ptc2[0:1]) + 2 and pos7 >= int(ptc2[1:2]) + 2) and (
            result2t0 != "" or result2t1 != "") and (result2t2 != "" or result2t3 != "") and (
            result5t4 != "" or result5t5 != ""):
        p85 = "9 digit - 2 digit repeat no. found and 2 digit repeat and 5 digit repeat no. found p85"
        print(p85)
        p85 = "0000016000" + p85
    if (sc4 > 0 and tc2 > 1) and (int(ptc2[1:2]) >= int(ptc2[0:1]) + 2 and int(psc4[0:1]) >= int(ptc2[1:2]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result2t2 != "" or result2t3 != "" or result2t4 != "") and (
            result4s4 != "" or result4s5 != "" or result4s6 != ""):
        p86 = "8 digit - 2 digit repeat no. found and 2 digit repeat and 4 digit seq no. found p86"
        print(p86)
    if (sc4 == 2 and tc2 == 2) and (int(ptc2[1:2]) >= int(ptc2[0:1]) + 2 and int(psc4[1:2]) >= int(ptc2[1:2]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result2t2 != "" or result2t3 != "" or result2t4 != "") and (
            result4s4 != "" or result4s5 != "" or result4s6 != ""):
        p86 = "8 digit - 2 digit repeat no. found and 2 digit repeat and 4 digit seq no. found p86"
        print(p86)
    if p86 != "":
        print(p86)
        p86 = "0000280000" + p86
    if (tc4 == 1) and (ptc4 != "" and int(ptc2[1:2]) >= int(ptc2[0:1]) + 2 and pos4 >= int(ptc2[1:2]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result2t2 != "" or result2t3 != "" or result2t4 != "") and (
            result4t4 != "" or result4t5 != "" or result4t6 != ""):
        p87 = "8 digit - 2 digit repeat no. found and 2 digit repeat and 4 digit repeat no. found p87"
        print(p87)
        p87 = "0000200000" + p87
    if (tc4 == 1 and tc5 < 1) and (pos3 > pos2 + 4) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result4t2 != "" or result4t3 != "" or result4t4 != "") and (
            result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p88 = "8 digit - 2 digit repeat no. found and 4 digit repeat and 2 digit repeat no. found p88"
        print(p88)
        p88 = "0000200000" + p88
    if (sc5 > 0 and tc2 > 1) and (
            psc5 != "" and int(ptc2[1:2]) >= int(ptc2[0:1]) + 2 and pos6 >= int(ptc2[1:2]) + 2) and (
            result2t0 != "" or result2t1 != "") and (result2t2 != "" or result2t3 != "") and (
            result5s4 != "" or result5s5 != ""):
        p89 = "9 digit - 2 digit repeat no. found and 2 digit repeat and 5 digit seq no. found p89"
        print(p89)
        p89 = "0000019200" + p89
    if (result2t0 != "") and (result8s2 != ""):
        p90 = "10 digit - 2 digit repeat no. and 8 digit seq no. found p90"
        print(p90)
        p90 = "0000000024" + p90
    if (result2t0 != "") and (result8t2 != ""):
        p91 = "10 digit - 2 digit repeat no. and 8 digit repeat no. found p91"
        print(p91)
        p91 = "0000000040" + p91
    if (result2t0 != "") and (result2t2 != "") and (result6t4 != ""):
        p92 = "10 digit - 2 digit repeat no. and 2 digit repeat and 6 digit repeat no. found p92"
        print(p92)
        p92 = "0000000400" + p92
    if (result2t0 != "") and (result2t2 != "") and (result6s4 != ""):
        p93 = "10 digit - 2 digit repeat no. and 2 digit repeat and 6 digit seq no. found p93"
        print(p93)
        p93 = "0000000400" + p93
    if (result2t0 != "") and (result6t2 != "") and (result2t8 != ""):
        p94 = "10 digit - 2 digit repeat no. and 6 digit repeat and 2 digit repeat no. found p94"
        print(p94)
        p94 = "0000000400" + p94
    if (result2t0 != "") and (result6s2 != "") and (result2t8 != ""):
        p95 = "10 digit - 2 digit repeat no. and 6 digit seq and 2 digit repeat no. found p95"
        print(p95)
        p95 = "0000000400" + p95
    if (result2t0 != "") and (result3t2 != "") and (result5t5 != ""):
        p96 = "10 digit - 2 digit repeat no. and 3 digit repeat and 5 digit repeat no. found p96"
        print(p96)
        p96 = "0000000400" + p96
    if (result2t0 != "") and (result3t2 != "") and (result5s5 != ""):
        p97 = "10 digit - 2 digit repeat no. and 3 digit repeat and 5 digit seq no. found p97"
        print(p97)
        p97 = "0000000480" + p97
    if (result2t0 != "") and (result3s2 != "") and (result5t5 != ""):
        p98 = "10 digit - 2 digit repeat no. and 3 digit seq and 5 digit repeat no. found p98"
        print(p98)
        p98 = "0000000640" + p98
    if (result2t0 != "") and (result5s2 != "") and (result3t7 != ""):
        p99 = "10 digit - 2 digit repeat no. and 5 digit seq and 3 digit repeat no. found p99"
        print(p99)
        p99 = "0000000480" + p99
    if (result2t0 != "") and (result5t2 != "") and (result3s7 != ""):
        p100 = "10 digit - 2 digit repeat no. and 5 digit repeat and 3 digit seq no. found p100"
        print(p100)
        p100 = "0000000640" + p100
    if (result2t0 != "") and (result5t2 != "") and (result3t7 != ""):
        p101 = "10 digit - 2 digit repeat no. and 5 digit repeat and 3 digit repeat no. found p101"
        print(p101)
        p101 = "0000000400" + p101
    if (result2t0 != "") and (result4t2 != "") and (result4t6 != ""):
        p102 = "10 digit - 2 digit repeat no. and 4 digit repeat and 4 digit repeat no. found p102"
        print(p102)
        p102 = "0000000400" + p102
    if (result2t0 != "") and (result4s2 != "") and (result4t6 != ""):
        p103 = "10 digit - 2 digit repeat no. and 4 digit seq and 4 digit repeat no. found p103"
        print(p103)
        p103 = "0000000560" + p103
    if (sc6 > 0 and tc2 > 0) and (ptc2 != "" and psc6 != "" and int(psc6[0:1]) >= int(ptc2[0:1]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result6s2 != "" or result6s3 != "" or result6s4 != ""):
        p104 = "8 digit - 2 digit repeat and 6 digit seq no.found p104"
        print(p104)
    if (sc6 == 2 and tc2 == 1) and (ptc2 != "" and psc6 != "" and int(psc6[1:2]) >= int(ptc2[0:1]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result6s2 != "" or result6s3 != "" or result6s4 != ""):
        p104 = "8 digit - 2 digit repeat and 6 digit seq no.found p104"
        print(p104)
    if p104 != "":
        print(p104)
        p104 = "0000016000" + p104
    if (result2t0 != "" and result6s2 != "" and result2t8 != ""):
        p105 = "10 digit - 2 digit repeat and 6 digit seq no. and 2 digit repeat mo. found p105"
        print(p105)
        p105 = "0000000400" + p105
    if (tc2 > 0 and tc6 == 1 and ptc6 != "" and ptc2 != "") and (int(ptc6[0:1]) >= int(ptc2[0:1]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result6t2 != "" or result6t3 != "" or result6t4 != ""):
        p106 = "8 digit - 2 digit repeat and 6 digit repeat no.found p106"
        print(p106)
        p106 = "0000016000" + p106
    if (result2t0 != "" and result6t2 != "" and result2t8 != ""):
        p107 = "10 digit - 2 digit repeat and 6 digit repeat no. and 2 digit repeat mo. found p107"
        print(p107)
        p107 = "0000000400" + p107
    if (tc2 > 0 and tc6 == 1) and (result6t0 != "" or result6t1 != "" or result6t2 != "") and (
            result2t6 != "" or result2t7 != "" or result2t8 != "") and (pos3 >= pos9 + 6):
        p108 = "8 digit - 6 digit repeat and 2 digit repeat no.found p108"
        print(p108)
        p108 = "0000016000" + p108
    if (result6t0 != "" and result2t6 != "" and result2t8 != ""):
        p109 = "10 digit - 6 digit repeat and 2 digit repeat and 2 digit repeat no.found p109"
        print(p109)
        p109 = "0000000400" + p109
    if ((ptc2 != "" and psc6 != "" and (int(ptc2[0:1]) >= int(psc6[0:1]) + 6) and tc3 == 0) or (
            ptc2 != "" and psc6 != "" and (int(ptc2[0:1]) >= int(psc6[0:1]) + 5) and tc3 == 1)) and (
            result6s0 != "" or result6s1 != "" or result6s2 != "") and (
            result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p110 = "8 digit - 6 digit seq and 2 digit repeat no.found p110"
        print(p110)
        p110 = "0000016000" + p110
    if (result6s0 != "" and result2t6 != "" and result2t8 != ""):
        p111 = "10 digit - 6 digit seq and 2 digit repeat and 2 digit repeat no.found p111"
        print(p111)
        p111 = "0000000400" + p111
    if ((tc3 == 4 and tc6 < 1) or (tc3 == 5 and tc6 == 1)) and (
            (result3t0 != "" and result5t3 != "") or (result3t0 != "" and result5t4 != "") or (
            result3t0 != "" and result5t5 != "") or (result3t1 != "" and result5t4 != "") or (
                    result3t1 != "" and result5t5 != "") or (result3t2 != "" and result5t5 != "")):
        p112 = "8 digit - 3 digit repeat and 5 digit repeat no.found p112"
        print(p112)
        p112 = "0000016000" + p112
    if (result3t0 != "" and result5t3 != "" and result2t8 != ""):
        p113 = "10 digit - 3 digit repeat and 5 digit repeat and 2 digit repeat no.found p113"
        print(p113)
        p113 = "0000000400" + p113
    if (sc5 > 0 and tc3 > 0) and (ptc3 != "" and psc5 != "" and int(psc5[0:1]) >= int(ptc3[0:1]) + 3) and (
            (result3t0 != "" or result3t1 != "" or result3t2 != "") and (
            result5s3 != "" or result5s4 != "" or result5s5 != "")):
        p114 = "8 digit - 3 digit repeat and 5 digit seq no.found p114"
        print(p114)
        p114 = "0000019200" + p114
    if (result3t0 != "" and result5s3 != "" and result2t8 != ""):
        p115 = "10 digit - 3 digit repeat and 5 digit seq and 2 digit repeat no.found p115"
        print(p115)
        p115 = "0000000480" + p115
    if (sc5 == 1 and sc3 == 4) and (psc3 != "" and psc5 != "" and int(psc5[0:1]) >= int(psc3[0:1]) + 3) and (
            (result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result5s3 != "" or result5s4 != "" or result5s5 != "")):
        p116 = "8 digit - 3 digit seq and 5 digit seq no.found p116"
        print(p116)
    if (sc5 == 1 and sc3 == 5) and (psc3 != "" and psc5 != "" and int(psc5[0:1]) >= int(psc3[0:1]) + 3) and (
            (result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result5s3 != "" or result5s4 != "" or result5s5 != "")):
        p116 = "8 digit - 3 digit seq and 5 digit seq no.found p116"
        print(p116)
    if p116 != "":
        print(p116)
        p116 = "0000022560" + p116
    if (result3s0 != "" and result5s3 != "" and result2t8 != ""):
        p117 = "10 digit - 3 digit seq and 5 digit seq and 2 digit repeat no.found p117"
        print(p117)
        p117 = "0000000720" + p117
    if ((ptc5 != "" and psc3 != "" and (int(ptc5[0:1]) >= int(psc3[0:1]) + 3) and tc6 == 0) or (
            ptc5 != "" and psc3 != "" and (int(ptc5[0:1]) >= int(psc3[0:1]) + 2) and tc6 == 1)) and (
            (result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result5t3 != "" or result5t4 != "" or result5t5 != "")):
        p118 = "8 digit - 3 digit seq and 5 digit repeat no.found p118"
        print(p118)
        p118 = "0000018800" + p118
    if (result3s0 != "" and result5t3 != "" and result2t8 != ""):
        p119 = "10 digit - 3 digit seq and 5 digit repeat and 2 digit repeat no.found p119"
        print(p119)
        p119 = "0000000600" + p119
    if ((ptc3 != "" and psc5 != "" and (int(ptc3[0:1]) >= int(psc5[0:1]) + 5) and tc4 == 0) or (
            ptc3 != "" and psc5 != "" and (int(ptc3[0:1]) >= int(psc5[0:1]) + 4) and tc4 == 1)) and (
            (result5s0 != "" or result5s1 != "" or result5s2 != "") and (
            result3t5 != "" or result3t6 != "" or result3t7 != "")):
        p120 = "8 digit - 5 digit seq and 3 digit repeat no.found p120"
        print(p120)
        p120 = "0000012800" + p120
    if (result5s0 != "" and result3t5 != "" and result2t8 != ""):
        p121 = "10 digit - 5 digit seq and 3 digit repeat and 2 digit repeat no.found p121"
        print(p121)
        p121 = "0000000400" + p121
    if (sc5 > 0) and (psc5 != "" and pos1 >= int(psc5[0:1]) + 5) and (
            (result5s0 != "" or result5s1 != "" or result5s2 != "") and (
            result3s5 != "" or result3s6 != "" or result3s7 != "")):
        p122 = "8 digit - 5 digit seq and 3 digit seq no.found p122"
        print(p122)
        p122 = "0000021760" + p122
    if (result5s0 != "" and result3s5 != "" and result2t8 != ""):
        p123 = "10 digit - 5 digit seq and 3 digit seq and 2 digit repeat no.found p123"
        print(p123)
        p123 = "0000000640" + p123
    if (tc5 > 0 and sc3 > 0) and (ptc5 != "" and psc3 != "" and pos1 >= int(ptc5[0:1]) + 5) and (
            (result5t0 != "" or result5t1 != "" or result5t2 != "") and (
            result3s5 != "" or result3s6 != "" or result3s7 != "")):
        p124 = "8 digit - 5 digit repeat and 3 digit seq no.found p124"
        print(p124)
        p124 = "0000019200" + p124
    if (result5t0 != "" and result3s5 != "" and result2t8 != ""):
        p125 = "10 digit - 5 digit repeat and 3 digit seq and 2 digit repeat no.found p125"
        print(p125)
        p125 = "0000000640" + p125
    if ((tc3 == 4 and tc6 < 1) or (tc3 > 4 and tc6 == 1)) and (
            (result5t0 != "" or result5t1 != "" or result5t2 != "") and (
            result3t5 != "" or result3t6 != "" or result3t7 != "")):
        p126 = "8 digit - 5 digit repeat and 3 digit repeat no.found p126"
        print(p126)
        p126 = "0000012000" + p126
    if (result5t0 != "" and result3t5 != "" and result2t8 != ""):
        p127 = "10 digit - 5 digit repeat and 3 digit repeat and 2 digit repeat no.found p127"
        print(p127)
        p127 = "0000000400" + p127
    if ((tc2 == 6 and tc5 < 1) or (tc2 > 6 and tc5 == 1)) and (
            (result4t0 != "" or result4t1 != "" or result4t2 != "") and (
            result4t4 != "" or result4t5 != "" or result4t6 != "")):
        p128 = "8 digit - 4 digit repeat and 4 digit repeat no.found p128"
        print(p128)
        p128 = "0000012000" + p128
    if (result4t0 != "" and result4t4 != "" and result2t8 != ""):
        p129 = "10 digit - 4 digit repeat and 4 digit repeat and 2 digit repeat no.found p129"
        print(p129)
        p129 = "0000000400" + p129
    if (sc4 > 0 and tc4 > 0) and (psc4 != "" and ptc4 != "" and int(psc4[0:1]) >= int(ptc4[0:1]) + 4) and (
            (result4t0 != "" or result4t1 != "" or result4t2 != "") and (
            result4s4 != "" or result4s5 != "" or result4s6 != "")):
        p130 = "8 digit - 4 digit repeat and 4 digit seq no.found p130"
        print(p130)
    if (sc4 == 2 and tc4 == 1) and (psc4 != "" and ptc4 != "" and int(psc4[1:2]) >= int(ptc4[0:1]) + 4) and (
            (result4t0 != "" or result4t1 != "" or result4t2 != "") and (
            result4s4 != "" or result4s5 != "" or result4s6 != "")):
        p130 = "8 digit - 4 digit repeat and 4 digit seq no.found p130"
        print(p130)
    if p130 != "":
        print(p130)
        p130 = "0000016800" + p130
    if result4t0 != "" and result4s4 != "" and result2t8 != "":
        p131 = "10 digit - 4 digit repeat and 4 digit seq and 2 digit repeat no.found p131"
        print(p131)
        p131 = "0000000560" + p131
    if (sc4 > 1) and (psc4 != "" and pos5 >= int(psc4[0:1]) + 4) and (
            result4s0 != "" or result4s1 != "" or result4s2 != "") and (
            result4s4 != "" or result4s5 != "" or result4s6 != ""):
        p132 = "8 digit - 4 digit seq and 4 digit seq no.found p132"
        print(p132)
        p132 = "0000018200" + p132
    if result4s0 != "" and result4s4 != "" and result2t8 != "":
        p133 = "10 digit - 4 digit seq and 4 digit seq and 2 digit repeat no.found p133"
        print(p133)
        p133 = "0000000700" + p133

    if (result4s0 != "" and result4t4 != "" and result2t8 != ""):
        p134 = "10 digit - 4 digit seq and 4 digit repeat and 2 digit repeat no.found p134"
        print(p134)
        p134 = "0000000500" + p134
    if (tc2 == 5 and tc3 == 3 and tc5 < 1) and (
            (result3t0 != "" or result3t1 != "" or result3t2 != "" or result3t3 != "") and (
            result4t3 != "" or result4t4 != "" or result4t5 != "" or result4t6 != "")):
        p135 = "7 digit - 3 digit repeat and 4 digit repeat no.found p135"
        print(p135)
        p135 = "0000160000" + p135
    if (tc2 == 6 and tc3 == 3 and tc5 < 1) and (
            (result3t0 != "" or result3t1 != "") and (result4t3 != "" or result4t4 != "") and (
            result2t8 != "" or result2t7 != "")):
        p136 = "9 digit - 3 digit repeat and 4 digit repeat and 2 digit repeat no.found p136"
        print(p136)
        p136 = "0000008000" + p136
    if (result3t0 != "") and (result4t3 != "") and (result3t7 != ""):
        p137 = "10 digit - 3 digit repeat and 4 digit repeat and 3 digit repeat no.found p137"
        print(p137)
        p137 = "0000000400" + p137
    if (result3t0 != "") and (result4t3 != "") and (result3s7 != ""):
        p138 = "10 digit - 3 digit repeat and 4 digit repeat and 3 digit seq no.found p138"
        print(p138)
        p138 = "0000000640" + p138
    if (tc3 > 0 and sc4 > 0) and (pos5 >= pos2 + 3 or (pos5 >= pos4 + 3 and ppc4 != "")) and (
            (result3t0 != "" or result3t1 != "" or result3t2 != "" or result3t3 != "") and (
            result4s3 != "" or result4s4 != "" or result4s5 != "" or result4s6 != "")) \
            :
        p139 = "7 digit - 3 digit repeat and 4 digit seq no.found p139"
        print(p139)
    if (tc3 == 2 and sc4 == 1) and (ptc3 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc3[0:1]) + 3) and (
            (result3t0 != "" or result3t1 != "" or result3t2 != "" or result3t3 != "") and (
            result4s3 != "" or result4s4 != "" or result4s5 != "" or result4s6 != "")) \
            :
        p139 = "7 digit - 3 digit repeat and 4 digit seq no.found p139"
        print(p139)
    if p139 != "":
        print(p139)
        p139 = "0000224000" + p139
    if (tc3 > 0 and sc4 > 0) and (
            ptc3 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc3[0:1]) + 3 and pos3 >= int(psc4[0:1]) + 4) and (
            result3t0 != "" or result3t1 != "") and (result4s3 != "" or result4s4 != "") and (
            result2t8 != "" or result2t7 != ""):
        p140 = "9 digit - 3 digit repeat and 4 digit seq and 2 digit repeat no.found p140"
        print(p140)
        p140 = "0000011200" + p140

    if (result3t0 != "" and result4s3 != "" and result3t7 != ""):
        p141 = "10 digit - 3 digit repeat and 4 digit seq and 3 digit repeat no.found p141"
        print(p141)
        p141 = "0000000500" + p141
    if (result3t0 != "" and result4s3 != "" and result3s7 != ""):
        p142 = "10 digit - 3 digit repeat and 4 digit seq and 3 digit seq no.found p142"
        print(p142)
        p142 = "0000000896" + p142
    if (sc3 > 2 and sc4 < 3) and (psc4 != "" and pos5 >= int(psc3[0:1]) + 3) and (
            (result3s0 != "" or result3s1 != "" or result3s2 != "" or result3s3 != "") and (
            result4s3 != "" or result4s4 != "" or result4s5 != "" or result4s6 != "")):
        p143 = "7 digit - 3 digit seq and 4 digit seq no.found p143"
        print(p143)
        p143 = "0000352800" + p143
    if (sc4 > 0 and tc2 > 0) and (
            ptc2 != "" and psc4 != "" and int(ptc2[0:1]) >= int(psc3[0:1]) + 7 and pos3 >= pos5 + 4) and (
            (result3s0 != "" or result3s1 != "") and (result4s3 != "" or result4s4 != "") and (
            result2t8 != "" or result2t7 != "")):
        p144 = "9 digit - 3 digit seq and 4 digit seq and 2 digit repeat no.found p144"
        print(p144)
    if (sc4 == 2 and tc2 == 2) and (ptc2 != "" and psc4 != "" and pos3 >= int(psc3[0:1]) + 7 and pos3 >= pos5 + 4) and (
            (result3s0 != "" or result3s1 != "") and (result4s3 != "" or result4s4 != "") and (
            result2t8 != "" or result2t7 != "")):
        p144 = "9 digit - 3 digit seq and 4 digit seq and 2 digit repeat no.found p144"
        print(p144)
    if (sc4 == 1 and tc2 == 3) and (ptc2 != "" and psc4 != "" and pos3 >= int(psc3[0:1]) + 7 and pos3 >= pos5 + 4) and (
            (result3s0 != "" or result3s1 != "") and (result4s3 != "" or result4s4 != "") and (
            result2t8 != "" or result2t7 != "")):
        p144 = "9 digit - 3 digit seq and 4 digit seq and 2 digit repeat no.found p144"
        print(p144)
    if (sc4 == 1 and tc2 == 2) and (
            ptc2 != "" and psc4 != "" and pos3 >= int(psc3[0:1]) + 7 and pos3 >= int(psc4[0:1]) + 4) and (
            (result3s0 != "" or result3s1 != "") and (result4s3 != "" or result4s4 != "") and (
            result2t8 != "" or result2t7 != "")):
        p144 = "9 digit - 3 digit seq and 4 digit seq and 2 digit repeat no.found p144"
        print(p144)
    if p144 != "":
        print(p144)
        p144 = "0000017360" + p144
    if result3s0 != "" and result4s3 != "" and result3t7 != "":
        p145 = "10 digit - 3 digit seq and 4 digit seq and 3 digit repeat no.found  p145"
        print(p145)
        p145 = "0000000840" + p145
    if result3s0 != "" and result4s3 != "" and result3s7 != "":
        p146 = "10 digit - 3 digit seq and 4 digit seq and 3 digit seq no.found  p146"
        print(p146)
        p146 = "0000001344" + p146
    if (sc3 > 0 and tc4 > 0) and (ptc4 != "" and psc3 != "" and int(ptc4[0:1]) >= int(psc3[0:1]) + 3) and (
            (result3s0 != "" or result3s1 != "" or result3s2 != "" or result3s3 != "") and (
            result4t3 != "" or result4t4 != "" or result4t5 != "" or result4t6 != "")):
        p147 = "7 digit - 3 digit seq and 4 digit repeat no.found p147"
        print(p147)
    if (sc3 == 1 and tc4 == 2) and (ptc4 != "" and psc3 != "" and pos4 >= int(psc3[0:1]) + 3) and (
            (result3s0 != "" or result3s1 != "" or result3s2 != "" or result3s3 != "") and (
            result4t3 != "" or result4t4 != "" or result4t5 != "" or result4t6 != "")):
        p147 = "7 digit - 3 digit seq and 4 digit repeat no.found p147"
        print(p147)
    if p147 != "":
        print(p147)
        p147 = "0000252000" + p147
    if (tc4 > 0 and sc3 > 0) and (
            ptc4 != "" and psc3 != "" and int(ptc4[0:1]) >= int(psc3[0:1]) + 3 and pos3 >= int(ptc4[0:1]) + 4) and (
            (result3s0 != "" or result3s1 != "") and (result4t3 != "" or result4t4 != "") and (
            result2t8 != "" or result2t7 != "")):
        p148 = "9 digit - 3 digit seq and 4 digit repeat and 2 digit repeat no.found p148"
        print(p148)
    if (tc4 == 2 and sc3 == 1 and tc2 == 5) and (
            ptc4 != "" and psc3 != "" and int(ptc4[1:2]) >= int(psc3[0:1]) + 3 and pos3 >= int(ptc4[1:2]) + 4) and (
            (result3s0 != "" or result3s1 != "") and (result4t3 != "" or result4t4 != "") and (
            result2t8 != "" or result2t7 != "")):
        p148 = "9 digit - 3 digit seq and 4 digit repeat and 2 digit repeat no.found p148"
        print(p148)
    if p148 != "":
        print(p148)
        p148 = "0000012400" + p148
    if result3s0 != "" and result4t3 != "" and result3t7 != "":
        p149 = "10 digit - 3 digit seq and 4 digit repeat and 3 digit repeat no.found p149"
        print(p149)
        p149 = "0000000600" + p149
    if result3s0 != "" and result4t3 != "" and result3s7 != "":
        p150 = "10 digit - 3 digit seq and 4 digit repeat and 3 digit seq no.found p150"
        print(p150)
        p150 = "0000000960" + p150
    if (tc4 > 0) and (ptc4 != "" and pos2 >= int(ptc4[0:1]) + 4) and (
            (result4t0 != "" or result4t1 != "" or result4t2 != "" or result4t3 != "") and (
            result3t4 != "" or result3t5 != "" or result3t6 != "" or result3t7 != "")):
        p151 = "7 digit - 4 digit repeat and 3 digit repeat no.found p151"
        print(p151)
        p151 = "0000160000" + p151
    if (tc2 == 6 and tc3 == 3 and tc5 < 1) and (
            (result4t0 != "" or result4t1 != "") and (result3t4 != "" or result3t5 != "") and (
            result2t8 != "" or result2t7 != "")):
        p152 = "9 digit - 4 digit repeat and 3 digit repeat and 2 digit repeat no.found p152"
        print(p152)
        p152 = "0000008000" + p152
    if (result4t0 != "") and (result3t4 != "") and (result3t7 != ""):
        p153 = "10 digit - 4 digit repeat and 3 digit repeat and 3 digit repeat no.found p153"
        print(p153)
        p153 = "0000000400" + p153
    if (result4t0 != "") and (result3t4 != "") and (result3s7 != ""):
        p154 = "10 digit - 4 digit repeat and 3 digit repeat and 3 digit seq no.found p154"
        print(p154)
        p154 = "0000000640" + p154
    if (tc4 > 0 and sc3 > 0) and ((result4t0 != "" or result4t1 != "" or result4t2 != "" or result4t3 != "") and (
            result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != "")) \
            and (ptc4 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc4[0:1]) + 4):
        p155 = "7 digit - 4 digit repeat and 3 digit seq no.found p155"
        print(p155)
        p155 = "0000256000" + p155
    if (tc4 > 0 and sc3 > 0) and (
            ptc2 != "" and ptc4 != "" and (int(psc3[0:1]) >= int(ptc4[0:1]) + 4) and pos3 >= int(psc3[0:1]) + 2) and (
            (result4t0 != "" or result4t1 != "") and (result3s4 != "" or result3s5 != "") and (
            result2t8 != "" or result2t7 != "")):
        p156 = "9 digit - 4 digit repeat and 3 digit seq and 2 digit repeat no.found p156"
        print(p156)
        p156 = "0000012800" + p156
    if (result4t0 != "") and (result3s4 != "") and (result3t7 != ""):
        p157 = "10 digit - 4 digit repeat and 3 digit seq and 3 digit repeat no.found p157"
        print(p157)
        p157 = "0000000640" + p157
    if (result4t0 != "") and (result3s4 != "") and (result3s7 != ""):
        p158 = "10 digit - 4 digit repeat and 3 digit seq and 3 digit seq no.found p158"
        print(p158)
        p158 = "0000001024" + p158
    if (sc3 == 3 and sc5 < 1) and (psc4 != "" and pos1 >= int(psc4[0:1]) + 4) and (
            (result4s0 != "" or result4s1 != "" or result4s2 != "" or result4s3 != "") and (
            result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != "")):
        p159 = "7 digit - 4 digit seq and 3 digit seq no.found p159"
        print(p159)
    if (sc3 == 4 and sc5 == 1) and (psc4 != "" and pos1 >= int(psc4[0:1]) + 4) and (
            (result4s0 != "" or result4s1 != "" or result4s2 != "" or result4s3 != "") and (
            result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != "")):
        p159 = "7 digit - 4 digit seq and 3 digit seq no.found p159"
        print(p159)
    if p159 != "":
        print(p159)
        p159 = "0000352800" + p159

    if (sc3 > 2 and sc5 < 2 and tc3 < 2) and (
            psc4 != "" and ptc2 != "" and pos1 > int(psc4[0:1]) + 3 and pos3 > int(psc4[0:1]) + 6) and (
            (result4s0 != "" or result4s1 != "") and (result3s4 != "" or result3s5 != "") and (
            result2t8 != "" or result2t7 != "")):
        p160 = "9 digit - 4 digit seq and 3 digit seq and 2 digit repeat no.found p160"
        print(p160)
        p160 = "0000017360" + p160
    if (result4s0 != "") and (result3s4 != "") and (result3t7 != ""):
        p161 = "10 digit - 4 digit seq and 3 digit seq and 3 digit repeat no.found p161"
        print(p161)
        p161 = "0000000800" + p161
    if (result4s0 != "") and (result3s4 != "") and (result3s7 != ""):
        p162 = "10 digit - 4 digit seq and 3 digit seq and 3 digit seq no.found p162"
        print(p162)
        p162 = "0000001280" + p162
    if (sc3 == 2 and sc5 < 1 and tc3 == 1 and tc4 < 1) and (pos5 + 4 <= pos2) and (
            (result4s0 != "" or result4s1 != "" or result4s2 != "" or result4s3 != "") and (
            result3t4 != "" or result3t5 != "" or result3t6 != "" or result3t7 != "")):
        p163 = "7 digit - 4 digit seq and 3 digit repeat no.found p163"
        print(p163)
    if (sc4 == 2 and sc6 < 1 and tc3 == 1 and tc4 < 1) and (pos5 + 4 <= pos2) and (
            (result4s0 != "" or result4s1 != "" or result4s2 != "" or result4s3 != "") and (
            result3t4 != "" or result3t5 != "" or result3t6 != "" or result3t7 != "")):
        p163 = "7 digit - 4 digit seq and 3 digit repeat no.found p163"
        print(p163)
    if (sc4 == 1 and sc6 < 1 and tc3 == 2 and tc5 < 1) and (
            (result4s0 != "" or result4s1 != "" or result4s2 != "" or result4s3 != "") and (
            result3t4 != "" or result3t5 != "" or result3t6 != "" or result3t7 != "")):
        p163 = "7 digit - 4 digit seq and 3 digit repeat no.found p163"
        print(p163)
    if (sc4 == 2 and tc3 == 1) and (ptc3 != "" and psc4 != "" and pos2 >= int(psc4[0:1]) + 4) and (
            (result4s0 != "" or result4s1 != "" or result4s2 != "" or result4s3 != "") and (
            result3t4 != "" or result3t5 != "" or result3t6 != "" or result3t7 != "")):
        p163 = "7 digit - 4 digit seq and 3 digit repeat no.found p163"
        print(p163)
    if p163 != "":
        print(p163)
        p163 = "0000218000" + p163

    if (tc3 > 0 and sc4 > 0) and (
            ptc3 != "" and psc4 != "" and int(ptc3[0:1]) >= int(psc4[0:1]) + 3 and pos3 >= int(ptc3[0:1]) + 3) and (
            (result4s0 != "" or result4s1 != "") and (result3t4 != "" or result3t5 != "") and (
            result2t8 != "" or result2t7 != "")):
        p164 = "9 digit - 4 digit seq and 3 digit repeat and 2 digit repeat no.found p164"
        print(p164)
        p164 = "0000010600" + p164
    if (result4s0 != "") and (result3t4 != "") and (result3t7 != ""):
        p165 = "10 digit - 4 digit seq and 3 digit repeat and 3 digit repeat no. found p165"
        print(p165)
        p165 = "0000000500" + p165
    if (result4s0 != "") and (result3t4 != "") and (result3s7 != ""):
        p166 = "10 digit - 4 digit seq and 3 digit repeat and 3 digit seq no. found p166"
        print(p166)
        p166 = "0000000800" + p166
    if (tc2 == 5 and tc6 < 1) and ((result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result5t2 != "" or result5t3 != "" or result5t4 != "" or result5t5 != "")):
        p167 = "7 digit - 2 digit repeat and 5 digit repeat no.found p167"
        print(p167)
        p167 = "0000160000" + p167
    if (tc2 == 6 and tc6 < 1) and ((result2t0 != "" or result2t1 != "") and (result5t2 != "" or result5t3 != "") and (
            result2t8 != "" or result2t7 != "")):
        p168 = "9 digit - 2 digit repeat and 5 digit repeat and 2 digit repeat no.found p168"
        print(p168)
        p168 = "0000008000" + p168
    if (result2t0 != "") and (result5t2 != "") and (result3t7 != ""):
        p169 = "10 digit - 2 digit repeat and 5 digit repeat and 3 digit repeat no.found p169"
        print(p169)
        p169 = "0000000400" + p169
    if (result2t0 != "") and (result5t2 != "") and (result3s7 != ""):
        p170 = "10 digit - 2 digit repeat and 5 digit repeat and 3 digit seq no.found p170"
        print(p170)
        p170 = "0000000640" + p170
    if (tc2 == 1 and sc5 == 1) and (ptc2 != "" and psc5 != "" and int(psc5[0:1]) >= int(ptc2[0:1]) + 2) and (
            (result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result5s2 != "" or result5s3 != "" or result5s4 != "" or result5s5 != "")):
        p171 = "7 digit - 2 digit repeat and 5 digit seq no.found p171"
        print(p171)
    if (tc2 == 2 and sc5 == 1 and tc4 < 1) and (
            ptc2 != "" and psc5 != "" and int(psc5[0:1]) >= int(ptc2[0:1]) + 2) and (
            (result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result5s2 != "" or result5s3 != "" or result5s4 != "" or result5s5 != "")):
        p171 = "7 digit - 2 digit repeat and 5 digit seq no.found p171"
        print(p171)
    if (tc2 == 1 and sc5 == 2 and tc4 < 1) and (
            ptc2 != "" and psc5 != "" and int(psc5[1:2]) >= int(ptc2[0:1]) + 2) and (
            (result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result5s2 != "" or result5s3 != "" or result5s4 != "" or result5s5 != "")):
        p171 = "7 digit - 2 digit repeat and 5 digit seq no.found p171"
        print(p171)
    if p171 != "":
        print(p171)
        p171 = "0000192000" + p171
    if sc5 == 1 and (
            ptc2 != "" and psc5 != "" and int(psc5[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc5[0:1]) + 5) and (
            (result2t0 != "" or result2t1 != "") and (result5s2 != "" or result5s3 != "") and (
            result2t8 != "" or result2t7 != "")):
        p172 = "9 digit - 2 digit repeat and 5 digit seq and 2 digit repeat no.found p172"
        print(p172)
    if sc5 == 2 and (
            ptc2 != "" and psc5 != "" and int(psc5[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc5[0:1]) + 5) and (
            (result2t0 != "" or result2t1 != "") and (result5s2 != "" or result5s3 != "") and (
            result2t8 != "" or result2t7 != "")):
        p172 = "9 digit - 2 digit repeat and 5 digit seq and 2 digit repeat no.found p172"
        print(p172)
    if sc5 == 2 and (
            ptc2 != "" and psc5 != "" and int(psc5[1:2]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc5[1:2]) + 5) and (
            (result2t0 != "" or result2t1 != "") and (result5s2 != "" or result5s3 != "") and (
            result2t8 != "" or result2t7 != "")):
        p172 = "9 digit - 2 digit repeat and 5 digit seq and 2 digit repeat no.found p172"
        print(p172)
    if p172 != "":
        print(p172)
        p172 = "0000009600" + p172
    if (result2t0 != "") and (result5s2 != "") and (result3t7 != ""):
        p173 = "10 digit - 2 digit repeat and 5 digit seq and 3 digit repeat no.found p173"
        print(p173)
        p173 = "0000000480" + p173
    if (result2t0 != "") and (result5s2 != "") and (result3s7 != ""):
        p174 = "10 digit - 2 digit repeat and 5 digit seq and 3 digit seq no.found p174"
        print(p174)
        p174 = "0000000768" + p174
    if (tc5 > 0) and (ptc5 != "" and pos3 >= int(ptc5[0:1]) + 5) and (
            (result5t0 != "" or result5t1 != "" or result5t2 != "" or result5t3 != "") and (
            result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != "")):
        p175 = "7 digit - 5 digit repeat and 2 digit repeat no.found p175"
        print(p175)
        p175 = "0000160000" + p175

    if (tc5 > 0 and tc3 == 3) and (pos3 >= pos7 + 7) and (
            (result5t0 != "" or result5t1 != "") and (result2t5 != "" or result2t6 != "") and (
            result2t8 != "" or result2t7 != "")):
        p176 = "9 digit - 5 digit repeat and 2 digit repeat and 2 digit repeat no.found p176"
        print(p176)
        p176 = "0000008000" + p176
    if (result5t0 != "") and (result2t5 != "") and (result3t7 != ""):
        p177 = "10 digit - 5 digit repeat and 2 digit repeat and 3 digit repeat no.found p177"
        print(p177)
        p177 = "0000000400" + p177
    if (result5t0 != "") and (result2t5 != "") and (result3s7 != ""):
        p178 = "10 digit - 5 digit repeat and 2 digit repeat and 3 digit seq no.found p178"
        print(p178)
        p178 = "0000000640" + p178
    if (tc2 > 0 and sc5 > 0) and (ptc2 != "" and psc5 != "" and int(ptc2[0:1]) >= int(psc5[0:1]) + 5) and (
            (result5s0 != "" or result5s1 != "" or result5s2 != "" or result5s3 != "") and (
            result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != "")):
        p179 = "7 digit - 5 digit seq and 2 digit repeat no.found p179"
        print(p179)
    if (tc2 == 2 and sc5 == 1) and (ptc2 != "" and psc5 != "" and int(ptc2[1:2]) >= int(psc5[0:1]) + 5) and (
            (result5s0 != "" or result5s1 != "" or result5s2 != "" or result5s3 != "") and (
            result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != "")):
        p179 = "7 digit - 5 digit seq and 2 digit repeat no.found p179"
        print(p179)
    if p179 != "":
        print(p179)
        p179 = "0000218000" + p179
    if (tc2 > 1 and sc5 > 0) and (
            ptc2 != "" and psc5 != "" and int(ptc2[0:1]) >= int(psc5[0:1]) + 5 and pos3 >= int(ptc2[0:1]) + 2) and (
            (result5s0 != "" or result5s1 != "") and (result2t5 != "" or result2t6 != "") and (
            result2t8 != "" or result2t7 != "")):
        p180 = "9 digit - 5 digit seq and 2 digit repeat and 2 digit repeat no.found p180"
        print(p180)
    if (tc2 == 3 and sc5 == 1) and (
            ptc2 != "" and psc5 != "" and int(ptc2[1:2]) >= int(psc5[0:1]) + 5 and pos3 >= int(ptc2[1:2]) + 2) and (
            (result5s0 != "" or result5s1 != "") and (result2t5 != "" or result2t6 != "") and (
            result2t8 != "" or result2t7 != "")):
        p180 = "9 digit - 5 digit seq and 2 digit repeat and 2 digit repeat no.found p180"
        print(p180)
    if p180 != "":
        print(p180)
        p180 = "0000010600" + p180
    if (result5s0 != "") and (result2t5 != "") and (result3t7 != ""):
        p181 = "10 digit - 5 digit seq and 2 digit repeat and 3 digit repeat no.found p181"
        print(p181)
        p181 = "0000000400" + p181
    if (result5s0 != "") and (result2t5 != "") and (result3s7 != ""):
        p182 = "10 digit - 5 digit seq and 2 digit repeat and 3 digit seq no.found p182"
        print(p182)
        p182 = "0000000640" + p182
    if (tc3 == 1 and tc4 < 1) and (
            ptc3 != "" and pos2 >= int(ptc2[1:2]) + 2 and int(ptc2[1:2]) >= int(ptc2[0:1]) + 2) and (
            (result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "") and (
                    result3t4 != "" or result3t5 != "" or result3t6 != "" or result3t7 != "")):
        p183 = "7 digit - 2 digit repeat and 2 digit repeat and 3 digit repeat no.found p183"
        print(p183)
        p183 = "0001600000" + p183
    if tc3 > 0 and tc2 > 3 and (ptc3 != "" and int(ptc3[0:1]) <= int(ptc2[3:4]) - 3 and pos3 >= pos2 + 5) and (
            (result3t0 != "" or result3t1 != "" or result3t2 != "" or result3t3 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "" or result2t6 != "") and (
                    result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != "")):
        p184 = "7 digit - 3 digit repeat and 2 digit repeat and 2 digit repeat no.found p184"
        print(p184)
        p184 = "0001600000" + p184
    if (sc3 > 0 and tc2 > 1) and (
            ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 4 and int(psc3[0:1]) >= int(
            ptc2[1:2]) + 2) and ((result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "") and (
                                         result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != "")):
        p185 = "7 digit - 2 digit repeat and 2 digit repeat and 3 digit seq no.found p185"
        print(p185)
    if (sc3 == 2 and tc2 == 2) and (
            ptc2 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 4 and int(psc3[1:2]) >= int(
            ptc2[1:2]) + 2) and ((result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "") and (
                                         result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != "")):
        p185 = "7 digit - 2 digit repeat and 2 digit repeat and 3 digit seq no.found p185"
        print(p185)
    if p185 != "":
        print(p185)
        p185 = "0002560000" + p185
    if (tc2 > 4 and tc3 > 0) and (pos2 == 2 or pos2 == 3) and (result2t0 != "" or result2t1 != "") and (
            result3t2 != "" or result3t3 != "") \
            and (result2t5 != "" or result2t6 != "") and (result2t7 != "" or result2t8 != ""):
        p186 = "9 digit - 2 digit repeat and 3 digit repeat and 2 digit repeat and 2 digit repeat no.found p186"
        print(p186)
        p186 = "0000080000" + p186
    if (tc2 > 4 and tc3 > 0) and (pos2 == 4 or pos2 == 4) and (result2t0 != "" or result2t1 != "") and (
            result2t2 != "" or result2t3 != "") \
            and (result3t4 != "" or result3t5 != "") and (result2t7 != "" or result2t8 != ""):
        p187 = "9 digit - 2 digit repeat and 2 digit repeat and 3 digit repeat and 2 digit repeat no.found p187"
        print(p187)
        p187 = "0000080000" + p187
    if (tc2 > 4 and tc3 > 0) and (ptc3 != "" and int(ptc2[2:3]) >= int(ptc3[0:1]) + 3 and int(ptc2[3:4]) >= int(
            ptc2[2:3]) + 2 and pos3 >= int(ptc2[3:4]) + 2) and (result3t0 != "" or result3t1 != "") and (
            result2t3 != "" or result2t4 != "") and (result2t5 != "" or result2t6 != "") and (
            result2t7 != "" or result2t8 != ""):
        p188 = "9 digit - 3 digit repeat and 2 digit repeat and 2 digit repeat and 2 digit repeat no.found p188"
        print(p188)
        p188 = "0000080000" + p188
    if (tc2 > 2 and sc3 > 0) and (
            ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 4 and int(psc3[0:1]) >= int(
            ptc2[1:2]) + 2 and pos3 >= int(psc3[0:1]) + 3) and (
            (result2t0 != "" or result2t1 != "") and (result2t2 != "" or result2t3 != "") and (
            result3s4 != "" or result3s5 != "") \
            and (result2t8 != "" or result2t7 != "")):
        p189 = "9 digit - 2 digit repeat and 2 digit repeat and 3 digit seq no. and 2 digit repeat found ap189"
        print(p189)

    if (tc2 == 4 and sc3 == 2 and tc3 == 0) and (
            ptc2 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 4 and int(psc3[1:2]) >= int(
            ptc2[1:2]) + 2 and pos3 >= int(psc3[1:2]) + 3) and (
            (result2t0 != "" or result2t1 != "") and (result2t2 != "" or result2t3 != "") and (
            result3s4 != "" or result3s5 != "") \
            and (result2t8 != "" or result2t7 != "")):
        p189 = "9 digit - 2 digit repeat and 2 digit repeat and 3 digit seq no. and 2 digit repeat found bp189"
        print(p189)

    if (tc2 == 3 and sc3 == 2 and tc3 == 0) and (
            ptc2 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 4 and int(psc3[1:2]) >= int(
            ptc2[1:2]) + 2 and pos3 >= int(psc3[1:2]) + 3) and (
            (result2t0 != "" or result2t1 != "") and (result2t2 != "" or result2t3 != "") and (
            result3s4 != "" or result3s5 != "") \
            and (result2t8 != "" or result2t7 != "")):
        p189 = "9 digit - 2 digit repeat and 2 digit repeat and 3 digit seq no. and 2 digit repeat found cp189"
        print(p189)

    if (tc2 == 3 and sc3 == 3 and tc3 == 0) and (
            ptc2 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 4 and int(psc3[1:2]) >= int(
            ptc2[1:2]) + 2 and pos3 >= int(psc3[1:2]) + 3) and (
            (result2t0 != "" or result2t1 != "") and (result2t2 != "" or result2t3 != "") and (
            result3s4 != "" or result3s5 != "") \
            and (result2t8 != "" or result2t7 != "")):
        p189 = "9 digit - 2 digit repeat and 2 digit repeat and 3 digit seq no. and 2 digit repeat found p189"
        print(p189)
    if p189 != "":
        print(p189)
        p189 = "0000128000" + p189

    if (result2t0 != "") and (result3s2 != "") and (result2t5 != "") and (result3t7 != ""):
        p190 = "10 digit - 2 digit repeat and 3 digit seq and 2 digit repeat and 3 digit repeat no.found p190"
        print(p190)
        p190 = "0000000400" + p190
    if (result2t0 != "") and (result3t2 != "") and (result2t5 != "") and (result3t7 != ""):
        p191 = "10 digit - 2 digit repeat and 3 digit repeat and 2 digit repeat and 3 digit repeat no.found p191"
        print(p191)
        p191 = "0000004000" + p191
    if (result2t0 != "") and (result2t2 != "") and (result3t4 != "") and (result3t7 != ""):
        p192 = "10 digit - 2 digit repeat and 2 digit repeat and 3 digit repeat and 3 digit repeat no.found p192"
        print(p192)
        p192 = "0000004000" + p192
    if (result3t0 != "") and (result2t3 != "") and (result2t5 != "") and (result3t7 != ""):
        p193 = "10 digit - 3 digit repeat and 2 digit repeat and 2 digit repeat and 3 digit repeat no.found p193"
        print(p193)
        p193 = "0000004000" + p193
    if (result2t0 != "") and (result2t2 != "") and (result3s4 != "") and (result3t7 != ""):
        p194 = "10 digit - 2 digit repeat and 2 digit repeat and 3 digit seq no. and 3 digit repeat found p194"
        print(p194)
        p194 = "0000006400" + p194
    if (result3s0 != "") and (result2t3 != "") and (result2t5 != "") and (result3t7 != ""):
        p195 = "10 digit - 3 digit seq and 2 digit repeat and 2 digit repeat and 3 digit repeat no.found p195"
        print(p195)
        p195 = "0000006000" + p195
    if (result2t0 != "") and (result3s2 != "") and (result2t5 != "") and (result3s7 != ""):
        p196 = "10 digit - 2 digit repeat and 3 digit seq and 2 digit repeat and 3 digit seq no.found p196"
        print(p196)
        p196 = "0000010240" + p196
    if (result2t0 != "") and (result3t2 != "") and (result2t5 != "") and (result3s7 != ""):
        p197 = "10 digit - 2 digit repeat and 3 digit repeat and 2 digit repeat and 3 digit seq no.found p197"
        print(p197)
        p197 = "0000006400" + p197
    if (result2t0 != "") and (result2t2 != "") and (result3t4 != "") and (result3s7 != ""):
        p198 = "10 digit - 2 digit repeat and 2 digit repeat and 3 digit repeat and 3 digit seq no.found p198"
        print(p198)
        p198 = "0000006400" + p198
    if (result3t0 != "") and (result2t3 != "") and (result2t5 != "") and (result3s7 != ""):
        p199 = "10 digit - 3 digit repeat and 2 digit repeat and 2 digit repeat and 3 digit seq no.found p199"
        print(p199)
        p199 = "0000006400" + p199
    if (result2t0 != "") and (result2t2 != "") and (result3s4 != "") and (result3s7 != ""):
        p200 = "10 digit - 2 digit repeat and 2 digit repeat and 3 digit seq no. and 3 digit seq found p200"
        print(p200)
        p200 = "0000010240" + p200
    if (result3s0 != "") and (result2t3 != "") and (result2t5 != "") and (result3s7 != ""):
        p201 = "10 digit - 3 digit seq and 2 digit repeat and 2 digit repeat and 3 digit seq no.found p201"
        print(p201)
        p201 = "0000009600" + p201
    if (tc7 == 1 and tc8 < 1) and (result7t0 != ""):
        p202 = "7 digit - 7 digit repeat no. found at start p202"
        print(p202)
        p202 = "0000004000" + p202
    if (tc7 == 1 and tc8 < 1) and (result7t1 != "" or result7t2 != "" or result7t3 != ""):
        p203 = "7 digit - 7 digit repeat no. found p203"
        print(p203)
        p203 = "0000016000" + p203
    if (result7t0 != "" and result3t7 != ""):
        p204 = "10 digit - 7 digit repeat no. and 3 digit repeat no. found p204"
        print(p204)
        p204 = "0000000040" + p204
    if (result7t0 != "" and result3s7 != ""):
        p205 = "10 digit - 7 digit repeat no. and 3 digit seq no. found p205"
        print(p205)
        p205 = "0000000064" + p205
    if (sc7 == 1 and sc8 < 1) and (result7s0 != ""):
        p206 = "7 digit - 7 digit seq no. found at start p206"
        print(p206)
        p206 = "0000004000" + p206
    if (sc7 == 1 and sc8 < 1) and (result7s1 != "" or result7s2 != "" or result7s3 != ""):
        p207 = "7 digit - 7 digit seq no. found p207"
        print(p207)
        p207 = "0000012800" + p207
    if (result7s0 != "" and result3t7 != ""):
        p208 = "10 digit - 7 digit seq no. and 3 digit repeat no. found p208"
        print(p208)
        p208 = "0000000040" + p208
    if (result7s0 != "" and result3s7 != ""):
        p209 = "10 digit - 7 digit seq no. and 3 digit seq no. found p209"
        print(p209)
        p209 = "0000000064" + p209
    if (tc6 == 1 and tc7 < 1) and (result6t0 != ""):
        p210 = "6 digit - 6 digit repeat no. found at start p210"
        print(p210)
        p210 = "0000040000" + p210
    if (tc6 == 1 and tc7 < 1) and (result6t1 != "" or result6t2 != "" or result6t3 != "" or result6t4 != ""):
        p211 = "6 digit - 6 digit repeat no. found p211"
        print(p211)
        p211 = "0000300000" + p211
    if (result6t0 != "") and (result4t6 != ""):
        p212 = "10 digit - 6 digit repeat and 4 digit repeat no. found p212"
        print(p212)
        p212 = "0000000040" + p212
    if (result6t0 != "") and (result4s6 != ""):
        p213 = "10 digit - 6 digit repeat and 4 digit seq no. found p213"
        print(p213)
        p213 = "0000000056" + p213
    if (result6t0 != "") and (result2t6 != "") and (result2t8 != ""):
        p214 = "10 digit - 6 digit repeat and 2 digit repeat no. 2 times found p214"
        print(p214)
        p214 = "0000000400" + p214
    if (sc6 == 1 and sc7 < 1) and (result6s0 != ""):
        p215 = "6 digit - 6 digit seq no. found at start p215"
        print(p215)
        p215 = "0000040000" + p215
    if (sc6 == 1 and sc7 < 1) and (result6s1 != "" or result6s2 != "" or result6s3 != "" or result6s4 != ""):
        p216 = "6 digit - 6 digit seq no. found p216"
        print(p216)
        p216 = "0000200000" + p216
    if (result6s0 != "") and (result4t6 != ""):
        p217 = "10 digit - 6 digit seq and 4 digit repeat no. found p217"
        print(p217)
        p217 = "0000000040" + p217
    if (result6s0 != "") and (result4s6 != ""):
        p218 = "10 digit - 6 digit seq and 4 digit seq no. found p218"
        print(p218)
        p218 = "0000000056" + p218
    if (result6s0 != "") and (result2t6 != "") and (result2t8 != ""):
        p219 = "10 digit - 6 digit seq and 2 digit repeat no. 2 times found p219"
        print(p219)
        p219 = "0000000400" + p219
    if (tc3 > 0 and sc6 > 0) and ((result3t0 != "" and result6s3 != "") or (result3t0 != "" and result6s4 != "") or (
            result3t1 != "" and result6s4 != "")):
        p220 = "9 digit - 3 digit repeat and 6 digit seq no.found p220"
        print(p220)
        p220 = "0000000800" + p220
    if (tc4 > 0 and sc4 > 0) and (ptc4 != "" and psc4 != "" and int(ptc4[0:1]) >= int(psc4[0:1]) + 4) and (
            result4s0 != "" or result4s1 != "" or result4s2 != "") and (
            result4t4 != "" or result4t5 != "" or result4t6 != ""):
        p221 = "8 digit - 4 digit seq and 4 digit repeat no.found p221"
        print(p221)
    if (tc4 == 2 and sc4 == 1) and (ptc4 != "" and psc4 != "" and pos4 >= int(psc4[0:1]) + 4) and (
            result4s0 != "" or result4s1 != "" or result4s2 != "") and (
            result4t4 != "" or result4t5 != "" or result4t6 != ""):
        p221 = "8 digit - 4 digit seq and 4 digit repeat no.found p221"
        print(p221)
    if p221 != "":
        print(p221)
        p221 = "0000016200" + p221
    if ((result3t0 != "" and result3s3 != "") or (result3t4 != "" and result3s7 != "")):
        p222 = "6 digit - 3 digit repeat and 3 digit seq no. found at start or end p222"
        print(p222)
        p222 = "0000640000" + p222
    if (tc3 > 0 and sc3 > 0) and (ptc3 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc3[0:1]) + 3) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "" or result3t3 != "" or result3t4 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p223 = "6 digit - 3 digit repeat and 3 digit seq no. found p223"
        print(p223)
    if (tc3 == 1 and sc3 == 2) and (ptc3 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc3[0:1]) + 3) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "" or result3t3 != "" or result3t4 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p223 = "6 digit - 3 digit repeat and 3 digit seq no. found p223"
        print(p223)
    if p223 != "":
        print(p223)
        p223 = "0003200000" + p223
    if (psc3 != "" and ptc3 != "" and int(psc3[0:1]) >= int(ptc3[0:1]) + 3 and pos3 >= int(psc3[0:1]) + 3) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p224 = "8 digit - 3 digit repeat and 3 digit seq no. found and 2 digit repeat no. found p224"
        print(p224)
    if (sc3 == 2 and tc3 == 2) and (
            psc3 != "" and ptc3 != "" and int(psc3[1:2]) >= int(ptc3[0:1]) + 3 and pos3 >= int(psc3[1:2]) + 3) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p224 = "8 digit - 3 digit repeat and 3 digit seq no. found and 2 digit repeat no. found p224"
        print(p224)
    if (sc3 == 2 and tc3 == 1) and (
            psc3 != "" and ptc3 != "" and int(psc3[1:2]) >= int(ptc3[0:1]) + 3 and pos3 >= int(psc3[1:2]) + 3) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p224 = "8 digit - 3 digit repeat and 3 digit seq no. found and 2 digit repeat no. found p224"
        print(p224)
    if p224 != "":
        print(p224)
        p224 = "0000192000" + p224
    if (tc3 > 1 and sc3 > 0) and (result3t0 != "" or result3t1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3t6 != "" or result3t7 != "") and (
            ptc3 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc3[0:1]) + 3 and pos3 >= int(psc3[0:1]) + 4):
        p225 = "9 digit - 3 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p225"
        print(p225)
    if (tc3 > 1 and sc3 > 1) and (result3t0 != "" or result3t1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3t6 != "" or result3t7 != "") and (
            ptc3 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc3[0:1]) + 3 and pos3 >= int(psc3[1:2]) + 4):
        p225 = "9 digit - 3 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p225"
        print(p225)
    if p225 != "":
        print(p225)
        p225 = "0000012800" + p225
    if (tc3 > 0 and sc3 > 1) and (result3t0 != "" or result3t1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3s6 != "" or result3s7 != "") and (
            ptc3 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc3[0:1]) + 3 and pos1 >= int(psc3[0:1]) + 3):
        p226 = "9 digit - 3 digit repeat and 3 digit seq no. found and 3 digit seq no. found p226"
        print(p226)
    if (tc3 == 1 and sc3 == 3) and (result3t0 != "" or result3t1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3s6 != "" or result3s7 != "") and (
            ptc3 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc3[0:1]) + 3 and pos1 >= int(psc3[1:2]) + 3):
        p226 = "9 digit - 3 digit repeat and 3 digit seq no. found and 3 digit seq no. found p226"
        print(p226)
    if (tc3 == 1 and sc3 == 4) and (result3t0 != "" or result3t1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3s6 != "" or result3s7 != "") and (
            ptc3 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc3[0:1]) + 3 and pos1 >= int(psc3[1:2]) + 3):
        p226 = "9 digit - 3 digit repeat and 3 digit seq no. found and 3 digit seq no. found p226"
        print(p226)
    if p226 != "":
        print(p226)
        p226 = "0000020480" + p226
    if (result3t0 != "") and (result3s3 != "") and (result2t6 != "") and (result2t8 != ""):
        p227 = "10 digit - 3 digit repeat and 3 digit seq no. found and 2 digit repeat no. 2 times found p227"
        print(p227)
        p227 = "0000006400" + p227
    if (result3t0 != "") and (result3s3 != "") and (result4t6 != ""):
        p228 = "10 digit - 3 digit repeat and 3 digit seq no. found and 4 digit repeat no. found p228"
        print(p228)
        p228 = "0000000640" + p228
    if (result3t0 != "") and (result3s3 != "") and (result4s6 != ""):
        p229 = "10 digit - 3 digit repeat and 3 digit seq no. found and 4 digit seq no. found p229"
        print(p229)
        p229 = "0000000672" + p229
    if (result2t0 != "" and result2t2 != "") and (result4t4 != "") and (result2t8 != ""):
        p230 = "10 digit - 2-2 digit repeat no. found and 4 digit repeat and 2 digit repeat no. found p230"
        print(p230)
        p230 = "0000004000" + p230
    if (result2t0 != "" and result2t2 != "") and (result4s4 != "") and (result2t8 != ""):
        p231 = "10 digit - 2-2 digit repeat no. found and 4 digit seq and 2 digit repeat no. found p231"
        print(p231)
        p231 = "0000005600" + p231
    if (tc3 == 1 and tc4 < 1) and (result3t0 != ""):
        p232 = "3 digit - 3 digit repeat no. found at start p232"
        print(p232)
        p232 = "0040000000" + p232
    if (tc3 == 1 and tc4 < 1) and (
            result3t1 != "" or result3t2 != "" or result3t3 != "" or result3t4 != "" or result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p233 = "3 digit - 3 digit repeat no. found p233"
        print(p233)
        p233 = "0320000000" + p233
    if (result3t0 != "") and (result7t3 != ""):
        p234 = "10 digit - 3 digit repeat no. found and 7 digit repeat no. found p234"
        print(p234)
        p234 = "0000000040" + p234
    if (result3t0 != "") and (result7s3 != ""):
        p235 = "10 digit - 3 digit repeat no. found and 7 digit seq no. found p235"
        print(p235)
        p235 = "0000000032" + p235
    if (result3t0 != "") and (result3t3 != "") and (result4t6 != ""):
        p236 = "10 digit - 3 digit repeat no. and 3 digit repeat no. and 4 digit repeat no. found p236"
        print(p236)
        p236 = "0000000400" + p236
    if (result3t0 != "") and (result4t3 != "") and (result3t7 != ""):
        p237 = "10 digit - 3 digit repeat no. and 4 digit repeat no. and 3 digit repeat no. found p237"
        print(p237)
        p237 = "0000000400" + p237
    if (result3t0 != "") and (result3t3 != "") and (result4s6 != ""):
        p238 = "10 digit - 3 digit repeat no. and 3 digit repeat no. and 4 digit seq no. found p238"
        print(p238)
        p238 = "0000000560" + p238
    if (result3t0 != "") and (result4t3 != "") and (result3s7 != ""):
        p239 = "10 digit - 3 digit repeat no. and 4 digit repeat no. and 3 digit seq no. found p239"
        print(p239)
        p239 = "0000000640" + p239
    if (result3t0 != "") and (result3s3 != "") and (result4t6 != ""):
        p240 = "10 digit - 3 digit repeat no. and 3 digit seq no. and 4 digit repeat no. found p240"
        print(p240)
        p240 = "0000000640" + p240
    if (result3t0 != "") and (result4s3 != "") and (result3t7 != ""):
        p241 = "10 digit - 3 digit repeat no. and 4 digit seq no. and 3 digit repeat no. found p241"
        print(p241)
        p241 = "0000000560" + p241
    if (result3t0 != "") and (result4s3 != "") and (result3s7 != ""):
        p242 = "10 digit - 3 digit repeat no. and 4 digit seq no. and 3 digit seq no. found p242"
        print(p242)
        p242 = "0000000896" + p242
    if (result3t0 != "") and (result3s3 != "") and (result4s6 != ""):
        p243 = "10 digit - 3 digit repeat no. and 3 digit seq no. and 4 digit seq no. found p243"
        print(p243)
        p243 = "0000000896" + p243
    if (result3t0 != "") and (result2t3 != "") and (result5t5 != ""):
        p244 = "10 digit - 3 digit repeat no. and 2 digit repeat no. and 5 digit repeat no. found p244"
        print(p244)
        p244 = "0000000400" + p244
    if (result3t0 != "") and (result5t3 != "") and (result2t8 != ""):
        p245 = "10 digit - 3 digit repeat no. and 5 digit repeat no. and 2 digit repeat no. found p245"
        print(p245)
        p245 = "0000000400" + p245
    if (result3t0 != "") and (result5s3 != "") and (result2t8 != ""):
        p246 = "10 digit - 3 digit repeat no. and 5 digit seq no. and 2 digit repeat no. found p246"
        print(p246)
        p246 = "0000000560" + p246
    if (result3t0 != "") and (result2t3 != "") and (result3s5 != "") and (result2t8 != ""):
        p247 = "10 digit - 3 digit repeat no. and 2 digit repeat no. and 3 digit seq no. and 2 digit repeat no. found p247"
        print(p247)
        p247 = "0000006400" + p247
    if (sc3 == 1 and sc4 < 1) and (result3s0 != ""):
        p248 = "3 digit - 3 digit seq no. found at start p248"
        print(p248)
        p248 = "0060000000" + p248
    if (sc3 == 1 and sc4 < 1) and (
            result3s1 != "" or result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p249 = "3 digit - 3 digit seq no. found p249"
        print(p249)
        p249 = "0512000000" + p249
    if (result3s0 != "") and (result7t3 != ""):
        p250 = "10 digit - 3 digit seq no. found and 7 digit repeat no. found p250"
        print(p250)
        p250 = "0000000060" + p250
    if (result3s0 != "") and (result7s3 != ""):
        p251 = "10 digit - 3 digit seq no. found and 7 digit seq no. found p251"
        print(p251)
        p251 = "0000000048" + p251
    if (result3s0 != "") and (result3t3 != "") and (result4t6 != ""):
        p252 = "10 digit - 3 digit seq no. and 3 digit repeat no. and 4 digit repeat no. found p252"
        print(p252)
        p252 = "0000000600" + p252
    if (result3s0 != "") and (result4t3 != "") and (result3t7 != ""):
        p253 = "10 digit - 3 digit seq no. and 4 digit repeat no. and 3 digit repeat no. found p253"
        print(p253)
        p253 = "0000000600" + p253
    if (result3s0 != "") and (result3t3 != "") and (result4s6 != ""):
        p254 = "10 digit - 3 digit seq no. and 3 digit repeat no. and 4 digit seq no. found p254"
        print(p254)
        p254 = "0000000840" + p254
    if (result2t0 != "" and result2t2 != "") and (result2t4 != "") and (result4t6 != ""):
        p255 = "10 digit - 2-2 digit repeat no. found and 2 digit repeat and 4 digit repeat no. found p255"
        print(p255)
        p255 = "0000004000" + p255
    if (result3s0 != "" and result3t3 != "") or (result3s4 != "" and result3t7 != ""):
        p256 = "6 digit - 3 digit seq and 3 digit repeat no. found at start p256"
        print(p256)
        p256 = "0000600000" + p256
    if (tc3 > 0 and sc3 > 0) and (
            result3t5 != "" or result3t6 != "" or result3t7 != "" or result3t3 != "" or result3t4 != "") and (
            result3s0 != "" or result3s1 != "" or result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (ptc3 != "" and psc3 != "" and pos2 >= int(psc3[0:1]) + 3):
        p257 = "6 digit - 3 digit seq and 3 digit repeat no. found p257"
        print(p257)
        p257 = "0003160000" + p257
    if (tc3 > 0 and sc3 > 0) and (
            ptc3 != "" and psc3 != "" and int(ptc3[0:1]) >= int(psc3[0:1]) + 3 and pos3 >= int(ptc3[0:1]) + 3) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result3t3 != "" or result3t4 != "" or result3t5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p258 = "8 digit - 3 digit seq and 3 digit repeat no. found and 2 digit repeat no. found p258"
        print(p258)
    if (tc3 == 2 and sc3 == 1 and tc2 == 4) and (
            ptc3 != "" and psc3 != "" and int(ptc3[1:2]) >= int(psc3[0:1]) + 3 and pos3 >= int(ptc3[1:2]) + 3) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result3t3 != "" or result3t4 != "" or result3t5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p258 = "8 digit - 3 digit seq and 3 digit repeat no. found and 2 digit repeat no. found p258"
        print(p258)
    if p258 != "":
        print(p258)
        p258 = "0000188000" + p258
    if (tc3 > 1 and sc3 > 0) and (
            ptc3 != "" and psc3 != "" and int(ptc3[0:1]) >= int(psc3[0:1]) + 3 and pos2 >= int(ptc3[0:1]) + 3) and (
            result3s0 != "" or result3s1 != "") and (result3t3 != "" or result3t4 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p259 = "9 digit - 3 digit seq and 3 digit repeat no. found and 3 digit repeat no. found p259"
        print(p259)
    if (tc3 == 3 and sc3 == 1 and tc2 == 5) and (
            ptc3 != "" and psc3 != "" and int(ptc3[1:2]) >= int(psc3[0:1]) + 3 and pos2 >= int(ptc3[1:2]) + 3) and (
            result3s0 != "" or result3s1 != "") and (result3t3 != "" or result3t4 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p259 = "9 digit - 3 digit seq and 3 digit repeat no. found and 3 digit repeat no. found p259"
        print(p259)
    if p259 != "":
        print(p259)
        p259 = "0000012400" + p259
    if (tc3 > 0 and sc3 > 1) and ((pos2 == 3 and pos1 == 6) or (pos2 == 4 and pos1 == 7)) and (
            result3s0 != "" or result3s1 != "") and (result3t3 != "" or result3t4 != "") \
            and (result3s6 != "" or result3s7 != "") and pos2 >= int(psc3[0:1]) + 3:
        p260 = "9 digit - 3 digit seq and 3 digit repeat no. found and 3 digit seq no. found p260"
        print(p260)
    if (tc3 == 3 and sc3 == 2) and (
            ptc3 != "" and psc3 != "" and int(ptc3[1:2]) >= int(psc3[0:1]) + 3 and pos1 >= int(ptc3[1:2]) + 3) and (
            result3s0 != "" or result3s1 != "") and (result3t3 != "" or result3t4 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p260 = "9 digit - 3 digit seq and 3 digit repeat no. found and 3 digit seq no. found p260"
        print(p260)
    if (tc3 == 2 and sc3 == 2) and (
            ptc3 != "" and psc3 != "" and int(ptc3[0:1]) >= int(psc3[0:1]) + 3 and pos1 >= int(ptc3[0:1]) + 3) and (
            result3s0 != "" or result3s1 != "") and (result3t3 != "" or result3t4 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p260 = "9 digit - 3 digit seq and 3 digit repeat no. found and 3 digit seq no. found p260"
        print(p260)
    if (tc3 == 2 and sc3 == 3) and (
            ptc3 != "" and psc3 != "" and int(ptc3[0:1]) >= int(psc3[0:1]) + 3 and pos1 >= int(ptc3[0:1]) + 3) and (
            result3s0 != "" or result3s1 != "") and (result3t3 != "" or result3t4 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p260 = "9 digit - 3 digit seq and 3 digit repeat no. found and 3 digit seq no. found p260"
        print(p260)
    if p260 != "":
        print(p260)
        p260 = "0000019840" + p260
    if (result3s0 != "") and (result3t3 != "") and (result2t6 != "" and result2t8 != ""):
        p261 = "10 digit - 3 digit seq and 3 digit repeat no. found and 2-2 digit repeat no. found p261"
        print(p261)
        p261 = "0000006000" + p261
    if (result3s0 != "") and (result3t3 != "") and (result4t6 != ""):
        p262 = "10 digit - 3 digit seq and 3 digit repeat no. found and 4 digit repeat no. found p262"
        print(p262)
        p262 = "0000000600" + p262
    if (result3s0 != "") and (result3t3 != "") and (result4s6 != ""):
        p263 = "10 digit - 3 digit seq and 3 digit repeat no. found and 4 digit seq no. found p263"
        print(p263)
        p263 = "0000000840" + p263
    if (result2t0 != "" and result2t2 != "") and (result2t4 != "") and (result4s6 != ""):
        p264 = "10 digit - 2-2 digit repeat no. found and 2 digit repeat and 4 digit seq no. found p264"
        print(p264)
        p264 = "0000005600" + p264
    if (sc3 == 2 and sc4 < 1) and (result3s0 != "" and result3s3 != ""):
        p265 = "6 digit - 3 digit seq and 3 digit seq no. found at start p265"
        print(p265)
        p265 = "0000960000" + p265
    if ((sc3 == 3 and sc4 == 1) or (sc3 == 2 and sc4 == 0)) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "" or result3s3 != "" or result3s4 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p266 = "6 digit - 3 digit seq and 3 digit seq no. found p266"
        print(p266)
        p266 = "0005056000" + p266
    if (sc3 > 1 and sc4 < 1) and (ptc2 != "" and psc3 != "" and pos3 >= int(psc3[0:1]) + 6 and pos3 >= pos1 + 3) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p267 = "8 digit - 3 digit seq and 3 digit seq no. found and 2 digit repeat no. found p267"
        print(p267)
    if (sc3 > 1 and sc4 < 2) and (
            ptc2 != "" and psc3 != "" and pos1 >= int(psc3[0:1]) + 3 and pos3 >= int(psc3[0:1]) + 6 and pos3 >= int(
            psc3[1:2]) + 3) and (result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p267 = "8 digit - 3 digit seq and 3 digit seq no. found and 2 digit repeat no. found p267"
        print(p267)
    if (sc3 == 4 and tc2 == 1) and (
            ptc2 != "" and psc3 != "" and pos1 >= int(psc3[1:2]) + 3 and pos3 >= int(psc3[0:1]) + 6) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p267 = "8 digit - 3 digit seq and 3 digit seq no. found and 2 digit repeat no. found p267"
        print(p267)
    if p267 != "":
        print(p267)
        p267 = "0000300800" + p267
    if (tc3 > 0 and sc3 > 1) and (ptc3 != "" and psc3 != "" and pos1 >= int(psc3[0:1]) + 3 and pos2 >= pos1 + 3) and (
            result3s0 != "" or result3s1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p268 = "9 digit - 3 digit seq and 3 digit seq no. found and 3 digit repeat no. found p268"
        print(p268)

    if (tc3 == 1 and sc3 == 4) and (
            ptc3 != "" and psc3 != "" and pos1 >= int(psc3[1:2]) + 3 and pos2 >= int(psc3[1:2]) + 6) and (
            result3s0 != "" or result3s1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p268 = "9 digit - 3 digit seq and 3 digit seq no. found and 3 digit repeat no. found p268"
        print(p268)
    if (tc3 == 1 and sc3 == 3) and (ptc3 != "" and psc3 != "" and pos1 >= int(psc3[0:1]) + 3 and pos2 >= int(
            psc3[0:1]) + 6 and pos2 >= pos1 + 3) and (result3s0 != "" or result3s1 != "") and (
            result3s3 != "" or result3s4 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p268 = "9 digit - 3 digit seq and 3 digit seq no. found and 3 digit repeat no. found p268"
        print(p268)
    if p268 != "":
        print(p268)
        p268 = "0000019840" + p268
    if (sc3 > 2) and (
            psc3 != "" and pos1 >= int(psc3[0:1]) + 6 and int(psc3[1:2]) >= int(psc3[0:1]) + 3 and pos1 >= int(
            psc3[1:2]) + 3) and (result3s0 != "" or result3s1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p269 = "9 digit - 3 digit seq and 3 digit seq no. found and 3 digit seq no. found p269"
        print(p269)
    if (sc3 == 4) and (
            psc3 != "" and pos1 >= int(psc3[0:1]) + 6 and int(psc3[2:3]) >= int(psc3[1:2]) + 3 and pos1 >= int(
            psc3[1:2]) + 3) and (result3s0 != "" or result3s1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p269 = "9 digit - 3 digit seq and 3 digit seq no. found and 3 digit seq no. found  p269"
        print(p269)
    if (sc3 == 5) and (
            psc3 != "" and pos1 >= int(psc3[0:1]) + 6 and int(psc3[2:3]) >= int(psc3[1:2]) + 3 and pos1 >= int(
            psc3[2:3]) + 3) and (result3s0 != "" or result3s1 != "") and (result3s3 != "" or result3s4 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p269 = "9 digit - 3 digit seq and 3 digit seq no. found and 3 digit seq no. found p269"
        print(p269)
    if p269 != "":
        print(p269)
        p269 = "0000031740" + p269
    if (tc2 == 2 and tc3 < 1) and (result3s0 != "") and (result3s3 != "") and (result2t6 != "" and result2t8 != ""):
        p270 = "10 digit - 3 digit seq and 3 digit seq no. found and 2-2 digit repeat no. found p270"
        print(p270)
        p270 = "0000009600" + p270
    if (tc4 == 1 and tc5 < 1) and (result3s0 != "") and (result3s3 != "") and (result4t6 != ""):
        p271 = "10 digit - 3 digit seq and 3 digit seq no. found and 4 digit repeat no. found p271"
        print(p271)
        p271 = "0000000960" + p271
    if (sc4 == 1 and sc5 < 1) and (result3s0 != "") and (result3s3 != "") and (result4s6 != ""):
        p272 = "10 digit - 3 digit seq and 3 digit seq no. found and 4 digit seq no. found p272"
        print(p272)
        p272 = "0000001344" + p272
    if (tc2 == 2 and tc3 < 1) and (result2t0 != "" and result2t2 != ""):
        p273 = "4 digit - 2-2 digit repeat no. found at start p273"
        print(p273)
        p273 = "0040000000" + p273
    if (tc3 == 2 and tc4 < 1) and (result3t0 != "" and result3t3 != ""):
        p274 = "6 digit - 3 digit repeat and 3 digit repeat no. found at start p274"
        print(p274)
        p274 = "0000400000" + p274
    if (tc3 > 1 and tc4 < 1) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "" or result3t3 != "" or result3t4 != "") and (
            result3t3 != "" or result3t4 != "" or result3t5 != "" or result3t6 != "" or result3t7 != "") \
            :
        p275 = "6 digit - 3 digit repeat and 3 digit repeat no. found p275"
        print(p275)
        p275 = "0002000000" + p275
    if (tc3 > 1) and (ptc3 != "" and int(ptc3[0:1]) <= int(ptc3[1:2]) - 3 and pos3 >= int(ptc3[1:2]) + 2) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "") and (
            result3t3 != "" or result3t4 != "" or result3t5 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p276 = "8 digit - 3 digit repeat and 3 digit repeat no. found and 2 digit repeat no. found p276"
        print(p276)
        p276 = "0000120000" + p276
    if (tc2 == 6 and tc3 == 3 and tc4 < 1) and (result3t0 != "" or result3t1 != "") and (
            result3t3 != "" or result3t4 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p277 = "9 digit - 3 digit repeat and 3 digit repeat no. found and 3 digit repeat no. found p277"
        print(p277)
        p277 = "0000008000" + p277
    if (tc3 > 1 and sc3 > 0) and (
            ptc3 != "" and psc3 != "" and int(ptc3[1:2]) >= int(ptc3[0:1]) + 3 and int(psc3[0:1]) >= int(
            ptc3[1:2]) + 3) and (result3t0 != "" or result3t1 != "") and (result3t3 != "" or result3t4 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p278 = "9 digit - 3 digit repeat and 3 digit repeat no. found and 3 digit seq no. found p278"
        print(p278)
        p278 = "0000012800" + p278
    if (result3t0 != "") and (result3t3 != "") and (result2t6 != "" and result2t8 != ""):
        p279 = "10 digit - 3 digit repeat and 3 digit repeat no. found and 2-2 digit repeat no. found p279"
        print(p279)
        p279 = "0000004000" + p279
    if (result3t0 != "") and (result3t3 != "") and (result4t6 != ""):
        p280 = "10 digit - 3 digit repeat and 3 digit repeat no. found and 4 digit repeat no. found p280"
        print(p280)
        p280 = "0000000400" + p280
    if (result3t0 != "") and (result3t3 != "") and (result4s6 != ""):
        p281 = "10 digit - 3 digit repeat and 3 digit repeat no. found and 4 digit seq no. found p281"
        print(p281)
        p281 = "0000000560" + p281
    if (result4t0 != "") and (result4s4 != "") and (result2t8 != ""):
        p282 = "10 digit - 4 digit repeat no. found and 4 digit seq and 2 digit repeat no. found p282"
        print(p282)
        p282 = "0000000560" + p282
    if (result2t0 != "" and result4s2 != ""):
        p283 = "6 digit - 2 digit repeat and 4 digit seq no. found at start p283"
        print(p283)
        p283 = "0000560000" + p283
    if (tc2 > 0 and sc4 > 0) and (ptc2 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc2[0:1]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "") and (
            result4s2 != "" or result4s3 != "" or result4s4 != "" or result4s5 != "" or result4s6 != ""):
        p284 = "6 digit - 2 digit repeat and 4 digit seq no. found p284"
        print(p284)
    if (tc2 == 1 and sc4 == 2) and (ptc2 != "" and psc4 != "" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "") and (
            result4s2 != "" or result4s3 != "" or result4s4 != "" or result4s5 != "" or result4s6 != ""):
        p284 = "6 digit - 2 digit repeat and 4 digit seq no. found p284"
        print(p284)
    if (tc2 == 3 and sc4 == 2) and (ptc2 != "" and psc4 != "" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "") and (
            result4s2 != "" or result4s3 != "" or result4s4 != "" or result4s5 != "" or result4s6 != ""):
        p284 = "6 digit - 2 digit repeat and 4 digit seq no. found p284"
        print(p284)
    if p284 != "":
        print(p284)
        p284 = "0002800000" + p284
    if (tc2 > 1 and sc4 > 0) and (
            ptc2 != " and psc4!=" and int(psc4[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc4[0:1]) + 4) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result4s2 != "" or result4s3 != "" or result4s4 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p285 = "8 digit - 2 digit repeat and 4 digit seq no. found and 2 digit repeat no. found ap285"
        print(p285)
    if (tc2 == 3 and sc4 == 2) and (
            ptc2 != " and psc4!=" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc4[1:2]) + 4) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result4s2 != "" or result4s3 != "" or result4s4 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p285 = "8 digit - 2 digit repeat and 4 digit seq no. found and 2 digit repeat no. found bp285"
        print(p285)
    if (tc2 == 2 and sc4 == 2) and (
            ptc2 != " and psc4!=" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc4[1:2]) + 4) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result4s2 != "" or result4s3 != "" or result4s4 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p285 = "8 digit - 2 digit repeat and 4 digit seq no. found and 2 digit repeat no. found cp285"
        print(p285)
    if (tc2 == 2 and sc4 == 3) and (
            ptc2 != " and psc4!=" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc4[1:2]) + 4) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result4s2 != "" or result4s3 != "" or result4s4 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p285 = "8 digit - 2 digit repeat and 4 digit seq no. found and 2 digit repeat no. found dp285"
        print(p285)
    if p285 != "":
        print(p285)
        p285 = "0000168000" + p285

    if (tc2 > 1 and tc3 > 0 and sc4 > 0) and (
            ptc3 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc2[0:1]) + 2 and int(ptc3[0:1]) >= int(
            psc4[0:1]) + 4) and (result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p286 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit repeat no. found p286"
        print(p286)
    if (tc2 == 4 and tc3 == 2 and sc4 == 1) and (
            ptc3 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc2[0:1]) + 2 and int(ptc3[1:2]) >= int(
            psc4[0:1]) + 4) and (result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p286 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit repeat no. found p286"
        print(p286)
    if (tc2 == 4 and tc3 == 2 and sc4 == 2) and (
            ptc3 != "" and psc4 != "" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2 and int(ptc3[1:2]) >= int(
            psc4[0:1]) + 4) and (result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p286 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit repeat no. found p286"
        print(p286)
    if (tc2 == 5 and tc3 == 3 and sc4 == 1) and (
            ptc3 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc2[0:1]) + 2 and int(ptc3[2:3]) >= int(
            psc4[0:1]) + 4) and (result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p286 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit repeat no. found p286"
        print(p286)
    if (tc2 == 3 and tc3 == 1 and sc4 == 2) and (
            ptc3 != "" and psc4 != "" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2 and int(ptc3[0:1]) >= int(
            psc4[1:2]) + 4) and (result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p286 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit repeat no. found p286"
        print(p286)
    if (tc2 == 3 and tc3 == 1 and sc4 == 3) and (
            ptc3 != "" and psc4 != "" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2 and int(ptc3[0:1]) >= int(
            psc4[1:2]) + 4) and (result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p286 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit repeat no. found p286"
        print(p286)
    if p286 != "":
        print(p286)
        p286 = "0000011200" + p286
    if (tc2 > 0 and sc4 > 0) and (
            ptc2 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc2[0:1]) + 2 and pos1 >= int(psc4[0:1]) + 4) and (
            result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p287 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit seq no. found p287"
        print(p287)
    if (tc2 == 1 and sc4 == 3) and (
            ptc2 != "" and psc4 != "" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2 and pos1 >= int(psc4[1:2]) + 4) and (
            result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p287 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit seq no. found p287"
        print(p287)
    if (tc2 == 2 and sc4 == 2) and (
            ptc2 != "" and psc4 != "" and int(psc4[1:2]) >= int(ptc2[0:1]) + 2 and pos1 >= int(psc4[1:2]) + 4) and (
            result2t0 != "" or result2t1 != "") and (result4s2 != "" or result4s3 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p287 = "9 digit - 2 digit repeat and 4 digit seq no. found and 3 digit seq no. found p287"
        print(p287)
    if p287 != "":
        print(p287)
        p287 = "0000017920" + p287
    if (result2t0 != "") and (result4s2 != "") and (result2t6 != "" and result2t8 != ""):
        p288 = "10 digit - 2 digit repeat and 4 digit seq no. found and 2 digit repeat no. 2 times found p288"
        print(p288)
        p288 = "0000005600" + p288
    if (result2t0 != "") and (result4s2 != "") and (result4t6 != ""):
        p289 = "10 digit - 2 digit repeat and 4 digit seq no. found and 4 digit repeat no. found p289"
        print(p289)
        p289 = "0000000560" + p289
    # if (result2t0!=""  ) and (result4s2!="") and (result4s6!="" ):
    #   p290 = "10 digit - 2 digit repeat and 4 digit seq no. found and 4 digit seq no. found p290"
    #   print(p290)
    #   p290 = "0000000784" + p290
    if (result4t0 != "") and (result4t4 != "") and (result2t8 != ""):
        p291 = "10 digit - 4 digit repeat no. found and 4 digit repeat and 2 digit repeat no. found p291"
        print(p291)
        p291 = "0000000400" + p291
    if (tc2 == 4 and tc3 == 2 and tc5 < 1) and (
            (result2t0 != "" and result4t2 != "") or (result2t4 != "" and result4t6 != "")):
        p292 = "6 digit - 2 digit repeat and 4 digit repeat no. found at start p292"
        print(p292)
        p292 = "0000400000" + p292
    if (tc2 == 4 and tc3 == 2 and tc5 < 1) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "") and (
            result4t2 != "" or result4t3 != "" or result4t4 != "" or result4t5 != "" or result4t6 != ""):
        p293 = "6 digit - 2 digit repeat and 4 digit repeat no. found p293"
        print(p293)
        p293 = "0002000000" + p293
    if (tc4 == 1 and tc5 < 1) and (
            ptc4 != "" and int(ptc4[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(ptc4[0:1]) + 4) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result4t2 != "" or result4t3 != "" or result4t4 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p294 = "8 digit - 2 digit repeat and 4 digit repeat no. found and 2 digit repeat no. found p294"
        print(p294)
        p294 = "0000120000" + p294
    if (tc4 == 1 and tc5 < 1) and (
            ptc4 != "" and int(ptc4[0:1]) >= int(ptc2[0:1]) + 2 and pos2 >= int(ptc4[0:1]) + 4) and (
            result2t0 != "" or result2t1 != "") and (result4t2 != "" or result4t3 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p295 = "9 digit - 2 digit repeat and 4 digit repeat no. found and 3 digit repeat no. found p295"
        print(p295)
        p295 = "0000008000" + p295
    if (tc4 > 0 and sc3 > 0) and (
            ptc4 != "" and psc3 != "" and int(ptc4[0:1]) >= int(ptc2[0:1]) + 2 and pos1 >= int(ptc4[0:1]) + 4) and (
            result2t0 != "" or result2t1 != "") and (result4t2 != "" or result4t3 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p296 = "9 digit - 2 digit repeat and 4 digit repeat no. found and 3 digit seq no. found p296"
        print(p296)
        p296 = "0000012800" + p296
    if (result2t0 != "") and (result4t2 != "") and (result2t6 != "" and result2t8 != ""):
        p297 = "10 digit - 2 digit repeat and 4 digit repeat no. found and 2-2 digit repeat no. found p297"
        print(p297)
        p297 = "0000004000" + p297
    if (result2t0 != "") and (result4t2 != "") and (result4t6 != ""):
        p298 = "10 digit - 2 digit repeat and 4 digit repeat no. found and 4 digit repeat no. found p298"
        print(p298)
        p298 = "0000000400" + p298
    if (result2t0 != "") and (result4t2 != "") and (result4s6 != ""):
        p299 = "10 digit - 2 digit repeat and 4 digit repeat no. found and 4 digit seq no. found p299"
        print(p299)
        p299 = "0000000560" + p299
    if (result4t0 != "") and (result2t4 != "") and (result4t6 != ""):
        p300 = "10 digit - 4 digit repeat no. found and 2 digit repeat and 4 digit repeat no. found p300"
        print(p300)
        p300 = "0000000400" + p300
    if (result4s0 != "" and result2t4 != ""):
        p301 = "6 digit - 4 digit seq and 2 digit repeat no. found at start p301"
        print(p301)
        p301 = "0000500000" + p301
    if ((ptc2 != "" and psc4 != "" and (int(ptc2[0:1]) >= int(psc4[0:1]) + 4) and tc3 == 0) or (
            ptc2 != "" and psc4 != "" and (int(ptc2[0:1]) >= int(psc4[0:1]) + 3) and tc3 == 1)) and (
            result4s0 != "" or result4s1 != "" or result4s2 != "" or result4s3 != "" or result4s4 != "") and (
            result2t4 != "" or result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p302 = "6 digit - 4 digit seq and 2 digit repeat no. found p302"
        print(p302)
        p302 = "0002740000" + p302
    if (tc2 > 1 and sc4 > 0) and (ptc2 != " and psc4!=" and int(ptc2[0:1]) >= int(psc4[0:1]) + 4 and pos3 >= int(
            ptc2[0:1]) + 2 and pos3 >= int(psc4[0:1]) + 6) and (
            result4s0 != "" or result4s1 != "" or result4s2 != "") and (
            result2t4 != "" or result2t5 != "" or result2t6 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p303 = "8 digit - 4 digit seq and 2 digit repeat no. found and 2 digit repeat no. found p303"
        print(p303)
    if (tc2 == 3 and sc4 == 1) and (ptc2 != " and psc4!=" and int(ptc2[1:2]) >= int(psc4[0:1]) + 4 and pos3 >= int(
            ptc2[1:2]) + 2 and pos3 >= int(psc4[0:1]) + 6) and (
            result4s0 != "" or result4s1 != "" or result4s2 != "") and (
            result2t4 != "" or result2t5 != "" or result2t6 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p303 = "8 digit - 4 digit seq and 2 digit repeat no. found and 2 digit repeat no. found p303"
        print(p303)
    if p303 != "":
        print(p303)
        p303 = "0000162000" + p303

    if (tc3 > 0 and sc4 > 0) and (
            ptc3 != "" and psc4 != "" and int(ptc2[0:1]) >= int(psc4[0:1]) + 4 and pos2 >= int(ptc2[0:1]) + 2) and (
            result4s0 != "" or result4s1 != "") and (result2t4 != "" or result2t5 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p304 = "9 digit - 4 digit seq and 2 digit repeat no. found and 3 digit repeat no. found p304"
        print(p304)
    if (tc3 == 2 and sc4 == 1 and tc2 == 4) and (
            ptc3 != "" and psc4 != "" and int(ptc2[1:2]) >= int(psc4[0:1]) + 4 and pos2 >= int(ptc2[1:2]) + 2) and (
            result4s0 != "" or result4s1 != "") and (result2t4 != "" or result2t5 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p304 = "9 digit - 4 digit seq and 2 digit repeat no. found and 3 digit repeat no. found p304"
        print(p304)
    if p304 != "":
        print(p304)
        p304 = "0000010600" + p304
    if (tc2 > 0 and sc4 > 0) and (
            ptc2 != "" and psc4 != "" and int(ptc2[0:1]) >= int(psc4[0:1]) + 4 and pos1 >= pos3 + 2) and (
            result4s0 != "" or result4s1 != "") and (result2t4 != "" or result2t5 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p305 = "9 digit - 4 digit seq and 2 digit repeat no. found and 3 digit seq no. found p305"
        print(p305)
    if (tc2 == 2 and sc4 == 2) and (
            ptc2 != "" and psc4 != "" and int(ptc2[1:2]) >= int(psc4[0:1]) + 4 and pos1 >= int(ptc2[0:1]) + 2) and (
            result4s0 != "" or result4s1 != "") and (result2t4 != "" or result2t5 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p305 = "9 digit - 4 digit seq and 2 digit repeat no. found and 3 digit seq no. found p305"
        print(p305)
    if (tc2 == 2 and sc4 == 1) and (
            ptc2 != "" and psc4 != "" and int(ptc2[1:2]) >= int(psc4[0:1]) + 4 and pos1 >= int(ptc2[0:1]) + 2) and (
            result4s0 != "" or result4s1 != "") and (result2t4 != "" or result2t5 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p305 = "9 digit - 4 digit seq and 2 digit repeat no. found and 3 digit seq no. found p305"
        print(p305)
    if (tc2 == 3 and sc4 == 1) and (
            ptc2 != "" and psc4 != "" and int(ptc2[1:2]) >= int(psc4[0:1]) + 4 and pos1 >= int(ptc2[1:2]) + 2) and (
            result4s0 != "" or result4s1 != "") and (result2t4 != "" or result2t5 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p305 = "9 digit - 4 digit seq and 2 digit repeat no. found and 3 digit seq no. found p305"
        print(p305)
    if p305 != "":
        print(p305)
        p305 = "0000016960" + p305
    if (result4s0 != "") and (result2t4 != "") and (result2t6 != "" and result2t8 != ""):
        p306 = "10 digit - 4 digit seq and 2 digit repeat no. found and 2-2 digit repeat no. found p306"
        print(p306)
        p306 = "0000005000" + p306
    if (result4s0 != "") and (result2t4 != "") and (result4t6 != ""):
        p307 = "10 digit - 4 digit seq and 2 digit repeat no. found and 4 digit repeat no. found p307"
        print(p307)
        p307 = "0000000500" + p307
    if (result4s0 != "") and (result2t4 != "") and (result4s6 != ""):
        p308 = "10 digit - 4 digit seq and 2 digit repeat no. found and 4 digit seq no. found p308"
        print(p308)
        p308 = "0000000700" + p308
    if (tc4 == 1 and tc5 < 1 and sc4 == 1 and sc5 < 1) and (result4t0 != "") and (result2t4 != "") and (
            result4s6 != ""):
        p309 = "10 digit - 4 digit repeat no. found and 2 digit repeat and 4 digit seq no. found p309"
        print(p309)
        p309 = "0000000560" + p309
    if (tc2 == 4 and tc3 == 2 and tc5 < 1) and (result4t0 != "" and result2t4 != ""):
        p310 = "6 digit - 4 digit repeat and 2 digit repeat no. found at start p310"
        print(p310)
        p310 = "0000400000" + p310
    if (tc2 == 4 and tc3 == 2 and tc5 < 1) and (ptc4 != "" and pos3 >= int(ptc4[0:1]) + 4) and (
            result4t0 != "" or result4t1 != "" or result4t2 != "" or result4t3 != "" or result4t4 != "") and (
            result2t4 != "" or result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p311 = "6 digit - 4 digit repeat and 2 digit repeat no. found p311"
        print(p311)
        p311 = "0002000000" + p311
    if (tc4 > 0 and tc2 > 3) and (
            ptc4 != "" and int(ptc4[0:1]) <= int(ptc2[3:4]) - 4 and pos3 >= int(ptc4[0:1]) + 6) and (
            result4t0 != "" or result4t1 != "" or result4t2 != "") and (
            result2t4 != "" or result2t5 != "" or result2t6 != "") \
            and (result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p312 = "8 digit - 4 digit repeat and 2 digit repeat no. found and 2 digit repeat no. found p312"
        print(p312)
        p312 = "0000120000" + p312
    if (tc2 == 6 and tc3 == 3 and tc5 < 1) and (result4t0 != "" or result4t1 != "") and (
            result2t4 != "" or result2t5 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p313 = "9 digit - 4 digit repeat and 2 digit repeat no. found and 3 digit repeat no. found p313"
        print(p313)
        p313 = "0000008000" + p313
    if (tc4 > 0 and sc3 > 0 and tc2 > 3) and (
            ptc4 != "" and psc3 != "" and int(ptc2[3:4]) >= int(ptc4[0:1]) + 4 and pos1 >= int(ptc2[3:4]) + 2) and (
            result4t0 != "" or result4t1 != "") and (result2t4 != "" or result2t5 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p314 = "9 digit - 4 digit repeat and 2 digit repeat no. found and 3 digit seq no. found p314"
        print(p314)
        p314 = "0000012800" + p314
    if (result4t0 != "") and (result2t4 != "") and (result2t6 != "" and result2t8 != ""):
        p315 = "10 digit - 4 digit repeat and 2 digit repeat no. found and 2-2 digit repeat no. found p315"
        print(p315)
        p315 = "0000004000" + p315
    if (result4t0 != "") and (result2t4 != "") and (result4t6 != ""):
        p316 = "10 digit - 4 digit repeat and 2 digit repeat no. found and 4 digit repeat no. found p316"
        print(p316)
        p316 = "0000000400" + p316
    if (result4t0 != "") and (result2t4 != "") and (result4s6 != ""):
        p317 = "10 digit - 4 digit repeat and 2 digit repeat no. found and 4 digit seq no. found p317"
        print(p317)
        p317 = "0000000560" + p317
    if (tc2 == 6 and tc5 < 1) and (result4t0 != "") and (result2t4 != "") and (result2t6 != "") and (result2t8 != ""):
        p318 = "10 digit - 4 digit repeat no. found and 2 digit repeat no. 3 times found p318"
        print(p318)
        p318 = "0000004000" + p318
    if (tc2 == 3 and tc3 < 1) and (result2t0 != "" and result2t2 != "" and result2t4 != ""):
        p319 = "6 digit - 2 digit repeat and 2 digit repeat and 2 digit repeat no. found at start p319"
        print(p319)
        p319 = "0004000000" + p319
    if (tc2 == 3 and tc3 < 1) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != "" or result2t4 != ""):
        p320 = "6 digit - 2 digit repeat and 2 digit repeat and 2 digit repeat no. found p320"
        print(p320)
        p320 = "0020000000" + p320
    if (result4t0 != "") and (result6s4 != ""):
        p321 = "10 digit - 4 digit repeat no. found and 6 digit seq no. found p321"
        print(p321)
        p321 = "0000000040" + p321
    if (tc2 == 5 and tc3 == 1 and tc4 < 1) and (result2t0 != "" or result2t1 != "") and (
            result2t2 != "" or result2t3 != "") \
            and (result2t4 != "" or result2t5 != "") \
            and (result3t6 != "" or result3t7 != ""):
        p322 = "9 digit - 2 digit repeat and 2 digit repeat and 2 digit repeat no. found and 3 digit repeat no. found p322"
        print(p322)
        p322 = "0000080000" + p322
    if (tc2 > 2 and sc3 > 0) and (
            ptc2 != "" and psc3 != "" and int(ptc2[2:3]) >= int(ptc2[1:2]) + 2 and pos1 >= int(ptc2[2:3]) + 2 and int(
            ptc2[1:2]) >= int(ptc2[0:1]) + 2) and (result2t0 != "" or result2t1 != "") and (
            result2t2 != "" or result2t3 != "") \
            and (result2t4 != "" or result2t5 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p323 = "9 digit - 2 digit repeat and 2 digit repeat and 2 digit repeat no. found and 3 digit seq no. found p323"
        print(p323)
    if (tc2 == 4 and sc3 == 1) and (
            ptc2 != "" and psc3 != "" and pos3 >= int(ptc2[0:1]) + 4 and int(ptc2[2:3]) >= int(ptc2[1:2]) + 2 and int(
            ptc2[1:2]) >= int(ptc2[0:1]) + 2) and (result2t0 != "" or result2t1 != "") and (
            result2t2 != "" or result2t3 != "") \
            and (result2t4 != "" or result2t5 != "") \
            and (result3s6 != "" or result3s7 != ""):
        p323 = "9 digit - 2 digit repeat and 2 digit repeat and 2 digit repeat no. found and 3 digit seq no. found p323"
        print(p323)
    if p323 != "":
        print(p323)
        p323 = "0000012800" + p323
    if (result4t0 != "") and (result6t4 != ""):
        p324 = "10 digit - 4 digit repeat no. found and 6 digit repeat no. found p324"
        print(p324)
        p324 = "0000000040" + p324
    if (tc4 == 1 and tc5 < 1) and (result2t0 != "") and (result2t2 != "") and (result2t4 != "") and (result4t6 != ""):
        p325 = "10 digit - 2 digit repeat and 2 digit repeat and 2 digit repeat no. found and 4 digit repeat no. found p325"
        print(p325)
        p325 = "0000004000" + p325
    if (result2t0 != "") and (result2t2 != "") and (result2t4 != "") and (result4s6 != ""):
        p326 = "10 digit - 2 digit repeat and 2 digit repeat and 2 digit repeat no. found and 4 digit seq no. found p326"
        print(p326)
        p326 = "0000005600" + p326
    if (result4t0 != "") and (result3t4 != "") and (result3t7 != ""):
        p327 = "10 digit - 4 digit repeat no. found and 3 digit repeat and 3 digit repeat no. found p327"
        print(p327)
        p327 = "0000000400" + p327
    if (tc3 == 1 and tc4 < 1) and (result3t0 != "" and result2t3 != ""):
        p328 = "5 digit - 3 digit repeat and 2 digit repeat no. found at start p328"
        print(p328)
        p328 = "0004000000" + p328
    if (tc2 == 3 and tc4 < 1) and (ptc3 != "" and (pos3 > int(ptc3[0:1]) + 2)) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "" or result3t3 != "" or result3t4 != "" or result3t5 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p329 = "5 digit - 3 digit repeat and 2 digit repeat no. found p329"
        print(p329)
        p329 = "0024000000" + p329
    if (result4t0 != "") and (result3t4 != "") and (result3s7 != ""):
        p330 = "10 digit - 4 digit repeat no. found and 3 digit repeat and 3 digit seq no. found p330"
        print(p330)
        p330 = "0000000640" + p330
    if (tc2 == 5 and tc3 == 2 and tc4 < 1) and (
            ptc3 != "" and pos2 >= int(ptc3[0:1]) + 5 and ptc3[0:1] == ptc2[0:1]) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p331 = "8 digit - 3 digit repeat and 2 digit repeat no. found and 3 digit repeat no. found p331"
        print(p331)
        p331 = "0000120000" + p331
    if (tc3 > 0 and sc3 > 0) and (
            ptc3 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc3[0:1]) + 5 and pos3 >= int(ptc3[0:1]) + 3) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p332 = "8 digit - 3 digit repeat and 2 digit repeat no. found and 3 digit seq no. found p332"
        print(p332)
    if (tc3 == 1 and tc2 == 3 and sc3 == 2) and (
            ptc3 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc3[0:1]) + 5 and pos1 >= int(ptc2[2:3]) + 2) and (
            result3t0 != "" or result3t1 != "" or result3t2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p332 = "8 digit - 3 digit repeat and 2 digit repeat no. found and 3 digit seq no. found p332"
        print(p332)
    if p332 != "":
        print(p332)
        p332 = "0000192000" + p332
    if (result4t0 != "") and (result3s4 != "") and (result3s7 != ""):
        p333 = "10 digit - 4 digit repeat no. found and 3 digit seq and 3 digit seq no. found p333"
        print(p333)
        p333 = "0000001024" + p333
    if (tc2 == 6 and tc3 == 3 and tc5 < 1) and (result3t0 != "" or result3t1 != "") and (
            result2t3 != "" or result2t4 != "") and (result4t5 != "" or result4t6 != ""):
        p334 = "9 digit - 3 digit repeat and 2 digit repeat no. found and 4 digit repeat no. found p334"
        print(p334)
        p334 = "0000008000" + p334
    if (tc2 > 2 and tc3 > 0 and sc4 > 0) and (
            ptc3 != "" and psc4 != "" and pos3 >= int(ptc3[0:1]) + 3 and int(psc4[0:1]) >= pos3 + 2) and (
            result3t0 != "" or result3t1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4s5 != "" or result4s6 != ""):
        p335 = "9 digit - 3 digit repeat and 2 digit repeat no. found and 4 digit seq no. found p335"
        print(p335)
    if (tc2 == 4 and tc3 == 2 and sc4 == 1) and (
            ptc3 != "" and psc4 != "" and int(ptc2[2:3]) >= int(ptc3[0:1]) + 3 and int(psc4[0:1]) >= int(
            ptc2[2:3]) + 2) and (result3t0 != "" or result3t1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4s5 != "" or result4s6 != ""):
        p335 = "9 digit - 3 digit repeat and 2 digit repeat no. found and 4 digit seq no. found p335"
        print(p335)
    if (tc2 == 3 and tc3 == 1 and sc4 == 2) and (
            ptc3 != "" and psc4 != "" and int(ptc2[2:3]) >= int(ptc3[0:1]) + 3 and int(psc4[1:2]) >= int(
            ptc2[2:3]) + 2) and (result3t0 != "" or result3t1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4s5 != "" or result4s6 != ""):
        p335 = "9 digit - 3 digit repeat and 2 digit repeat no. found and 4 digit seq no. found p335"
        print(p335)
    if p335 != "":
        print(p335)
        p335 = "0000011200" + p335
    if (result4t0 != "") and (result3s4 != "") and (result3t7 != ""):
        p336 = "10 digit - 4 digit repeat no. found and 3 digit seq and 3 digit repeat no. found p336"
        print(p336)
        p336 = "0000000640" + p336
    if (tc3 == 2 and tc4 < 1) and (result3t0 != "") and (result2t3 != "") and ((result2t5 != "") and result3t7 != ""):
        p337 = "10 digit - 3 digit repeat and 2 digit repeat no. found and 2 digit repeat  no. and 3 digit repeat no. found p337"
        print(p337)
        p337 = "0000004000" + p337
    if (tc4 == 1 and tc5 < 1) and (
            result4t1 != "" or result4t2 != "" or result4t3 != "" or result4t4 != "" or result4t5 != "" or result4t6 != ""):
        p338 = "4 digit - 4 digit repeat no. found p338"
        print(p338)
        p338 = "0028000000" + p338
    if (tc3 == 1 and tc4 < 1 and sc3 == 1 and sc4 < 1) and (result3t0 != "") and (result2t3 != "") and (
            result3s5 != "") and (result2t8 != ""):
        p339 = "10 digit - 3 digit repeat and 2 digit repeat no. found and 3 digit seq  no. and 2 digit repeat no. found p339"
        print(p339)
        p339 = "0000006400" + p339
    if (tc3 == 2 and tc4 < 1) and (result3t0 != "") and (result2t3 != "") and (result3t5 != "") and (result2t8 != ""):
        p340 = "10 digit - 3 digit repeat and 2 digit repeat no. found and 3 digit repeat  no. and 2 digit repeat no. found p340"
        print(p340)
        p340 = "0000004000" + p340
    if (result3t0 != "") and (result2t3 != "") and (result5t5 != ""):
        p341 = "10 digit - 3 digit repeat and 2 digit repeat no. found and 5 digit repeat no. found p341"
        print(p341)
        p341 = "0000000400" + p341
    if (result3t0 != "") and (result2t3 != "") and (result5s5 != ""):
        p342 = "10 digit - 3 digit repeat and 2 digit repeat no. found and 5 digit seq no. found p342"
        print(p342)
        p342 = "0000000480" + p342
    if (result3s0 != "" and result2t3 != ""):
        p343 = "5 digit - 3 digit seq and 2 digit repeat no. found at start p343"
        print(p343)
        p343 = "0006000000" + p343
    if (sc3 > 0 and tc2 > 0) and (ptc2 != "" and psc3 != "" and pos3 >= int(psc3[0:1]) + 3) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p344 = "5 digit - 3 digit seq and 2 digit repeat no. found p344"
        print(p344)
        p344 = "0038000000" + p344
    if (sc3 > 0 and tc2 > 1) and (
            ptc2 != "" and psc3 != "" and int(ptc2[0:1]) >= int(psc3[0:1]) + 3 and pos3 >= int(ptc2[0:1]) + 2) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "" or result3s3 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "" or result2t6 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p345 = "7 digit - 3 digit seq and 2 digit repeat no. found and 2 digit repeat no. found p345"
        print(p345)
    if (sc3 == 1 and tc2 == 3) and (
            ptc2 != "" and psc3 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos3 >= int(ptc2[1:2]) + 2) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "" or result3s3 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "" or result2t6 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p345 = "7 digit - 3 digit seq and 2 digit repeat no. found and 2 digit repeat no. found p345"
        print(p345)
    if p345 != "":
        print(p345)
        p345 = "0002520000" + p345

    if (sc3 > 0 and tc3 > 0) and (
            ptc3 != "" and psc3 != "" and int(ptc2[0:1]) >= int(psc3[0:1]) + 3 and pos2 >= int(ptc2[0:1]) + 2) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p346 = "8 digit - 3 digit seq and 2 digit repeat no. found and 3 digit repeat no. found p346"
        print(p346)
    if (sc3 == 1 and tc3 == 2 and tc2 == 4) and (
            ptc3 != "" and psc3 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos2 >= int(ptc2[1:2]) + 2) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p346 = "8 digit - 3 digit seq and 2 digit repeat no. found and 3 digit repeat no. found p346"
        print(p346)
    if p346 != "":
        print(p346)
        p346 = "0000188000" + p346
    if (sc3 > 1 and tc2 > 0) and (
            ptc2 != "" and psc3 != "" and int(ptc2[0:1]) >= int(psc3[0:1]) + 3 and pos1 >= int(ptc2[0:1]) + 2) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p347 = "8 digit - 3 digit seq and 2 digit repeat no. found and 3 digit seq no. found p347"
        print(p347)
    if (sc3 == 3 and tc2 == 2) and (
            ptc2 != "" and psc3 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos1 >= pos3 + 2) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p347 = "8 digit - 3 digit seq and 2 digit repeat no. found and 3 digit seq no. found p347"
        print(p347)
    if (sc3 == 2 and tc2 == 2) and (
            ptc2 != "" and psc3 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos1 >= int(ptc2[1:2]) + 2) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p347 = "8 digit - 3 digit seq and 2 digit repeat no. found and 3 digit seq no. found p347"
        print(p347)
    if (sc3 == 2 and tc2 == 3) and (
            ptc2 != "" and psc3 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos1 >= int(ptc2[1:2]) + 2) and (
            result3s0 != "" or result3s1 != "" or result3s2 != "") and (
            result2t3 != "" or result2t4 != "" or result2t5 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p347 = "8 digit - 3 digit seq and 2 digit repeat no. found and 3 digit seq no. found p347"
        print(p347)
    if p347 != "":
        print(p347)
        p347 = "0000300800" + p347
    if (sc3 > 0 and tc2 > 2) and (
            ptc2 != "" and psc3 != "" and int(ptc2[0:1]) >= int(psc3[0:1]) + 3 and pos3 >= int(ptc2[1:2]) + 2 and int(
            ptc2[1:2]) >= int(ptc2[0:1]) + 2) and (result3s0 != "" or result3s1 != "") and (
            result2t3 != "" or result2t4 != "") and (
            (result2t5 != "" or result2t6 != "") and (result2t7 != "" or result2t8 != "")):
        p348 = "9 digit - 3 digit seq and 2 digit repeat no. found and 2 digit repeat no. and 2 digit repeat no. found ap348"
        print(p348)
    if (sc3 == 1 and tc2 == 4) and (
            ptc2 != "" and psc3 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos3 >= int(ptc2[1:2]) + 4 and int(
            ptc2[2:3]) >= int(ptc2[1:2]) + 2) and (result3s0 != "" or result3s1 != "") and (
            result2t3 != "" or result2t4 != "") and (
            (result2t5 != "" or result2t6 != "") and (result2t7 != "" or result2t8 != "")):
        p348 = "9 digit - 3 digit seq and 2 digit repeat no. found and 2 digit repeat no. and 2 digit repeat no. found bp348"
        print(p348)
    if p348 != "":
        print(p348)
        p348 = "0000064000" + p348
    if (sc3 > 0 and tc4 > 0) and (
            ptc4 != "" and psc3 != "" and int(ptc2[0:1]) >= int(psc3[0:1]) + 3 and pos4 >= int(ptc2[0:1]) + 2) and (
            result3s0 != "" or result3s1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4t5 != "" or result4t6 != ""):
        p349 = "9 digit - 3 digit seq and 2 digit repeat no. found and 4 digit repeat no. found p349"
        print(p349)
    if (sc3 == 1 and tc4 == 1 and tc2 == 5) and (
            ptc4 != "" and psc3 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos4 >= int(ptc2[1:2]) + 2) and (
            result3s0 != "" or result3s1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4t5 != "" or result4t6 != ""):
        p349 = "9 digit - 3 digit seq and 2 digit repeat no. found and 4 digit repeat no. found p349"
        print(p349)
    if p349 != "":
        print(p349)
        p349 = "0000012400" + p349
    if (tc2 > 0 and sc4 > 0) and (
            ptc2 != "" and psc4 != "" and int(ptc2[0:1]) >= int(psc3[0:1]) + 3 and pos5 >= int(ptc2[0:1]) + 2) and (
            result3s0 != "" or result3s1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4s5 != "" or result4s6 != ""):
        p350 = "9 digit - 3 digit seq and 2 digit repeat no. found and 4 digit seq no. found p350"
        print(p350)
    if (tc2 == 3 and sc4 == 1) and (
            ptc2 != "" and psc4 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos5 >= int(ptc2[1:2]) + 2) and (
            result3s0 != "" or result3s1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4s5 != "" or result4s6 != ""):
        p350 = "9 digit - 3 digit seq and 2 digit repeat no. found and 4 digit seq no. found p350"
        print(p350)
    if (tc2 == 2 and sc4 == 2) and (
            ptc2 != "" and psc4 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos5 >= int(ptc2[1:2]) + 2) and (
            result3s0 != "" or result3s1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4s5 != "" or result4s6 != ""):
        p350 = "9 digit - 3 digit seq and 2 digit repeat no. found and 4 digit seq no. found p350"
        print(p350)
    if (tc2 == 2 and sc4 == 1) and (
            ptc2 != "" and psc4 != "" and int(ptc2[1:2]) >= int(psc3[0:1]) + 3 and pos5 >= int(ptc2[1:2]) + 2) and (
            result3s0 != "" or result3s1 != "") and (result2t3 != "" or result2t4 != "") and (
            result4s5 != "" or result4s6 != ""):
        p350 = "9 digit - 3 digit seq and 2 digit repeat no. found and 4 digit seq no. found p350"
        print(p350)
    if p350 != "":
        print(p350)
        p350 = "0000017360" + p350
    if (tc4 == 1 and tc5 < 1) and (result4t0 != ""):
        p351 = "4 digit - 4 digit repeat no. found at start p351"
        print(p351)
        p351 = "0004000000" + p351
    if (result3s0 != "") and (result2t3 != "") and ((result2t5 != "") and result3t7 != ""):
        p352 = "10 digit - 3 digit seq and 2 digit repeat no. found and 2 digit repeat  no. and 3 digit repeat no. found p352"
        print(p352)
        p352 = "0000006000" + p352
    if (result4s0 != "") and (result4s4 != "") and (result2t8 != ""):
        p353 = "10 digit - 4 digit seq no. found and 4 digit seq and 2 digit repeat no. found p353"
        print(p353)
        p353 = "0000000700" + p353
    if (result3s0 != "") and (result2t3 != "") and (result3s5 != "") and (result2t8 != ""):
        p354 = "10 digit - 3 digit seq and 2 digit repeat no. found and 3 digit seq  no. and 2 digit repeat no. found p354"
        print(p354)
        p354 = "0000009600" + p354
    if (result3s0 != "") and (result2t3 != "") and (result3t5 != "") and (result2t8 != ""):
        p355 = "10 digit - 3 digit seq and 2 digit repeat no. found and 3 digit repeat  no. and 2 digit repeat no. found p355"
        print(p355)
        p355 = "0000006000" + p355
    if (result3s0 != "") and (result2t3 != "") and (result5t5 != ""):
        p356 = "10 digit - 3 digit seq and 2 digit repeat no. found and 5 digit repeat no. found p356"
        print(p356)
        p356 = "0000000600" + p356
    if (result3s0 != "") and (result2t3 != "") and (result5s5 != ""):
        p357 = "10 digit - 3 digit seq and 2 digit repeat no. found and 5 digit seq no. found p357"
        print(p357)
        p357 = "0000000720" + p357
    if (tc2 == 3 and tc3 == 1 and tc4 < 1) and (result2t0 != "" and result3t2 != ""):
        p358 = "5 digit - 2 digit repeat and 3 digit repeat no. found at start p358"
        print(p358)
        p358 = "0004000000" + p358
    if (tc2 == 3 and tc3 == 1 and tc4 < 1) and (
            ptc2 != "" and ptc3 != "" and int(ptc3[0:1]) >= int(ptc2[0:1]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "") and (
            result3t2 != "" or result3t3 != "" or result3t4 != "" or result3t5 != "" or
            result3t6 != "" or result3t7 != ""):
        p359 = "5 digit - 2 digit repeat and 3 digit repeat no. found p359"
        print(p359)
        p359 = "0024000000" + p359
    if (tc3 == 1) and (ptc3 != "" and int(ptc3[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= pos2 + 3) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result3t2 != "" or result3t3 != "" or result3t4 != "" or result3t5 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p360 = "7 digit - 2 digit repeat and 3 digit repeat no. found and 2 digit repeat no. found p360"
        print(p360)
        p360 = "0001600000" + p360
    if (tc3 == 2) and (ptc3 != "" and int(ptc3[0:1]) >= int(ptc2[0:1]) + 2 and pos2 >= int(ptc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3t2 != "" or result3t3 != "" or result3t4 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p361 = "8 digit - 2 digit repeat and 3 digit repeat no. found and 3 digit repeat no. found p361"
        print(p361)
        p361 = "0000120000" + p361
    if (sc3 > 0 and tc3 > 0) and (
            ptc3 != "" and psc3 != "" and int(ptc3[0:1]) >= int(ptc2[0:1]) + 2 and int(psc3[0:1]) >= int(
            ptc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3t2 != "" or result3t3 != "" or result3t4 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p362 = "8 digit - 2 digit repeat and 3 digit repeat no. found and 3 digit seq no. found p362"
        print(p362)
    if (sc3 == 2 and tc3 == 1) and (
            ptc3 != "" and psc3 != "" and int(ptc3[0:1]) >= int(ptc2[0:1]) + 2 and int(psc3[1:2]) >= int(
            ptc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3t2 != "" or result3t3 != "" or result3t4 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p362 = "8 digit - 2 digit repeat and 3 digit repeat no. found and 3 digit seq no. found p362"
        print(p362)
    if p362 != "":
        print(p362)
        p362 = "0000192000" + p362
    if (result4s0 != "") and (result4t4 != "") and (result2t8 != ""):
        p363 = "10 digit - 4 digit seq no. found and 4 digit repeat and 2 digit repeat no. found p363"
        print(p363)
        p363 = "0000000500" + p363
    if (tc4 == 1) and (ptc4 != "" and int(ptc3[0:1]) >= int(ptc2[0:1]) + 2 and pos4 >= int(ptc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "") and (result3t2 != "" or result3t3 != "") and (
            result4t5 != "" or result4t6 != ""):
        p364 = "9 digit - 2 digit repeat and 3 digit repeat no. found and 4 digit repeat no. found p364"
        print(p364)
        p364 = "0000008000" + p364
    if (sc4 > 0 and tc2 > 2) and (
            ptc3 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc2[0:1]) + 5 and int(psc4[0:1]) >= pos2 + 3) and (
            result2t0 != "" or result2t1 != "") and (result3t2 != "" or result3t3 != "") and (
            result4s5 != "" or result4s6 != ""):
        p365 = "9 digit - 2 digit repeat and 3 digit repeat no. found and 4 digit seq no. found p365"
        print(p365)
    if (sc4 == 1 and tc2 == 4) and (
            ptc3 != "" and psc4 != "" and int(psc4[0:1]) >= int(ptc2[0:1]) + 5 and int(ptc3[0:1]) >= int(
            ptc2[0:1]) + 2) and (result2t0 != "" or result2t1 != "") and (result3t2 != "" or result3t3 != "") and (
            result4s5 != "" or result4s6 != ""):
        p365 = "9 digit - 2 digit repeat and 3 digit repeat no. found and 4 digit seq no. found p365"
        print(p365)
    if (sc4 == 2 and tc2 == 3) and (
            ptc3 != "" and psc4 != "" and int(psc4[1:2]) >= int(ptc2[0:1]) + 5 and int(psc4[1:2]) >= int(
            ptc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "") and (result3t2 != "" or result3t3 != "") and (
            result4s5 != "" or result4s6 != ""):
        p365 = "9 digit - 2 digit repeat and 3 digit repeat no. found and 4 digit seq no. found p365"
        print(p365)
    if p365 != "":
        print(p365)
        p365 = "0000011200" + p365
    if (result4s0 != "") and (result2t4 != "") and (result4t6 != ""):
        p366 = "10 digit - 4 digit seq no. found and 2 digit repeat and 4 digit repeat no. found p366"
        print(p366)
        p366 = "0000000500" + p366
    if (result2t0 != "") and (result3t2 != "") and ((result2t5 != "") and result3t7 != ""):
        p367 = "10 digit - 2 digit repeat and 3 digit repeat no. found and 2 digit repeat  no. and 3 digit repeat no. found p367"
        print(p367)
        p367 = "0000004000" + p367
    if (result2t0 != "") and (result3t2 != "") and (result2t5 != "") and (result3s7 != ""):
        p368 = "10 digit - 2 digit repeat and 3 digit repeat no. found and 2 digit repeat  no. and 3 digit seq no. found p368"
        print(p368)
        p368 = "0000006400" + p368
    if (result2t0 != "") and (result3t2 != "") and (result3s5 != "") and (result2t8 != ""):
        p369 = "10 digit - 2 digit repeat and 3 digit repeat no. found and 3 digit seq  no. and 2 digit repeat no. found p369"
        print(p369)
        p369 = "0000006400" + p369
    if (result2t0 != "") and (result3t2 != "") and (result3t5 != "") and (result2t8 != ""):
        p370 = "10 digit - 2 digit repeat and 3 digit repeat no. found and 3 digit repeat  no. and 2 digit repeat no. found p370"
        print(p370)
        p370 = "0000004000" + p370
    if (result2t0 != "") and (result3t2 != "") and (result5t5 != ""):
        p371 = "10 digit - 2 digit repeat and 3 digit repeat no. found and 5 digit repeat no. found p371"
        print(p371)
        p371 = "0000000400" + p371
    if (result2t0 != "") and (result3t2 != "") and (result5s5 != ""):
        p372 = "10 digit - 2 digit repeat and 3 digit repeat no. found and 5 digit seq no. found p372"
        print(p372)
        p372 = "0000000480" + p372
    if (result2t0 != "" and result3s2 != ""):
        p373 = "5 digit - 2 digit repeat and 3 digit seq no. found at start p373"
        print(p373)
        p373 = "0006400000" + p373
    if (sc3 > 0 and tc2 > 0) and (ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p374 = "5 digit - 2 digit repeat and 3 digit seq no. found p374"
        print(p374)
    if (sc3 == 2 and tc2 == 1) and (ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 1) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p374 = "5 digit - 2 digit repeat and 3 digit seq no. found p374"
        print(p374)
    if (sc3 == 2 and tc2 == 2) and (ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 1) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p374 = "5 digit - 2 digit repeat and 3 digit seq no. found p374"
        print(p374)
    if p374 != "":
        print(p374)
        p374 = "0038400000" + p374
    if (sc3 > 0 and tc2 > 1) and (
            ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p375 = "7 digit - 2 digit repeat and 3 digit seq no. found and 2 digit repeat no. found p375"
        print(p375)
    if (sc3 == 2 and tc2 == 3) and (
            ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p375 = "7 digit - 2 digit repeat and 3 digit seq no. found and 2 digit repeat no. found p375"
        print(p375)
    if (sc3 == 2 and tc2 == 2) and (
            ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(ptc2[0:1]) + 5) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p375 = "7 digit - 2 digit repeat and 3 digit seq no. found and 2 digit repeat no. found p375"
        print(p375)
    if (sc3 == 3 and tc2 == 2) and (
            ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(ptc2[0:1]) + 5) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "" or result3s5 != "") \
            and (result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p375 = "7 digit - 2 digit repeat and 3 digit seq no. found and 2 digit repeat no. found p375"
        print(p375)
    if p375 != "":
        print(p375)
        p375 = "0002560000" + p375
    if (sc3 > 0 and tc3 > 0) and (
            ptc3 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and int(ptc3[0:1]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p376 = "8 digit - 2 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p376"
        print(p376)
    if (sc3 == 1 and tc3 == 2) and (
            ptc3 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and int(ptc3[0:1]) >= int(
            psc3[0:1]) + 2) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p376 = "8 digit - 2 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p376"
        print(p376)
    if (sc3 == 1 and tc3 == 3) and (
            ptc3 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(psc3[0:1]) + 4) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p376 = "8 digit - 2 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p376"
        print(p376)
    if (sc3 == 1 and tc3 == 2) and (
            ptc3 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and int(ptc3[1:2]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p376 = "8 digit - 2 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p376"
        print(p376)
    if (sc3 == 2 and tc3 == 2) and (
            ptc3 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 2 and int(ptc3[1:2]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p376 = "8 digit - 2 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p376"
        print(p376)
    if (sc3 == 2 and tc3 == 1) and (
            ptc3 != "" and psc3 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 2 and int(ptc3[0:1]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p376 = "8 digit - 2 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p376"
        print(p376)
    if (sc3 == 3 and tc3 == 1) and (
            ptc3 != "" and psc3 != "" and int(psc3[2:3]) >= int(ptc2[0:1]) + 2 and int(ptc3[0:1]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (result3t5 != "" or result3t6 != "" or result3t7 != ""):
        p376 = "8 digit - 2 digit repeat and 3 digit seq no. found and 3 digit repeat no. found p376"
        print(p376)
    if p376 != "":
        print(p376)
        p376 = "0000192000" + p376
    if (sc3 > 1 and tc2 > 0) and (
            ptc2 != "" and psc3 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and pos1 >= int(psc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "") and (
            result3s2 != "" or result3s3 != "" or result3s4 != "") \
            and (result3s5 != "" or result3s6 != "" or result3s7 != ""):
        p377 = "8 digit - 2 digit repeat and 3 digit seq no. found and 3 digit seq no. found p377"
        print(p377)
        p377 = "0000307200" + p377
    if (sc3 > 0 and tc2 > 2) and (psc3 != "" and ptc2 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and pos3 >= int(
            psc3[0:1]) + 5 and pos3 >= int(ptc2[1:2]) + 2) and (result2t0 != "" or result2t1 != "") and (
            result3s2 != "" or result3s3 != "") and (
            (result2t5 != "" or result2t6 != "") and (result2t7 != "" or result2t8 != "")):
        p378 = "9 digit - 2 digit repeat and 3 digit seq no. found and 2 digit repeat no.  and 2 digit repeat no. found p378"
        print(p378)
        p378 = "0000128000" + p378
    if (sc3 > 0 and tc4 > 0) and (
            psc3 != "" and ptc4 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and int(ptc4[0:1]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4t5 != "" or result4t6 != ""):
        p379 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit repeat no. found p379"
        print(p379)
    if (sc3 == 2 and tc4 == 2) and (
            psc3 != "" and ptc4 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 2 and int(ptc4[0:1]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4t5 != "" or result4t6 != ""):
        p379 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit repeat no. found p379"
        print(p379)
    if (sc3 == 2 and tc4 == 1) and (
            psc3 != "" and ptc4 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 2 and int(ptc4[0:1]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4t5 != "" or result4t6 != ""):
        p379 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit repeat no. found p379"
        print(p379)
    if (sc3 == 3 and tc4 == 1) and (
            psc3 != "" and ptc4 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 2 and int(ptc4[0:1]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4t5 != "" or result4t6 != ""):
        p379 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit repeat no. found p379"
        print(p379)
    if (sc3 == 1 and tc4 == 2) and (
            psc3 != "" and ptc4 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and int(ptc4[1:2]) >= int(
            psc3[0:1]) + 3) and (result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4t5 != "" or result4t6 != ""):
        p379 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit repeat no. found p379"
        print(p379)
    if p379 != "":
        print(p379)
        p379 = "0000012800" + p379
    if (sc4 > 0 and tc2 > 0) and (
            ptc2 != "" and psc4 != "" and int(psc3[0:1]) >= int(ptc2[0:1]) + 2 and pos5 >= int(psc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4s5 != "" or result4s6 != ""):
        p380 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit seq no. found p380"
        print(p380)
    if (sc4 == 3 and tc2 == 1) and (
            ptc2 != "" and psc4 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 2 and pos5 >= int(psc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4s5 != "" or result4s6 != ""):
        p380 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit seq no. found p380"
        print(p380)
    if (sc4 == 2 and tc2 == 2) and (
            ptc2 != "" and psc4 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 2 and pos5 >= int(psc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4s5 != "" or result4s6 != ""):
        p380 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit seq no. found p380"
        print(p380)
    if (sc4 == 2 and tc2 == 1) and (
            ptc2 != "" and psc4 != "" and int(psc3[1:2]) >= int(ptc2[0:1]) + 2 and pos5 >= int(psc3[0:1]) + 3) and (
            result2t0 != "" or result2t1 != "") and (result3s2 != "" or result3s3 != "") and (
            result4s5 != "" or result4s6 != ""):
        p380 = "9 digit - 2 digit repeat and 3 digit seq no. found and 4 digit seq no. found p380"
        print(p380)
    if p380 != "":
        print(p380)
        p380 = "0000017920" + p380
    if (result4s0 != "") and (result2t4 != "") and (result4s6 != ""):
        p381 = "10 digit - 4 digit seq no. found and 2 digit repeat and 4 digit seq no. found p381"
        print(p381)
        p381 = "0000000700" + p381
    if (result2t0 != "") and (result3s2 != "") and ((result2t5 != "") and result3t7 != ""):
        p382 = "10 digit - 2 digit repeat and 3 digit seq no. found and 2 digit repeat  no. and 3 digit repeat no. found p382"
        print(p382)
        p382 = "0000006400" + p382
    if (result2t0 != "") and (result3s2 != "") and (result2t5 != "") and (result3s7 != ""):
        p383 = "10 digit - 2 digit repeat and 3 digit seq no. found and 2 digit repeat  no. and 3 digit seq no. found p383"
        print(p383)
        p383 = "0000010240" + p383
    if (result2t0 != "") and (result3s2 != "") and (result3s5 != "") and (result2t8 != ""):
        p384 = "10 digit - 2 digit repeat and 3 digit seq no. found and 3 digit seq  no. and 2 digit repeat no. found p384"
        print(p384)
        p384 = "0000010240" + p384
    if (result2t0 != "") and (result3s2 != "") and (result3t5 != "") and (result2t8 != ""):
        p385 = "10 digit - 2 digit repeat and 3 digit seq no. found and 3 digit repeat  no. and 2 digit repeat no. found p385"
        print(p385)
        p385 = "0000006400" + p385
    if (result2t0 != "") and (result3s2 != "") and (result5t5 != ""):
        p386 = "10 digit - 2 digit repeat and 3 digit seq no. found and 5 digit repeat no. found p386"
        print(p386)
        p386 = "0000000640" + p386
    if (result2t0 != "") and (result3s2 != "") and (result5s5 != ""):
        p387 = "10 digit - 2 digit repeat and 3 digit seq no. found and 5 digit seq no. found p387"
        print(p387)
        p387 = "0000000768" + p387
    if (tc5 == 1 and tc6 < 1) and (result5t0 != ""):
        p388 = "5 digit - 5 digit repeat no. found at start p388"
        print(p388)
        p388 = "0000400000" + p388
    if (tc5 == 1 and tc6 < 1) and (
            result5t1 != "" or result5t2 != "" or result5t3 != "" or result5t4 != "" or result5t5 != ""):
        p389 = "5 digit - 5 digit repeat no. found p389"
        print(p389)
        p389 = "0002400000" + p389
    if (result5s0 != "") and ((result2t5 != "") and result3t7 != ""):
        p390 = "10 digit - 5 digit seq no. found and 2 digit repeat  no. and 3 digit repeat no. found p390"
        print(p390)
        p390 = "0000000400" + p390
    if (result5s0 != "") and (result2t5 != "") and (result3s7 != ""):
        p391 = "10 digit - 5 digit seq no. found and 2 digit repeat  no. and 3 digit seq no. found p391"
        print(p391)
        p391 = "0000000640" + p391
    if (result5s0 != "") and (result3s5 != "") and (result2t8 != ""):
        p392 = "10 digit - 5 digit seq no. found and 3 digit seq  no. and 2 digit repeat no. found p392"
        print(p392)
        p392 = "0000000640" + p392
    if (result5s0 != "") and (result3t5 != "") and (result2t8 != ""):
        p393 = "10 digit - 5 digit seq no. found and 3 digit repeat  no. and 2 digit repeat no. found p393"
        print(p393)
        p393 = "0000000400" + p393
    if (result5s0 != "") and (result5t5 != ""):
        p394 = "10 digit - 5 digit seq no. found and 5 digit repeat no. found p394"
        print(p394)
        p394 = "0000000040" + p394
    if (result5s0 != "") and (result5s5 != ""):
        p395 = "10 digit - 5 digit seq no. found and 5 digit seq no. found p395"
        print(p395)
        p395 = "0000000048" + p395
    if (result4s0 != "" or result4s6 != ""):
        p396 = "4 digit - 4 digit seq no. found at start or end p396"
        print(p396)
        p396 = "0005000000" + p396
    if (result5t0 != "") and ((result2t5 != "") and result3t7 != ""):
        p397 = "10 digit - 5 digit repeat no. found and 2 digit repeat  no. and 3 digit repeat no. found p397"
        print(p397)
        p397 = "0000000400" + p397
    if (result5t0 != "") and (result2t5 != "") and (result3s7 != ""):
        p398 = "10 digit - 5 digit repeat no. found and 2 digit repeat  no. and 3 digit seq no. found p398"
        print(p398)
        p398 = "0000000640" + p398
    if (result5t0 != "") and (result3s5 != "") and (result2t8 != ""):
        p399 = "10 digit - 5 digit repeat no. found and 3 digit seq  no. and 2 digit repeat no. found p399"
        print(p399)
        p399 = "0000000640" + p399
    if (result5t0 != "") and (result3t5 != "") and (result2t8 != ""):
        p400 = "10 digit - 5 digit repeat no. found and 3 digit repeat  no. and 2 digit repeat no. found p400"
        print(p400)
        p400 = "0000000400" + p400
    if (result5t0 != "") and (result5t5 != ""):
        p401 = "10 digit - 5 digit repeat no. found and 5 digit repeat no. found p401"
        print(p401)
        p401 = "0000000040" + p401
    if (result5t0 != "") and (result5s5 != ""):
        p402 = "10 digit - 5 digit repeat no. found and 5 digit seq no. found p402"
        print(p402)
        p402 = "0000000048" + p402
    if (sc5 == 1 and sc6 < 1) and (result5s0 != ""):
        p403 = "5 digit - 5 digit seq no. found at start p403"
        print(p403)
        p403 = "0000400000" + p403
    if (sc5 == 1 and sc6 < 1) and (
            result5s1 != "" or result5s2 != "" or result5s3 != "" or result5s4 != "" or result5s5 != ""):
        p404 = "5 digit - 5 digit seq no. found p404"
        print(p404)
        p404 = "0002800000" + p404
    if (sc4 == 1 and sc5 < 1) and (
            result4s1 != "" or result4s2 != "" or result4s3 != "" or result4s4 != "" or result4s5 != "" or result4s5 != ""):
        p405 = "4 digit - 4 digit seq no. found p405"
        print(p405)
        p405 = "0038600000" + p405
    if (result4s0 != "") and (result3s4 != "") and (result3t7 != ""):
        p406 = "10 digit - 4 digit seq no. found and 3 digit seq and 3 digit repeat no. found p406"
        print(p406)
        p406 = "0000000800" + p406
    if (result4s0 != "") and (result3t4 != "") and (result3s7 != ""):
        p407 = "10 digit - 4 digit seq no. found and 3 digit repeat and 3 digit seq no. found p407"
        print(p407)
        p407 = "0000000800" + p407
    if (result4s0 != "") and (result3t4 != "") and (result3t7 != ""):
        p408 = "10 digit - 4 digit seq no. found and 3 digit repeat and 3 digit repeat no. found p408"
        print(p408)
        p408 = "0000000500" + p408
    if (result4s0 != "") and (result6t4 != ""):
        p409 = "10 digit - 4 digit seq no. found and 6 digit repeat no. found p409"
        print(p409)
        p409 = "0000000050" + p409
    if (sc4 == 1 and sc5 < 1 and tc2 == 3 and tc3 < 1) and (result4s0 != "") and (result2t4 != "") and (
            result2t6 != "") and (result2t8 != ""):
        p410 = "10 digit - 4 digit seq no. found and 2 digit repeat no. 3 times found p410"
        print(p410)
        p410 = "0000005000" + p410

    if result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4 and result2p0 == result2p6 and result2p0 == result2p8:
        p501 = "10 digit - same 2 digit no. 5 times found p501"
        print(p501)
        p501 = "0000000040" + p501
    if (result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4 and result2p0 == result2p6) or (
            result2p2 != "" and result2p2 == result2p4 and result2p2 == result2p6 and result2p2 == result2p8):
        p502 = "8 digit - same 2 digit no. 4 times found at start p502"
        print(p502)
        p502 = "0000004000" + p502
    if (result2p1 != "" and result2p1 == result2p3 and result2p1 == result2p5 and result2p1 == result2p7) and (
            result1p0 == result1p9):
        p503 = "10 digit - same 2 digit no. 4 times found with same starting and ending no. p503"
        print(p503)
        p503 = "0000000400" + p503
    if pc2 == 4 or pc3 == 4 or pc4 == 4:
        p504 = "8 digit - 2 digit same no. 4 times found p504"
        print(p504)
        p504 = "0000012000" + p504
    if ((
            result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4 and result2p0 == result2p6 and result2t8 != "") or (
            result2p2 != "" and result2p2 == result2p4 and result2p2 == result2p6 and result2p2 == result2p8 and result2t0 != "") or (
            result2p0 != "" and result2p0 == result2p4 and result2p0 == result2p6 and result2p0 == result2p8 and result2t2 != "") or (
            result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p6 and result2p0 == result2p8 and result2t4 != "") or (
            result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4 and result2p0 == result2p8 and result2t6 != "")):
        p505 = "10 digit - same 2 digit no. 4 times with 2 digit repeat no. found p505"
        print(p505)
        p505 = "0000000400" + p505
    if (
            result2p0 != "" and result2p0 == result2p2 and result2p4 != "" and result2p4 != result2p0 and result2p4 == result2p6) or (
            result2p2 != "" and result2p2 == result2p4 and result2p6 != result2p4 and result2p6 != "" and result2p6 == result2p8):
        p506 = "8 digit - same 2 digit no. 2 times and different 2 digit no. 2 times found at start p506"
        print(p506)
        p506 = "0000400000" + p506
    if (
            result2p1 != "" and result2p1 == result2p3 and result2p5 != "" and result2p5 != result2p1 and result2p5 == result2p7 and result1p0 == result1p9):
        p507 = "10 digit - same 2 digit no. 2 times and different 2 digit no. 2 times found with same starting and ending no. p507"
        print(p507)
        p507 = "0000040000" + p507
    if ((
            result2p0 != "" and result2p0 == result2p2 and result2p4 != "" and result2p4 != result2p0 and result2p4 == result2p6 and result2t8 != "") or (
            result2p2 != "" and result2p2 == result2p4 and result2p6 != "" and result2p6 != result2p2 and result2p6 == result2p8 and result2t0 != "")):
        p508 = "10 digit - same 2 digit no. 2 times and different 2 digit no. 2 times found at start or end and 2 digit repeat no. found p508"
        print(p508)
        p508 = "0000040000" + p508
    if ((dp0 == 3) and (dp1 == 2 or dp2 == 2 or dp3 == 2)) or ((dp0 == 2) and (dp1 == 3 or dp2 == 3 or dp3 == 3)):
        p509 = "10 digit - same 2 digit no. 3 times and different 2 digit no. 2 times found p509"
        print(p509)
        p509 = "0000004000" + p509
    if ((pc2 > 1) and ((pc4 == 2 and (int(ppc2[0:1]) > int(ppc4) + 1 or int(ppc2[0:1]) < int(ppc4) - 1) and (
            int(ppc2[0:1]) > 3 or int(ppc2[0:1]) < 1)) or (
                               pc5 == 2 and (int(ppc2[0:1]) > int(ppc5) + 1 or int(ppc2[0:1]) < int(ppc5) - 1) and (
                               int(ppc2[0:1]) > 4 or int(ppc2[0:1]) < 2)) or (
                               pc6 == 2 and (int(ppc2[0:1]) > int(ppc6) + 1 or int(ppc2[0:1]) < int(ppc6) - 1) and (
                               int(ppc2[0:1]) > 5 or int(ppc2[0:1]) < 3)) or (
                               pc7 == 2 and (int(ppc2[0:1]) > int(ppc7) + 1 or int(ppc2[0:1]) < int(ppc7) - 1) and (
                               int(ppc2[0:1]) > 6 or int(ppc2[0:1]) < 4)) or (
                               pc8 == 2 and (int(ppc2[0:1]) > int(ppc8) + 1 or int(ppc2[0:1]) < int(ppc8) - 1) and (
                               int(ppc2[0:1]) > 7 or int(ppc2[0:1]) < 5)))):
        p510 = "8 digit - same 2 digit no. 2 times and different 2 digit no. 2 times found ap510"
        print(p510)
    if ((pc3 > 1) and ((pc5 == 2 and (int(ppc3[0:1]) > int(ppc5) + 1 or int(ppc3[0:1]) < int(ppc5) - 1) and (
            int(ppc3[0:1]) > 4 or int(ppc3[0:1]) < 2)) or (
                               pc6 == 2 and (int(ppc3[0:1]) > int(ppc6) + 1 or int(ppc3[0:1]) < int(ppc6) - 1) and (
                               int(ppc3[0:1]) > 5 or int(ppc3[0:1]) < 3)) or (
                               pc7 == 2 and (int(ppc3[0:1]) > int(ppc7) + 1 or int(ppc3[0:1]) < int(ppc7) - 1) and (
                               int(ppc3[0:1]) > 6 or int(ppc3[0:1]) < 4)) or (
                               pc8 == 2 and (int(ppc3[0:1]) > int(ppc8) + 1 or int(ppc3[0:1]) < int(ppc8) - 1) and (
                               int(ppc3[0:1]) > 7 or int(ppc3[0:1]) < 5)))):
        p510 = "8 digit - same 2 digit no. 2 times and different 2 digit no. 2 times found bp510"
        print(p510)
    if ((pc4 == 2) and ((pc6 == 2 and (int(ppc4[0:1]) > int(ppc6) + 1 or int(ppc4[0:1]) < int(ppc6) - 1) and (
            int(ppc4[0:1]) > 5 or int(ppc4[0:1]) < 3)) or (
                                pc7 == 2 and (int(ppc4[0:1]) > int(ppc7) + 1 or int(ppc4[0:1]) < int(ppc7) - 1) and (
                                int(ppc4[0:1]) > 6 or int(ppc4[0:1]) < 4)) or (
                                pc8 == 2 and (int(ppc4[0:1]) > int(ppc8) + 1 or int(ppc4[0:1]) < int(ppc8) - 1) and (
                                int(ppc4[0:1]) > 7 or int(ppc4[0:1]) < 5)))):
        p510 = "8 digit - same 2 digit no. 2 times and different 2 digit no. 2 times found cp510"
        print(p510)
    if p510 != "":
        print(p510)
        p510 = "0001200000" + p510
    if ((dp0 == 2 and (dp1 == 2 or dp2 == 2 or dp3 == 2)) or (dp1 == 2 and (dp2 == 2 or dp3 == 2)) or (
            dp2 == 2 and (dp3 == 2))) and (
            result2t0 != "" or result2t2 != "" or result2t6 != "" or result2t8 != "" or result2t4 != ""):
        p511 = "10 digit same - 2 digit no. 2 times and different 2 digit no. 2 times and 2 digit repeat no. found p511"
        print(p511)
        p511 = "0000040000" + p511
    if (result1p0 == result1p9) and ((pc3 == 2 and (pc5 == 2 or pc7 == 2)) or (pc5 == 2 and (pc7 == 2))):
        p512 = "10 digit - same 2 digit no. 2 times and different 2 digit no. 2 times with same starting and ending no. found p512"
        print(p512)
        p512 = "0000040000" + p512
    if (tc6 == 1 and tc7 < 1) and (result6t0 != "") and (result2p6 != "" and result2p6 == result2p8):
        p513 = "10 digit - 6 digit repeat and 2-2 digit same no. found p513"
        print(p513)
        p513 = "0000000400" + p513
    if (sc6 == 1 and sc7 < 1) and (result6s0 != "") and (result2p6 != "" and result2p6 == result2p8):
        p514 = "10 digit - 6 digit seq and 2-2 digit same no. found p514"
        print(p514)
        p514 = "0000000400" + p514
    if (result2p0 != "" and result2p0 == result2p2 and result2p2 == result2p4) or (
            result2p4 != "" and result2p4 == result2p6 and result2p6 == result2p8):
        p515 = "6 digit - 2-2-2 digit same no. found at start or end p515"
        print(p515)
        p515 = "0000400000" + p515
    if (tc4 == 1 and tc5 < 1) and (result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4) and (
            result4t6 != ""):
        p516 = "10 digit - 6 digit 2-2-2 digit same no. and 4 digit repeat no. found p516"
        print(p516)
        p516 = "0000000400" + p516
    if (sc4 == 1 and sc5 < 1) and (result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4) and (
            result4s6 != ""):
        p517 = "10 digit - 6 digit 2-2-2 digit same no. and 4 digit seq no. found p517"
        print(p517)
        p517 = "0000000560" + p517
    if (tc2 == 2 and tc3 < 1) and (result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4) and (
            result2t6 != "" and result2t8 != ""):
        p518 = "10 digit - 6 digit 2-2-2 digit same no. and 2-2 digit repeat no. found p518"
        print(p518)
        p518 = "0000004000" + p518
    if (result2p0 != "" and result2p0 == result2p2 and result2p0 == result2p4) and (
            result2p6 != "" and result2p6 != result2p4 and result2p6 == result2p8):
        p519 = "10 digit - 6 digit 2-2-2 digit same no. and 2-2 digit other same no. found p519"
        print(p519)
        p519 = "0000004000" + p519
    if (result3t0 != "") and (result3s3 != "") and (result2p6 != "" and result2p6 == result2p8):
        p520 = "10 digit - 3 digit repeat and 3 digit seq no. found and 2 digit same no. 2 times found p520"
        print(p520)
        p520 = "0000006400" + p520
    if (result3s0 != "") and (result3t3 != "") and (result2p6 != "" and result2p6 == result2p8):
        p521 = "10 digit - 3 digit seq and 3 digit repeat no. found and 2 digit same no. 2 times found p521"
        print(p521)
        p521 = "0000006000" + p521
    if (result3s0 != "") and (result3s3 != "") and (result2p6 != "" and result2p6 == result2p8):
        p522 = "10 digit - 3 digit seq and 3 digit seq no. found and 2-2 digit same no. found p522"
        print(p522)
        p522 = "0000009600" + p522
    if (result3t0 != "") and (result3t3 != "") and (result2p6 != "" and result2p6 == result2p8):
        p523 = "10 digit - 3 digit repeat and 3 digit repeat no. found and 2-2 digit same no. found p523"
        print(p523)
        p523 = "0000004000" + p523
    if (result2t0 != "") and (result4s2 != "") and (result2p6 != "" and result2p6 == result2p8):
        p524 = "10 digit - 2 digit repeat and 4 digit seq no. found and 2-2 digit same no. found p524"
        print(p524)
        p524 = "0000005600" + p524
    if (result2t0 != "") and (result4t2 != "") and (result2p6 != "" and result2p6 == result2p8):
        p525 = "10 digit - 2 digit repeat and 4 digit repeat no. found and 2-2 digit same no. found p525"
        print(p525)
        p525 = "0000004000" + p525
    if (result4s0 != "") and (result2t4 != "") and (result2p6 != "" and result2p6 == result2p8):
        p526 = "10 digit - 4 digit seq and 2 digit repeat no. found and 2-2 digit same no. found p526"
        print(p526)
        p526 = "0000005000" + p526
    if (result4t0 != "") and (result2t4 != "") and (result2p6 != "" and result2p6 == result2p8):
        p527 = "10 digit - 4 digit repeat and 2 digit repeat no. found and 2-2 digit same no. found p527"
        print(p527)
        p527 = "0000004000" + p527
    if (tc2 == 5 and tc3 < 1) and (result2t0 != "") and (result2t2 != "") and (result2t4 != "") and (
            result2p6 != "" and result2p6 == result2p8):
        p528 = "10 digit - 2 digit repeat and 2 digit repeat and 2 digit repeat no. found and 2-2 digit same no. found p528"
        print(p528)
        p528 = "0000040000" + p528
    if (result4s0 != "") and (
            result2p4 != "" and result2p4 == result2p6 and result2p4 == result2p8 and result2p4 == result2p8):
        p529 = "10 digit - 4 digit seq no. found and 2 digit same no. 3 times found p529"
        print(p529)
        p529 = "0000000500" + p529
    if (result4t0 != "") and (
            result2p4 != "" and result2p4 == result2p6 and result2p4 == result2p8 and result2p4 == result2p8):
        p530 = "10 digit - 4 digit repeat no. found and 2 digit same no. 3 times found p530"
        print(p530)
        p530 = "0000000400" + p530
    if (result2t0 != "" and result2t2 != "") and (
            result2p4 != "" and result2p4 == result2p6 and result2p4 == result2p8 and result2p4 == result2p8):
        p531 = "10 digit - 2 digit repeat no. 2 times found and 2 digit same no. 3 times found p531"
        print(p531)
        p531 = "0000004000" + p531
    if ((result2p0 != "" and result2p0 == result2p2) or (result2p6 != "" and result2p6 == result2p8)):
        p532 = "4 digit - 2 digit same no. found 2 times at start or end p532"
        print(p532)
        p532 = "0040000000" + p532
    if pc2 == 2 or pc3 == 2 or pc4 == 2 or pc5 == 2 or pc6 == 2 or pc7 == 2 or pc8 == 2:
        p533 = "4 digit - 2 digit same no. 2 times found p533"
        print(p533)
        p533 = "0320000000" + p533
    if ((result2p0 != "" and result2p0 == result2p2)) and (result3s4 != "") and (result3t7 != ""):
        p534 = "10 digit - 2 digit same no. 2 times found and 3 digit seq and 3 digit repeat no. found p534"
        print(p534)
        p534 = "0000006400" + p534
    if ((result2p0 != "" and result2p0 == result2p2)) and (result3s4 != "") and (result3s7 != ""):
        p535 = "10 digit - 2 digit same no. 2 times found and 3 digit seq and 3 digit seq no. found p535"
        print(p535)
        p535 = "0000010240" + p535
    if ((result2p0 != "" and result2p0 == result2p2)) and (result3t4 != "") and (result3s7 != ""):
        p536 = "10 digit - 2 digit same no. 2 times found and 3 digit repeat and 3 digit seq no. found p536"
        print(p536)
        p536 = "0000006400" + p536
    if ((result2p0 != "" and result2p0 == result2p2)) and (result3t4 != "") and (result3t7 != ""):
        p537 = "10 digit - 2 digit same no. 2 times found and 3 digit repeat and 3 digit repeat no. found p537"
        print(p537)
        p537 = "0000004000" + p537
    if ((result2p0 != "" and result2p0 == result2p2)) and (result6t4 != ""):
        p538 = "10 digit - 2 digit same no. 2 times found and 6 digit repeat no. found p538"
        print(p538)
        p538 = "0000000400" + p538
    if ((result2p0 != "" and result2p0 == result2p2)) and (result6s4 != ""):
        p539 = "10 digit - 2 digit same no. 2 times found and 6 digit seq no. found p539"
        print(p539)
        p539 = "0000000400" + p539
    if ((result2p0 != "" and result2p0 == result2p2)) and (
            result2p4 != "" and result2p4 != result2p0 and result2p4 == result2p6 and result2p4 == result2p8 and result2p4 == result2p8):
        p540 = "10 digit - 2 digit same no. 2 times found and different 2 digit same no. 3 times found p540"
        print(p540)
        p540 = "0000004000" + p540
    if ((result2p0 != "" and result2p0 == result2p2)) and (result2t4 != "") and (result4s6 != ""):
        p541 = "10 digit - 2 digit same no. 2 times found and 2 digit repeat and 4 digit seq no. found p541"
        print(p541)
        p541 = "0000005600" + p541
    if ((result2p0 != "" and result2p0 == result2p2)) and (result2t4 != "") and (result4t6 != ""):
        p542 = "10 digit - 2 digit same no. 2 times found and 2 digit repeat and 4 digit repeat no. found p542"
        print(p542)
        p542 = "0000004000" + p542
    if ((result2p0 != "" and result2p0 == result2p2)) and (result4t4 != "") and (result2t8 != ""):
        p543 = "10 digit - 2 digit same no. 2 times found and 4 digit repeat and 2 digit repeat no. found p543"
        print(p543)
        p543 = "0000004000" + p543
    if ((result2p0 != "" and result2p0 == result2p2)) and (result4s4 != "") and (result2t8 != ""):
        p544 = "10 digit - 2 digit same no. 2 times found and 4 digit seq and 2 digit repeat no. found p544"
        print(p544)
        p544 = "0000005600" + p544
    if (result2t0 != "") and (
            result2p2 != "" and result2p2 == result2p4 and result2p2 == result2p6 and result2p2 == result2p8):
        p545 = "10 digit - 2 digit repeat no. and 2 digit same no. 4 times found p545"
        print(p545)
        p545 = "0000000400" + p545
    if mobile[0:5] == mobile[5:10]:
        p546 = "10 digit - Mirror no. found p546"
        print(p546)
        p546 = "0000040000" + p546
    if mobile[0:1] == mobile[9:10] and mobile[1:2] == mobile[8:9] and mobile[2:3] == mobile[7:8] and mobile[
                                                                                                     3:4] == mobile[
                                                                                                             6:7] and mobile[
                                                                                                                      4:5] == mobile[
                                                                                                                              5:6]:
        p547 = "10 digit - 5 digit palindrome no. found p547"
        print(p547)
        p547 = "0000040000" + p547
    start5a = mobile[0:2]
    start5b = mobile[5:7]
    if start5a == start5b:
        p548 = "10 digit - 5 digit no. start from same 2 digit no. p548"
        print(p548)
        p548 = "0040000000" + p548
    start5c = mobile[0:3]
    start5d = mobile[5:8]
    if start5c == start5d:
        p549 = "10 digit - 5 digit no. start from same 3 digit no. p549"
        print(p549)
        p549 = "0004000000" + p549
    start5e = mobile[0:4]
    start5f = mobile[5:9]
    if start5e == start5f:
        p550 = "10 digit - 5 digit no. start from same 4 digit no. p550"
        print(p550)
        p550 = "0000400000" + p550
    if pc4p == 2 or pc4p1 == 2 or pc4p2 == 2:
        p551 = "8 digit - semi mirror 4 digit same no. 2 times found p551"
        print(p551)
        p551 = "0000400000" + p551
    if (result4p1 == result4p5) and (result1p0 == result1p9):
        p552 = "10 digit - semi mirror 4 digit same no. 2 times found with same starting and ending no.  p552"
        print(p552)
        p552 = "0000040000" + p552
    if (result4p0 == result4p4) and (result2t8 != ""):
        p553 = "10 digit - semi mirror 4 digit same no. 2 times with 2 digit repeat no. found p553"
        print(p553)
        p553 = "0000040000" + p553
    if (result4p2 == result4p6) and (result2t0 != ""):
        p554 = "10 digit - semi mirror 2 digit repeat no. with 4 digit same no. 2 times found p554"
        print(p554)
        p554 = "0000040000" + p554
    if (result4p0 == result4p6) and (result2t4 != ""):
        p555 = "10 digit - semi mirror 4 digit same no. 2 times with 2 digit repeat no. at middle found p555"
        print(p555)
        p555 = "0000040000" + p555
    if pc3p == 2 or pc3p1 == 2 or pc3p2 == 2 or pc3p3 == 2 or pc3p4 == 2:
        p556 = "6 digit - 3 digit same no. 2 times found p556"
        print(p556)
        p556 = "0020000000" + p556
    if (pc3p == 3 or pc3p1 == 3) and result3t0 == "" and result3t1 == "":
        p557 = "9 digit - 3 digit same no. 3 times found p557"
        print(p557)
        p557 = "0000012000" + p557
    if (pc4p == 2 or pc4p1 == 2 or pc4p2 == 2) and (result4p1 == "1008" or result4p2 == "1008"):
        p558 = "8 digit - 1008 special no. 2 times found p558"
        print(p558)
        p558 = "0000000120" + p558
    if (result4p1 == result4p5) and (result1p0 == result1p9) and (result4p1 == "1008"):
        p559 = "10 digit - 1008 special no. 2 times found with same starting and ending no.  p559"
        print(p559)
        p559 = "0000000004" + p559
    if (result4p2 == result4p6) and (result2t0 != "") and (result4p2 == "1008"):
        p560 = "10 digit - 2 digit repeat no. with 1008 special no. 2 times found p560"
        print(p560)
        p560 = "0000000004" + p560
    if (
            result4p1 == "1008" or result4p2 == "1008" or result4p3 == "1008" or result4p4 == "1008" or result4p5 == "1008" or result4p6 == "1008"):
        p561 = "4 digit - 1008 special no. found p561"
        print(p561)
        p561 = "0002400000" + p561
    if (pc3p == 2 or pc3p1 == 2 or pc3p2 == 2 or pc3p3 == 2 or pc3p4 == 2) and (
            result3p0 == "786" or result3p1 == "786" or result3p2 == "786" or result3p3 == "786" or result3p4 == "786"):
        p562 = "6 digit - 786 special no. 2 times found p562"
        print(p562)
        p562 = "0000020000" + p562
    if (pc3p == 3 or pc3p1 == 3) and (result3p0 == "786" or result3p1 == "786"):
        p563 = "9 digit - 786 special no. 3 times found p563"
        print(p563)
        p563 = "0000000034" + p563
    if (pc3p == 2 or pc3p1 == 2 or pc3p2 == 2 or pc3p3 == 2 or pc3p4 == 2) and (
            result3p0 == "786" and result3p5 == "786"):
        p564 = "10 digit - 5 digit no. start from special 3 digit no.786 p564"
        print(p564)
        p564 = "0000010000" + p564
    if (mobile[0:5] == mobile[5:10]) and (mobile[2:5] == "786"):
        p565 = "10 digit - Mirror no. found with special no. 786 at end p565"
        print(p565)
        p565 = "0000000040" + p565
    if (mobile[0:5] == mobile[5:10]) and (mobile[1:4] == "786"):
        p566 = "10 digit - Mirror no. found with special no. 786 at middle p566"
        print(p566)
        p566 = "0000000040" + p566
    if (mobile[0:5] == mobile[5:10]) and (mobile[0:3] == "786"):
        p567 = "10 digit - Mirror no. found with starting special no. 786 p567"
        print(p567)
        p567 = "0000000100" + p567
    if (result4p6 == "1008"):
        p568 = "4 digit - 1008 special no. found at end p568"
        print(p568)
        p568 = "0000400000" + p568
    if (result3p0 == "786"):
        p569 = "3 digit - 786 special no. found at start p569"
        print(p569)
        p569 = "0010000000" + p569
    if (result3p7 == "786"):
        p570 = "3 digit - 786 special no. found at end p570"
        print(p570)
        p570 = "0004000000" + p570
    if (
            result3p1 == "786" or result3p2 == "786" or result3p3 == "786" or result3p4 == "786" or result3p5 == "786" or result3p6 == "786"):
        p571 = "3 digit - 786 special no. found  p571"
        print(p571)
        p571 = "0038000000" + p571
    if (result3p0 == "786" and result3p3 == "786"):
        p572 = "6 digit - 786 special no. found 2 times at start p572"
        print(p572)
        p572 = "0000010000" + p572
    if (result3p7 == "786" and result3p4 == "786"):
        p573 = "6 digit - 786 special no. found 2 times at end p573"
        print(p573)
        p573 = "0000004000" + p573

    if (
            result3p2 != "" and result3p3 != "" and result3p4 != "" and result3p5 != "" and result3p6 != "" and result3p7 != "") and (
            result2t0 != "" and (
            result3p2 == result3p5 or result3p2 == result3p6 or result3p2 == result3p7 or result3p3 == result3p6 or result3p3 == result3p7 or result3p4 == result3p7)):
        p574 = "8a digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if (result3p3 != "" and result3p4 != "" and result3p5 != "" and result3p6 != "" and result3p7 != "") and (
            result2t1 != "" and (result3p3 == result3p6 or result3p3 == result3p7 or result3p4 == result3p7)):
        p574 = "8b digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if (result3p4 != "" and result3p5 != "" and result3p6 != "" and result3p7 != "") and (
            result2t2 != "" and (result3p4 == result3p7)):
        p574 = "8c digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if (result3p0 != "" and result3p5 != "" and result3p6 != "" and result3p7 != "") and (
            result2t3 != "" and (result3p0 == result3p5 or result3p0 == result3p6 or result3p0 == result3p7)):
        p574 = "8d digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if (result3p0 != "" and result3p1 != "" and result3p6 != "" and result3p7 != "") and (result2t4 != "" and (
            result3p0 == result3p6 or result3p0 == result3p7 or result3p1 == result3p6 or result3p1 == result3p7)):
        p574 = "8e digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if (result3p0 != "" and result3p1 != "" and result3p2 != "" and result3p7 != "") and (
            result2t5 != "" and (result3p0 == result3p7 or result3p1 == result3p7 or result3p2 == result3p7)):
        p574 = "8f digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if (result3p0 != "" and result3p3 != "") and (result2t6 != "" and (result3p0 == result3p3)):
        p574 = "8g digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if (result3p0 != "" and result3p3 != "" and result3p4 != "" and result3p1 != "") and (
            result2t7 != "" and (result3p0 == result3p3 or result3p0 == result3p4 or result3p1 == result3p4)):
        p574 = "8h digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if (
            result3p0 != "" and result3p3 != "" and result3p4 != "" and result3p5 != "" and result3p1 != "" and result3p2 != "") and (
            result2t8 != "" and (
            result3p0 == result3p3 or result3p0 == result3p4 or result3p0 == result3p5 or result3p1 == result3p4 or result3p1 == result3p5 or result3p2 == result3p5)):
        p574 = "8i digit - 3 digit same no. 2 times and 2 digit repeat no. found p574"
        print(p574)
    if p574 != "":
        print(p574)
        p574 = "0002000000" + p574
    p575 = ""
    if (result3p3 != "" and result3p4 != "" and result3p6 != "" and result3p7 != "") and (
            result3t0 != "" and (result3p3 == result3p6 or result3p3 == result3p7 or result3p4 == result3p7)):
        p575 = "9a digit - 3 digit same no. 2 times and 3 digit repeat no. found p575"
        print(p575)
    if (result3p4 != "" and result3p7 != "") and (result3t1 != "" and (result3p4 == result3p7)):
        p575 = "9b digit - 3 digit same no. 2 times and 3 digit repeat no. found p575"
        print(p575)
    if (result3p0 != "" and result3p6 != "" and result3p7 != "") and (
            result3t3 != "" and (result3p0 == result3p6 or result3p0 == result3p7)):
        p575 = "9c digit - 3 digit same no. 2 times and 3 digit repeat no. found p575"
        print(p575)
    if (result3p0 != "" and result3p1 != "" and result3p7 != "") and (
            result3t4 != "" and (result3p0 == result3p7 or result3p1 == result3p7)):
        p575 = "9d digit - 3 digit same no. 2 times and 3 digit repeat no. found p575"
        print(p575)
    if (result3p0 != "" and result3p3 != "") and (result3t6 != "" and (result3p0 == result3p3)):
        p575 = "9e digit - 3 digit same no. 2 times and 3 digit repeat no. found p575"
        print(p575)
    if (result3p0 != "" and result3p1 != "" and result3p3 != "" and result3p4 != "") and (
            result3t7 != "" and (result3p0 == result3p3 or result3p0 == result3p4 or result3p1 == result3p4)):
        p575 = "9f digit - 3 digit same no. 2 times and 3 digit repeat no. found p575"
        print(p575)
    if p575 != "":
        print(p575)
        p575 = "0000160000" + p575
    p576 = ""
    if (result3p3 != "" and result3p4 != "" and result3p6 != "" and result3p7 != "") and (
            result3s0 != "" and (result3p3 == result3p6 or result3p3 == result3p7 or result3p4 == result3p7)):
        p576 = "9a digit - 3 digit same no. 2 times and 3 digit seq no. found p576"
        print(p576)
    if (result3p4 != "" and result3p7 != "") and (result3s1 != "" and (result3p4 == result3p7)):
        p576 = "9b digit - 3 digit same no. 2 times and 3 digit seq no. found p576"
        print(p576)
    if (result3p0 != "" and result3p6 != "" and result3p7 != "") and (
            result3s3 != "" and (result3p0 == result3p6 or result3p0 == result3p7)):
        p576 = "9c digit - 3 digit same no. 2 times and 3 digit seq no. found p576"
        print(p576)
    if (result3p0 != "" and result3p1 != "" and result3p7 != "") and (
            result3s4 != "" and (result3p0 == result3p7 or result3p1 == result3p7)):
        p576 = "9d digit - 3 digit same no. 2 times and 3 digit seq no. found p576"
        print(p576)
    if (result3p0 != "" and result3p3 != "") and (result3s6 != "" and (result3p0 == result3p3)):
        p576 = "9e digit - 3 digit same no. 2 times and 3 digit seq no. found p576"
        print(p576)
    if (result3p0 != "" and result3p1 != "" and result3p3 != "" and result3p4 != "") and (
            result3s7 != "" and (result3p0 == result3p3 or result3p0 == result3p4 or result3p1 == result3p4)):
        p576 = "9f digit - 3 digit same no. 2 times and 3 digit seq no. found p576"
        print(p576)
    if p576 != "":
        print(p576)
        p576 = "0000252000" + p576
    if ((result4t0 != "" and (result3p4 == result3p7)) or (result4t3 != "" and (result3p0 == result3p7)) or (
            result4t6 != "" and (result3p0 == result3p3))):
        p577 = "10 digit - 3 digit same no. 2 times and 4 digit repeat no. found p577"
        print(p577)
        p577 = "0000004000" + p577
    if ((result4s0 != "" and (result3p4 == result3p7)) or (result4s3 != "" and (result3p0 == result3p7)) or (
            result4s6 != "" and (result3p0 == result3p3))):
        p578 = "10 digit - 3 digit same no. 2 times and 4 digit seq no. found p578"
        print(p578)
        p578 = "0000005600" + p578
    if ((result2t0 != "" and result2t2 != "" and (result3p4 == result3p7)) or (
            result2t0 != "" and result2t5 != "" and (result3p2 == result3p7)) or (
            result2t0 != "" and result2t8 != "" and (result3p2 == result3p5)) or (
            result2t6 != "" and result2t8 != "" and (result3p0 == result3p3)) or (
            result2t3 != "" and result2t8 != "" and (result3p0 == result3p5)) or (
            result2t3 != "" and result2t5 != "" and (result3p0 == result3p7))):
        p579 = "10 digit - 3 digit same no. 2 times and 2 digit repeat no. 2 times found p579"
        print(p579)
        p579 = "0000040000" + p579
    if (int(mobile[0:4]) == int(mobile[4:8]) + 1000 or int(mobile[0:4]) == int(mobile[5:9]) + 1000 or int(
            mobile[0:4]) == int(mobile[6:10]) + 1000 or int(mobile[1:5]) == int(mobile[5:9]) + 1000 or int(
            mobile[1:5]) == int(mobile[6:10]) + 1000 or int(mobile[2:6]) == int(mobile[6:10]) + 1000):
        p580 = "8 digit - 4 digit no. descending 2 times -1000 found p580"
        print(p580)
        p580 = "0001600000" + p580
    if int(mobile[0:5]) == int(mobile[5:10]) - 1:
        p581 = "10 digit - 5 digit no. ascending 2 times +1 found p581"
        print(p581)
        p581 = "0000040000" + p581
    if int(mobile[0:5]) == int(mobile[5:10]) + 1:
        p582 = "10 digit - 5 digit no. descending 2 times -1 found p582"
        print(p582)
        p582 = "0000040000" + p582
    if int(mobile[0:5]) == int(mobile[5:10]) - 10000:
        p583 = "10 digit - 5 digit no. ascending 2 times +10000 found p583"
        print(p583)
        p583 = "0000030000" + p583
    if int(mobile[0:5]) == int(mobile[5:10]) + 10000:
        p584 = "10 digit - 5 digit no. descending 2 times -10000 found p584"
        print(p584)
        p584 = "0000040000" + p584
    if plus1 != "":
        p585 = plus1
        print(p585 + " p585")
        if int(plus1[0:1]) == 4:
            p585 = "0320000000" + p585 + " p585"
        if int(plus1[0:1]) == 6:
            p585 = "0002400000" + p585 + " p585"
        if int(plus1[0:1]) == 8:
            p585 = "0000016000" + p585 + " p585"
        if int(plus1[0:1]) == 1:
            p585 = "0000000040" + p585 + " p585"
    if minus1 != "":
        p586 = minus1
        print(p586 + " p586")
        if int(minus1[0:1]) == 4:
            p586 = "0320000000" + p586 + " p586"
        if int(minus1[0:1]) == 6:
            p586 = "0002400000" + p586 + " p586"
        if int(minus1[0:1]) == 8:
            p586 = "0000016000" + p586 + " p586"
        if int(minus1[0:1]) == 1:
            p586 = "0000000040" + p586 + " p586"

    if plus2 != "":
        p587 = plus2
        print(p587 + " p587")
        if int(plus2[0:1]) == 4:
            p587 = "0320000000" + p587 + " p587"
        if int(plus2[0:1]) == 6:
            p587 = "0002400000" + p587 + " p587"
        if int(plus2[0:1]) == 8:
            p587 = "0000016000" + p587 + " p587"
        if int(plus2[0:1]) == 1:
            p587 = "0000000040" + p587 + " p587"

    if minus2 != "":
        p588 = minus2
        print(p588 + " p588")
        if int(minus2[0:1]) == 4:
            p588 = "0320000000" + p588 + " p588"
        if int(minus2[0:1]) == 6:
            p588 = "0002400000" + p588 + " p588"
        if int(minus2[0:1]) == 8:
            p588 = "0000016000" + p588 + " p588"
        if int(minus2[0:1]) == 1:
            p588 = "0000000040" + p588 + " p588"

    if plus3 != "":
        p589 = plus3
        print(p589 + " p589")
        if int(plus3[0:1]) == 4:
            p589 = "0320000000" + p589 + " p589"
        if int(plus3[0:1]) == 6:
            p589 = "0002400000" + p589 + " p589"
        if int(plus3[0:1]) == 8:
            p589 = "0000016000" + p589 + " p589"
        if int(plus3[0:1]) == 1:
            p589 = "0000000040" + p589 + " p589"

    if minus3 != "":
        p590 = minus3
        print(p590 + " p590")
        if int(minus3[0:1]) == 4:
            p590 = "0320000000" + p590 + " p590"
        if int(minus3[0:1]) == 6:
            p590 = "0002400000" + p590 + " p590"
        if int(minus3[0:1]) == 8:
            p590 = "0000016000" + p590 + " p590"
        if int(minus3[0:1]) == 1:
            p590 = "0000000040" + p590 + " p590"

    if plus4 != "":
        p591 = plus4
        print(p591 + " p591")
        if int(plus4[0:1]) == 4:
            p591 = "0320000000" + p591 + " p591"
        if int(plus4[0:1]) == 6:
            p591 = "0002400000" + p591 + " p591"
        if int(plus4[0:1]) == 8:
            p591 = "0000016000" + p591 + " p591"
        if int(plus4[0:1]) == 1:
            p591 = "0000000040" + p591 + " p591"

    if minus4 != "":
        p592 = minus4
        print(p592 + " p592")
        if int(minus4[0:1]) == 4:
            p592 = "0320000000" + p592 + " p592"
        if int(minus4[0:1]) == 6:
            p592 = "0002400000" + p592 + " p592"
        if int(minus4[0:1]) == 8:
            p592 = "0000016000" + p592 + " p592"
        if int(minus4[0:1]) == 1:
            p592 = "0000000040" + p592 + " p592"

    if plus5 != "":
        p593 = plus5
        print(p593 + " p593")
        if int(plus5[0:1]) == 4:
            p593 = "0320000000" + p593 + " p593"
        if int(plus5[0:1]) == 6:
            p593 = "0002400000" + p593 + " p593"
        if int(plus5[0:1]) == 8:
            p593 = "0000016000" + p593 + " p593"
        if int(plus5[0:1]) == 1:
            p593 = "0000000040" + p593 + " p593"

    if minus5 != "":
        p594 = minus5
        print(p594 + " p594")
        if int(minus5[0:1]) == 4:
            p594 = "0320000000" + p594 + " p594"
        if int(minus5[0:1]) == 6:
            p594 = "0002400000" + p594 + " p594"
        if int(minus5[0:1]) == 8:
            p594 = "0000016000" + p594 + " p594"
        if int(minus5[0:1]) == 1:
            p594 = "0000000040" + p594 + " p594"

    if plus10 != "":
        p595 = plus10
        print(p595 + " p595")
        if int(plus10[0:1]) == 4:
            p595 = "0320000000" + p595 + " p595"
        if int(plus10[0:1]) == 6:
            p595 = "0002400000" + p595 + " p595"
        if int(plus10[0:1]) == 8:
            p595 = "0000016000" + p595 + " p595"
        if int(plus10[0:1]) == 1:
            p595 = "0000000040" + p595 + " p595"

    if minus10 != "":
        p596 = minus10
        print(p596 + " p596")
        if int(minus10[0:1]) == 4:
            p596 = "0320000000" + p596 + " p596"
        if int(minus10[0:1]) == 6:
            p596 = "0002400000" + p596 + " p596"
        if int(minus10[0:1]) == 8:
            p596 = "0000016000" + p596 + " p596"
        if int(minus10[0:1]) == 1:
            p596 = "0000000040" + p596 + " p596"

    if (int(mobile[0:3]) == int(mobile[3:6]) - 1 and int(mobile[3:6]) == int(mobile[6:9]) - 1) or (
            int(mobile[0:3]) == int(mobile[3:6]) - 1 and int(mobile[3:6]) == int(mobile[7:10]) - 1) or (
            int(mobile[0:3]) == int(mobile[4:7]) - 1 and int(mobile[4:7]) == int(mobile[7:10]) - 1) or (
            int(mobile[1:4]) == int(mobile[4:7]) - 1 and int(mobile[4:7]) == int(mobile[7:10]) - 1):
        p597 = "9 digit - 3 digit no. ascending 3 times +1 found p597"
        print(p597)
        p597 = "0000008000" + p597
    if int(mobile[0:3]) == int(mobile[3:6]) - 1 or int(mobile[0:3]) == int(mobile[4:7]) - 1 or int(mobile[0:3]) == int(
            mobile[5:8]) - 1 or int(mobile[0:3]) == int(mobile[6:9]) - 1 or int(mobile[0:3]) == int(mobile[7:10]) - 1:
        p598 = "6a digit - 3 digit no. ascending 2 times +1 found p598"
        print(p598)
    if int(mobile[1:4]) == int(mobile[4:7]) - 1 or int(mobile[1:4]) == int(mobile[5:8]) - 1 or int(mobile[1:4]) == int(
            mobile[6:9]) - 1 or int(mobile[1:4]) == int(mobile[7:10]) - 1:
        p598 = "6b digit - 3 digit no. ascending 2 times +1 found p598"
        print(p598)
    if int(mobile[2:5]) == int(mobile[5:8]) - 1 or int(mobile[2:5]) == int(mobile[6:9]) - 1 or int(mobile[2:5]) == int(
            mobile[7:10]) - 1:
        p598 = "6c digit - 3 digit no. ascending 2 times +1 found p598"
        print(p598)
    if int(mobile[3:6]) == int(mobile[6:9]) - 1 or int(mobile[3:6]) == int(mobile[7:10]) - 1 or int(mobile[4:7]) == int(
            mobile[7:10]) - 1:
        p598 = "6d digit - 3 digit no. ascending 2 times +1 found p598"
        print(p598)

    if p598 != "":
        print(p598)
        p598 = "0016000000" + p598
    if (int(mobile[0:3]) == int(mobile[3:6]) + 1 and int(mobile[3:6]) == int(mobile[6:9]) + 1) or (
            int(mobile[0:3]) == int(mobile[3:6]) + 1 and int(mobile[3:6]) == int(mobile[7:10]) + 1) or (
            int(mobile[0:3]) == int(mobile[4:7]) + 1 and int(mobile[4:7]) == int(mobile[7:10]) + 1) or (
            int(mobile[1:4]) == int(mobile[4:7]) + 1 and int(mobile[4:7]) == int(mobile[7:10]) + 1):
        p599 = "9 digit - 3 digit no. descending 3 times -1 found p599"
        print(p599)
        p599 = "0000016000" + p599
    if int(mobile[0:3]) == int(mobile[3:6]) + 1 or int(mobile[0:3]) == int(mobile[4:7]) + 1 or int(mobile[0:3]) == int(
            mobile[5:8]) + 1 or int(mobile[0:3]) == int(mobile[6:9]) + 1 or int(mobile[0:3]) == int(mobile[7:10]) + 1:
        p600 = "6a digit - 3 digit no. descending 2 times -1 found p600"
        print(p600)
    if int(mobile[1:4]) == int(mobile[4:7]) + 1 or int(mobile[1:4]) == int(mobile[5:8]) + 1 or int(mobile[1:4]) == int(
            mobile[6:9]) + 1 or int(mobile[1:4]) == int(mobile[7:10]) + 1:
        p600 = "6b digit - 3 digit no. descending 2 times -1 found p600"
        print(p600)
    if int(mobile[2:5]) == int(mobile[5:8]) + 1 or int(mobile[2:5]) == int(mobile[6:9]) + 1 or int(mobile[2:5]) == int(
            mobile[7:10]) + 1:
        p600 = "6c digit - 3 digit no. descending 2 times -1 found p600"
        print(p600)
    if int(mobile[3:6]) == int(mobile[6:9]) + 1 or int(mobile[3:6]) == int(mobile[7:10]) + 1 or int(mobile[4:7]) == int(
            mobile[7:10]) + 1:
        p600 = "6d digit - 3 digit no. descending 2 times -1 found p600"
        print(p600)
    if p600 != "":
        print(p600)
        p600 = "0016000000" + p600
    if (int(mobile[0:4]) == int(mobile[4:8]) - 1 or int(mobile[0:4]) == int(mobile[5:9]) - 1 or int(mobile[0:4]) == int(
            mobile[6:10]) - 1 or int(mobile[1:5]) == int(mobile[5:9]) - 1 or int(mobile[1:5]) == int(
            mobile[6:10]) - 1 or int(mobile[2:6]) == int(mobile[6:10]) - 1):
        p601 = "8 digit - 4 digit no. ascending 2 times +1 found p601"
        print(p601)
        p601 = "0001200000" + p601
    if (int(mobile[0:4]) == int(mobile[4:8]) + 1 or int(mobile[0:4]) == int(mobile[5:9]) + 1 or int(mobile[0:4]) == int(
            mobile[6:10]) + 1 or int(mobile[1:5]) == int(mobile[5:9]) + 1 or int(mobile[1:5]) == int(
            mobile[6:10]) + 1 or int(mobile[2:6]) == int(mobile[6:10]) + 1):
        p602 = "8 digit - 4 digit no. descending 2 times -1 found p602"
        print(p602)
        p602 = "0001200000" + p602
    if plus1 != "" and minus1 != "":
        p603 = int(plus1[0:1]) + int(minus1[0:1])
        if p603 <= 10:
            p603 = str(p603) + " digit - " + plus1[10:50] + " and " + minus1[10:50] + " p603"
            print(p603)
            p603 = "0032000000" + p603
    if plus1 != "" and plus2 != "":
        t604 = int(plus1[0:1]) + int(plus2[0:1])
        if t604 <= 10:
            p604 = str(t604) + " digit - " + plus1[10:50] + " and " + plus2[10:50] + " p604"
            print(p604)
            p604 = "0032000000" + p604
        if t604 > 10:
            t604 = 10
            p604 = str(t604) + " digit - " + plus1[10:50] + " and " + plus2[10:50] + " p604"
            print(p604)
            p604 = "0001600000" + p604
    if plus5 != "" and minus5 != "":
        t605 = int(plus5[0:1]) + int(minus5[0:1])
        if t605 <= 10:
            p605 = str(p605) + " digit - " + plus5[10:50] + " and " + minus5[10:50] + " p605"
            print(p605)
            p605 = "0032000000" + p605
    if plus10 != "" and minus10 != "":
        t606 = int(plus10[0:1]) + int(minus10[0:1])
        if t606 <= 10:
            p606 = str(p606) + " digit - " + plus10[10:50] + " and " + minus10[10:50] + " p606"
            print(p606)
            p606 = "0032000000" + p606
    p607 = ""
    if (pc2 == 2) and ((result2t0 != "" and (result2p1 != result2p0)) or (
            result2t1 != "" and (result2p2 != result2p0) and (result2p0 != result2p0)) or (
                               result2t2 != "" and (result2p3 != result2p0) and (result2p1 != result2p0)) or (
                               result2t3 != "" and (result2p4 != result2p0) and (result2p2 != result2p0)) or (
                               result2t4 != "" and (result2p5 != result2p0) and (result2p3 != result2p0))
                       or (result2t5 != "" and (result2p6 != result2p0) and (result2p4 != result2p0)) or (
                               result2t6 != "" and (result2p7 != result2p0) and (result2p5 != result2p0)) or (
                               result2t7 != "" and (result2p8 != result2p0) and (result2p6 != result2p0)) or (
                               result2t8 != "" and (result2p7 != result2p0))):
        p607 = "6a digit - 2 digit same no. 2 times and 2 digit repeat no. found p607"
        print(p607)

    if (pc3 == 2) and ((result2t0 != "" and (result2p1 != result2p1)) or (
            result2t1 != "" and (result2p2 != result2p1) and (result2p0 != result2p1)) or (
                               result2t2 != "" and (result2p3 != result2p1) and (result2p1 != result2p1)) or (
                               result2t3 != "" and (result2p4 != result2p1) and (result2p2 != result2p1)) or (
                               result2t4 != "" and (result2p5 != result2p1) and (result2p3 != result2p1))
                       or (result2t5 != "" and (result2p6 != result2p1) and (result2p4 != result2p1)) or (
                               result2t6 != "" and (result2p7 != result2p1) and (result2p5 != result2p1)) or (
                               result2t7 != "" and (result2p8 != result2p1) and (result2p6 != result2p1)) or (
                               result2t8 != "" and (result2p7 != result2p1))):
        p607 = "6b digit - 2 digit same no. 2 times and 2 digit repeat no. found p607"
        print(p607)

    if (pc4 == 2) and ((result2t0 != "" and (result2p1 != result2p2)) or (
            result2t1 != "" and (result2p2 != result2p2) and (result2p0 != result2p2)) or (
                               result2t2 != "" and (result2p3 != result2p2) and (result2p1 != result2p2)) or (
                               result2t3 != "" and (result2p4 != result2p2) and (result2p2 != result2p2)) or (
                               result2t4 != "" and (result2p5 != result2p2) and (result2p3 != result2p2))
                       or (result2t5 != "" and (result2p6 != result2p2) and (result2p4 != result2p2)) or (
                               result2t6 != "" and (result2p7 != result2p2) and (result2p5 != result2p2)) or (
                               result2t7 != "" and (result2p8 != result2p2) and (result2p6 != result2p2)) or (
                               result2t8 != "" and (result2p7 != result2p2))):
        p607 = "6c digit - 2 digit same no. 2 times and 2 digit repeat no. found p607"
        print(p607)
    if (pc5 == 2) and ((result2t0 != "" and (result2p1 != result2p3)) or (
            result2t1 != "" and (result2p2 != result2p3) and (result2p0 != result2p3)) or (
                               result2t2 != "" and (result2p1 != result2p3) and (result2p3 != result2p3)) or (
                               result2t3 != "" and (result2p4 != result2p3) and (result2p2 != result2p3)) or (
                               result2t4 != "" and (result2p5 != result2p3) and (result2p3 != result2p3))
                       or (result2t5 != "" and (result2p6 != result2p3) and (result2p4 != result2p3)) or (
                               result2t6 != "" and (result2p7 != result2p3) and (result2p5 != result2p3)) or (
                               result2t7 != "" and (result2p8 != result2p3) and (result2p6 != result2p3)) or (
                               result2t8 != "" and (result2p7 != result2p3))):
        p607 = "6d digit - 2 digit same no. 2 times and 2 digit repeat no. found p607"
        print(p607)

    if (pc6 == 2) and ((result2t0 != "" and (result2p1 != result2p4)) or (
            result2t1 != "" and (result2p2 != result2p4) and (result2p0 != result2p4)) or (
                               result2t2 != "" and (result2p3 != result2p4) and (result2p1 != result2p4)) or (
                               result2t3 != "" and (result2p2 != result2p4) and (result2p4 != result2p4)) or (
                               result2t4 != "" and (result2p3 != result2p4) and (result2p5 != result2p4))
                       or (result2t5 != "" and (result2p6 != result2p4) and (result2p4 != result2p4)) or (
                               result2t6 != "" and (result2p7 != result2p4) and (result2p5 != result2p4)) or (
                               result2t7 != "" and (result2p8 != result2p4) and (result2p6 != result2p4)) or (
                               result2t8 != "" and (result2p7 != result2p4))):
        p607 = "6e digit - 2 digit same no. 2 times and 2 digit repeat no. found p607"
        print(p607)
    if (pc7 == 2) and ((result2t0 != "" and (result2p1 != result2p5)) or (
            result2t1 != "" and (result2p2 != result2p5) and (result2p0 != result2p5)) or (
                               result2t2 != "" and (result2p3 != result2p5) and (result2p1 != result2p5)) or (
                               result2t3 != "" and (result2p2 != result2p5) and (result2p4 != result2p5))
                       or (result2t4 != "" and (result2p3 != result2p5) and (result2p5 != result2p5)) or (
                               result2t5 != "" and (result2p6 != result2p5) and (result2p4 != result2p5)) or (
                               result2t6 != "" and (result2p7 != result2p5) and (result2p5 != result2p5)) or (
                               result2t7 != "" and (result2p8 != result2p5) and (result2p6 != result2p5)) or (
                               result2t8 != "" and (result2p7 != result2p5))):
        p607 = "6f digit - 2 digit same no. 2 times and 2 digit repeat no. found p607"
        print(p607)
    if (pc8 == 2) and ((result2t0 != "" and (result2p1 != result2p6)) or (
            result2t1 != "" and (result2p2 != result2p6) and (result2p0 != result2p6)) or (
                               result2t2 != "" and (result2p3 != result2p6) and (result2p1 != result2p6)) or (
                               result2t3 != "" and (result2p2 != result2p6) and (result2p4 != result2p6))
                       or (result2t4 != "" and (result2p3 != result2p6) and (result2p5 != result2p6)) or (
                               result2t5 != "" and (result2p6 != result2p6) and (result2p4 != result2p6)) or (
                               result2t6 != "" and (result2p7 != result2p6) and (result2p5 != result2p6)) or (
                               result2t7 != "" and (result2p8 != result2p6) and (result2p6 != result2p6)) or (
                               result2t8 != "" and (result2p7 != result2p6))):
        p607 = "6g digit - 2 digit same no. 2 times and 2 digit repeat no. found p607"
        print(p607)

    if (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            result2t0 != "" or result2t1 != "" or result2t2 != "" or result2t3 != "" or result2t4 != "" or result2t5 != "" or result2t6 != "" or result2t7 != "" or result2t8 != ""):
        p607 = "6h digit - 2 digit same no. 2 times and 2 digit repeat no. found p607"
        print(p607)
    if p607 != "":
        print(p607)
        p607 = "0028000000" + p607
    p608 = ""
    if result2t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p3 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p3 == result2p6 and result2t8 != "") or (result2p3 == result2p7 and result2t5 != "") or (
                    result2p3 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p4 == result2p6 and (result2t2 != "" or result2t8 != "")) or (
                    result2p4 == result2p7 and (result2t2 != "")) or (
                    result2p4 == result2p8 and (result2t2 != "" or result2t6 != "")) or (
                    result2p5 == result2p7 and (result2t2 != "" or result2t3 != "")) or (
                    result2p5 == result2p8 and (result2t2 != "" or result2t3 != "")) or (
                    result2p6 == result2p8 and (result2t2 != "" or result2t3 != "" or result2t4 != ""))
            or (result2p2 == result2p4 and (result2t6 != "" or result2t7 != "" or result2t8 != "")) or (
                    result2p2 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
                    result2p2 == result2p6 and (result2t4 != "" or result2t8 != "")) or (
                    result2p2 == result2p7 and (result2t4 != "" or result2t5 != "")) or (
                    result2p2 == result2p8 and (result2t4 != "" or result2t5 != "" or result2t6 != ""))):
        p608 = "8a digit - 2 digit same no. 2 times and 2 digit repeat no. 2 times found p608"
        print(p608)
    if result2t1 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p3 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p3 == result2p6 and result2t8 != "") or (result2p3 == result2p7 and result2t5 != "") or (
                    result2p3 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p4 == result2p6 and result2t8 != "") or (result2p4 == result2p8 and result2t6 != "") or (
                    result2p5 == result2p7 and (result2t3 != "")) or (
                    result2p5 == result2p8 and (result2t3 != "" or result2t4 != "")) or (
                    result2p6 == result2p8 and (result2t3 != "" or result2t4 != ""))):
        p608 = "8b digit - 2 digit same no. 2 times and 2 digit repeat no. 2 times found p608"
        print(p608)
    if result2t2 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p0 == result2p6 and (result2t4 != "" or result2t8 != "")) or (
                    result2p0 == result2p7 and (result2t4 != "" or result2t5 != "")) or (
                    result2p0 == result2p8 and (result2t4 != "" or result2t5 != "" or result2t6 != "")) or (
                    result2p4 == result2p6 and (result2t0 != "" or result2t8 != "")) or (
                    result2p4 == result2p7 and result2t0 != "") or (
                    result2p4 == result2p8 and (result2t0 != "" or result2t6 != ""))
            or (result2p5 == result2p7 and (result2t0 != "")) or (result2p5 == result2p8 and (result2t0 != "")) or (
                    result2p6 == result2p8 and (result2t0 != "" or result2t4 != ""))):
        p608 = "8c digit - 2 digit same no. 2 times and 2 digit repeat no. 2 times found p608"
        print(p608)

    if result2t3 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p0 == result2p6 and result2t8 != "") or (result2p0 == result2p8 and result2t6 != "") or (
                    result2p1 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
                    result2p1 == result2p6 and result2t8 != "") or (result2p1 == result2p7 and result2t5 != "") or (
                    result2p1 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p5 == result2p7 and (result2t0 != "" or result2t1 != ""))
            or (result2p5 == result2p8 and (result2t0 != "" or result2t1 != "")) or (
                    result2p6 == result2p8 and (result2t0 != "" or result2t1 != ""))):
        p608 = "8d digit - 2 digit same no. 2 times and 2 digit repeat no. 2 times found p608"
        print(p608)

    if result2t4 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t6 != "" or result2t7 != "" or result2t8 != "")) or (
            result2p0 == result2p6 and (result2t2 != "" or result2t8 != "")) or (
                    result2p0 == result2p7 and (result2t2 != "")) or (
                    result2p0 == result2p8 and (result2t2 != "" or result2t6 != "")) or (
                    result2p1 == result2p6 and (result2t8 != "")) or (result2p1 == result2p8 and (result2t6 != "")) or (
                    result2p2 == result2p6 and (result2t0 != "" or result2t8 != "")) or (
                    result2p2 == result2p7 and (result2t0 != "")) or (
                    result2p2 == result2p8 and (result2t0 != "" or result2t6 != "")) or (
                    result2p6 == result2p8 and (result2t0 != "" or result2t1 != "" or result2t2 != ""))):
        p608 = "8e digit - 2 digit same no. 2 times and 2 digit repeat no. 2 times found p608"
        print(p608)

    if result2t5 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t7 != "" or result2t8 != "")) or (
            result2p0 == result2p3 and (result2t7 != "" or result2t8 != "")) or (
                    result2p0 == result2p7 and (result2t2 != "" or result2t3 != "")) or (
                    result2p0 == result2p8 and (result2t2 != "" or result2t3 != "")) or (
                    result2p1 == result2p3 and (result2t7 != "" or result2t8 != "")) or (
                    result2p1 == result2p7 and result2t3 != "") or (result2p1 == result2p8 and result2t3 != "") or (
                    result2p2 == result2p7 and result2t0 != "") or (result2p2 == result2p8 and result2t0 != "")):
        p608 = "8f digit - 2 digit same no. 2 times and 2 digit repeat no. 2 times found p608"
        print(p608)

    if result2t6 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t4 != "" or result2t8 != "")) or (
            result2p0 == result2p3 and (result2t8 != "")) or (
                    result2p0 == result2p4 and (result2t2 != "" or result2t8 != "")) or (
                    result2p0 == result2p8 and (result2t2 != "" or result2t3 != "" or result2t4 != ""))
            or (result2p1 == result2p3 and (result2t8 != "")) or (result2p1 == result2p4 and (result2t8 != "")) or (
                    result2p1 == result2p8 and (result2t3 != "" or result2t4 != "")) or (
                    result2p2 == result2p4 and (result2t0 != "" or result2t8 != "")) or (
                    result2p2 == result2p8 and (result2t0 != "" or result2t6 != "")) or (
                    result2p3 == result2p8 and (result2t0 != "" or result2t1 != "")) or (
                    result2p4 == result2p8 and (result2t0 != "" or result2t1 != "" or result2t2 != ""))):
        p608 = "8g digit - 2 digit same no. 2 times and 2 digit repeat no. 2 times found p608"
        print(p608)
    if p608 != "":
        print(p608)
        p608 = "0002400000" + p608
    p609 = ""
    if result3t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p3 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p3 == result2p6 and result2t8 != "") or (result2p3 == result2p7 and result2t5 != "") or (
                    result2p3 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p4 == result2p6 and result2t8 != "") or (result2p4 == result2p8 and result2t6 != "") or (
                    result2p5 == result2p7 and result2t3 != "") or (result2p5 == result2p8 and result2t3 != "") or (
                    result2p6 == result2p8 and (result2t3 != "" or result2t4 != ""))):
        p609 = "9a digit - 2 digit same no. 2 times and 3 digit repeat no. and 2 digit repeat no. found p609"
        print(p609)
    if result3t1 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p4 == result2p6 and result2t8 != "") or (result2p4 == result2p8 and result2t6 != "") or (
            result2p5 == result2p7 and result2t3 != "") or (result2p5 == result2p8 and result2t3 != "") or (
                    result2p6 == result2p8 and result2t4 != "")):
        p609 = "9b digit - 2 digit same no. 2 times and 3 digit repeat no. and 2 digit repeat no. found p609"
        print(p609)
    if result3t2 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p0 == result2p6 and result2t8 != "") or (result2p0 == result2p7 and result2t5 != "") or (
                    result2p0 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p5 == result2p7 and result2t0 != "") or (result2p5 == result2p8 and result2t0 != "") or (
                    result2p6 == result2p8 and result2t0 != "")):
        p609 = "9c digit - 2 digit same no. 2 times and 3 digit repeat no. and 2 digit repeat no. found p609"
        print(p609)
    if result3t3 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p6 and result2t8 != "") or (result2p0 == result2p8 and result2t6 != "") or (
            result2p1 == result2p6 and result2t8 != "") or (result2p1 == result2p8 and result2t6 != "") or (
                    result2p6 == result2p8 and (result2t0 != "" or result2t1 != ""))):
        p609 = "9d digit - 2 digit same no. 2 times and 3 digit repeat no. and 2 digit repeat no. found p609"
        print(p609)
    if result3t4 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t7 != "" or result2t8 != "")) or (
            result2p2 == result2p7 and result2t0 != "") or (result2p2 == result2p8 and result2t0 != "")):
        p609 = "9e digit - 2 digit same no. 2 times and 3 digit repeat no. and 2 digit repeat no. found p609"
        print(p609)
    if result3t5 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and result2t8 != "") or (result2p0 == result2p3 and result2t8 != "") or (
            result2p0 == result2p8 and (result2t2 != "" or result2t3 != "")) or (
                    result2p1 == result2p3 and result2t8 != "") or (result2p1 == result2p8 and result2t3 != "") or (
                    result2p2 == result2p8 and result2t0 != "")):
        p609 = "9f digit - 2 digit same no. 2 times and 3 digit repeat no. and 2 digit repeat no. found p609"
        print(p609)
    if result3t6 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and result2t6 != "") or (result2p0 == result2p4 and result2t2 != "") or (
            result2p2 == result2p4 and result2t0 != "")):
        p609 = "9g digit - 2 digit same no. 2 times and 3 digit repeat no. and 2 digit repeat no. found p609"
        print(p609)
    if result3t7 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t4 != "" or result2t5 != "")) or (
            result2p0 == result2p3 and result2t5 != "") or (result2p0 == result2p4 and result2t2 != "") or (
                    result2p0 == result2p5 and (result2t2 != "" or result2t3 != "")) or (
                    result2p1 == result2p3 and result2t5 != "") or (result2p1 == result2p5 and result2t3 != "") or (
                    result2p2 == result2p4 and result2t0 != "") or (result2p2 == result2p5 and result2t0 != "")):
        p609 = "9h digit - 2 digit same no. 2 times and 3 digit repeat no. and 2 digit repeat no. found p609"
        print(p609)
    if p609 != "":
        print(p609)
        p609 = "0000160000" + p609
    p610 = ""
    if result3t0 != "" and ((result2p3 != "" and (
            result2p3 == result2p5 or result2p3 == result2p6 or result2p3 == result2p7 or result2p3 == result2p8)) or (
                                    result2p4 != "" and (
                                    result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8)) or (
                                    result2p5 != "" and (result2p5 == result2p7 or result2p5 == result2p8)) or (
                                    result2p6 != "" and result2p6 == result2p8)):
        p610 = "7a digit - 2 digit same no. 2 times and 3 digit repeat no. found p610"
        print(p610)
    if result3t1 != "" and (
            (result2p4 != "" and (result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8)) or (
            result2p5 != "" and (result2p5 == result2p7 or result2p5 == result2p8)) or (
                    result2p6 != "" and (result2p6 == result2p8))):
        p610 = "7b digit - 2 digit same no. 2 times and 3 digit repeat no. found p610"
        print(p610)
    if result3t2 != "" and ((result2p0 != "" and (
            result2p0 == result2p5 or result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8)) or (
                                    result2p5 != "" and (
                                    result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8))):
        p610 = "7c digit - 2 digit same no. 2 times and 3 digit repeat no. found p610"
        print(p610)
    if result3t3 != "" and (
            (result2p0 != "" and (result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p6 or result2p1 == result2p7 or result2p1 == result2p8)) or (
                    result2p6 != "" and (result2p6 == result2p8))):
        p610 = "7d digit - 2 digit same no. 2 times and 3 digit repeat no. found p610"
        print(p610)
    if result3t4 != "" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p7 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p7 or result2p1 == result2p8)) or (
                    result2p2 != "" and (result2p2 == result2p7 or result2p2 == result2p8))):
        p610 = "7e digit - 2 digit same no. 2 times and 3 digit repeat no. found p610"
        print(p610)
    if result3t5 != "" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p3 or result2p1 == result2p8)) or (
                    result2p2 != "" and (result2p2 == result2p8)) or (result2p3 != "" and (result2p3 == result2p8))):
        p610 = "7f digit - 2 digit same no. 2 times and 3 digit repeat no. found p610"
        print(p610)
    if result3t6 != "" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4)) or (
            result2p1 != "" and (result2p1 == result2p3 or result2p1 == result2p4)) or (
                    result2p2 != "" and (result2p2 == result2p4))):
        p610 = "7g digit - 2 digit same no. 2 times and 3 digit repeat no. found p610"
        print(p610)
    if result3t7 != "" and ((result2p0 != "" and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4 or result2p0 == result2p5)) or (
                                    result2p1 != "" and (
                                    result2p1 == result2p3 or result2p1 == result2p4 or result2p1 == result2p5)) or (
                                    result2p2 != "" and (result2p2 == result2p4 or result2p2 == result2p5))):
        p610 = "7h digit - 2 digit same no. 2 times and 3 digit repeat no. found p610"
        print(p610)
    if p610 != "":
        print(p610)
        p610 = "0002000000" + p610
    p611 = ""
    if result3s0 != "" and ((result2p3 != "" and (
            result2p3 == result2p5 or result2p3 == result2p6 or result2p3 == result2p7 or result2p3 == result2p8)) or (
                                    result2p4 != "" and (
                                    result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8)) or (
                                    result2p5 != "" and (result2p5 == result2p7 or result2p5 == result2p8)) or (
                                    result2p6 != "" and result2p6 == result2p8)):
        p611 = "7a digit - 2 digit same no. 2 times and 3 digit seq no. found p611"
        print(p611)
    if result3s1 != "" and (
            (result2p4 != "" and (result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8)) or (
            result2p5 != "" and (result2p5 == result2p7 or result2p5 == result2p8)) or (
                    result2p6 != "" and (result2p6 == result2p8))):
        p611 = "7b digit - 2 digit same no. 2 times and 3 digit seq no. found p611"
        print(p611)
    if result3s2 != "" and ((result2p0 != "" and (
            result2p0 == result2p5 or result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8)) or (
                                    result2p5 != "" and (
                                    result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8))):
        p611 = "7c digit - 2 digit same no. 2 times and 3 digit seq no. found p611"
        print(p611)
    if result3s3 != "" and (
            (result2p0 != "" and (result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p6 or result2p1 == result2p7 or result2p1 == result2p8)) or (
                    result2p6 != "" and (result2p6 == result2p8))):
        p611 = "7d digit - 2 digit same no. 2 times and 3 digit seq no. found p611"
        print(p611)
    if result3s4 != "" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p7 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p7 or result2p1 == result2p8)) or (
                    result2p2 != "" and (result2p2 == result2p7 or result2p2 == result2p8))):
        p611 = "7e digit - 2 digit same no. 2 times and 3 digit seq no. found p611"
        print(p611)
    if result3s5 != "" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p3 or result2p1 == result2p8)) or (
                    result2p2 != "" and (result2p2 == result2p8))):
        p611 = "7f digit - 2 digit same no. 2 times and 3 digit seq no. found p611"
        print(p611)
    if result3s6 != "" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4)) or (
            result2p1 != "" and (result2p1 == result2p3 or result2p1 == result2p4)) or (
                    result2p2 != "" and (result2p2 == result2p4))):
        p611 = "7g digit - 2 digit same no. 2 times and 3 digit seq no. found p611"
        print(p611)
    if result3s7 != "" and ((result2p0 != "" and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4 or result2p0 == result2p5)) or (
                                    result2p1 != "" and (
                                    result2p1 == result2p3 or result2p1 == result2p4 or result2p1 == result2p5)) or (
                                    result2p2 != "" and (result2p2 == result2p4 or result2p2 == result2p5))):
        p611 = "7h digit - 2 digit same no. 2 times and 3 digit seq no. found p611"
        print(p611)
    if p611 != "":
        print(p611)
        p611 = "0003200000" + p611
    p612 = ""
    if result4t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8 or result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8):
        p612 = "8a digit - 2 digit same no. 2 times and 4 digit repeat no. found p612"
        print(p612)

    if result4t1 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8):
        p612 = "8b digit - 2 digit same no. 2 times and 4 digit repeat no. found p612"
        print(p612)

    if result4t2 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p6 == result2p8 or result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8):
        p612 = "8c digit - 2 digit same no. 2 times and 4 digit repeat no. found p612"
        print(p612)

    if result4t3 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p7 == result2p0 or result2p7 == result2p1):
        p612 = "8d digit - 2 digit same no. 2 times and 4 digit repeat no. found p612"
        print(p612)

    if result4t4 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p8 == result2p0 or result2p8 == result2p1 or result2p8 == result2p2):
        p612 = "8e digit - 2 digit same no. 2 times and 4 digit repeat no. found p612"
        print(p612)

    if result4t5 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p1 == result2p3):
        p612 = "8f digit - 2 digit same no. 2 times and 4 digit repeat no. found p612"
        print(p612)

    if result4t6 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4 or result2p1 == result2p3 or result2p1 == result2p4 or result2p2 == result2p4):
        p612 = "8g digit - 2 digit same no. 2 times and 4 digit repeat no. found p612"
        print(p612)
    if p612 != "":
        print(p612)
        p612 = "0000160000" + p612

    p613 = ""
    if result4s0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8 or result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8):
        p613 = "8a digit - 2 digit same no. 2 times and 4 digit seq no. found p613"
        print(p613)

    if result4s1 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8):
        p613 = "8b digit - 2 digit same no. 2 times and 4 digit seq no. found p613"
        print(p613)

    if result4s2 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p6 == result2p8 or result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8):
        p613 = "8c digit - 2 digit same no. 2 times and 4 digit seq no. found p613"
        print(p613)

    if result4s3 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p7 == result2p0 or result2p7 == result2p1):
        p613 = "8d digit - 2 digit same no. 2 times and 4 digit seq no. found p613"
        print(p613)

    if result4s4 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p8 == result2p0 or result2p8 == result2p1 or result2p8 == result2p2):
        p613 = "8e digit - 2 digit same no. 2 times and 4 digit seq no. found p613"
        print(p613)

    if result4s5 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p1 == result2p3):
        p613 = "8f digit - 2 digit same no. 2 times and 4 digit seq no. found pp613"
        print(p613)

    if result4s6 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4 or result2p1 == result2p3 or result2p1 == result2p4 or result2p2 == result2p4):
        p613 = "8g digit - 2 digit same no. 2 times and 4 digit seq no. found p613"
        print(p613)
    if p613 != "":
        print(p613)
        p613 = "0000224000" + p613
    p614 = ""
    if result5t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8):
        p614 = "9a digit - 2 digit same no. 2 times and 5 digit repeat no. found p614"
        print(p614)

    if result5t1 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p6 == result2p8):
        p614 = "9b digit - 2 digit same no. 2 times and 5 digit repeat no. found p614"
        print(p614)

    if result5t2 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p7 or result2p0 == result2p8):
        p614 = "9c digit - 2 digit same no. 2 times and 5 digit repeat no. found p614"
        print(p614)

    if result5t3 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p8 or result2p1 == result2p8):
        p614 = "9d digit - 2 digit same no. 2 times and 5 digit repeat no. found p614"
        print(p614)

    if result5t4 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2):
        p614 = "9e digit - 2 digit same no. 2 times and 5 digit repeat no. found p614"
        print(p614)

    if result5t5 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p1 == result2p3):
        p614 = "9f digit - 2 digit same no. 2 times and 5 digit repeat no. found p614"
        print(p614)
    if p614 != "":
        print(p614)
        p614 = "0000012000" + p614
    p615 = ""
    if result5s0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8):
        p615 = "9a digit - 2 digit same no. 2 times and 5 digit seq no. found p615"
        print(p615)

    if result5s1 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p6 == result2p8):
        p615 = "9b digit - 2 digit same no. 2 times and 5 digit seq no. found p615"
        print(p615)

    if result5s2 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p7 or result2p0 == result2p8):
        p615 = "9c digit - 2 digit same no. 2 times and 5 digit seq no. found p615"
        print(p615)

    if result5s3 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p8 or result2p1 == result2p8):
        p615 = "9d digit - 2 digit same no. 2 times and 5 digit seq no. found p615"
        print(p615)

    if result5s4 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2):
        p615 = "9e digit - 2 digit same no. 2 times and 5 digit seq no. found p615"
        print(p615)

    if result5s5 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p1 == result2p3):
        p615 = "9f digit - 2 digit same no. 2 times and 5 digit seq no. found p615"
        print(p615)
    if p615 != "":
        print(p615)
        p615 = "0000014400" + p615
    p616 = ""
    if result3p0 == "786" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p3 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p3 == result2p6 and result2t8 != "") or (result2p3 == result2p7 and result2t5 != "") or (
                    result2p3 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p4 == result2p6 and result2t8 != "") or (result2p4 == result2p8 and result2t6 != "") or (
                    result2p5 == result2p7 and result2t3 != "") or (result2p5 == result2p8 and result2t3 != "") or (
                    result2p6 == result2p8 and (result2t3 != "" or result2t4 != ""))):
        p616 = "9a digit - 2 digit same no. 2 times and special 3 digit no. 786 and 2 digit repeat no. found p616"
        print(p616)
    if result3p1 == "786" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p4 == result2p6 and result2t8 != "") or (result2p4 == result2p8 and result2t6 != "") or (
            result2p5 == result2p7 and result2t3 != "") or (result2p5 == result2p8 and result2t3 != "") or (
                    result2p6 == result2p8 and result2t4 != "")):
        p616 = "9b digit - 2 digit same no. 2 times and special 3 digit no. 786 and 2 digit repeat no. found p616"
        print(p616)
    if result3p2 == "786" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p0 == result2p6 and result2t8 != "") or (result2p0 == result2p7 and result2t5 != "") or (
                    result2p0 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p5 == result2p7 and result2t0 != "") or (result2p5 == result2p8 and result2t0 != "") or (
                    result2p6 == result2p8 and result2t0 != "")):
        p616 = "9c digit - 2 digit same no. 2 times and special 3 digit no. 786 and 2 digit repeat no. found p616"
        print(p616)
    if result3p3 == "786" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p6 and result2t8 != "") or (result2p0 == result2p8 and result2t6 != "") or (
            result2p1 == result2p6 and result2t8 != "") or (result2p1 == result2p8 and result2t6 != "") or (
                    result2p6 == result2p8 and (result2t0 != "" or result2t1 != ""))):
        p616 = "9d digit - 2 digit same no. 2 times and special 3 digit no. 786 and 2 digit repeat no. found p616"
        print(p616)
    if result3p4 == "786" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t7 != "" or result2t8 != "")) or (
            result2p2 == result2p7 and result2t0 != "") or (result2p2 == result2p8 and result2t0 != "")):
        p616 = "9e digit - 2 digit same no. 2 times and special 3 digit no. 786 and 2 digit repeat no. found p616"
        print(p616)
    if result3p5 == "786" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and result2t8 != "") or (result2p0 == result2p3 and result2t8 != "") or (
            result2p0 == result2p8 and (result2t2 != "" or result2t3 != "")) or (
                    result2p1 == result2p3 and result2t8 != "") or (result2p1 == result2p8 and result2t3 != "") or (
                    result2p2 == result2p8 and result2t0 != "")):
        p616 = "9f digit - 2 digit same no. 2 times and special 3 digit no. 786 and 2 digit repeat no. found p616"
        print(p616)
    if result3p6 == "786" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and result2t6 != "") or (result2p0 == result2p4 and result2t2 != "") or (
            result2p2 == result2p4 and result2t0 != "")):
        p616 = "9g digit - 2 digit same no. 2 times and special 3 digit no. 786 and 2 digit repeat no. found p616"
        print(p616)
    if result3p7 == "786" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t4 != "" or result2t5 != "")) or (
            result2p0 == result2p3 and result2t5 != "") or (result2p0 == result2p4 and result2t2 != "") or (
                    result2p0 == result2p5 and (result2t2 != "" or result2t3 != "")) or (
                    result2p1 == result2p3 and result2t5 != "") or (result2p1 == result2p5 and result2t3 != "") or (
                    result2p2 == result2p4 and result2t0 != "") or (result2p2 == result2p5 and result2t0 != "")):
        p616 = "9h digit - 2 digit same no. 2 times and special 3 digit no. 786 and 2 digit repeat no. found p616"
        print(p616)
    if p616 != "":
        print(p616)
        p616 = "0000016000" + p616
    p617 = ""
    if result3p0 == "786" and ((result2p3 != "" and (
            result2p3 == result2p5 or result2p3 == result2p6 or result2p3 == result2p7 or result2p3 == result2p8)) or (
                                       result2p4 != "" and (
                                       result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8)) or (
                                       result2p5 != "" and (result2p5 == result2p7 or result2p5 == result2p8)) or (
                                       result2p6 != "" and result2p6 == result2p8)):
        p617 = "7a digit - 2 digit same no. 2 times and 3 digit special no. 786 found p617"
        print(p617)
    if result3p1 == "786" and (
            (result2p4 != "" and (result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8)) or (
            result2p5 != "" and (result2p5 == result2p7 or result2p5 == result2p8)) or (
                    result2p6 != "" and (result2p6 == result2p8))):
        p617 = "7b digit - 2 digit same no. 2 times and 3 digit special no. 786 found p617"
        print(p617)
    if result3p2 == "786" and ((result2p0 != "" and (
            result2p0 == result2p5 or result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8)) or (
                                       result2p5 != "" and (
                                       result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8))):
        p617 = "7c digit - 2 digit same no. 2 times and 3 digit special no. 786 found p617"
        print(p617)
    if result3p3 == "786" and (
            (result2p0 != "" and (result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p6 or result2p1 == result2p7 or result2p1 == result2p8)) or (
                    result2p6 != "" and (result2p6 == result2p8))):
        p617 = "7d digit - 2 digit same no. 2 times and 3 digit special no. 786 found p617"
        print(p617)
    if result3p4 == "786" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p7 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p7 or result2p1 == result2p8)) or (
                    result2p2 != "" and (result2p2 == result2p7 or result2p2 == result2p8))):
        p617 = "7e digit - 2 digit same no. 2 times and 3 digit special no. 786 found p617"
        print(p617)
    if result3p5 == "786" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p8)) or (
            result2p1 != "" and (result2p1 == result2p3 or result2p1 == result2p8)) or (
                    result2p2 != "" and (result2p2 == result2p8))):
        p617 = "7f digit - 2 digit same no. 2 times and 3 digit special no. 786 found p617"
        print(p617)
    if result3p6 == "786" and (
            (result2p0 != "" and (result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4)) or (
            result2p1 != "" and (result2p1 == result2p3 or result2p1 == result2p4)) or (
                    result2p2 != "" and (result2p2 == result2p4))):
        p617 = "7g digit - 2 digit same no. 2 times and 3 digit special no. 786 found p617"
        print(p617)
    if result3p7 == "786" and ((result2p0 != "" and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4 or result2p0 == result2p5)) or (
                                       result2p1 != "" and (
                                       result2p1 == result2p3 or result2p1 == result2p4 or result2p1 == result2p5)) or (
                                       result2p2 != "" and (result2p2 == result2p4 or result2p2 == result2p5))):
        p617 = "7h digit - 2 digit same no. 2 times and 3 digit special no. 786 found p617"
        print(p617)
    if p617 != "":
        print(p617)
        p617 = "0000200000" + p617
    p618 = ""
    if result4p0 == "1008" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p4 == result2p6 or result2p4 == result2p7 or result2p4 == result2p8 or result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8):
        p618 = "8a digit - 2 digit same no. 2 times and 4 digit special no. 1008  no. found p618"
        print(p618)

    if result4p1 == "1008" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p5 == result2p7 or result2p5 == result2p8 or result2p6 == result2p8):
        p618 = "8b digit - 2 digit same no. 2 times and 4 digit special no. 1008  no. found p618"
        print(p618)

    if result4p2 == "1008" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p6 == result2p8 or result2p0 == result2p6 or result2p0 == result2p7 or result2p0 == result2p8):
        p618 = "8c digit - 2 digit same no. 2 times and 4 digit special no. 1008  no. found p618"
        print(p618)

    if result4p3 == "1008" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p7 == result2p0 or result2p7 == result2p1):
        p618 = "8d digit - 2 digit same no. 2 times and 4 digit special no. 1008  no. found p618"
        print(p618)

    if result4p4 == "1008" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p8 == result2p0 or result2p8 == result2p1 or result2p8 == result2p2):
        p618 = "8e digit - 2 digit same no. 2 times and 4 digit special no. 1008  no. found p618"
        print(p618)

    if result4p5 == "1008" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p1 == result2p3):
        p618 = "8f digit - 2 digit same no. 2 times and 4 digit special no. 1008  no. found p618"
        print(p618)

    if result4p6 == "1008" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p0 == result2p2 or result2p0 == result2p3 or result2p0 == result2p4 or result2p1 == result2p3 or result2p1 == result2p4 or result2p2 == result2p4):
        p618 = "8g digit - 2 digit same no. 2 times and 4 digit special no. 1008  no. found p618"
        print(p618)
    if p618 != "":
        print(p618)
        p618 = "0000016000" + p618

    if (int(mobile[0:3]) == int(mobile[3:6]) - 100 and int(mobile[3:6]) == int(mobile[6:9]) - 100) or (
            int(mobile[0:3]) == int(mobile[3:6]) - 100 and int(mobile[3:6]) == int(mobile[7:10]) - 100) or (
            int(mobile[0:3]) == int(mobile[4:7]) - 100 and int(mobile[4:7]) == int(mobile[7:10]) - 100) or (
            int(mobile[1:4]) == int(mobile[4:7]) - 100 and int(mobile[4:7]) == int(mobile[7:10]) - 100):
        p619 = "9 digit - 3 digit no. ascending 3 times +100 found p619"
        print(p619)
        p619 = "0000016000" + p619
    if int(mobile[0:3]) == int(mobile[3:6]) - 100 or int(mobile[0:3]) == int(mobile[4:7]) - 100 or int(
            mobile[0:3]) == int(mobile[5:8]) - 100 or int(mobile[0:3]) == int(mobile[6:9]) - 100 or int(
            mobile[0:3]) == int(mobile[7:10]) - 100:
        p620 = "6a digit - 3 digit no. ascending 2 times +100 found p620"
        print(p620)
    if int(mobile[1:4]) == int(mobile[4:7]) - 100 or int(mobile[1:4]) == int(mobile[5:8]) - 100 or int(
            mobile[1:4]) == int(mobile[6:9]) - 100 or int(mobile[1:4]) == int(mobile[7:10]) - 100:
        p620 = "6b digit - 3 digit no. ascending 2 times +100 found p620"
        print(p620)
    if int(mobile[2:5]) == int(mobile[5:8]) - 100 or int(mobile[2:5]) == int(mobile[6:9]) - 100 or int(
            mobile[2:5]) == int(mobile[7:10]) - 100:
        p620 = "6c digit - 3 digit no. ascending 2 times +100 found p620"
        print(p620)
    if int(mobile[3:6]) == int(mobile[6:9]) - 100 or int(mobile[3:6]) == int(mobile[7:10]) - 100 or int(
            mobile[4:7]) == int(mobile[7:10]) - 100:
        p620 = "6d digit - 3 digit no. ascending 2 times +100 found p620"
        print(p620)
    if p620 != "":
        print(p620)
        p620 = "0016000000" + p620
    if (int(mobile[0:3]) == int(mobile[3:6]) + 100 and int(mobile[3:6]) == int(mobile[6:9]) + 100) or (
            int(mobile[0:3]) == int(mobile[3:6]) + 100 and int(mobile[3:6]) == int(mobile[7:10]) + 100) or (
            int(mobile[0:3]) == int(mobile[4:7]) + 100 and int(mobile[4:7]) == int(mobile[7:10]) + 100) or (
            int(mobile[1:4]) == int(mobile[4:7]) + 100 and int(mobile[4:7]) == int(mobile[7:10]) + 100):
        p621 = "9 digit - 3 digit no. descending 3 times -100 found p621"
        print(p621)
        p621 = "0000016000" + p621
    if int(mobile[0:3]) == int(mobile[3:6]) + 100 or int(mobile[0:3]) == int(mobile[4:7]) + 100 or int(
            mobile[0:3]) == int(mobile[5:8]) + 100 or int(mobile[0:3]) == int(mobile[6:9]) + 100 or int(
            mobile[0:3]) == int(mobile[7:10]) + 100:
        p622 = "6a digit - 3 digit no. descending 2 times -100 found p622"
        print(p622)
    if int(mobile[1:4]) == int(mobile[4:7]) + 100 or int(mobile[1:4]) == int(mobile[5:8]) + 100 or int(
            mobile[1:4]) == int(mobile[6:9]) + 100 or int(mobile[1:4]) == int(mobile[7:10]) + 100:
        p622 = "6b digit - 3 digit no. descending 2 times -100 found p622"
        print(p622)
    if int(mobile[2:5]) == int(mobile[5:8]) + 100 or int(mobile[2:5]) == int(mobile[6:9]) + 100 or int(
            mobile[2:5]) == int(mobile[7:10]) + 100:
        p622 = "6c digit - 3 digit no. descending 2 times -100 found p622"
        print(p622)
    if int(mobile[3:6]) == int(mobile[6:9]) + 100 or int(mobile[3:6]) == int(mobile[7:10]) + 100 or int(
            mobile[4:7]) == int(mobile[7:10]) + 100:
        p622 = "6d digit - 3 digit no. descending 2 times -100 found p622"
        print(p622)
    if p622 != "":
        print(p622)
        p622 = "0020000000" + p622
    if (int(mobile[0:4]) == int(mobile[4:8]) - 1000 or int(mobile[0:4]) == int(mobile[5:9]) - 1000 or int(
            mobile[0:4]) == int(mobile[6:10]) - 1000 or int(mobile[1:5]) == int(mobile[5:9]) - 1000 or int(
            mobile[1:5]) == int(mobile[6:10]) - 1000 or int(mobile[2:6]) == int(mobile[6:10]) - 1000):
        p623 = "8 digit - 4 digit no. ascending 2 times +1000 found p623"
        print(p623)
        p623 = "0001200000" + p623
    if result3s0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result3t3 != "" and result2p6 != "" and result2p6 == result2p8) or (
            result3t7 != "" and result2p3 != "" and result2p3 == result2p7) or (
                    result3t5 != "" and result2p3 != "" and result2p3 == result2p8)):
        p624 = "10a digit - 2 digit same no. 2 times and 3 digit repeat no. and 3 digit seq found p624"
        print(p624)

    if result3t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result3s3 != "" and result2p6 == result2p8) or (result3s7 != "" and result2p3 == result2p7) or (
            result3s5 != "" and result2p3 == result2p8)):
        p624 = "10b digit - 2 digit same no. 2 times and 3 digit repeat no. and 3 digit seq found p624"
        print(p624)

    if result2p0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result3s2 != "" and result2p5 == result2p0 and result3t7 != "") or (
            result3t2 != "" and result2p5 == result2p0 and result3s7 != "") or (
                    result3s4 != "" and result2p2 == result2p0 and result3t7 != "") or (
                    result3t4 != "" and result2p2 == result2p0 and result3s7 != "") or (
                    result3s2 != "" and result2p8 == result2p0 and result3t5 != "") or (
                    result3t2 != "" and result2p8 == result2p0 and result3s5 != "")):
        p624 = "10c digit - 2 digit same no. 2 times and 3 digit repeat no. and 3 digit seq found p624"
        print(p624)
    if p624 != "":
        print(p624)
        p624 = "0000025600" + p624

    if result3t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result3t3 != "" and result2p6 != "" and result2p6 == result2p8) or (
            result3t7 != "" and result2p3 != "" and result2p3 == result2p5) or (
                    result3t5 != "" and result2p3 != "" and result2p3 == result2p8)):
        p625 = "10a digit - 2 digit same no. 2 times and 3 digit repeat no. 2 times found p625"
        print(p625)
    if result2p0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result3t2 != "" and result2p5 == result2p0 and result3t7 != "") or (
            result3t4 != "" and result2p2 == result2p0 and result3t7 != "") or (
                    result3t2 != "" and result2p8 == result2p0 and result3t5 != "")):
        p625 = "10b digit - 2 digit same no. 2 times and 3 digit repeat no. 2 times found p625"
        print(p625)
    if p625 != "":
        print(p625)
        p625 = "0000016000" + p625

    if result3s0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result3s3 != "" and result2p6 != "" and result2p6 == result2p8) or (
            result3s7 != "" and result2p3 != "" and result2p3 == result2p7) or (
                    result3s5 != "" and result2p3 != "" and result2p3 == result2p8)):
        p626 = "10a digit - 2 digit same no. 2 times and 3 digit seq no. 2 times found p626"
        print(p626)

    if result2p0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result3s2 != "" and result2p5 == result2p0 and result3s7 != "") or (
            result3s4 != "" and result2p2 == result2p0 and result3s7 != "") or (
                    result3s2 != "" and result2p8 == result2p0 and result3s5 != "")):
        p626 = "10b digit - 2 digit same no. 2 times and 3 digit seq no. 2 times found p626"
        print(p626)
    if p626 != "":
        print(p626)
        p626 = "0000040960" + p626
    if result4t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2t4 != "" and result2p6 != "" and result2p6 == result2p8) or (
            result2t6 != "" and result2p4 != "" and result2p4 == result2p8) or (
                    result2t8 != "" and result2p4 == result2p6)):
        p627 = "10a digit - 2 digit same no. 2 times and 2 digit repeat no. and 4 digit repeat no. found p627"
        print(p627)

    if result2t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result4t2 != "" and result2p6 != "" and result2p6 == result2p8) or (
            result4t4 != "" and result2p2 != "" and result2p2 == result2p8) or (
                    result4t6 != "" and result2p2 != "" and result2p2 == result2p4)):
        p627 = "10b digit - 2 digit same no. 2 times and 2 digit repeat no. and 4 digit repeat no. found p627"
        print(p627)

    if result2p0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2t2 != "" and result4t4 != "" and result2p8 == result2p0) or (
            result4t2 != "" and result2t6 != "" and result2p8 == result2p0) or (
                    result2t2 != "" and result4t6 != "" and result2p2 == result2p0) or (
                    result4t4 != "" and result2t8 != "" and result2p2 == result2p0) or (
                    result2t2 != "" and result4t6 != "" and result2p4 == result2p0) or (
                    result4t2 != "" and result2t8 != "" and result2p6 == result2p0)):
        p627 = "10c digit - 2 digit same no. 2 times and 2 digit repeat no. and 4 digit repeat no. found p627"
        print(p627)
    if p627 != "":
        print(p627)
        p627 = "0000016000" + p627

    if result4s0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2t4 != "" and result2p6 != "" and result2p6 == result2p8) or (
            result2t6 != "" and result2p4 != "" and result2p4 == result2p8) or (
                    result2t8 != "" and result2p4 == result2p6)):
        p628 = "10a digit - 2 digit same no. 2 times and 2 digit repeat no. and 4 digit seq no. found p628"
        print(p628)

    if result2t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result4s2 != "" and result2p6 != "" and result2p6 == result2p8) or (
            result4s4 != "" and result2p2 != "" and result2p2 == result2p8) or (
                    result4s6 != "" and result2p2 != "" and result2p2 == result2p4)):
        p628 = "10b digit - 2 digit same no. 2 times and 2 digit repeat no. and 4 digit seq no. found p628"
        print(p628)

    if result2p0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2t2 != "" and result4s4 != "" and result2p8 == result2p0) or (
            result4s2 != "" and result2t6 != "" and result2p8 == result2p0) or (
                    result2t2 != "" and result4s6 != "" and result2p2 == result2p0) or (
                    result4s4 != "" and result2t8 != "" and result2p2 == result2p0) or (
                    result2t2 != "" and result4s6 != "" and result2p4 == result2p0) or (
                    result4s2 != "" and result2t8 != "" and result2p6 == result2p0)):
        p628 = "10c digit - 2 digit same no. 2 times and 2 digit repeat no. and 4 digit seq no. found p628"
        print(p628)
    if p628 != "":
        print(p628)
        p628 = "0000022400" + p628
    if (pc2 == 3 or pc3 == 3 or pc4 == 3 or pc5 == 3 or pc6 == 3):
        p629 = "6 digit - 2 digit same no. 3 times found p629"
        print(p629)
        p629 = "0002800000" + p629
    if result6t0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p6 == result2p8):
        p630 = "10a digit - 2 digit same no. 2 times and 6 digit repeat no. found p630"
        print(p630)

    if result2p0 != "" and (
            (result2p2 == result2p0 and result6t4 != "") or (result2p8 == result2p0 and result6t2 != "")):
        p630 = "10b digit - 2 digit same no. 2 times and 6 digit repeat no. found p630"
        print(p630)
    if p630 != "":
        print(p630)
        p630 = "0000001200" + p630
    if result6s0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p6 == result2p8):
        p631 = "10a digit - 2 digit same no. 2 times and 6 digit seq no. found p631"
        print(p631)

    if result2p0 != "" and (
            (result2p2 == result2p0 and result6s4 != "") or (result2p8 == result2p0 and result6s2 != "")):
        p631 = "10b digit - 2 digit same no. 2 times and 6 digit seq no. found p631"
        print(p631)
    if p631 != "":
        print(p631)
        p631 = "0000001200" + p631

    if (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p2 == result2p0 and (result2t4 != "" and result2t6 != "" and result2t8 != "")) or (
            result2p4 == result2p0 and (result2t2 != "" and result2t6 != "" and result2t8 != "")) or (
                    result2p6 == result2p0 and (result2t2 != "" and result2t4 != "" and result2t8 != "")) or (
                    result2p8 == result2p0 and (result2t4 != "" and result2t6 != "" and result2t2 != ""))):
        p632 = "10a digit - 2 digit same no. 2 times and 2 digit repeat no. 3 times found p632"
        print(p632)

    if (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            result2p2 == result2p4 and (result2t0 != "" and result2t6 != "" and result2t8 != "")) or (
            result2p2 == result2p6 and (result2t0 != "" and result2t4 != "" and result2t8 != "")) or (
            result2p2 == result2p8 and (result2t0 != "" and result2t6 != "" and result2t4 != "")) or (
            result2p4 == result2p6 and (result2t0 != "" and result2t2 != "" and result2t8 != "")) or (
            result2p4 == result2p8 and (result2t0 != "" and result2t2 != "" and result2t6 != "")) or (
            result2p6 == result2p8 and (result2t0 != "" and result2t2 != "" and result2t4 != "")):
        p632 = "10b digit - 2 digit same no. 2 times and 2 digit repeat no. 3 times found p632"
        print(p632)
    if p632 != "":
        print(p632)
        p632 = "0000200000" + p632
    p736 = ""
    if result3s0 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p3 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p3 == result2p6 and result2t8 != "") or (result2p3 == result2p7 and result2t5 != "") or (
                    result2p3 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p4 == result2p6 and result2t8 != "") or (result2p4 == result2p8 and result2t6 != "") or (
                    result2p5 == result2p7 and result2t3 != "") or (result2p5 == result2p8 and result2t3 != "") or (
                    result2p6 == result2p8 and (result2t3 != "" or result2t4 != ""))):
        p633 = "9a digit - 2 digit same no. 2 times and 3 digit seq no. and 2 digit repeat no. found p633"
        print(p633)
    if result3s1 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p4 == result2p6 and result2t8 != "") or (result2p4 == result2p8 and result2t6 != "") or (
            result2p5 == result2p7 and result2t3 != "") or (result2p5 == result2p8 and result2t3 != "") or (
                    result2p6 == result2p8 and result2t4 != "")):
        p633 = "9b digit - 2 digit same no. 2 times and 3 digit seq no. and 2 digit repeat no. found p633"
        print(p633)
    if result3s2 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p5 and (result2t7 != "" or result2t8 != "")) or (
            result2p0 == result2p6 and result2t8 != "") or (result2p0 == result2p7 and result2t5 != "") or (
                    result2p0 == result2p8 and (result2t5 != "" or result2t6 != "")) or (
                    result2p5 == result2p7 and result2t0 != "") or (result2p5 == result2p8 and result2t0 != "") or (
                    result2p6 == result2p8 and result2t0 != "")):
        p633 = "9c digit - 2 digit same no. 2 times and 3 digit seq no. and 2 digit repeat no. found p633"
        print(p633)
    if result3s3 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p6 and result2t8 != "") or (result2p0 == result2p8 and result2t6 != "") or (
            result2p1 == result2p6 and result2t8 != "") or (result2p1 == result2p8 and result2t6 != "") or (
                    result2p6 == result2p8 and (result2t0 != "" or result2t1 != ""))):
        p633 = "9d digit - 2 digit same no. 2 times and 3 digit seq no. and 2 digit repeat no. found p633"
        print(p633)
    if result3s4 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t7 != "" or result2t8 != "")) or (
            result2p2 == result2p7 and result2t0 != "") or (result2p2 == result2p8 and result2t0 != "")):
        p633 = "9e digit - 2 digit same no. 2 times and 3 digit seq no. and 2 digit repeat no. found p633"
        print(p633)
    if result3s5 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and result2t8 != "") or (result2p0 == result2p3 and result2t8 != "") or (
            result2p0 == result2p8 and (result2t2 != "" or result2t3 != "")) or (
                    result2p1 == result2p3 and result2t8 != "") or (result2p1 == result2p8 and result2t3 != "") or (
                    result2p2 == result2p8 and result2t0 != "")):
        p633 = "9f digit - 2 digit same no. 2 times and 3 digit seq no. and 2 digit repeat no. found p633"
        print(p633)
    if result3s6 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and result2t6 != "") or (result2p0 == result2p4 and result2t2 != "") or (
            result2p2 == result2p4 and result2t0 != "")):
        p633 = "9g digit - 2 digit same no. 2 times and 3 digit seq no. and 2 digit repeat no. found p633"
        print(p633)
    if result3s7 != "" and (pc2 > 1 or pc3 > 1 or pc4 > 1 or pc5 > 1 or pc6 > 1 or pc7 > 1 or pc8 > 1) and (
            (result2p0 == result2p2 and (result2t4 != "" or result2t5 != "")) or (
            result2p0 == result2p3 and result2t5 != "") or (result2p0 == result2p4 and result2t2 != "") or (
                    result2p0 == result2p5 and (result2t2 != "" or result2t3 != "")) or (
                    result2p1 == result2p3 and result2t5 != "") or (result2p1 == result2p5 and result2t3 != "") or (
                    result2p2 == result2p4 and result2t0 != "") or (result2p2 == result2p5 and result2t0 != "")):
        p633 = "9h digit - 2 digit same no. 2 times and 3 digit seq no. and 2 digit repeat no. found p633"
        print(p633)
    if p633 != "":
        print(p633)
        p633 = "0000384000" + p633

    p634 = ""
    if (pc2 > 2) and ((result2t2 != "" and (result2p3 != result2p0)) or (
            result2t3 != "" and (result2p4 != result2p0) and (result2p2 != result2p0)) or (
                              result2t4 != "" and (result2p4 != result2p0) and (result2p3 != result2p0))
                      or (result2t5 != "" and (result2p6 != result2p0) and (result2p4 != result2p0)) or (
                              result2t6 != "" and (result2p7 != result2p0) and (result2p5 != result2p0)) or (
                              result2t7 != "" and (result2p8 != result2p0) and (result2p6 != result2p0)) or (
                              result2t8 != "" and (result2p7 != result2p0))):
        p634 = "8a digit - 2 digit same no. 3 times and 2 digit repeat no. found p634"
        print(p634)

    if (pc4 > 2) and ((result2t0 != "" and (result2p1 != result2p2)) or (
            result2t4 != "" and (result2p5 != result2p2) and (result2p3 != result2p2))
                      or (result2t5 != "" and (result2p6 != result2p2) and (result2p4 != result2p2)) or (
                              result2t6 != "" and (result2p7 != result2p2) and (result2p5 != result2p2)) or (
                              result2t7 != "" and (result2p8 != result2p2) and (result2p6 != result2p2)) or (
                              result2t8 != "" and (result2p7 != result2p2))):
        p634 = "8c digit - 2 digit same no. 3 times and 2 digit repeat no. found p634"
        print(p634)
    if (pc3 > 2) and ((result2t3 != "" and (result2p4 != result2p1)) or (
            result2t4 != "" and (result2p5 != result2p1) and (result2p3 != result2p1))
                      or (result2t5 != "" and (result2p6 != result2p1) and (result2p4 != result2p1)) or (
                              result2t6 != "" and (result2p7 != result2p1) and (result2p5 != result2p1)) or (
                              result2t7 != "" and (result2p8 != result2p1) and (result2p6 != result2p1)) or (
                              result2t8 != "" and (result2p7 != result2p1))):
        p634 = "8b digit - 2 digit same no. 3 times and 2 digit repeat no. found p634"
        print(p634)
    if (pc5 > 2) and ((result2t0 != "" and (result2p1 != result2p3)) or (
            result2t1 != "" and (result2p2 != result2p3) and (result2p0 != result2p3)) or (
                              result2t2 != "" and (result2p1 != result2p3) and (result2p3 != result2p3)) or (
                              result2t3 != "" and (result2p4 != result2p3) and (result2p2 != result2p3)) or (
                              result2t4 != "" and (result2p4 != result2p3) and (result2p3 != result2p3))
                      or (result2t5 != "" and (result2p6 != result2p3) and (result2p4 != result2p3)) or (
                              result2t6 != "" and (result2p7 != result2p3) and (result2p5 != result2p3)) or (
                              result2t7 != "" and (result2p8 != result2p3) and (result2p6 != result2p3)) or (
                              result2t8 != "" and (result2p7 != result2p3))):
        p634 = "8d digit - 2 digit same no. 3 times and 2 digit repeat no. found p634"
        print(p634)

    if (pc6 > 2) and ((result2t0 != "" and (result2p1 != result2p4)) or (
            result2t1 != "" and (result2p2 != result2p4) and (result2p0 != result2p4)) or (
                              result2t2 != "" and (result2p3 != result2p0) and (result2p1 != result2p4)) or (
                              result2t3 != "" and (result2p2 != result2p4))
                      or (result2t5 != "" and (result2p6 != result2p4)) or (
                              result2t6 != "" and (result2p7 != result2p4) and (result2p5 != result2p4)) or (
                              result2t7 != "" and (result2p8 != result2p4) and (result2p6 != result2p4)) or (
                              result2t8 != "" and (result2p7 != result2p4))):
        p634 = "8e digit - 2 digit same no. 3 times and 2 digit repeat no. found p634"
        print(p634)
    if p634 != "":
        print(p634)
        p634 = "0000240000" + p634
    if (dp0 == 3) and (tc2 > 1) and ((result2t2 != "" and result2p3 != result2p0) or (
            result2t4 != "" and result2p3 != result2p0 and result2p5 != result2p0) or (
                                             result2t6 != "" and result2p7 != result2p0 and result2p5 != result2p0) or (
                                             result2t8 != "" and result2p7 != result2p0)):
        p635 = "10a digit - 2 digit same no. 3 times and 2 digit repeat no. 2 times found p635"
        print(p635)
    if (dp1 == 3) and (tc2 > 1) and ((result2t0 != "" and result2p1 != result2p2) or (
            result2t4 != "" and result2p3 != result2p2 and result2p5 != result2p2) or (
                                             result2t6 != "" and result2p7 != result2p2 and result2p5 != result2p2) or (
                                             result2t8 != "" and result2p7 != result2p2)):
        p635 = "10b digit - 2 digit same no. 3 times and 2 digit repeat no. 2 times found p635"
        print(p635)
    if (dp2 == 3) and (tc2 > 1) and ((result2t0 != "" and result2p1 != result2p4) or (
            result2t2 != "" and result2p3 != result2p4 and result2p1 != result2p4) or (
                                             result2t6 != "" and result2p7 != result2p4 and result2p5 != result2p4) or (
                                             result2t8 != "" and result2p7 != result2p4)):
        p635 = "10c digit - 2 digit same no. 3 times and 2 digit repeat no. 2 times found p635"
        print(p635)
    if p635 != "":
        print(p635)
        p635 = "0000020000" + p635
    p636 = ""

    if result3t0 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p3 == result2p5 and result2p3 == result2p7) or (
            result2p3 == result2p5 and result2p3 == result2p8) or (
                    result2p3 == result2p6 and result2p3 == result2p8) or (
                    result2p4 == result2p6 and result2p4 == result2p8)):
        p636 = "9a digit - 2 digit same no. 3 times and 3 digit repeat no. found p636"
        print(p636)
    if result3t1 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
    (result2p4 == result2p6 and result2p4 == result2p8)):
        p636 = "9b digit - 2 digit same no. 3 times and 3 digit repeat no. found p636"
        print(p636)
    if result3t2 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p5 and result2p0 == result2p7) or (
            result2p0 == result2p5 and result2p0 == result2p8) or (result2p0 == result2p6 and result2p0 == result2p8)):
        p636 = "9c digit - 2 digit same no. 3 times and 3 digit repeat no. found p636"
        print(p636)
    if result3t3 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p6 and result2p0 == result2p8) or (result2p1 == result2p6 and result2p1 == result2p8)):
        p636 = "9d digit - 2 digit same no. 3 times and 3 digit repeat no. found p636"
        print(p636)
    if result3t4 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p2 and result2p0 == result2p7) or (result2p0 == result2p2 and result2p0 == result2p8)):
        p636 = "9e digit - 2 digit same no. 3 times and 3 digit repeat no. found p636"
        print(p636)
    if result3t5 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p2 and result2p0 == result2p8) or (
            result2p0 == result2p3 and result2p0 == result2p8) or (result2p1 == result2p3 and result2p1 == result2p8)):
        p636 = "9f digit - 2 digit same no. 3 times and 3 digit repeat no. found p636"
        print(p636)
    if result3t6 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
    (result2p0 == result2p2 and result2p0 == result2p4)):
        p636 = "9g digit - 2 digit same no. 3 times and 3 digit repeat no. found pp636"
        print(p636)
    if result3t7 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p2 and result2p0 == result2p4) or (
            result2p0 == result2p2 and result2p0 == result2p5) or (result2p1 == result2p3 and result2p1 == result2p5)):
        p636 = "9h digit - 2 digit same no. 3 times and 3 digit repeat no. found p636"
        print(p636)
    if p636 != "":
        print(p636)
        p636 = "0000024000" + p636
    p637 = ""
    if result3s0 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p3 == result2p5 and result2p3 == result2p7) or (
            result2p3 == result2p5 and result2p3 == result2p8) or (
                    result2p3 == result2p6 and result2p3 == result2p8) or (
                    result2p4 == result2p6 and result2p4 == result2p8)):
        p637 = "9a digit - 2 digit same no. 3 times and 3 digit seq no. found p637"
        print(p637)
    if result3s1 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
    (result2p4 == result2p6 and result2p4 == result2p8)):
        p637 = "9b digit - 2 digit same no. 3 times and 3 digit seq no. found p637"
        print(p637)
    if result3s2 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p5 and result2p0 == result2p7) or (
            result2p0 == result2p5 and result2p0 == result2p8) or (result2p0 == result2p6 and result2p0 == result2p8)):
        p637 = "9c digit - 2 digit same no. 3 times and 3 digit seq no. found p637"
        print(p637)
    if result3s3 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p6 and result2p0 == result2p8) or (result2p1 == result2p6 and result2p1 == result2p8)):
        p637 = "9d digit - 2 digit same no. 3 times and 3 digit seq no. found p637"
        print(p637)
    if result3s4 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p2 and result2p0 == result2p7) or (result2p0 == result2p2 and result2p0 == result2p8)):
        p637 = "9e digit - 2 digit same no. 3 times and 3 digit seq no. found p637"
        print(p637)
    if result3s5 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p2 and result2p0 == result2p8) or (
            result2p0 == result2p3 and result2p0 == result2p8) or (result2p1 == result2p3 and result2p1 == result2p8)):
        p637 = "9f digit - 2 digit same no. 3 times and 3 digit seq no. found p637"
        print(p637)
    if result3s6 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
    (result2p0 == result2p2 and result2p0 == result2p4)):
        p637 = "9g digit - 2 digit same no. 3 times and 3 digit seq no. found p637"
        print(p637)
    if result3s7 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            (result2p0 == result2p2 and result2p0 == result2p4) or (
            result2p0 == result2p2 and result2p0 == result2p5) or (result2p1 == result2p3 and result2p1 == result2p5)):
        p637 = "9h digit - 2 digit same no. 3 times and 3 digit seq no. found p637"
        print(p637)
    if p637 != "":
        print(p637)
        p637 = "0000038400" + p637
    if result4t0 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            result2p4 == result2p6 and result2p4 == result2p8):
        p638 = "10a digit - 2 digit same no. 3 times and 4 digit repeat no. found p638"
        print(p638)

    if result2p0 != "" and ((result2p0 == result2p6 and result2p0 == result2p8 and result4t2 != "") or (
            result2p0 == result2p2 and result2p0 == result2p8 and result4t4 != "") or (
                                    result2p0 == result2p2 and result2p0 == result2p4 and result4t6 != "")):
        p638 = "10b digit - 2 digit same no. 3 times and 4 digit repeat no. found p638"
        print(p638)
    if p638 != "":
        print(p638)
        p638 = "0000001600" + p638
    if result4s0 != "" and (pc2 > 2 or pc3 > 2 or pc4 > 2 or pc5 > 2 or pc6 > 2 or pc7 > 2 or pc8 > 2) and (
            result2p4 == result2p6 and result2p4 == result2p8):
        p639 = "10a digit - 2 digit same no. 3 times and 4 digit seq no. found p639"
        print(p639)
    if result2p0 != "" and ((result2p0 == result2p6 and result2p0 == result2p8 and result4s2 != "") or (
            result2p0 == result2p2 and result2p0 == result2p8 and result4s4 != "") or (
                                    result2p0 == result2p2 and result2p0 == result2p4 and result4s6 != "")):
        p639 = "10b digit - 2 digit same no. 3 times and 4 digit seq no. found p639"
        print(p639)
    if p639 != "":
        print(p639)
        p639 = "0000002560" + p639

    # extracting date of birth from mobile no.
    current_date = date.today()
    tn = 0
    while tn < 36501:
        pdate = (current_date - timedelta(tn))
        datestr = pdate.strftime("%d%m%Y")
        datestr1 = pdate.strftime("%d-%m-%Y")
        locdate = mobile[1:10].find(datestr)
        if locdate != -1:
            p803 = "8 digit - Date of Birth " + datestr1 + " found  p803"
            print(p803)
            p803 = "0000000080" + p803
            if (mobile[0:2] == "66" or mobile[0:2] == "77" or mobile[0:2] == "88" or mobile[0:2] == "99") and (
                    mobile[2:10] == datestr):
                p804 = "10 digit - Date of Birth " + datestr1 + " found with starting 2 digit repeat no. p804"
                print(p804)
                p804 = "0000000004" + p804
            if (mobile[0:1] == mobile[9:10]) and (mobile[1:9] == datestr):
                p805 = "10 digit - Date of Birth " + datestr1 + " found with same starting and ending no. p805"
                print(p805)
                p805 = "0000000004" + p805
            total1 = int(datestr[0:1]) + int(datestr[1:2])

            total1 = str(total1)
            if len(total1) == 1:
                total1 = int(total1)
            else:
                total1 = int(total1[0:1]) + int(total1[1:2])
            if total1 == total:
                p802 = (
                            "10 digit - Very Very Lucky Number. Numerological Value of Day of Birth and this Mobile no. is same... Date: " + datestr1 + " Numerological Value: " + str(
                        total1))
                print(p802)
                p802 = "0000000080" + p802
            # print(p803)
        tn = tn + 1

    fc = 0
    ft = 1
    low = 90000000000
    while ft != 1000:
        fa = "p" + str(ft)
        fa1 = vars()[fa]

        fa2 = fa1[0:10]

        if fa2 != "":
            fa2 = int(fa2)
            if fa2 < low:
                low = fa2
                ftext = fa
        ft = ft + 1
    print("=========================================================")
    no1 = int(4000000000 / low)
    lenno1 = len(str(no1))
    if low < 41:
        tag = "This is Super Super VIP Five Star ***** Number"
    elif low > 40 and low < 401:
        tag = "This is Super Super VIP Four Star **** Number"
    elif low > 400 and low < 4001:
        tag = "This is Super VIP Three Star *** Number"
    elif low > 4000 and low < 40001:
        tag = "This is Super VIP Two Star ** Number"
    elif low > 40000 and low < 400001:
        tag = "This is VIP One Star * Number"
    elif low > 400000 and low < 4000001:
        tag = "This is VIP Number"
    elif low > 4000000:
        tag = "This is a Normal Number"

    if lenno1 == 1 or lenno1 == 2 or lenno1 == 3:
        divi = 1
        lenno1 = ""

    if lenno1 == 4 or lenno1 == 5:
        divi = 1000
        lenno1 = "thousand"
    if lenno1 == 6 or lenno1 == 7:
        divi = 100000
        lenno1 = "lac"
    if lenno1 == 8 or lenno1 == 9 or lenno1 == 10:
        lenno1 = "crore"
        divi = 10000000
    p905 = "Your Number is among 1 out of " + str(int(no1 / divi)) + " " + lenno1 + " numbers"
    priceindex = 2
    price = priceindex * (no1 / divi)
    price = round(price, 1)
    print(price)
    p907 = "Approximate Value of your Mobile number is in range of Rs " + str(
        price / 5) + " " + lenno1 + " to Rs " + str(price) + " " + lenno1
    p906 = tag
    # print(ftext)
    fa1 = vars()[ftext]
    lenfa1 = len(fa1)
    fa1 = fa1[10:lenfa1]
    lfind1 = fa1.find("-")
    rfind1 = fa1.rfind("p")
    fa1 = fa1[lfind1 + 1:rfind1]
    # fa1=mobile+"-"+fa1
    print(fa1)
    print(p905)
    print(p906)
    p1001 = "Numerological value of this Number is : " + str(total)
    print(p1001)
    savemessage = mobile + " - " + p906 + "\n\n" + p905 + "\n\n" + "Top Pattern of this number - " + fa1 + "\n\n" + p907 + "\n\n" + p1001
    for i in range(1000):
        globals()[f'p{i}'] = ""

    message = savemessage
    if mobile!="0000000000":
     st.write(message)
    break




