def read_keyboard_packet_file(name):

    usb_codes = {
            0x04:"aA", 0x05:"bB", 0x06:"cC", 0x07:"dD", 0x08:"eE", 0x09:"fF",
            0x0A:"gG", 0x0B:"hH", 0x0C:"iI", 0x0D:"jJ", 0x0E:"kK", 0x0F:"lL",
            0x10:"mM", 0x11:"nN", 0x12:"oO", 0x13:"pP", 0x14:"qQ", 0x15:"rR",
            0x16:"sS", 0x17:"tT", 0x18:"uU", 0x19:"vV", 0x1A:"wW", 0x1B:"xX",
            0x1C:"yY", 0x1D:"zZ", 0x1E:"1!", 0x1F:"2@", 0x20:"3#", 0x21:"4$",
            0x22:"5%", 0x23:"6^", 0x24:"7&", 0x25:"8*", 0x26:"9(", 0x27:"0)",
            0x2C:"  ", 0x2D:"-_", 0x2E:"=+", 0x2F:"[{", 0x30:"]}",  0x32:"#~",
            0x33:";:", 0x34:"'\"",  0x36:",<",  0x37:".>", 0x38:"/?", 0x4f:">",
            0x50:"<"
            }

    buf = [[""]]
    x = 0
    y = 0

    with open(name) as f:
        for l in f.readlines():
            xs = l.strip().split(':')
            k = int(xs[2], 16)
            if k == 0x28:
                # return
                y += 1
                x = 0
                buf.insert(y, [""])

            elif k == 0x51:
                # down
                if y + 1 < len(buf):
                    y += 1
                    x = min(x, len(buf[y]))

            elif k == 0x52:
                # up
                if y > 0:
                    y -= 1
                    x = min(x, len(buf[y]))

            elif k == 0x50:
                # left
                if x == 0:
                    if y > 0:
                        y -= 1
                        x = len(buf[y])
                else:
                    x -= 1

            elif k == 0x4f:
                # right
                if x == len(buf[y]):
                    y += 1
                    x = 0
                    if len(buf) <= y:
                        buf.append([""])

            elif k == 0x2a:
                # backspace
                if x == 0:
                    if y > 0:
                        buf[y-1] += buf[y]
                        buf = buf[:y] + buf[y+1:]
                else:
                    buf[y] = buf[y][:x] + buf[y][x+1:]
                    x -= 1

            else:
                if k in usb_codes:
                    buf[y].insert(x, usb_codes[k][int(int(xs[0], 16) == 2)])
                    x += 1

    for i in range(len(buf)):
        buf[i] = ''.join(buf[i])

    return '\n'.join(buf)
