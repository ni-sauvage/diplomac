import units, territories, countries, orders
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

class Board():
    def __init__(self):

        self.terr = []
        self.board = nx.Graph()
        # seas
        mao = territories.Sea('mao', None)
        nao = territories.Sea('nao', None)
        nwg = territories.Sea('nwg', None)
        bar = territories.Sea('bar', None)
        nth = territories.Sea('nth', None)
        hel = territories.Sea('hel', None)
        ska = territories.Sea('ska', None)
        bal = territories.Sea('bal', None)
        bot = territories.Sea('bot', None)
        iri = territories.Sea('iri', None)
        eng = territories.Sea('eng', None)
        wes = territories.Sea('wes', None)
        lyo = territories.Sea('lyo', None)
        tys = territories.Sea('tys', None)
        ion = territories.Sea('ion', None)
        adr = territories.Sea('adr', None)
        aeg = territories.Sea('aeg', None)
        eas = territories.Sea('eas', None)
        bla = territories.Sea('bla', None)

        self.board.add_node(nao)
        self.board.add_node(mao)
        self.board.add_node(nwg)
        self.board.add_node(mao)
        self.board.add_node(bar)
        self.board.add_node(nth)
        self.board.add_node(hel)
        self.board.add_node(ska)
        self.board.add_node(bal)
        self.board.add_node(bot)
        self.board.add_node(iri)
        self.board.add_node(eng)
        self.board.add_node(wes)
        self.board.add_node(lyo)
        self.board.add_node(tys)
        self.board.add_node(ion)
        self.board.add_node(adr)
        self.board.add_node(aeg)
        self.board.add_node(eas)
        self.board.add_node(bla)

        # Non-Coastal Land

        par = territories.Inland('par', True, True, None)
        bur = territories.Inland('bur', False, False, None)
        ruh = territories.Inland('ruh', False, False, None)
        mun = territories.Inland('mun', True, True, units.Army('ger'))
        tyr = territories.Inland('tyr', False, False, None)
        boh = territories.Inland('boh', False, False, None)
        sil = territories.Inland('sil', False, False, None)
        war = territories.Inland('war', True, True, units.Army('rus'))
        vie = territories.Inland('vie', True, True, units.Army('aus'))
        bud = territories.Inland('bud', True, True, units.Army('aus'))
        ser = territories.Inland('ser', True, False, None)
        gal = territories.Inland('gal', False, False, None)
        ukr = territories.Inland('ukr', False, False, None)
        mos = territories.Inland('mos', True, True, units.Army('rus'))

        self.board.add_node(par)
        self.board.add_node(bur)
        self.board.add_node(ruh)
        self.board.add_node(mun)
        self.board.add_node(tyr)
        self.board.add_node(boh)
        self.board.add_node(sil)
        self.board.add_node(war)
        self.board.add_node(vie)
        self.board.add_node(bud)
        self.board.add_node(ser)
        self.board.add_node(gal)
        self.board.add_node(ukr)
        self.board.add_node(mos)

        # Coastal Land

        bre = territories.Coastal('bre', True, True, units.Fleet('fra'))
        gas = territories.Coastal('gas', False, False, None)
        spanc = territories.Coastal('spa/nc', True, False, None)
        spasc = territories.Coastal('spa/sc', True, False, None)
        por = territories.Coastal('por', True, False, None)
        mar = territories.Coastal('mar', True, True, units.Army('fra'))
        pie = territories.Coastal('por', False, False, None)
        tus = territories.Coastal('tus', False, False, None)
        rom = territories.Coastal('por', True, True, units.Army('ita'))
        nap = territories.Coastal('nap', True, True, units.Fleet('ita'))
        apu = territories.Coastal('apu', False, False, None)
        ven = territories.Coastal('ven', True, True, units.Army('ita'))
        tri = territories.Coastal('tri', True, True, units.Fleet('aus'))
        alb = territories.Coastal('alb', False, False, None)
        gre = territories.Coastal('gre', True, False, None)
        bulsc = territories.Coastal('bul/sc', True, False, None)
        con = territories.Coastal('con', True, True, units.Army('tur'))
        smy = territories.Coastal('smy', True, True, units.Army('tur'))
        ank = territories.Coastal('ank', True, True, units.Fleet('tur')) 
        bulec = territories.Coastal('bul/ec', True, False, None)
        rum = territories.Coastal('rum', True, False, None)
        sev = territories.Coastal('sev', True, True, units.Fleet('rus'))
        arm = territories.Coastal('arm', False, False, None)
        pic = territories.Coastal('pic', False, False, None)
        bel = territories.Coastal('bel', True, False, None)
        hol = territories.Coastal('hol', True, False, None)
        kie = territories.Coastal('kie', True, True, units.Fleet('ger'))
        ber = territories.Coastal('ber', True, True, units.Army('ger'))
        pru = territories.Coastal('pru', False, False, None)
        lvn = territories.Coastal('lvn', False, False, None)
        den = territories.Coastal('den', True, False, None)
        swe = territories.Coastal('swe', True, False, None)
        nwy = territories.Coastal('nwy', True, False, None)
        fin = territories.Coastal('fin', False, False, None)
        stpnc = territories.Coastal('stp/nc', True, True, None)
        stpsc = territories.Coastal('stp/sc', True, True, units.Fleet('rus'))
        lon = territories.Coastal('lon', True, True, units.Fleet('eng'))
        lvp = territories.Coastal('lvp', True, True, units.Army('eng'))
        edi = territories.Coastal('edi', True, True, units.Fleet('eng'))
        yor = territories.Coastal('con', False, False, None)
        cly = territories.Coastal('cly', False, False, None)
        wal = territories.Coastal('wal', False, False, None)
        naf = territories.Coastal('naf', False, False, None)
        syr = territories.Coastal('syr', False, False, None)
        tun = territories.Coastal('tun', True, False, None)

        self.board.add_node(bre)
        self.board.add_node(gas)
        self.board.add_node(spanc)
        self.board.add_node(spasc)
        self.board.add_node(por)
        self.board.add_node(pie)
        self.board.add_node(tus)
        self.board.add_node(rom)
        self.board.add_node(nap)
        self.board.add_node(apu)
        self.board.add_node(ven)
        self.board.add_node(tri)
        self.board.add_node(alb)
        self.board.add_node(gre)
        self.board.add_node(bulsc)
        self.board.add_node(con)
        self.board.add_node(smy)
        self.board.add_node(ank)
        self.board.add_node(bulec)
        self.board.add_node(rum)
        self.board.add_node(sev)
        self.board.add_node(arm)
        self.board.add_node(bel)
        self.board.add_node(kie)
        self.board.add_node(den)
        self.board.add_node(swe)
        self.board.add_node(nwy)
        self.board.add_node(fin)
        self.board.add_node(stpnc)
        self.board.add_node(stpsc)
        self.board.add_node(lon)
        self.board.add_node(lvp)
        self.board.add_node(edi)
        self.board.add_node(yor)
        self.board.add_node(cly)
        self.board.add_node(wal)
        self.board.add_node(ber)
        self.board.add_node(pru)
        self.board.add_node(lvn)
        self.board.add_node(tun)
        self.board.add_node(naf)
        self.board.add_node(syr)



        for territory in self.board.nodes():
            self.terr.append((territory.name, territory))

        # There's quite a few edges. Ow. Also South/North coasts are *really* annoying

        self.board.add_edges_from([(nwg, bar), (nwg, nao), (nwg, nth), 
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

        self.board.add_edges_from([(cly, edi), (edi, yor), (yor, lon),
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

        self.board.add_edges_from([(bre, par), (par, bur), (par, pic),
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
                              (pie, ven), (smy, ank), (smy, arm),
                              (ruh, bel), (ruh, hol), (ruh, kie)
                            ], label=['A'])

        country_eng = countries.Country([lon, lvp, edi], 3, 3)
        country_fra = countries.Country([bre, par, mar], 3, 3)
        country_ger = countries.Country([kie, ber, mun], 3, 3)
        country_ita = countries.Country([ven, rom, nap], 3, 3)
        country_aus = countries.Country([tri, vie, bud], 3, 3)
        country_tur = countries.Country([smy, con, ank], 3, 3)
        country_rus = countries.Country([war, sev, mos, stpnc, stpsc], 4, 4)

        self.countries = {
            'eng' : country_eng,
            'fra' : country_fra,
            'ger' : country_ger,
            'ita' : country_ita,
            'aus' : country_aus,
            'tur' : country_tur,
            'rus' : country_tur
        }
    
    def visualise(self):
        nx.draw(self.board, with_labels=True)
        plt.show()
        
    
    def adjudicate(self, input : str):
        lines = input.split('\n')

        order_map = {
            'hsup': {
                'F' : [],
                'A' : []
            },
            'msup': {
                'F' : [],
                'A' : []
            },
            'hold': {
                'F' : [],
                'A' : []
            },
            'move': {
                'F' : [],
                'A' : []
            },
            'con' : {
                'F' : [],
                'A' : []
            }
        }

        for line in lines:
            order = None
            parts = line.split(' ')
            if len(parts) < 3:
                raise ValueError('Too few arguments for order')
            if parts[0] not in ['A', 'F']:
                raise ValueError('Neither fleet nor army specified')
            if parts[2] not in ['S', 'C', 'H', '-']:
                raise ValueError('Malformed order specification')
            if parts[1] not in self.terr and parts[1] not in ['bul', 'stp', 'spa']:
                raise ValueError('Starting state not specified correctly')
            match parts[2]:
                case 'H':
                    order = orders.Hold(parts[0], parts[1])
                    order_map['hold'][parts[0]].append(order)
                case '-':
                    if len(parts) < 4:
                        raise ValueError('Too few arguments for move order')
                    if parts[3] not in self.terr and parts[3] not in ['bul', 'stp', 'spa']:
                        raise ValueError('End location for move not a state')
                    order = orders.Move(parts[0], parts[1], parts[3])
                    order_map['move'][parts[0]].append(order)
                case 'S':
                    if len(parts) < 4:
                        raise ValueError('Too few arguments for support order')
                    if parts[3] not in self.terr and parts[3] not in ['bul', 'stp', 'spa']:
                        raise ValueError('Supported location not a state')
                    if len(parts) == 4:
                        order = orders.HoldSupport(parts[0], parts[1], parts[3])
                        order_map['hsup'][parts[0]].append(order)
                    elif len(parts) == 6:
                        if parts[4] != '-':
                            raise ValueError('Malformed support error')
                        if parts[5] not in self.terr and parts[5] not in ['bul', 'stp', 'spa']:
                           raise ValueError('End support location not a state')
                        order = orders.MoveSupport(parts[0], parts[1], parts[3], parts[5])
                        order_map['msup'][parts[0]].append(order)
                    else:
                        raise ValueError('Incorrect count of arguments for support order')
                case 'C':
                    if len(parts) != 6:
                        raise ValueError('Incorrect count of arguments for convoy order')
                    if parts[3] not in self.terr and parts[3] not in ['bul', 'stp', 'spa']:
                        raise ValueError('Convoy start location not a state')
                    if parts[5] not in self.terr and parts[5] not in ['bul', 'stp', 'spa']:
                        raise ValueError('Convoy end location not a state')
                    if parts[4] != '-':
                            raise ValueError('Malformed convoy error')
                    order = orders.Convoy(parts[0], parts[1], parts[3], parts[5])
                    order_map['con'][parts[0]].append(order)
                case _:
                    raise ValueError('Order type malformed')
                