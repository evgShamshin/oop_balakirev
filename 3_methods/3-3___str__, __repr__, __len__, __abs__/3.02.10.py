# VAR_1
class PolyLine:
    def __init__(self, *args):
        self.points = list(args)

    def add_coord(self, x, y):
        self.points.append((x, y))

    def remove_coord(self, indx):
        self.points.pop(indx)

    def get_coords(self):
        return self.points

    def __str__(self):
        return f'{self.points}'


# TEST-TASK___________________________________
poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
print(poly)


# VAR_2
exec(__import__('base64').b64decode("""

        Y2xhc             3MgUG        
       9seUxp              bmU6C       
      iAgIC                 BkZWY      
      gX19p                 bml0X      
      18oc2VsZiwgKmFyZ3MpOgogICAg      
      ICAgIHNlbGYuY29vcmRzID0gbGl      
        zdChhcmdzKQoKICAgIGRlZi        
      BhZGRfY29vcmQoc2VsZiwgeCwge      
      Sk6CiAg     ICAgICAg    c2V      
      sZi5jb2     9yZHMuYX     Bw      
      ZW5kKCh     4LCB5KSk     KC      
      iAgICBk     ZWYgcmVt     b3      
      ZlX2Nvb3JkKHNlbGYsIGluZHgpO      
      gogICAgICAgIHNlbGYuY29vcmRz      
                  LnBvcChpbm           

      R4KQ   oKICAgIGRlZi   BnZXR      
     fY29vc  mRzKHNlbGYpOg  ogICA      
   gICAgIHJ  ldHVybiBzZWxm  LmNvb3Jk   
   cwoKI   yAgKG       MpICB   PbGVn   
    I  F   Bpdm9       2YXJv   d i     
           AyMDI       yCg==           

"""))