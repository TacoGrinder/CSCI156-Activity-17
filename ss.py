__author__ = 'Sean'


class SS:
    class InvalidSocial(ValueError):
        pass
    def __init(self):
        self.social = self.sn()
    def inp(self):
        area, group, serial = self.social.split('-')
        t = area, group, serial
        q = t[0]+'-'+t[1]+'-'+t[2]
        if len(t) == 3:
            if t[2] == '':
                raise self.InvalidSocial
            elif '666' in t[0]:
                raise self.InvalidSocial
            elif len(t[0]) != 3:
                raise self.InvalidSocial
            elif len(t[1]) != 2:
                raise self.InvalidSocial
            elif len(t[2]) != 4:
                raise self.InvalidSocial
            elif '000' in t[0]:
                raise self.InvalidSocial
            elif '00' in t[1]:
                raise self.InvalidSocial
            elif '0000' in t[2]:
                raise self.InvalidSocial
            elif area + group + serial == '078' + '05' + '1120':
                raise self.InvalidSocial
        area = int(area)
        group = int(group)
        serial = int(serial)
        if 900 <= area <= 999:
            raise self.InvalidSocial
        else:
            return q

    def soc(self):
        self.sn = input("Input Social Security Number, AAA-GG-SSSS").strip()
        try:
            self.inp()
            return self.sn
        except self.InvalidSocial:
            print("Invalid Social Security Number")
            self.soc()
