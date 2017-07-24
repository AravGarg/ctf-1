#Establish the encrypted flag.txt data
flag = [0xF5D1, 0x4D6B, 0xED6A, 0x08A6, 0x38DD, 0xF7FA, 0x609E, 0xEBC4, 0xE55F, 0xE6D1, 0x7C89, 0xED5B, 0x0871, 0x1A69, 0x5D58, 0x72DE, 0x224B, 0x3AA6, 0x0845, 0x7DD6, 0x58FB, 0xE9CC, 0x0A2D, 0x76B8, 0xED60, 0x251A, 0x1F6B, 0x32CC, 0xE78D, 0x12FA, 0x201A, 0xE889, 0x2D25, 0x922A, 0x4BC5, 0xF5FF, 0xF8E5, 0xC79B, 0x3A77, 0x4BDB, 0xEA11, 0x5941, 0x58BD, 0x3A95, 0xF5C9, 0xA225, 0xAD40, 0xF8BD, 0x095D, 0x70B6, 0x458C, 0xE7A9, 0xEA68, 0x252F, 0x094B, 0x5E41, 0x0969, 0x6015, 0x5ED5, 0xF6E5, 0x59B9, 0x7CAF, 0x66DF, 0x265B, 0x7837, 0x57B4, 0x7CAF, 0xAED9, 0xF707, 0x6A3C, 0xF8E5, 0xF509, 0x7C8B, 0x0915, 0x2235, 0x336F, 0x33E9, 0x2D14, 0x7C91, 0x5804, 0x83E5, 0xE78D, 0xF4EA, 0x0874, 0xED6B, 0x4B35, 0xE839, 0x57B4, 0xE77C, 0xEA68, 0x2525, 0xAD41, 0xED6F, 0x3A4A, 0x4BCC, 0x6015, 0xF440, 0x0858, 0x3AA6, 0x7809, 0x671D, 0x0874, 0xEA77, 0x63AF, 0x2E91, 0x5845, 0xF6C4, 0x086D, 0x7795, 0x3939, 0x57B4, 0x7C89, 0x82DC, 0x32ED, 0xB994, 0xC7AF, 0x9135, 0x0E65, 0x1B66, 0xED5B, 0x3235, 0x6577, 0x5A80, 0x3AD3, 0xE776, 0x1EE5, 0xAD41, 0xED59, 0x864C, 0x70B4, 0x3876, 0xED67, 0x64D6, 0xF8E5, 0xF505, 0xEAD9, 0x7C9C, 0x32ED, 0xB994, 0xB4EF, 0x0C6C, 0xF665, 0xF5F5, 0x9047, 0x521A, 0xE99E, 0xEA68, 0x252F, 0x9D09, 0x76B7, 0xE776, 0x1ED0, 0x095D, 0x0D4D, 0x5D5A, 0x087B, 0x2005, 0x1526, 0x7E76, 0x85AD, 0x78B9, 0xE8B6, 0x782C, 0x251C, 0x32ED, 0x7F68, 0xEBE3, 0xEA41, 0x57FD, 0xED59, 0x846D, 0x7A05, 0xB994, 0xBB78, 0xED6A, 0x08A6, 0x38DD, 0x3B5D, 0x7E45, 0xE839, 0x738C, 0xE9CC, 0x0A2D, 0x764A, 0x609E, 0xE8B6, 0xEA68, 0x2524, 0xE6BB, 0x7C9C, 0x639F, 0x3A95, 0x0895, 0xF40F, 0x8328, 0xEA69, 0x7EE5, 0xF8BD, 0x7F7D, 0x0D6D, 0x70B6, 0x458C, 0xE8B6, 0xEA68, 0x251C, 0x6065, 0xB35F, 0xC789, 0x5845, 0x7F7D, 0x6D89, 0x4C6E, 0xA20E, 0x60B5, 0x7E45, 0xED59, 0xF707, 0x69EF, 0x922A, 0x4BC5, 0xF6EF, 0x8635, 0xF4B9, 0x57B4, 0x7CF8, 0xED60, 0x2510, 0x095D, 0x20AF, 0x3545, 0xF40F, 0x8328, 0xEA41, 0x58A4, 0x225D, 0x7E7C, 0x4BDB, 0xF8BD, 0x082C, 0xEAE7, 0x5D57, 0x5D50, 0x0914, 0xE7C7, 0x8624, 0x7CF8, 0xED60, 0x2511, 0x7C8E, 0x7159, 0x8416, 0x7EF9, 0xE7E5, 0x774A, 0x3895, 0x1EC9, 0x7C90, 0x09B9, 0x58BD, 0x5FF5, 0xE99E, 0xEA68, 0x250A, 0x224C, 0xEA3D, 0x73F5, 0x7C89, 0x53A6, 0x3190, 0x3B5D, 0x1526, 0x7DD5, 0x666A, 0x0919, 0x225F, 0xCDEF, 0x79E1, 0x7E7B, 0x7E6B, 0x082C, 0xA277, 0xE885, 0xE8BB, 0xE775, 0x5FF7, 0xEA68, 0x251B, 0x7FDF, 0x589D, 0x7A05, 0x779A, 0x8A5A, 0x7C91, 0x5D5C, 0x32ED, 0xF628, 0x2195, 0xF49A, 0x0C77, 0xEAE1, 0x59B9, 0x58BD, 0xE570, 0xE99E, 0xEA3D, 0x73F9, 0x13AD, 0x2BF5, 0x225D, 0x7F7D, 0x70B6, 0x4A9C, 0x337A, 0x1EC9, 0x4D05, 0x7E75, 0x2578, 0xED59, 0x38E5, 0x1ECA, 0xA210, 0x3B5D, 0x779A, 0x8A6F, 0xC790, 0x2518, 0x4B41, 0x7C89, 0x5D49, 0x4D05, 0x152D, 0x73C5, 0x79F9, 0x4BED, 0x913C, 0x37C9, 0x5D4D, 0x53C8, 0x0941, 0x7C97, 0x5D5B, 0x346A, 0x82D8, 0x5F36, 0x801F, 0xC800]

#Establish the ctable
ctable = "\x00abcdefghijklmnopqrstuvwxyz0123456789 \n\x00ABCDEFGHIJKLMNOPQRSTUVWXYZ(!@#,.?/*)<>\x00"

#Establish the decrypt function, which essentially splits the 4 character hex strings into the original three integers
def decrypt():
     dectext = []
     for j in flag:
          x = (j/1600) 
          y = (j/40) % 40
          z = j % 40
          dectext += [x,y,z]
     return dectext

#Establish the regroup function, which takes the integers over 39, and readds the (39 + (i - 39)) so the remapping can go smoothly
def regroup(dectext):
     postext = []
     i = 0
     while i < len(dectext):
          if dectext[i] == 39:
               postext += [39 + dectext[i + 1]]
               i += 2
          else:
               postext += [dectext[i]]
               i += 1
     return postext

#Established the remap function, which takes the integers from the reqroup function, and outputs the corresponding characters from ctable
def remap(postext):
     maptext = ""
     for i in xrange(len(postext)):
          x = postext[i]
          if ctable[x] != "\x00":
               maptext += ctable[x]
     return maptext

#Runs the decrypt function
dectext = []
dectext += decrypt()
#print dectext

#Takes the output from decrypt, and pipes it into the regroup function
postext = []
postext = regroup(dectext)
#print postext

#Takes the output from the regroup function, pipes it into the remap function, then prints out the unecrpyted flag.txt data
maptext = ""
maptext = remap(postext)
print maptext
