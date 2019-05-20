import struct


def tamper(student_id):
  with open('C:\Users\姜\Desktop\python2\binary-file-process-GingerCoca','r+b') as f
     f.seek(54)
     f.read(3)
     for number in student_id:
        i=int(number)
        if (i==0):
           i=10
         i=i-1
         f.read(a*3)
         f.write(b'\x00\x00\x00')
   f.close()




def detect():
  with open('lenna.bmp', 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
