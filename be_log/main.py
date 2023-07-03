from territories import *
import networkx as nx
import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout

board = None
terr = []

def main():
    board = nx.Graph()
    # seas
    nao = Sea('nao', None)
    mao = Sea('mao', None)
    nwg = Sea('nwg', None)
    bar = Sea('bar', None)
    nth = Sea('nth', None)
    hel = Sea('hel', None)
    ska = Sea('ska', None)
    bal = Sea('bal', None)
    bot = Sea('bot', None)
    iri = Sea('iri', None)
    eng = Sea('eng', None)
    wes = Sea('wes', None)
    lyo = Sea('lyo', None)
    tys = Sea('tys', None)
    ion = Sea('ion', None)
    adr = Sea('adr', None)
    aeg = Sea('aeg', None)
    eas = Sea('eas', None)
    bla = Sea('bla', None)

    board.add_node(nao)
    board.add_node(mao)
    board.add_node(nwg)
    board.add_node(mao)
    board.add_node(bar)
    board.add_node(nth)
    board.add_node(hel)
    board.add_node(ska)
    board.add_node(bal)
    board.add_node(bot)
    board.add_node(iri)
    board.add_node(eng)
    board.add_node(wes)
    board.add_node(lyo)
    board.add_node(tys)
    board.add_node(ion)
    board.add_node(adr)
    board.add_node(aeg)
    board.add_node(eas)
    board.add_node(bla)

    # Non-Coastal Land

    par = Inland('par', True, True, None)
    bur = Inland('bur', False, False, None)
    ruh = Inland('ruh', False, False, None)
    mun = Inland('mun', True, True, None)
    tyr = Inland('tyr', False, False, None)
    boh = Inland('boh', False, False, None)
    sil = Inland('sil', False, False, None)
    war = Inland('war', True, True, None)
    vie = Inland('vie', True, True, None)
    bud = Inland('bud', True, True, None)
    ser = Inland('ser', True, False, None)
    gal = Inland('gal', False, False, None)
    ukr = Inland('ukr', False, False, None)
    mos = Inland('mos', True, True, None)
    
    board.add_node(par)
    board.add_node(bur)
    board.add_node(ruh)
    board.add_node(mun)
    board.add_node(tyr)
    board.add_node(boh)
    board.add_node(sil)
    board.add_node(war)
    board.add_node(vie)
    board.add_node(bud)
    board.add_node(ser)
    board.add_node(gal)
    board.add_node(ukr)
    board.add_node(mos)

    # Coastal Land

    bre = Coastal('bre', True, True, None)
    gas = Coastal('gas', False, False, None)
    spanc = Coastal('spanc', True, False, None)
    spasc = Coastal('spasc', True, False, None)
    por = Coastal('por', True, False, None)
    pie = Coastal('por', False, False, None)
    tus = Coastal('tus', False, False, None)
    rom = Coastal('por', True, True, None)
    nap = Coastal('nap', True, True, None)
    apu = Coastal('apu', False, False, None)
    ven = Coastal('ven', True, True, None)
    tri = Coastal('tri', True, True, None)
    alb = Coastal('alb', False, False, None)
    gre = Coastal('gre', True, False, None)
    bulsc = Coastal('bulsc', True, False, None)
    con = Coastal('con', True, True, None)
    smy = Coastal('smy', True, True, None)
    ank = Coastal('ank', True, True, None)  
    bulec = Coastal('bulnc', True, False, None)
    rum = Coastal('rum', True, False, None)
    sev = Coastal('sev', True, True, None)
    arm = Coastal('arm', False, False, None)
    bel = Coastal('bel', True, False, None)
    kie = Coastal('kie', True, True, None)
    den = Coastal('den', True, False, None)
    swe = Coastal('swe', True, False, None)
    nor = Coastal('nor', True, False, None)
    fin = Coastal('fin', False, False, None)
    stpnc = Coastal('stpnc', True, True, None)
    stpsc = Coastal('stpsc', True, True, None)
    lon = Coastal('lon', True, True, None)
    lvp = Coastal('lvp', True, True, None)
    edi = Coastal('edi', True, True, None)
    yor = Coastal('con', False, False, None)
    cly = Coastal('cly', False, False, None)
    wal = Coastal('wal', False, False, None)
    
    board.add_node(bre)
    board.add_node(gas)
    board.add_node(spanc)
    board.add_node(spasc)
    board.add_node(por)
    board.add_node(pie)
    board.add_node(tus)
    board.add_node(rom)
    board.add_node(nap)
    board.add_node(apu)
    board.add_node(ven)
    board.add_node(tri)
    board.add_node(alb)
    board.add_node(gre)
    board.add_node(bulsc)
    board.add_node(con)
    board.add_node(smy)
    board.add_node(ank)
    board.add_node(bulec)
    board.add_node(rum)
    board.add_node(sev)
    board.add_node(arm)
    board.add_node(bel)
    board.add_node(kie)
    board.add_node(den)
    board.add_node(swe)
    board.add_node(nor)
    board.add_node(fin)
    board.add_node(stpnc)
    board.add_node(stpsc)
    board.add_node(lon)
    board.add_node(lvp)
    board.add_node(edi)
    board.add_node(yor)
    board.add_node(cly)
    board.add_node(wal)





    for territory in board.nodes():
        terr.append((territory.name, territory))

    board.add_edges_from([(nwg, bar), (nwg, nao), (nwg, nth), \
                            (nao, iri), (nao, mao), (mao, eng), \
                            (mao, wes), (mao, iri), (eng, nth), \
                            (nth, hel), (nth, ska), (bal, bot), \
                            (wes, lyo), (wes, tys), (tys, ion), \
                            (lyo, tys), (ion, aeg), (ion, eas), \
                            (aeg, eas), (adr, ion)]) 
    nx.draw(board, with_labels=True)

    plt.show()


if __name__ == "__main__":
    main()