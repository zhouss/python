from snap import *
# create a graph PNGraph



  # traverse the nodes
#for NI in G2.Nodes():
#   print "node id %d with out-degree %d and in-degree %d" % (
#	 NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
  # traverse the edges
#for EI in G2.Edges():
#   print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
  # traverse the edges by nodes
#for NI in G2.Nodes():
#   for Id in NI.GetOutEdges():
#      print "edge (%d %d)" % (NI.GetId(), Id)

# generate a network using Forest Fire model
G3 = GenForestFire(100, 0.35, 0.35)
  # save and load binary
FOut = TFOut("test.graph")
G3.Save(FOut)
FOut.Flush()
FIn = TFIn("test.graph")
G4 = TNGraph.Load(FIn)
  # save and load from a text file
SaveEdgeList(G4, "test.txt", "Save as tab-separated list of edges")
G5 = LoadEdgeList(PNGraph, "test.txt", 0, 1)


import snap
Graph = snap.GenRndGnm(snap.PNGraph, 10, 20)
snap.DrawGViz(Graph, snap.gvlDot, "graph.png", "graph 1")

UGraph = snap.GenRndGnm(snap.PUNGraph, 10, 40)
snap.DrawGViz(UGraph, snap.gvlNeato, "graph_undirected.png", "graph 2", True)

NIdColorH = snap.TIntStrH()
NIdColorH[0] = "green"
NIdColorH[1] = "red"
NIdColorH[2] = "purple"
NIdColorH[3] = "blue"
NIdColorH[4] = "yellow"
Network = snap.GenRndGnm(snap.PNEANet, 5, 10)
snap.DrawGViz(Network, snap.gvlSfdp, "network.png", "graph 3", True, NIdColorH)