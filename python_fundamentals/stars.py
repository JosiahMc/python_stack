


x = [4, 6, 1, 3, 5, 7, 25,"dlakfjasdf","asdl;kfjasd;lfjkasdljfa",4323423232342342342332]
def drawstars(lst):
        for elem in lst:
            star_row = ""
            if type(elem) is str:
                for i in range (0, len(elem)):
                    star_row += elem[0].lower()
            else:
                for i in range(0, elem):
                    star_row += "*"
            print star_row



drawstars (x)

