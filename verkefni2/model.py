from verkefni2 import jon

def book(baekur):
    def nafn():
        listi=[]
        for x in baekur:
            listi.append(x["nafn"])
        return listi

bokalisti=[{"nafn":"The Fellowship Of The Ring","útgáfufyrirtæki":"George Allen & Unwin","útgáfuár":"1954","höfundur":"J. R. R. Tolkein"},
    {"nafn":"The Two Towers","útgáfufyrirtæki":"George Allen & Unwin","útgáfuár":"1954","höfundur":"J. R. R. Tolkein"},
    {"nafn":"Return Of The King","útgáfufyrirtæki":"George Allen & Unwin","útgáfuár":"1955","höfundur":"J. R. R. Tolkein"}]