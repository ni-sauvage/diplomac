from territories import Territory
import networkx as nx
import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout

board = None
terr = []

def main():
    board = nx.Graph()
    # seas
    nao = Territory('nao', False, False, None)
    mao = Territory('mao', False, False, None)
    nwg = Territory('nwg', False, False, None)
    bar = Territory('bar', False, False, None)
    nth = Territory('nth', False, False, None)
    hel = Territory('hel', False, False, None)
    ska = Territory('ska', False, False, None)
    bal = Territory('bal', False, False, None)
    bot = Territory('bot', False, False, None)
    iri = Territory('iri', False, False, None)
    eng = Territory('eng', False, False, None)
    wes = Territory('wes', False, False, None)
    lyo = Territory('lyo', False, False, None)
    tys = Territory('tys', False, False, None)
    ion = Territory('ion', False, False, None)
    adr = Territory('adr', False, False, None)
    aeg = Territory('aeg', False, False, None)
    eas = Territory('eas', False, False, None)
    bla = Territory('bla', False, False, None)

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