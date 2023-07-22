from territories import *
import networkx as nx
import matplotlib.pyplot as plt
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
    mar = Coastal('mar', True, True, None)
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
    pic = Coastal('pic', False, False, None)
    bel = Coastal('bel', True, False, None)
    hol = Coastal('hol', True, False, None)
    kie = Coastal('kie', True, True, None)
    ber = Coastal('ber', True, True, None)
    pru = Coastal('pru', False, False, None)
    lvn = Coastal('lvn', False, False, None)
    den = Coastal('den', True, False, None)
    swe = Coastal('swe', True, False, None)
    nwy = Coastal('nwy', True, False, None)
    fin = Coastal('fin', False, False, None)
    stpnc = Coastal('stpnc', True, True, None)
    stpsc = Coastal('stpsc', True, True, None)
    lon = Coastal('lon', True, True, None)
    lvp = Coastal('lvp', True, True, None)
    edi = Coastal('edi', True, True, None)
    yor = Coastal('con', False, False, None)
    cly = Coastal('cly', False, False, None)
    wal = Coastal('wal', False, False, None)
    naf = Coastal('naf', False, False, None)
    syr = Coastal('syr', False, False, None)
    tun = Coastal('tun', True, False, None)
    
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
    board.add_node(nwy)
    board.add_node(fin)
    board.add_node(stpnc)
    board.add_node(stpsc)
    board.add_node(lon)
    board.add_node(lvp)
    board.add_node(edi)
    board.add_node(yor)
    board.add_node(cly)
    board.add_node(wal)
    board.add_node(ber)
    board.add_node(pru)
    board.add_node(lvn)
    board.add_node(tun)
    board.add_node(naf)
    board.add_node(syr)



    for territory in board.nodes():
        terr.append((territory.name, territory))
    
    # There's quite a few edges. Ow. Also South/North coasts are *really* annoying
    
    board.add_edges_from([(nwg, bar), (nwg, nao), (nwg, nth), 
                            (nao, iri), (nao, mao), (mao, eng), 
                            (mao, wes), (mao, iri), (eng, nth), 
                            (nth, hel), (nth, ska), (bal, bot), 
                            (wes, lyo), (wes, tys), (tys, ion), 
                            (lyo, tys), (ion, aeg), (ion, eas), 
                            (aeg, eas), (adr, ion), (bre, mao), 
                            (bre, eng), (spanc, mao), (spasc, lyo), 
                            (spasc, wes), (mar, lyo), (pie, lyo),
                            (tus, lyo), (tus, tys), (rom, tys), 
                            (nap, tys), (nap, ion), (naf, mao),
                            (naf, wes), (tun, wes), (tun, tys),
                            (tun, ion), (syr, eas), (gas, mao),
                            (cly, nao), (cly, nwg), (lvp, nao),
                            (lvp, iri), (wal, iri), (wal, eng),
                            (lon, eng), (lon, nth), (yor, nth),
                            (edi, nth), (edi, nwg), (apu, adr),
                            (apu, ion), (tri, adr), (alb, adr),
                            (alb, ion), (gre, ion), (gre, aeg),
                            (bulsc, aeg), (con, bla), (con, aeg),
                            (smy, eas), (bulec, bla), (rum, bla),
                            (sev, bla), (arm, bla), (ank, bla),
                            (pic, eng), (bel, eng), (hol, nth),
                            (hol, hel), (kie, hel), (kie, bal),
                            (den, hel), (den, nth), (den, ska),
                            (den, bal), (ber, bal), (pru, bal),
                            (lvn, bal), (lvn, bot), (stpsc, bot),
                            (stpnc, bar), (nwy, bar), (nwy, nwg),
                            (nwy, nth), (nwy, ska), (swe, ska),
                            (swe, bal), (swe, bot), (fin, bot),
                            (por, mao)
                            ], label=['F'])
    
    board.add_edges_from([(cly, edi), (edi, yor), (yor, lon),
                          (lon, wal), (wal, lvp), (lvp, cly),
                          (naf, tun), (bre, pic), (pic, bel),
                          (bel, hol), (hol, kie), (kie, den),
                          (kie, ber), (ber, pru), (pru, lvn),
                          (lvn, stpsc), (stpsc, fin), (fin, swe),
                          (swe, den), (swe, nwy), (nwy, stpnc),
                          (bre, gas), (gas, spanc), (spanc, por),
                          (por, spasc), (spasc, mar), (mar, pie),
                          (pie, tus), (tus, rom), (rom, nap),
                          (nap, apu), (apu, ven), (ven, tri),
                          (tri, alb), (alb, gre), (gre, bulsc),
                          (bulsc, con), (bulec, con), (con, ank),
                          (ank, arm), (arm, sev), (sev, rum),
                          (rum, bulec), (con, smy), (smy, syr)
                        ], label=['A', 'F'])
    
    board.add_edges_from([(bre, par), (par, bur), (par, pic),
                          (par, gas), (bur, pic), (bur, bel),
                          (bur, ruh), (bur, mun), (bur, mar),
                          (bur, gas), (mun, ber), (mun, kie),
                          (mun, ruh), (mun, tyr), (mun, boh),
                          (mun, tyr), (mun, sil), (sil, war),
                          (sil, pru), (sil, boh), (sil, gal),
                          (boh, gal), (boh, vie), (boh, tyr),
                          (war, pru), (war, lvn), (war, mos),
                          (war, ukr), (war, gal), (tyr, vie),
                          (tyr, tri), (tyr, ven), (mos, stpnc),
                          (mos, stpsc), (mos, lvn), (mos, ukr),
                          (mos, sev), (ukr, gal), (ukr, rum),
                          (gal, rum), (gal, bud), (vie, bud),
                          (vie, tri), (vie, gal), (bud, tri),
                          (bud, rum), (bud, ser), (ser, alb),
                          (ser, gre), (ser, bulec), (ser, bulsc),
                          (pie, ven), (smy, ank), (smy, arm)
                        ], label=['A'])
    nx.draw(board, with_labels=True)

    plt.show()


if __name__ == "__main__":
    main()